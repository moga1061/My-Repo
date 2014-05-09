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
        print 'aob get Movie Titles Menu %s' % url
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
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles1', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view')  
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

###################################################################################################################################################################################################

def GetTitles2(section, url, startPage= '1', numOfPages= '1'): # hornywhores
        print 'aob get Movie Titles Menu %s' % url
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
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles2', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view')  
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#############################################################################################################################################################################################################

def GetTitles3(section, url, startPage= '1', numOfPages= '1'): #naughtyblog
        print 'aob get Movie Titles Menu %s' % url
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
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles3', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view')  
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#############################################################################################################################################################################################################

def GetTitles4(section, url, startPage= '1', numOfPages= '1'): # pornorips
        print 'aob get Movie Titles Menu %s' % url
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
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles4', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view')  
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

###########################################################################################################################################################################################

def GetTitles5(section, url, startPage= '1', numOfPages= '1'): #scenelog
        print 'aob get Movie Titles Menu %s' % url
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
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img=IconPath + 'sl1.png', fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles5', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

###########################################################################################################################################################################################

def GetTitles6(section, url, startPage= '1', numOfPages= '1'): # pornreleasez
        print 'aob get Movie Titles Menu %s' % url
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
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles6', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view') 
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

################################################################################################################################################################################################

def GetTitles7(section, url, startPage= '1', numOfPages= '1'): # naked
        print 'aob get Movie Titles Menu %s' % url
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
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles7', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view') 
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

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
        addon.add_directory({'mode': 'Menu1'}, {'title':  '[COLOR hotpink][B]Adult bay >[/B][/COLOR] >'}, img=IconPath + 'ab1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'Menu2'}, {'title':  '[COLOR hotpink][B]Horny Whores >[/B][/COLOR] >'}, img=IconPath + 'hw1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'Menu3'}, {'title':  '[COLOR hotpink][B]Naughty Blog >[/B][/COLOR] >'}, img=IconPath + 'nb1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'Menu5'}, {'title':  '[COLOR hotpink][B]SceneLog XXX >[/B][/COLOR] >'}, img=IconPath + 'sl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'Menu6'}, {'title':  '[COLOR hotpink][B]PornReleasez >[/B][/COLOR] >'}, img=IconPath + 'pr2.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'Menu4'}, {'title':  '[COLOR hotpink][B]PornoRips >[/B][/COLOR] >'}, img=IconPath + 'pr1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'Menu7'}, {'title':  '[COLOR hotpink][B]Naked XXX >[/B][/COLOR] >'}, img=IconPath + 'ns.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'ResolverSettings'}, {'title':  '[COLOR red]Resolver Settings[/COLOR] - [COLOR pink]real-debird & alldebird login[/COLOR]'}, img=IconPath + 'rset.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'help'}, {'title':  '[COLOR red]FOR HELP PLEASE GOTO...[/COLOR] [COLOR blue][B][I]www.xbmchub.com[/B][/I][/COLOR]'}, img=IconPath + 'help2.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'help'}, {'title':  '[COLOR gold][B]FOLLOW ME ON TWITTER [/B][/COLOR] [COLOR aqua][B]@TheYid009 [/B][/COLOR] '}, img=IconPath + 'theyid.png', fanart=FanartPath + 'fanart.png')
        dialog = xbmcgui.Dialog()
        if dialog.yesno("Adult's Only [COLOR deeppink][B]HUB[/B][/COLOR]","                         [COLOR red]XXX[/COLOR] [COLOR pink][B]OVER 18's/ 21's ONLY !!![/B][/COLOR] [COLOR red]XXX[/COLOR]" , "       [COLOR pink]You will need a debrid premium account for this addon[/COLOR]" , '        [COLOR lime][B]ARE YOU OVER 18/21 & HAVE DEBRID ACCOUNT ??[/COLOR][/B]','[COLOR red]NO & EXIT[/COLOR]','[COLOR lime]YES[/COLOR]'):
                exit
        else:
                exit()
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

###########################################################################################################

def Menu1():    #adult bay
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL1 + '/category/movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Movies >>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'ab1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL1 + '/category/hdtv/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Movies HD>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'ab1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL1 + '/category/clips/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX clips>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'ab1.png', fanart=FanartPath + 'fanart.png')
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
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#############################################################################################################

def Menu3():    #NaughtyBlog
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/category/siterips/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Movies SiteRips>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'nb1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/category/movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Movies Latest>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'nb1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/category/clips/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Movies Clips>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'nb1.png', fanart=FanartPath + 'fanart.png')
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
elif mode == 'GetLinks':
	GetLinks(section, url)
elif mode == 'ResolverSettings':
        urlresolver.display_settings()
elif mode == 'PlayVideo':
	PlayVideo(url, listitem)

xbmcplugin.endOfDirectory(int(sys.argv[1]))