import xbmc, xbmcgui, xbmcaddon, xbmcplugin
import urllib, urllib2
import re, string, sys, os
import urlresolver
from TheYid.common.addon import Addon
from TheYid.common.net import Net
from htmlentitydefs import name2codepoint as n2cp
import HTMLParser

try:
	from sqlite3 import dbapi2 as sqlite
	print "Loading sqlite3 as DB engine"
except:
	from pysqlite2 import dbapi2 as sqlite
	print "Loading pysqlite2 as DB engine"

addon_id = 'plugin.video.ddlvalley'
plugin = xbmcaddon.Addon(id=addon_id)

DB = os.path.join(xbmc.translatePath("special://database"), 'ddlvalley.db')
BASE_URL = 'http://www.ddlvalley.eu/'
net = Net()
addon = Addon('plugin.video.ddlvalley', sys.argv)
showAllParts = True
showPlayAll = True

#PATHS
AddonPath = addon.get_path()
IconPath = AddonPath + "/icons/"

if plugin.getSetting('showAllParts') == 'false':
        showAllParts = False

if plugin.getSetting('showPlayAll') == 'false':
        showPlayAll = False

##### Queries ##########
mode = addon.queries['mode']
url = addon.queries.get('url', None)
content = addon.queries.get('content', None)
query = addon.queries.get('query', None)
startPage = addon.queries.get('startPage', None)
numOfPages = addon.queries.get('numOfPages', None)
listitem = addon.queries.get('listitem', None)
urlList = addon.queries.get('urlList', None)
section = addon.queries.get('section', None)
##### Queries ##########


def GetTitles(section, url, startPage= '1', numOfPages= '1'): # Get Movie Titles
        print 'ddlvalley get Movie Titles Menu %s' % url

        # handle paging
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + 'page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        CLEAN(html)

        start = int(startPage)
        end = start + int(numOfPages)

        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + 'page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content
                        CLEAN(html)
                        
                match = re.compile('<h2>.+?href="(.+?)".+?>(.+?)<.+?src="(.+?)".+?', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.ddlvalley/?mode=Search&query=%s)' %(name.strip())
        		cm.append(('Search on ddlvalley', runstring))
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img= img)



                addon.add_directory({'mode': 'GetTitles', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nexts.png')
        
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))


def GetLinks(section, url): # Get Links
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(str(url)).content
        CLEAN(html)
        sources = []
        listitem = GetMediaInfo(html)
        print 'LISTITEM: '+str(listitem)
        content = html
        print'CONTENT: '+str(listitem)
        r = re.search('<strong>Links.*</strong>', html)
        if r:
                content = content[:r.start()]

        match = re.compile('href="(.+?)"').findall(content)
        listitem = GetMediaInfo(content)
        for url in match:
                host = GetDomain(url)

                if 'Unknown' in host:
                                continue

                # ignore .rar files
                r = re.search('\part1\part2\part3\part4\part5\.rar.html\.rar\.file[(?:\.html|\.htm)]*', url, re.IGNORECASE)
                if r:
                        continue

                print '*****************************' + host + ' : ' + url
                title = url.rpartition('/')
                title = title[2].replace('.html', '')
                title = title.replace('.htm', '')
                title = title.replace('file', '[COLOR red][B][I]RAR no streaming[/B][/I][/COLOR]')
                title = title.replace('.rar', '[COLOR red][B][I]RAR no streaming[/B][/I][/COLOR]')
                title = title.replace('www.', '')
                title = title.replace ('-','')
                title = title.replace('_',' ')
                title = title.replace('gaz','')
                title = title.replace('NTb','')
                title = title.replace('part1','')
                title = title.replace('part2','')
                title = title.replace('part3','')
                title = title.replace('part4','')
                title = title.replace('part5','')
                title = title.replace('.',' ')
                title = title.replace('720p','[COLOR gold][B][I]720p[/B][/I][/COLOR]')
                title = title.replace('1080p','[COLOR orange][B][I]1080p[/B][/I][/COLOR]')
                title = title.replace('DDLValley eu','')
                title = title.replace('mkv','[COLOR gold][B][I]MKV[/B][/I][/COLOR] ')
                title = title.replace('avi','[COLOR pink][B][I]AVI[/B][/I][/COLOR] ')
                title = title.replace('mp4','[COLOR purple][B][I]MP4[/B][/I][/COLOR] ')
                name = host+'-'+title
                hosted_media = urlresolver.HostedMediaFile(url=url, title=name)
                sources.append(hosted_media)


        source = urlresolver.choose_source(sources)
        if source: stream_url = source.resolve()
        else: stream_url = ''
        xbmc.Player().play(stream_url)
                       

def CLEAN(string):
    def substitute_entity(match):
        ent = match.group(3)
        if match.group(1) == "#":
            if match.group(2) == '':
                return unichr(int(ent))
            elif match.group(2) == 'x':
                return unichr(int('0x'+ent, 16))
        else:
            cp = n2cp.get(ent)
            if cp: return unichr(cp)
            else: return match.group()
    entity_re = re.compile(r'&(#?)(x?)(\d{1,5}|\w{1,8});')
    return entity_re.subn(substitute_entity, string)[0]


def GetDomain(url):
        tmp = re.compile('//(.+?)/').findall(url)
        domain = 'Unknown'
        if len(tmp) > 0 :
            domain = tmp[0].replace('www.', '')
        return domain


def GetMediaInfo(html):
        listitem = xbmcgui.ListItem()
        match = re.search('og:title" content="(.+?) \((.+?)\)', html)
        if match:
                print match.group(1) + ' : '  + match.group(2)
                listitem.setInfo('video', {'Title': match.group(1), 'Year': int(match.group(2)) } )
        return listitem

        
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def MainMenu():    #homescreen
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/tv-shows/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue]Latest Tv shows >>[/COLOR]'}, img=IconPath + 'tvs.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/tv-shows/hd-720/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Tv shows 720p >>'}, img=IconPath + 'tvs.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/tv-shows/sports/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Tv sports >>'}, img=IconPath + 'tvs.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/tv-shows/tv-pack/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Tv packs >>'}, img=IconPath + 'tvs.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/tv-shows/web-dl/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Tv web-dl >>'}, img=IconPath + 'tvs.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue]Latest Movies >>[/COLOR]'}, img=IconPath + 'movies.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/movies/dvdrip-movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'DVDRip Movies >>'}, img=IconPath + 'movies.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/movies/dvdscr/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'DVDScr Movies >>'}, img=IconPath + 'movies.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/movies/bdrip/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'BDRip Movies >>'}, img=IconPath + 'movies.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/movies/bluray-720p/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Bluray Movies >>'}, img=IconPath + 'movies.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/movies/cam/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Cam Movies >>'}, img=IconPath + 'movies.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/movies/ts/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Ts Movies >>'}, img=IconPath + 'movies.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/movies/r5-movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'R5 Movies >>'}, img=IconPath + 'movies.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/movies/web-dl-movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Web-dl Movies >>'}, img=IconPath + 'movies.png')
        addon.add_directory({'mode': 'GetSearchQuery'},  {'title':  '[COLOR blue][B]DDL[/B] [COLOR green]Search[/COLOR]'}, img=IconPath + 'searchs.png')
        addon.add_directory({'mode': 'GetSearchQuery3'},  {'title':  '[COLOR silver][B]Tv-Release[/B][/COLOR] [COLOR green]Search[/COLOR]'}, img=IconPath + 'search3.png')
        addon.add_directory({'mode': 'GetSearchQuery4'},  {'title':  '[COLOR silver][B]Tv Show Pad[/B][/COLOR] [COLOR green]Search[/COLOR]'}, img=IconPath + 'search4.png')
        addon.add_directory({'mode': 'GetSearchQuery2'},  {'title':  '[COLOR silver][B]filescroptube[/B][/COLOR] [COLOR green]Search[/COLOR]'}, img=IconPath + 'search2.png')
        addon.add_directory({'mode': 'ResolverSettings'}, {'title':  '[COLOR red]Resolver Settings[/COLOR]'}, img=IconPath + 'resolver.png')
        addon.add_directory({'mode': 'Help'}, {'title':  '[COLOR pink]FOR HELP ON THIS ADDON PLEASE GOTO...[/COLOR] [COLOR gold][B][I]www.xbmchub.com[/B][/I][/COLOR]'}, img=IconPath + 'helps.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))



def GetSearchQuery():
	last_search = addon.load_data('search')
	if not last_search: last_search = ''
	keyboard = xbmc.Keyboard()
        keyboard.setHeading('[COLOR green]Search ddlvalley[/COLOR]')
	keyboard.setDefault(last_search)
	keyboard.doModal()
	if (keyboard.isConfirmed()):
                query = keyboard.getText()
                addon.save_data('search',query)
                Search(query)
	else:
                return

        
def Search(query):
        url = 'http://www.google.com/search?q=site:ddlvalley.eu ' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        CLEAN(html)
        match = re.compile('<h3 class="r"><a href="(.+?)".+?onmousedown=".+?">(.+?)</a>').findall(html)
        for url, title in match:
                title = title.replace('<b>...</b>', '').replace('<em>', '').replace('</em>', '')
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title})
	xbmcplugin.endOfDirectory(int(sys.argv[1]))


def GetSearchQuery2():
	last_search = addon.load_data('search')
	if not last_search: last_search = ''
	keyboard = xbmc.Keyboard()
        keyboard.setHeading('[COLOR green]Search filescroptube[/COLOR]')
	keyboard.setDefault(last_search)
	keyboard.doModal()
	if (keyboard.isConfirmed()):
                query = keyboard.getText()
                addon.save_data('search',query)
                Search2(query)
	else:
                return

        
def Search2(query):
        url = 'http://www.google.com/search?q=site:filescroptube.com ' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        CLEAN(html)
        match = re.compile('<h3 class="r"><a href="(.+?)".+?onmousedown=".+?">(.+?)</a>').findall(html)
        for url, title in match:
                title = title.replace('<b>...</b>', '').replace('<em>', '').replace('</em>', '')
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title})
	xbmcplugin.endOfDirectory(int(sys.argv[1]))


def GetSearchQuery3():
	last_search = addon.load_data('search')
	if not last_search: last_search = ''
	keyboard = xbmc.Keyboard()
        keyboard.setHeading('[COLOR green]Search tv-release[/COLOR]')
	keyboard.setDefault(last_search)
	keyboard.doModal()
	if (keyboard.isConfirmed()):
                query = keyboard.getText()
                addon.save_data('search',query)
                Search3(query)
	else:
                return

        
def Search3(query):
        url = 'http://www.google.com/search?q=site:tv-release.net ' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        CLEAN(html)
        match = re.compile('<h3 class="r"><a href="(.+?)".+?onmousedown=".+?">(.+?)</a>').findall(html)
        for url, title in match:
                title = title.replace('<b>...</b>', '').replace('<em>', '').replace('</em>', '')
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title})
	xbmcplugin.endOfDirectory(int(sys.argv[1]))



def GetSearchQuery4():
	last_search = addon.load_data('search')
	if not last_search: last_search = ''
	keyboard = xbmc.Keyboard()
        keyboard.setHeading('[COLOR green]Search TvShowPad[/COLOR]')
	keyboard.setDefault(last_search)
	keyboard.doModal()
	if (keyboard.isConfirmed()):
                query = keyboard.getText()
                addon.save_data('search',query)
                Search4(query)
	else:
                return

        
def Search4(query):
        url = 'http://www.google.com/search?q=site:tvshowspad.com ' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        CLEAN(html)
        match = re.compile('<h3 class="r"><a href="(.+?)".+?onmousedown=".+?">(.+?)</a>').findall(html)
        for url, title in match:
                title = title.replace('<b>...</b>', '').replace('<em>', '').replace('</em>', '')
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title})
	xbmcplugin.endOfDirectory(int(sys.argv[1]))


if mode == 'main': 
	MainMenu()
elif mode == 'GetTitles': 
	GetTitles(section, url, startPage, numOfPages)
elif mode == 'GetLinks':
	GetLinks(section, url)
elif mode == 'GetSearchQuery':
	GetSearchQuery()
elif mode == 'Search':
	Search(query)
elif mode == 'GetSearchQuery2':
	GetSearchQuery2()
elif mode == 'Search2':
	Search2(query)
elif mode == 'GetSearchQuery3':
	GetSearchQuery3()
elif mode == 'Search3':
	Search3(query)
elif mode == 'GetSearchQuery4':
	GetSearchQuery4()
elif mode == 'Search4':
	Search4(query)
elif mode == 'PlayVideo':
	PlayVideo(url, listitem)	
elif mode == 'ResolverSettings':
        urlresolver.display_settings()

