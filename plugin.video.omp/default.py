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

addon_id = 'plugin.video.omp'
plugin = xbmcaddon.Addon(id=addon_id)

DB = os.path.join(xbmc.translatePath("special://database"), 'omp.db')
BASE_URL = 'http://www.onlinemoviesplayer.com/'
net = Net()
addon = Addon('plugin.video.omp', sys.argv)

#PATHS
AddonPath = addon.get_path()
IconPath = AddonPath + "/icons/"
FanartPath = AddonPath + "/icons/"


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
        print 'omp get Movie Titles Menu %s' % url
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
                match = re.compile('<div class=".+?"><a class=".+?" href="(.+?)"><img width=".+?" height=".+?" src="(.+?)" .+?rel=.+?>(.+?)Watch Online ', re.DOTALL).findall(html)
                for movieUrl, img, name in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR darkorchid][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view')  
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

##################################################################################################################################

def GetTitles1(section, url, startPage= '1', numOfPages= '1'): # Get Movie Titles #222222222
        print 'omp get Movie Titles Menu %s' % url
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + '/' + 'page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        CLEAN(html)
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + '/' + 'page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content
                        CLEAN(html)  
                match = re.compile('<div class=".+?"><a class=".+?" href="(.+?)"><img width=".+?" height=".+?" src="(.+?)" .+?rel=.+?>(.+?)Watch Online <', re.DOTALL).findall(html)
                for movieUrl, img, name in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles1', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR darkorchid][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view')      
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#########################################################################################################################################################################

def GetTitles2(section, url, startPage= '1', numOfPages= '1'): # Get Movie Titles #33333
        print 'omp get Movie Titles Menu %s' % url
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + '/page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        CLEAN(html)
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + '/page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content
                        CLEAN(html) 
                match = re.compile('<div class=".+?"><a class=".+?" href="(.+?)"><img width=".+?" height=".+?" src="(.+?)" .+?rel=.+?>(.+?)Watch Online ', re.DOTALL).findall(html)
                for movieUrl, img, name in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles2', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR darkorchid][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view')      
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#######################################################################################################################################################################

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
                content = html[r.end():]

        match = re.compile('href="(.+?)"').findall(content)
        listitem = GetMediaInfo(content)
        for url in match:
                host = GetDomain(url)

                if 'Unknown' in host:

                        continue
                print '*****************************' + host
                title = url.rpartition('/')
                host = host.replace('movreel.com','movreel.com - [COLOR red]Download/Streaming limit of 2GB a day !![/COLOR]')
                host = host.replace('.com','')
                name = host
                hosted_media = urlresolver.HostedMediaFile(url=url, title=name)
                sources.append(hosted_media)

                
        find = re.search('commentblock', html)
        if find:
                print 'in comments if'
                html = html[find.end():]
                CLEAN(html)###
                print 'MATCH IS: '+str(match)
                print len(match)
                for url in match:
                        host = GetDomain(url)
                        if 'Unknown' in host:
                                continue

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
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorchid]LATEST ADDED [/COLOR]>>'}, img=IconPath + 'la.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL + '/category/old-movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorchid]CLASSIC MOVIES [/COLOR]>>'}, img=IconPath + 'ca.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/boxing/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorchid]SPORTS [/COLOR]>>'}, img=IconPath + 'spo.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GenreMenu'}, {'title':  '[COLOR darkorchid]GENRE [/COLOR]>>'}, img=IconPath + 'gen.png', fanart=FanartPath + 'fanart.png') 
        addon.add_directory({'mode': 'AzMenu'}, {'title':  '[COLOR darkorchid] A-Z [/COLOR]>>'}, img=IconPath + 'az.png', fanart=FanartPath + 'fanart.png')  
        addon.add_directory({'mode': 'DateMenu'}, {'title':  '[COLOR darkorchid]DATE [/COLOR]>>'}, img=IconPath + 'da.png', fanart=FanartPath + 'fanart.png')  
        addon.add_directory({'mode': 'GetSearchQuery'},  {'title':  '[COLOR green]SEARCH [/COLOR]'}, img=IconPath + 'se1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'ResolverSettings'}, {'title':  '[COLOR red]Resolver Settings[/COLOR]'}, img=IconPath + 'res.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'Help'}, {'title':  '[COLOR pink]FOR HELP PLEASE GOTO...[/COLOR] [COLOR gold][B][I]www.xbmchub.com[/B][/I][/COLOR]'}, img=IconPath + 'help.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'help'}, {'title':  '[COLOR aqua][B]FOLLOW ME ON TWITTER [/B][/COLOR] [COLOR gold][B][I]@TheYid009 [/B][/I][/COLOR] '}, img=IconPath + 'theyids1.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GenreMenu():
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL + '/tag/action',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Action >>'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL + '/tag/adventure',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Adventure >>'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL + '/tag/animation',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Animation >>'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL + '/tag/comedy',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Comedy >>'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL + '/tag/crime',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Crime >>'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL + '/tag/drama',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Drama >>'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL + '/tag/fantasy',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Fantasy >>'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL + '/tag/horror',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Horror >>'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL + '/tag/romance',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Romance >>'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL + '/tag/sci-Fi',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sci Fi >>'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL + '/tag/thriller',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Thriller >>'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL + '/tag/western',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Western >>'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))


def AzMenu():
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL + '/tag/0-9-hollywood',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '1?2 >>'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL + '/tag/a-hollywood',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'A >>'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL + '/tag/b-hollywood',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'B >>'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL + '/tag/c-hollywood',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'C >>'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL + '/tag/d-hollywood',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'D >>'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL + '/tag/e-hollywood',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'E >>'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL + '/tag/f-hollywood',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'F >>'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL + '/tag/g-hollywood',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'G >>'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL + '/tag/h-hollywood',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'H >>'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL + '/tag/i-hollywood',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'I >>'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL + '/tag/j-hollywood',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'J >>'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL + '/tag/k-hollywood',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'K >>'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL + '/tag/l-hollywood',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'L >>'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL + '/tag/m-hollywood',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'M >>'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL + '/tag/n-hollywood',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'N >>'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL + '/tag/o-hollywood',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'O >>'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL + '/tag/p-hollywood',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'P >>'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL + '/tag/q-hollywood',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Q >>'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL + '/tag/r-hollywood',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'R >>'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL + '/tag/s-hollywood',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'S >>'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL + '/tag/t-hollywood',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'T >>'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL + '/tag/u-hollywood',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'U >>'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL + '/tag/v-hollywood',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'V >>'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL + '/tag/w-hollywood',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'W >>'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL + '/tag/x-hollywood',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'X >>'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL + '/tag/y-hollywood',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Y >>'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL + '/tag/z-hollywood',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Z >>'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def DateMenu():
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL + '/tag/2000-english-movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '2000 >>'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL + '/tag/2001-english-movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '2001 >>'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL + '/tag/2002-english-movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '2002 >>'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL + '/tag/2003-english-movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '2003 >>'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL + '/tag/2004-english-movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '2004 >>'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL + '/tag/2005-english-movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '2005 >>'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL + '/tag/2006-english-movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '2006 >>'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL + '/tag/2007-english-movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '2007 >>'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL + '/tag/2008-english-movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '2008 >>'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL + '/tag/2009-english-movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '2009 >>'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL + '/tag/2010-english-movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '2010 >>'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL + '/tag/2011-english-movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '2011 >>'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL + '/tag/2012-english-movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '2012 >>'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL + '/tag/2013-english-movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '2013 >>'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.png')
        #addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL + '/tag/2014-english-movies',
                             #'startPage': '1', 'numOfPages': '1'}, {'title':  '2014 >>'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))



def GetSearchQuery():
	last_search = addon.load_data('search')
	if not last_search: last_search = ''
	keyboard = xbmc.Keyboard()
        keyboard.setHeading('[COLOR green]Search[/COLOR]')
	keyboard.setDefault(last_search)
	keyboard.doModal()
	if (keyboard.isConfirmed()):
                query = keyboard.getText()
                addon.save_data('search',query)
                Search(query)
	else:
                return

        
def Search(query):
        url = 'http://www.google.com/search?q=site:onlinemoviesplayer.com ' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        CLEAN(html)
        match = re.compile('<h3 class="r"><a href="(.+?)".+?onmousedown=".+?">(.+?)</a>').findall(html)
        for url, title in match:
                title = title.replace('<b>...</b>', '').replace('<em>', '').replace('</em>', '')
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title})
	xbmcplugin.endOfDirectory(int(sys.argv[1]))



def setView(content, viewType):

	if content:
		xbmcplugin.setContent(int(sys.argv[1]), content)
	if addon.get_setting('auto-view') == 'true':
		xbmc.executebuiltin("Container.SetViewMode(%s)" % addon.get_setting(viewType) )


	xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_UNSORTED )
	xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_LABEL )
	xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_VIDEO_RATING )
	xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_DATE )
	xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_PROGRAM_COUNT )
	xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_VIDEO_RUNTIME )
	xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_GENRE )




if mode == 'main': 
	MainMenu()
elif mode == 'GetTitles': 
	GetTitles(section, url, startPage, numOfPages)
elif mode == 'GetTitles1': 
	GetTitles1(section, url, startPage, numOfPages)
elif mode == 'GetTitles2': 
	GetTitles2(section, url, startPage, numOfPages)
elif mode == 'GetLinks':
	GetLinks(section, url)
elif mode == 'GetSearchQuery':
	GetSearchQuery()
elif mode == 'Search':
	Search(query)
elif mode == 'PlayVideo':
	PlayVideo(url, listitem)	
elif mode == 'ResolverSettings':
        urlresolver.display_settings()
elif mode == 'GenreMenu':
        GenreMenu()
elif mode == 'AzMenu':
        AzMenu()
elif mode == 'DateMenu':
        DateMenu()


