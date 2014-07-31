import xbmc, xbmcgui, xbmcaddon, xbmcplugin
import re, string, sys, os
import urlresolver
from TheYid.common.addon import Addon
from TheYid.common.net import Net
import HTMLParser

addon_id = 'plugin.video.aob'
plugin = xbmcaddon.Addon(id=addon_id)
DB = os.path.join(xbmc.translatePath("special://database"), 'aob.db')
net = Net()
addon = Addon('plugin.video.aob', sys.argv)
BASE_URL = ''
BASE_URL1 = 'http://adultbay.org/'
BASE_URL2 = 'http://www.hornywhores.net/'
BASE_URL3 = 'http://www.naughtyblog.org/'
BASE_URL4 = 'http://pornorips.com/'
BASE_URL5 = 'http://scenelog.eu/'
BASE_URL6 = 'http://pornreleasez.com/'
BASE_URL7 = 'http://naked-sluts.us/'
BASE_URL8 = 'http://webwarez.it/'
BASE_URL35 = 'https://raw.githubusercontent.com/TheYid/yidpics/master'

######PATHS########
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

#################################################################################### Get Movie Titles #####################################################################################

def GetTitles1(section, url, startPage= '1', numOfPages= '1'): # adult-bay
    try:
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + 'page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + 'page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content
                match = re.compile('post_headerr.+?href="(.+?)".+?>(.+?)<.+?src="(.+?)".+?', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.aob/?mode=Search3&query=%s)' %(name.strip())
        		cm.append(('[COLOR hotpink][B]A[/B][/COLOR]dult [COLOR hotpink][B]HUB[/B][/COLOR] [COLOR green]Search[/COLOR]', runstring))
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles1', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view')  
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

###################################################################################################################################################################################################

def GetTitles2(section, url, startPage= '1', numOfPages= '1'): # hornywhores
    try:
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + 'page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + 'page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content
                match = re.compile('<h3.+?href="(.+?)".+?>(.+?)<.+?src="(.+?)".+?', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.aob/?mode=Search3&query=%s)' %(name.strip())
        		cm.append(('[COLOR hotpink][B]A[/B][/COLOR]dult [COLOR hotpink][B]HUB[/B][/COLOR] [COLOR green]Search[/COLOR]', runstring))
                        addon.add_directory({'mode': 'GetLinks2', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles2', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view')  
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#############################################################################################################################################################################################################

def GetTitles3(section, url, startPage= '1', numOfPages= '1'): #naughtyblog
    try:
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + 'page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + 'page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content
                match = re.compile('<h3.+?href="(.+?)".+?>(.+?)<.+?src="(.+?)".+?', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.aob/?mode=Search3&query=%s)' %(name.strip())
        		cm.append(('[COLOR hotpink][B]A[/B][/COLOR]dult [COLOR hotpink][B]HUB[/B][/COLOR] [COLOR green]Search[/COLOR]', runstring))
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles3', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view')  
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#############################################################################################################################################################################################################

def GetTitles4(section, url, startPage= '1', numOfPages= '1'): # pornorips
    try:
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + 'page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + 'page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content 
                match = re.compile('entry.+?href="(.+?)".+?>(.+?)<.+?src="(.+?)".+?', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.aob/?mode=Search3&query=%s)' %(name.strip())
        		cm.append(('[COLOR hotpink][B]A[/B][/COLOR]dult [COLOR hotpink][B]HUB[/B][/COLOR] [COLOR green]Search[/COLOR]', runstring))
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles4', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view')  
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

###########################################################################################################################################################################################

def GetTitles5(section, url, startPage= '1', numOfPages= '1'): #scenelog
    try:
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + 'page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + 'page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content
                match = re.compile('<h1>.+?href="(.+?)".+?>(.+?)<.+?', re.DOTALL).findall(html)
                for movieUrl, name in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.aob/?mode=Search3&query=%s)' %(name.strip())
        		cm.append(('[COLOR hotpink][B]A[/B][/COLOR]dult [COLOR hotpink][B]HUB[/B][/COLOR] [COLOR green]Search[/COLOR]', runstring))
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img=IconPath + 'sl1.png', fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles5', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

###########################################################################################################################################################################################

def GetTitles6(section, url, startPage= '1', numOfPages= '1'): # pornreleasez
    try:
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + 'page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + 'page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content  
                match = re.compile('entry-title.+?href="(.+?)".+?>(.+?)<.+?src="(.+?)"', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.aob/?mode=Search3&query=%s)' %(name.strip())
        		cm.append(('[COLOR hotpink][B]A[/B][/COLOR]dult [COLOR hotpink][B]HUB[/B][/COLOR] [COLOR green]Search[/COLOR]', runstring))
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles6', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view') 
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

################################################################################################################################################################################################

def GetTitles7(section, url, startPage= '1', numOfPages= '1'): # naked
    try:
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + 'page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + 'page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content
                match = re.compile('<h2.+?href="(.+?)".+?>(.+?)<.+?src="(.+?)".+?', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.aob/?mode=Search3&query=%s)' %(name.strip())
        		cm.append(('[COLOR hotpink][B]A[/B][/COLOR]dult [COLOR hotpink][B]HUB[/B][/COLOR] [COLOR green]Search[/COLOR]', runstring))
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles7', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view') 
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

################################################################################################################################################################################################

def GetTitles8(section, url, startPage= '1', numOfPages= '1'): # webwarez
    try:
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + 'page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + 'page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content
                match = re.compile('<div class="quadrato">\s*?<a href="(.+?)" title="(.+?)"><p style=".+?"><img src="(.+?)"', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.aob/?mode=Search3&query=%s)' %(name.strip())
        		cm.append(('[COLOR hotpink][B]A[/B][/COLOR]dult [COLOR hotpink][B]HUB[/B][/COLOR] [COLOR green]Search[/COLOR]', runstring))
                        addon.add_directory({'mode': 'GetLinks3', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles7', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view') 
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#------------------------------------------------------------------------------- github iptv -------------------------------------------------------------------------------------#

def GetTitles35(url):                                           
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('<>title="(.+?)" href="(.+?)" />< src="(.+?)"').findall(content)
        for name, url, img in match:
                addon.add_directory({'mode': 'PlayVideo1', 'url': url, 'listitem': listitem}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------------------- github help -----------------------------------------------------------------------------------#

def GetTitles37(url):
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('<>title="(.+?)" href="(.+?)" />< src="(.+?)"').findall(content)
        for name, url, img in match:
                addon.add_directory({'mode': 'PlayVideo1', 'url': url, 'listitem': listitem}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def PlayVideo1(url, listitem):
    try:
        print 'in PlayVideo %s' % url
        stream_url = urlresolver.HostedMediaFile(url).resolve()
        xbmc.Player().play(stream_url)
        addon.add_directory({'mode': 'help'}, {'title':  '[COLOR slategray][B]^^^ Press back ^^^[/B] [/COLOR]'},'','')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry Link may have been removed ![/B][/COLOR],[COLOR lime][B]Please try a different link/host !![/B][/COLOR],7000,"")")



##.replace('/', ' ')## \s*? ##
######################################################################## Get Links ####################################################################################################

def GetLinks(section, url): # Get Links
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('href="(.+?)"').findall(content)
        listitem = GetMediaInfo(content)
        for url in match:
                host = GetDomain(url)
                if 'Unknown' in host:
                                continue
                        
                # ignore .rar files
                r = re.search('\.rar[(?:\.html|\.htm)]*', url, re.IGNORECASE)
                if r:
                        continue
                print '*****************************' + host + ' : ' + url
                if urlresolver.HostedMediaFile(url= url):
                        print 'in GetLinks if loop'
                        title = url.rpartition('/')
                        title = title[2].replace('.html', '')
                        title = title.replace('.htm', '')
                        title = title.replace('.rar', '[COLOR red][B][I]RAR no streaming[/B][/I][/COLOR]')
                        title = title.replace('rar', '[COLOR red][B][I]RAR no streaming[/B][/I][/COLOR]')
                        title = title.replace('x264','')
                        title = title.replace('XXX','[COLOR red][B][I]XXX[/B][/I][/COLOR]')
                        title = title.replace('480p','[COLOR coral][B][I]480p[/B][/I][/COLOR]')
                        title = title.replace('720p','[COLOR gold][B][I]720p[/B][/I][/COLOR]')
                        title = title.replace('1080p','[COLOR orange][B][I]1080p[/B][/I][/COLOR]')
                        title = title.replace('mkv','[COLOR gold][B][I]MKV[/B][/I][/COLOR] ')
                        title = title.replace('avi','[COLOR pink][B][I]AVI[/B][/I][/COLOR] ')
                        title = title.replace('mp4','[COLOR purple][B][I]MP4[/B][/I][/COLOR] ')
                        host = host.replace('k2s.cc','[COLOR red]Unsupported Link[/COLOR]')
                        host = host.replace('keep2share.cc','[COLOR red]Unsupported Link[/COLOR]')
                        host = host.replace('ryushare.com','[COLOR red]Unsupported Link[/COLOR]')
                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title': host + ' [COLOR pink][B]:-[/B][/COLOR] ' + title}, img=IconPath + 'play1.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

######################################################################## Get Links2 ####################################################################################################

def GetLinks2(section, url): # Get Links2
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('<p><a href="(.+?)"').findall(content)
        match2 = re.compile('<a href="(.+?)"').findall(content)
        listitem = GetMediaInfo(content)
        for url in match + match2:
                host = GetDomain(url)
                if 'Unknown' in host:
                                continue
                        
                # ignore .rar files
                r = re.search('\.rar[(?:\.html|\.htm)]*', url, re.IGNORECASE)
                if r:
                        continue
                print '*****************************' + host + ' : ' + url
                if urlresolver.HostedMediaFile(url= url):
                        print 'in GetLinks if loop'
                        title = url.rpartition('/')
                        title = title[2].replace('.html', '')
                        title = title.replace('.htm', '')
                        title = title.replace('.rar', '[COLOR red][B][I]RAR no streaming[/B][/I][/COLOR]')
                        title = title.replace('rar', '[COLOR red][B][I]RAR no streaming[/B][/I][/COLOR]')
                        title = title.replace('x264','')
                        title = title.replace('XXX','[COLOR red][B][I]XXX[/B][/I][/COLOR]')
                        title = title.replace('480p','[COLOR coral][B][I]480p[/B][/I][/COLOR]')
                        title = title.replace('720p','[COLOR gold][B][I]720p[/B][/I][/COLOR]')
                        title = title.replace('1080p','[COLOR orange][B][I]1080p[/B][/I][/COLOR]')
                        title = title.replace('mkv','[COLOR gold][B][I]MKV[/B][/I][/COLOR] ')
                        title = title.replace('avi','[COLOR pink][B][I]AVI[/B][/I][/COLOR] ')
                        title = title.replace('mp4','[COLOR purple][B][I]MP4[/B][/I][/COLOR] ')
                        host = host.replace('k2s.cc','[COLOR red]Unsupported Link[/COLOR]')
                        host = host.replace('keep2share.cc','[COLOR red]Unsupported Link[/COLOR]')
                        host = host.replace('ryushare.com','[COLOR red]Unsupported Link[/COLOR]')
                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title': host + ' [COLOR pink][B]:-[/B][/COLOR] ' + title}, img=IconPath + 'play1.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

######################################################################## Get Links3 ####################################################################################################

def GetLinks3(section, url): # Get Links3
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('<p><a rel="nofollow" target="_blank" href=".+?">(.+?)</a></p>').findall(content)
        match2 = re.compile('class="external" title="(.+?)"').findall(content)
        listitem = GetMediaInfo(content)
        for url in match + match2:
                host = GetDomain(url)
                if 'Unknown' in host:
                                continue
                        
                # ignore .rar files
                r = re.search('\.rar[(?:\.html|\.htm)]*', url, re.IGNORECASE)
                if r:
                        continue
                print '*****************************' + host + ' : ' + url
                if urlresolver.HostedMediaFile(url= url):
                        print 'in GetLinks if loop'
                        title = url.rpartition('/')
                        title = title[2].replace('.html', '')
                        title = title.replace('.htm', '')
                        title = title.replace('.rar', '[COLOR red][B][I]RAR no streaming[/B][/I][/COLOR]')
                        title = title.replace('rar', '[COLOR red][B][I]RAR no streaming[/B][/I][/COLOR]')
                        title = title.replace('x264','')
                        title = title.replace('XXX','[COLOR red][B][I]XXX[/B][/I][/COLOR]')
                        title = title.replace('480p','[COLOR coral][B][I]480p[/B][/I][/COLOR]')
                        title = title.replace('720p','[COLOR gold][B][I]720p[/B][/I][/COLOR]')
                        title = title.replace('1080p','[COLOR orange][B][I]1080p[/B][/I][/COLOR]')
                        title = title.replace('mkv','[COLOR gold][B][I]MKV[/B][/I][/COLOR] ')
                        title = title.replace('avi','[COLOR pink][B][I]AVI[/B][/I][/COLOR] ')
                        title = title.replace('mp4','[COLOR purple][B][I]MP4[/B][/I][/COLOR] ')
                        host = host.replace('k2s.cc','[COLOR red]Unsupported Link[/COLOR]')
                        host = host.replace('keep2share.cc','[COLOR red]Unsupported Link[/COLOR]')
                        host = host.replace('ryushare.com','[COLOR red]Unsupported Link[/COLOR]')
                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title': host + ' [COLOR pink][B]:-[/B][/COLOR] ' + title}, img=IconPath + 'play1.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

############################################################################################################################################

def PlayVideo(url, listitem):
    try:
        print 'in PlayVideo %s' % url
        stream_url = urlresolver.HostedMediaFile(url).resolve()
        xbmc.Player().play(stream_url)
        addon.add_directory({'mode': 'help'}, {'title':  '[COLOR slategray][B]^ Press back ^[/B] [/COLOR]'},'','')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry Link may have been removed ![/B][/COLOR],[COLOR lime][B]Please try a different link/host !![/B][/COLOR],7000,"")")

############################################################################################################################################

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

################################################################################################################################################################################

def MainMenu():    #homescreen
        addon.add_directory({'mode': 'GetSearchQuery3'},  {'title':  '[COLOR khaki][B]M[/COLOR][COLOR blue]E[/COLOR][COLOR salmon]G[/COLOR][COLOR darkseagreen]A[/COLOR][/B] : [COLOR hotpink][B]A[/B][/COLOR]dult [COLOR hotpink][B]HUB[/B][/COLOR] [COLOR green]Search[/COLOR]'}, img=IconPath + 'msearch.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'Menu1'}, {'title':  '[COLOR hotpink][B]Adult bay >[/B][/COLOR] >'}, img=IconPath + 'ab1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'Menu2'}, {'title':  '[COLOR hotpink][B]Horny Whores >[/B][/COLOR] >'}, img=IconPath + 'hw1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'Menu3'}, {'title':  '[COLOR hotpink][B]Naughty Blog >[/B][/COLOR] >'}, img=IconPath + 'nb1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'Menu5'}, {'title':  '[COLOR hotpink][B]SceneLog XXX >[/B][/COLOR] >'}, img=IconPath + 'sl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'Menu6'}, {'title':  '[COLOR hotpink][B]PornReleasez >[/B][/COLOR] >'}, img=IconPath + 'pr2.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'Menu4'}, {'title':  '[COLOR hotpink][B]PornoRips >[/B][/COLOR] >'}, img=IconPath + 'pr1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'Menu7'}, {'title':  '[COLOR hotpink][B]Naked XXX >[/B][/COLOR] >'}, img=IconPath + 'ns.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'Menu8'}, {'title':  '[COLOR hotpink][B]webwarez >[/B][/COLOR] >'}, img=IconPath + 'ww.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'ResolverSettings'}, {'title':  '[COLOR red]Resolver Settings[/COLOR] - [COLOR pink]real-debird & alldebird login[/COLOR]'}, img=IconPath + 'rset.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'help'}, {'title':  '[COLOR red]FOR HELP PLEASE GOTO...[/COLOR] [COLOR blue][B][I]www.xbmchub.com[/B][/I][/COLOR]'}, img=IconPath + 'help2.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'HelpMenu'}, {'title':  '[COLOR hotpink][B]News & Help  >[/B][/COLOR] >'}, img=IconPath + 'hn.png', fanart=FanartPath + 'fanart.png')
        dialog = xbmcgui.Dialog()
        if dialog.yesno("Adult's Only [COLOR deeppink][B]HUB[/B][/COLOR]","                         [COLOR red]XXX[/COLOR] [COLOR pink][B]OVER 18's/ 21's ONLY !!![/B][/COLOR] [COLOR red]XXX[/COLOR]" , "       [COLOR pink]You will need a debrid premium account for this addon[/COLOR]" , '        [COLOR lime][B]ARE YOU OVER 18/21 & HAVE DEBRID ACCOUNT ??[/COLOR][/B]','[COLOR red]NO & EXIT[/COLOR]','[COLOR lime]YES[/COLOR]'):
                exit
        else:
                exit()
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#-----------------------help---------------------------------------help-----------------------------help--------------------------help-------------------------------help-------#

def HelpMenu(): 
        addon.add_directory({'mode': 'Help'}, {'title':  '[COLOR hotpink][B]A[/B][/COLOR]dult [COLOR hotpink][B]HUB[/B][/COLOR] : [COLOR lime]News >[/COLOR] >'}, img=IconPath + 'hn.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles37', 'url': BASE_URL35 + '/help.txt'}, {'title':  '[COLOR deeppink]How to videos >[/COLOR] >'}, img=IconPath + 'hn.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'ResolverSettings'}, {'title':  '[COLOR red]Resolver Settings >[/COLOR] >'}, img=IconPath + 'rset.png', fanart=FanartPath + 'fanart.png')  
        addon.add_directory({'mode': 'HelpMenu'}, {'title':  '[B][COLOR gold]If you like this addon[/COLOR][/B]'}, img=IconPath + 'theyid.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'HelpMenu'}, {'title':  '[B][COLOR gold]Please install Entertainment HUB from TheYids REPO[/COLOR][/B]'}, img= 'https://raw.githubusercontent.com/TheYid/My-Repo/master/plugin.video.allinone/icon.png', fanart= 'https://raw.githubusercontent.com/TheYid/My-Repo/master/plugin.video.allinone/fanart.jpg')
        addon.add_directory({'mode': 'HelpMenu'}, {'title':  '[B][COLOR gold]& if you like rave music install Rave player from TheYids REPO[/COLOR][/B]'}, img= 'https://raw.githubusercontent.com/TheYid/My-Repo/master/plugin.audio.raveplayer/icon.png', fanart= 'https://raw.githubusercontent.com/TheYid/My-Repo/master/plugin.audio.raveplayer/fanart.jpg')
        addon.add_directory({'mode': 'HelpMenu'}, {'title':  '[B][COLOR blue]System/Add-ons/Get Add-ons/TheYids REPO[/COLOR][/B]'}, img= 'https://raw.githubusercontent.com/TheYid/My-Repo/master/repository.TheYid/icon.png', fanart= 'https://raw.githubusercontent.com/TheYid/My-Repo/master/plugin.video.allinone/fanart.jpg')
        addon.add_directory({'mode': 'HelpMenu'}, {'title':  '[B][COLOR aqua]@TheYid009[/COLOR][/B] - [B][COLOR gold]Add me on twitter for all the latest news & updates..[/COLOR][/B]'}, img=IconPath + 'theyid.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

###########################################################################################################

def Menu1():    #adult bay
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL1 + '/category/movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Movies >>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'ab1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL1 + '/category/hdtv/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Movies HD>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'ab1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL1 + '/category/clips/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX clips>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'ab1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetSearchQuery1'},  {'title':  '[COLOR green]Search[/COLOR] [COLOR pink]Adult Bay[/COLOR]'}, img=IconPath + 'searches.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#############################################################################################################

def Menu2():    #hornywhores
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL2 + '/category/movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Movies>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'hw1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL2 + '/category/clips/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Movies Clips>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'hw1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL2 + '/category/hd/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Movies HD>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'hw1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL2 + '/category/movies/dvd-r/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Movies DVD-R>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'hw1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetSearchQuery'},  {'title':  '[COLOR green]Search[/COLOR] [COLOR pink]Horny Whores[/COLOR]'}, img=IconPath + 'searches.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#############################################################################################################

def Menu3():    #NaughtyBlog
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/category/siterips/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Movies SiteRips>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'nb1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/category/movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Movies Latest>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'nb1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/category/clips/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Movies Clips>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'nb1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetSearchQuery2'},  {'title':  '[COLOR green]Search[/COLOR] [COLOR pink]NaughtyBlog[/COLOR]'}, img=IconPath + 'searches.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

############################################################################################################

def Menu4():    #PornoRips
        addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL4 + '/category/movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Movies>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'pr1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL4 + '/category/clips/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Movies Clips>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'pr1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL4 + '/category/hd-porn/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Movies HD>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'pr1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL4 + '/category/movies/no-english-movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Movies None english>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'pr1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL4 + '/category/adult-sites-rips/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Movies SiteRips>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'pr1.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

###########################################################################################################

def Menu5():    #SceneLog
        addon.add_directory({'mode': 'GetTitles5', 'section': 'ALL', 'url': BASE_URL5 + '/xxx/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Movies HD 1080p 720p >>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'sl1.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

###########################################################################################################

def Menu6():    #pornreleasez
        addon.add_directory({'mode': 'GetTitles6', 'section': 'ALL', 'url': BASE_URL6 + '/category/clips/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Movies Clips>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'pr2.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles6', 'section': 'ALL', 'url': BASE_URL6 + '/category/clips/clips-hd/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Movies Clips HD>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'pr2.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles6', 'section': 'ALL', 'url': BASE_URL6 + '/category/movies/dvdr/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Movies Dvdr>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'pr2.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles6', 'section': 'ALL', 'url': BASE_URL6 + '/category/movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Movies >>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'pr2.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles6', 'section': 'ALL', 'url': BASE_URL6 + '/category/movies/movies-hd/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Movies HD>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'pr2.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles6', 'section': 'ALL', 'url': BASE_URL6 + '/category/site-rips/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Movies Site Rips>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'pr2.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles6', 'section': 'ALL', 'url': BASE_URL6 + '/category/movies/vintage/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Movies Vintage>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'pr2.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles6', 'section': 'ALL', 'url': BASE_URL6 + '/category/clips/celebrity/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Movies Celebrity>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'pr2.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

###########################################################################################################

def Menu7():    #naked
        addon.add_directory({'mode': 'GetTitles7', 'section': 'ALL', 'url': BASE_URL7 + '/category/clips/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Movies Clips>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'ns.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles7', 'section': 'ALL', 'url': BASE_URL7 + '/category/clips/hd-clips/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Movies Clips HD>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'ns.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles7', 'section': 'ALL', 'url': BASE_URL7 + '/category/movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Movies >>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'ns.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles7', 'section': 'ALL', 'url': BASE_URL7 + '/category/movies/hd-movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Movies HD>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'ns.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles7', 'section': 'ALL', 'url': BASE_URL7 + '/category/siterips/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Movies Site Rips>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'ns.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

###########################################################################################################

def Menu8():  #webwarez
        addon.add_directory({'mode': 'GetTitles8', 'section': 'ALL', 'url': BASE_URL8 + '/xxx/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Latest added>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'ww.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles8', 'section': 'ALL', 'url': BASE_URL8 + '/xxx/category/straight/clips/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Latest clips>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'ww.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles8', 'section': 'ALL', 'url': BASE_URL8 + '/xxx/category/movies-xxx/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Latest movies>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'ww.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles8', 'section': 'ALL', 'url': BASE_URL8 + '/xxx/category/straight/movies-xxx/international-movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Latest international movies>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'ww.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles8', 'section': 'ALL', 'url': BASE_URL8 + '/xxx/category/film-porno-italian/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Latest italian movies>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'ww.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

###################################################################################### viewType  ##########################################################################

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

######################################################################## searches #################################################################################################

#hw
def GetSearchQuery():
	last_search = addon.load_data('search')
	if not last_search: last_search = ''
	keyboard = xbmc.Keyboard()
        keyboard.setHeading('[COLOR green]Search [/COLOR] [COLOR pink]Horny Whores[/COLOR]')
	keyboard.setDefault(last_search)
	keyboard.doModal()
	if (keyboard.isConfirmed()):
                query = keyboard.getText()
                addon.save_data('search',query)
                Search(query)
	else:
                return  
def Search(query):
        url = 'http://www.hornywhores.net/search/ ' + query 
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h3.+?href="(.+?)".+?>(.+?)<.+?src="(.+?)".+?', re.DOTALL).findall(html)
        for url, title, img in match:
                addon.add_directory({'mode': 'GetLinks2', 'url': url}, {'title':  title}, img= img, fanart=FanartPath + 'fanart.png')
	xbmcplugin.endOfDirectory(int(sys.argv[1]))

###############################################################################

#ab
def GetSearchQuery1():
	last_search = addon.load_data('search')
	if not last_search: last_search = ''
	keyboard = xbmc.Keyboard()
        keyboard.setHeading('[COLOR green]Search [/COLOR] [COLOR pink]Adult Bay[/COLOR]')
	keyboard.setDefault(last_search)
	keyboard.doModal()
	if (keyboard.isConfirmed()):
                query = keyboard.getText()
                addon.save_data('search',query)
                Search1(query)
	else:
                return  
def Search1(query):
        url = 'http://adultbay.org/search/ ' + query 
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('post_headerr.+?href="(.+?)".+?>(.+?)<.+?src="(.+?)".+?', re.DOTALL).findall(html)
        for url, title, img in match:
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title}, img= img, fanart=FanartPath + 'fanart.png')
	xbmcplugin.endOfDirectory(int(sys.argv[1]))

###############################################################################

#nb
def GetSearchQuery2():
	last_search = addon.load_data('search')
	if not last_search: last_search = ''
	keyboard = xbmc.Keyboard()
        keyboard.setHeading('[COLOR green]Search [/COLOR] [COLOR pink]NaughtyBlog[/COLOR]')
	keyboard.setDefault(last_search)
	keyboard.doModal()
	if (keyboard.isConfirmed()):
                query = keyboard.getText()
                addon.save_data('search',query)
                Search2(query)
	else:
                return  
def Search2(query):
        url = 'http://www.naughtyblog.org/?s= ' + query 
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h3.+?href="(.+?)".+?>(.+?)<.+?src="(.+?)".+?', re.DOTALL).findall(html)
        for url, title, img in match:
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title}, img= img, fanart=FanartPath + 'fanart.png')
	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------mega search---------------------------------------------------------------------------------------#

def GetSearchQuery3():
	last_search = addon.load_data('search')
	if not last_search: last_search = ''
	keyboard = xbmc.Keyboard()
        keyboard.setHeading('[COLOR khaki][B]M[/COLOR][COLOR blue]E[/COLOR][COLOR salmon]G[/COLOR][COLOR darkseagreen]A[/COLOR][/B] : [COLOR hotpink][B]A[/B][/COLOR]dult [COLOR hotpink][B]HUB[/B][/COLOR] [COLOR green]Search[/COLOR]')
	keyboard.setDefault(last_search)
	keyboard.doModal()
	if (keyboard.isConfirmed()):
                query = keyboard.getText()
                addon.save_data('search',query)
                Search3(query)
	else:
                return  
def Search3(query):
    try:
        url = 'http://www.hornywhores.net/search/ ' + query 
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h3.+?href="(.+?)".+?>(.+?)<.+?src="(.+?)".+?', re.DOTALL).findall(html)
        for url, title, img in match:
                addon.add_directory({'mode': 'GetLinks2', 'url': url}, {'title':  title + ' - ' + '[COLOR pink]hornywhores[/COLOR]'}, img= img, fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry hornywhores search is down [/B][/COLOR],[COLOR olive][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))
    try:
        url = 'http://adultbay.org/search/ ' + query 
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('post_headerr.+?href="(.+?)".+?>(.+?)<.+?src="(.+?)".+?', re.DOTALL).findall(html)
        for url, title, img in match:
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title + ' - ' + '[COLOR pink]adultbay[/COLOR]'}, img= img, fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry adultbay search is down [/B][/COLOR],[COLOR olive][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))
    try:
        url = 'http://www.naughtyblog.org/?s= ' + query 
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h3.+?href="(.+?)".+?>(.+?)<.+?src="(.+?)".+?', re.DOTALL).findall(html)
        for url, title, img in match:
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title + ' - ' + '[COLOR pink]NaughtyBlog[/COLOR]'}, img= img, fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry naughtyblog search is down [/B][/COLOR],[COLOR olive][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))
    try:
        url = 'http://naked-sluts.us/?s= ' + query 
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h2.+?href="(.+?)".+?>(.+?)<.+?src="(.+?)".+?', re.DOTALL).findall(html)
        for url, title, img in match:
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title + ' - ' + '[COLOR pink]naked-sluts[/COLOR]'}, img= img, fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry naked-sluts search is down [/B][/COLOR],[COLOR olive][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))
    try:
        url = 'http://pornreleasez.com/?s= ' + query 
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('entry-title.+?href="(.+?)".+?>(.+?)<.+?src="(.+?)"', re.DOTALL).findall(html)
        for url, title, img in match:
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title + ' - ' + '[COLOR pink]pornreleasez[/COLOR]'}, img= img, fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry pornreleasez search is down [/B][/COLOR],[COLOR olive][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))
    try:
        url = 'http://scnlog.eu/?s= ' + query + '&cat=9'
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h1>.+?href="(.+?)".+?>(.+?)<.+?', re.DOTALL).findall(html)
        for url, title in match:
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title + ' - ' + '[COLOR pink]scnlog[/COLOR]'}, img= 'https://raw.githubusercontent.com/TheYid/yidpics/8333f2912d71cc7ddd71a7cee9714dfe263ee543/icons/nopic.png', fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry scnlog search is down [/B][/COLOR],[COLOR olive][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))
    try:
        url = 'http://www.filestube.to/query.html?q='+ query + '&select=All'
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('target="_blank" rel="nofollow" href=".+?"><span id="/video/(.+?)">.+?</span></a>', re.DOTALL).findall(html)
        for url in match:
                addon.add_directory({'mode': 'GetLinks', 'url': 'http://www.filestube.to/video/' + url}, {'title': url.replace('-', ' ').replace('.html', ' ') + ' [COLOR lavender](filetube)[/COLOR]'}, img= 'https://raw.githubusercontent.com/TheYid/yidpics/8333f2912d71cc7ddd71a7cee9714dfe263ee543/icons/nopic.png', fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry filetube search is down [/B][/COLOR],[COLOR olive][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))
    try:
        url = 'http://pornorips.com/?s= ' + query 
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<center><h2><a href="(.+?)" rel="bookmark" title=".+?">(.+?)</a></h2></center>\s*?</div>\s*?<div class="post-content" style="padding-top:7px;">\s*?<div class="thumb">\s*?<a href=".+?" rel="bookmark" title= ".+?"><img src="(.+?)" ', re.DOTALL).findall(html)
        for url, title, img in match:
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title + ' - ' + '[COLOR pink]pornorips[/COLOR]'}, img= img, fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry pornorips search is down [/B][/COLOR],[COLOR olive][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))
    try:
        url = 'http://webwarez.it/xxx/?s= ' + query 
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<div class="quadrato">\s*?<a href="(.+?)" title="(.+?)"><p style=".+?"><img src="(.+?)"', re.DOTALL).findall(html)
        for url, title, img in match:
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title + ' - ' + '[COLOR pink]webwarez[/COLOR]'}, img= img, fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry webwarez search is down [/B][/COLOR],[COLOR olive][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))


##.replace('/', ' ')## \s*? ##
##########################################################################################################################################################################################

if mode == 'main': 
	MainMenu()
elif mode == 'GetTitles': 
	GetTitles(section, url, startPage, numOfPages)
elif mode == 'GetTitles1': 
	GetTitles1(section, url, startPage, numOfPages)
elif mode == 'GetTitles2': 
	GetTitles2(section, url, startPage, numOfPages)
elif mode == 'GetTitles3': 
	GetTitles3(section, url, startPage, numOfPages)
elif mode == 'GetTitles4': 
	GetTitles4(section, url, startPage, numOfPages)
elif mode == 'GetTitles5': 
	GetTitles5(section, url, startPage, numOfPages)	
elif mode == 'GetTitles6': 
	GetTitles6(section, url, startPage, numOfPages)	
elif mode == 'GetTitles7': 
	GetTitles7(section, url, startPage, numOfPages)
elif mode == 'GetTitles8': 
	GetTitles8(section, url, startPage, numOfPages)
elif mode == 'GetTitles35': 
	GetTitles35(section, url, startPage, numOfPages)
elif mode == 'GetTitles37': 
	GetTitles37(section, url, startPage, numOfPages)
elif mode == 'Categories':
        Categories(section)
elif mode == 'Categories1':
        Categories1(section)
elif mode == 'Menu0':
        Menu0()
elif mode == 'Menu1':
        Menu1()
elif mode == 'Menu2':
        Menu2()
elif mode == 'Menu3':
        Menu3()
elif mode == 'Menu4':
        Menu4()
elif mode == 'Menu5':
        Menu5()
elif mode == 'Menu6':
        Menu6()
elif mode == 'Menu7':
        Menu7()
elif mode == 'Menu8':
        Menu8()
elif mode == 'HelpMenu':
        HelpMenu()
elif mode == 'GetLinks':
	GetLinks(section, url)
elif mode == 'GetLinks2':
	GetLinks2(section, url)
elif mode == 'GetLinks3':
	GetLinks3(section, url)
elif mode == 'ResolverSettings':
        urlresolver.display_settings()
elif mode == 'PlayVideo':
	PlayVideo(url, listitem)
elif mode == 'PlayVideo1':
	PlayVideo1(url, listitem)
elif mode == 'GetSearchQuery':
	GetSearchQuery()
elif mode == 'Search':
	Search(query)
elif mode == 'GetSearchQuery1':
	GetSearchQuery1()
elif mode == 'Search1':
	Search1(query)
elif mode == 'GetSearchQuery2':
	GetSearchQuery2()
elif mode == 'Search2':
	Search2(query)
elif mode == 'GetSearchQuery3':
	GetSearchQuery3()
elif mode == 'Search3':
	Search3(query)
elif mode == 'Help':
    import helpbox
    helpbox.HelpBox()

xbmcplugin.endOfDirectory(int(sys.argv[1]))