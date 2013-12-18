################MyZmovies#################
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

addon_id = 'plugin.video.myZmovies'
plugin = xbmcaddon.Addon(id=addon_id)

DB = os.path.join(xbmc.translatePath("special://database"), 'myZmovies.db')
BASE_URL = 'http://www1.zmovie.tw/'
net = Net()
addon = Addon('plugin.video.myZmovies', sys.argv)
showAllParts = True
showPlayAll = True

#PATHS
AddonPath = addon.get_path()
IconPath = AddonPath + "/icons/"
FanartPath = AddonPath + "/icons/"

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
        print 'myZmovies get Movie Titles Menu %s' % url

        # handle paging
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + '/' + startPage + ''
        print pageUrl
        html = net.http_GET(pageUrl).content
        CLEAN(html)

        start = int(startPage)
        end = start + int(numOfPages)

        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + '/' + str(page) + ''
                        html = net.http_GET(pageUrl).content
                        CLEAN(html)
                        
                match = re.compile('width: 68px; height: 100px; position: relative;.+?href="(.+?)" title=(.+?)>.+?src=.+?src="(.+?)"', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.myZmovies/?mode=Search&query=%s)' %(name.strip())
        		cm.append(('Search on myZmovies', runstring))
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img= img)



                addon.add_directory({'mode': 'GetTitles', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'znext.png', fanart=FanartPath + 'fanart.png')
        
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#################################                        ##################################                        ##################################                      #################

def GetTitles1(section, url, startPage= '1', numOfPages= '1'): # Get Movie Titles
        print 'myZmovies get Movie Titles Menu %s' % url

        # handle paging
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + '/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        CLEAN(html)

        start = int(startPage)
        end = start + int(numOfPages)

        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + '/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content
                        CLEAN(html)
                        
                match = re.compile('width: 68px; height: 100px; position: relative;.+?href="(.+?)" title=(.+?)>.+?src=.+?src="(.+?)"', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.myZmovies/?mode=Search&query=%s)' %(name.strip())
        		cm.append(('Search on myZmovies', runstring))
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img= img)


        
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
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL + '/movies/new',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue]New Release[/COLOR] >>'}, img=IconPath + 'newre.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL + '/movies/recent',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue]Recently Added[/COLOR] >>'}, img=IconPath + 'radded.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/movies/featured',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR dodgerblue]Featured Movies[/COLOR] >>'}, img=IconPath + 'femovies.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GenreMenu'}, {'title':  '[COLOR cornflowerblue]Movie by Genre[/COLOR] >>'}, img=IconPath + 'mg.png', fanart=FanartPath + 'fanart.png') 
        addon.add_directory({'mode': 'AzMenu'}, {'title':  '[COLOR lightskyblue]Movie by A-Z[/COLOR] >>'}, img=IconPath + 'az.png', fanart=FanartPath + 'fanart.png') 
        addon.add_directory({'mode': 'DateMenu'}, {'title':  '[COLOR lightsteelblue]Movie by Date[/COLOR] >>'}, img=IconPath + 'md.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetSearchQuery'},  {'title':  '[COLOR green]Search [/COLOR]'}, img=IconPath + 'sea.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'ResolverSettings'}, {'title':  '[COLOR red]Resolver Settings[/COLOR]'}, img=IconPath + 'resttings.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'Help'}, {'title':  '[COLOR pink]FOR HELP PLEASE GOTO...[/COLOR] [COLOR gold][B][I]www.xbmchub.com[/B][/I][/COLOR]'}, img=IconPath + 'zzhub.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'help'}, {'title':  '[COLOR aqua][B]FOLLOW ME ON TWITTER [/B][/COLOR] [COLOR gold][B][I]@TheYid009 [/B][/I][/COLOR] '}, img=IconPath + 'twit.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))


def GenreMenu():
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/genre/action',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Action >>'}, img=IconPath + 'mg.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/genre/adventure',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Adventure >>'}, img=IconPath + 'mg.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/genre/animation',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Animation >>'}, img=IconPath + 'mg.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/genre/Comedy',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Comedy >>'}, img=IconPath + 'mg.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/genre/crime',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Crime >>'}, img=IconPath + 'mg.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/genre/documentary',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Documentary >>'}, img=IconPath + 'mg.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/genre/drama',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Drama >>'}, img=IconPath + 'mg.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/genre/fantasy',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Fantasy >>'}, img=IconPath + 'mg.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/genre/horror',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Horror >>'}, img=IconPath + 'mg.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/genre/romance',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Romance >>'}, img=IconPath + 'mg.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/genre/sci-Fi',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sci Fi >>'}, img=IconPath + 'mg.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/genre/thriller',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Thriller >>'}, img=IconPath + 'mg.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/genre/sport',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sport >>'}, img=IconPath + 'mg.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/genre/western',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Western >>'}, img=IconPath + 'mg.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))


def AzMenu():
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/alpha/0-9',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '1?2 >>'}, img=IconPath + 'az.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/alpha/A',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'A >>'}, img=IconPath + 'az.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/alpha/B',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'B >>'}, img=IconPath + 'az.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/alpha/C',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'C >>'}, img=IconPath + 'az.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/alpha/D',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'D >>'}, img=IconPath + 'az.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/alpha/E',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'E >>'}, img=IconPath + 'az.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/alpha/F',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'F >>'}, img=IconPath + 'az.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/alpha/G',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'G >>'}, img=IconPath + 'az.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/alpha/H',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'H >>'}, img=IconPath + 'az.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/alpha/I',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'I >>'}, img=IconPath + 'az.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/alpha/J',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'J >>'}, img=IconPath + 'az.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/alpha/K',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'K >>'}, img=IconPath + 'az.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/alpha/L',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'L >>'}, img=IconPath + 'az.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/alpha/M',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'M >>'}, img=IconPath + 'az.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/alpha/N',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'N >>'}, img=IconPath + 'az.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/alpha/O',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'O >>'}, img=IconPath + 'az.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/alpha/P',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'P >>'}, img=IconPath + 'az.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/alpha/Q',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Q >>'}, img=IconPath + 'az.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/alpha/R',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'R >>'}, img=IconPath + 'az.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/alpha/S',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'S >>'}, img=IconPath + 'az.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/alpha/T',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'T >>'}, img=IconPath + 'az.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/alpha/U',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'U >>'}, img=IconPath + 'az.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/alpha/V',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'V >>'}, img=IconPath + 'az.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/alpha/W',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'W >>'}, img=IconPath + 'az.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/alpha/X',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'X >>'}, img=IconPath + 'az.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/alpha/Y',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Y >>'}, img=IconPath + 'az.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/alpha/Z',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Z >>'}, img=IconPath + 'az.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))


def DateMenu():
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/date/1970',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '1970 >>'}, img=IconPath + 'md.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/date/1980',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '1980 >>'}, img=IconPath + 'md.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/date/1981',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '1981 >>'}, img=IconPath + 'md.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/date/1982',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '1982 >>'}, img=IconPath + 'md.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/date/1983',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '1983 >>'}, img=IconPath + 'md.png', fanart=FanartPath + 'fanart.png') 
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/date/1984',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '1984 >>'}, img=IconPath + 'md.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/date/1985',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '1985 >>'}, img=IconPath + 'md.png', fanart=FanartPath + 'fanart.png') 
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/date/1986',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '1986 >>'}, img=IconPath + 'md.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/date/1987',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '1987 >>'}, img=IconPath + 'md.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/date/1988',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '1988 >>'}, img=IconPath + 'md.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/date/1989',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '1989 >>'}, img=IconPath + 'md.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/date/1990',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '1990 >>'}, img=IconPath + 'md.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/date/1991',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '1991 >>'}, img=IconPath + 'md.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/date/1992',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '1992 >>'}, img=IconPath + 'md.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/date/1993',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '1993 >>'}, img=IconPath + 'md.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/date/1994',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '1994 >>'}, img=IconPath + 'md.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/date/1995',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '1995 >>'}, img=IconPath + 'md.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/date/1996',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '1996 >>'}, img=IconPath + 'md.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/date/1997',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '1997 >>'}, img=IconPath + 'md.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/date/1998',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '1998 >>'}, img=IconPath + 'md.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/date/1999',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '1999 >>'}, img=IconPath + 'md.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/date/2000',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '2000 >>'}, img=IconPath + 'md.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/date/2001',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '2001 >>'}, img=IconPath + 'md.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/date/2002',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '2002 >>'}, img=IconPath + 'md.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/date/2003',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '2003 >>'}, img=IconPath + 'md.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/date/2004',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '2004 >>'}, img=IconPath + 'md.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/date/2005',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '2005 >>'}, img=IconPath + 'md.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/date/2006',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '2006 >>'}, img=IconPath + 'md.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/date/2007',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '2007 >>'}, img=IconPath + 'md.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/date/2008',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '2008 >>'}, img=IconPath + 'md.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/date/2009',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '2009 >>'}, img=IconPath + 'md.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/date/2010',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '2010 >>'}, img=IconPath + 'md.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/date/2011',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '2011 >>'}, img=IconPath + 'md.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/date/2012',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '2012 >>'}, img=IconPath + 'md.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/search/date/2013',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '2013 >>'}, img=IconPath + 'md.png', fanart=FanartPath + 'fanart.png')
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
        url = 'http://www.google.com/search?q=site:zmovie.tw ' + query
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
elif mode == 'GetTitles1': 
	GetTitles1(section, url, startPage, numOfPages)
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

