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

addon_id = 'plugin.video.1-linkmovies'
plugin = xbmcaddon.Addon(id=addon_id)

DB = os.path.join(xbmc.translatePath("special://database"), '1-linkmovies.db')
BASE_URL = 'http://1-linkmovies.com/'
net = Net()
addon = Addon('plugin.video.1-linkmovies', sys.argv)

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
        print '1-linkmovies get Movie Titles Menu %s' % url
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + '/page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + '/page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content
                match = re.compile('video-baslik.+?href="(.+?)".+?>(.+?)<.+?src=.+?', re.DOTALL).findall(html)
                for movieUrl, name in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img=IconPath + 'logo.png', fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]NEXT PAGE >>[/I][/B][/COLOR]'}, img=IconPath + 'next.png', fanart=FanartPath + 'fanart.png')
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))


def GetLinks(section, url): # Get Links
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(str(url)).content
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
                name = host
                hosted_media = urlresolver.HostedMediaFile(url=url, title=name)
                sources.append(hosted_media)

                
        find = re.search('commentblock', html)
        if find:
                print 'in comments if'
                html = html[find.end():]
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
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue]Latest Movies [/COLOR]>> [COLOR red] (Movies with[/COLOR] BRRIP 720p[COLOR red] at the end have no links)[/COLOR]'}, img=IconPath + '99.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GMenu'}, {'title':  '[COLOR blue]Categories[/COLOR] >>'}, img=IconPath + '99.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetSearchQuery'},  {'title':  '[COLOR green]Search 1-linkmovies[/COLOR]'}, img=IconPath + 'search.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'ResolverSettings'}, {'title':  '[COLOR red]Resolver Settings[/COLOR]'}, img=IconPath + 'settings.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'Help'}, {'title':  '[COLOR pink]FOR HELP ON THIS ADDON PLEASE GOTO...[/COLOR] [COLOR gold][B][I]www.xbmchub.com[/B][/I][/COLOR]'}, img=IconPath + 'help.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'help'}, {'title':  '[COLOR aqua][B]FOLLOW ME ON TWITTER [/B][/COLOR] [COLOR gold][B][I]@TheYid009 [/B][/I][/COLOR]'}, img=IconPath + 'theyid.png', fanart=FanartPath + 'fanart.png')

        addon_handle = int(sys.argv[1])
        xbmcplugin.setContent(addon_handle, 'audio')
        url = 'http://www.'
        li = xbmcgui.ListItem('[B][COLOR gold]Please download Entertainment HUB from TheYids REPO[/COLOR][/B]', thumbnailImage= 'https://raw.githubusercontent.com/TheYid/My-Repo/master/plugin.video.allinone/icon.png')
        li.setProperty('fanart_image', 'https://raw.githubusercontent.com/TheYid/My-Repo/master/plugin.video.allinone/fanart.jpg')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

        addon_handle = int(sys.argv[1])
        xbmcplugin.setContent(addon_handle, 'audio')
        url = 'http://www.'
        li = xbmcgui.ListItem('[B][COLOR gold]Or if you like rave music download Rave player from TheYids REPO[/COLOR][/B]', thumbnailImage= 'https://raw.githubusercontent.com/TheYid/My-Repo/master/plugin.audio.raveplayer/icon.png')
        li.setProperty('fanart_image', 'https://raw.githubusercontent.com/TheYid/My-Repo/master/plugin.audio.raveplayer/fanart.jpg')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
        xbmcplugin.endOfDirectory(addon_handle)

def GMenu():    #G
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/categories/movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Movies >>'}, img=IconPath + '99.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/categories/action',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Action >>'}, img=IconPath + '99.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/categories/adventure',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Adventure >>'}, img=IconPath + '99.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/categories/classic-movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Classic >>'}, img=IconPath + '99.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/categories/comedy',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Comedy >>'}, img=IconPath + '99.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/categories/crime',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Crime >>'}, img=IconPath + '99.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/categories/documentary',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Documentary >>'}, img=IconPath + '99.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/categories/drama',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Drama >>'}, img=IconPath + '99.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/categories/fantasy',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Fantasy >>'}, img=IconPath + '99.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/categories/horror',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Horror >>'}, img=IconPath + '99.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/categories/romance',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Romance >>'}, img=IconPath + '99.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/categories/science-fiction',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sci Fi >>'}, img=IconPath + '99.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/categories/thriller',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Thriller >>'}, img=IconPath + '99.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/categories/war-movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'War >>'}, img=IconPath + '99.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/categories/western',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Western >>'}, img=IconPath + '99.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/categories/kidz-only-zone',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue]Kidz only zone >>[/COLOR]'}, img=IconPath + '99.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/categories/disney-movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Disney >>'}, img=IconPath + '99.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/categories/cartoons',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'cartoons >>'}, img=IconPath + '99.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))




def GetSearchQuery():
	last_search = addon.load_data('search')
	if not last_search: last_search = ''
	keyboard = xbmc.Keyboard()
        keyboard.setHeading('[COLOR green]Search 1-link movies[/COLOR]')
	keyboard.setDefault(last_search)
	keyboard.doModal()
	if (keyboard.isConfirmed()):
                query = keyboard.getText()
                addon.save_data('search',query)
                Search(query)
	else:
                return

        
def Search(query):
        url = 'http://www.google.com/search?q=site:1-linkmovies.com ' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h3 class="r"><a href="(.+?)".+?onmousedown=".+?">(.+?)</a>').findall(html)
        for url, title in match:
                title = title.replace('<b>...</b>', '').replace('<em>', '').replace('</em>', '')
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title})
	xbmcplugin.endOfDirectory(int(sys.argv[1]))



if mode == 'main': 
	MainMenu()
elif mode == 'GMenu':
        GMenu()
elif mode == 'GetTitles': 
	GetTitles(section, url, startPage, numOfPages)
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

