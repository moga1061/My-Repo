import xbmc, xbmcgui, xbmcaddon, xbmcplugin
import re, string, sys, os
import urlresolver
from TheYid.common.addon import Addon
from TheYid.common.net import Net
import HTMLParser
addon_id = 'plugin.video.theyidrh'
plugin = xbmcaddon.Addon(id=addon_id)
net = Net()
addon = Addon('plugin.video.theyidrh', sys.argv)
DB = os.path.join(xbmc.translatePath("special://database"), 'theyidrh.db')

########### url's ##########
BASE_URL = 'http://rls-center.com/'
BASE_URL1 = 'http://www.scnsrc.me/'
BASE_URL2 = 'http://scenelog.eu/'
BASE_URL3 = 'http://crazyhdsource.com/'
BASE_URL5 = 'http://www.theextopia.com/'
BASE_URL6 = 'http://com2dl.com/'
BASE_URL7 = 'http://www.wrzko.eu/'
BASE_URL8 = 'http://sceper.ws/'
BASE_URL9 = 'http://scenedown.in/'
BASE_URL10 = 'http://www.ddlvalley.rocks/'
BASE_URL11 = 'http://www.rlsbb.com/'
BASE_URL12 = 'http://300mbmovies4u.com/'
BASE_URL13 = 'http://shawnrebecca.com/'
BASE_URL15 = 'http://www.fullmatches.net/'
BASE_URL16 = 'http://tv-release.net/'
BASE_URL20 = 'http://movie4download.com/'
BASE_URL21 = 'http://rls1click.com/'
BASE_URL22 = 'http://irweb-dl.com/'
BASE_URL23 = 'http://binflix.com/'
BASE_URL24 = 'http://dx-tv.com/'
BASE_URL25 = 'http://www.flixanity.com/'
BASE_URL26 = 'http://www.tvhq.info/'
BASE_URL27 = 'https://raw.githubusercontent.com/TheYid/yidpics/master'
BASE_URL28 = 'http://www.movie.huborama.com/'
BASE_URL29 = 'http://www.movierulz.com/'
BASE_URL30 = 'http://www.moviesready.com/'

###### PATHS #########
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

#----------------------------------------------------------------------Release Center----------------------------------------------------------------------------------------------#

def GetTitles(section, url, startPage= '1', numOfPages= '1'):  
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
                match = re.compile('<h2 class="post-title"><a href="(.+?)".+?>(.+?)<.+?src="(.+?)"', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.theyidrh/?mode=Search10&query=%s)' %(name.strip().replace('.', ' '))
        		cm.append(('[COLOR blue]R[/COLOR]elease Search', runstring))
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip().replace('.', ' ')}, contextmenu_items= cm, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')        
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#--------------------------------------------------------------------------------scenelog------------------------------------------------------------------------------------------------#

def GetTitles2(section, url, startPage= '1', numOfPages= '1'): 
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
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.theyidrh/?mode=Search10&query=%s)' %(name.strip().replace('.', ' '))
        		cm.append(('[COLOR blue]R[/COLOR]elease Search', runstring))
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip().replace('.', ' ')}, contextmenu_items= cm, img= 'https://raw.githubusercontent.com/TheYid/yidpics/8333f2912d71cc7ddd71a7cee9714dfe263ee543/icons/nopic.png', fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles2', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#-----------------------------------------------------------------------------------crazyhdsource---------------------------------------------------------------------------------------------#

def GetTitles3(section, url, startPage= '1', numOfPages= '1'): 
    try:
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
                match = re.compile('<h4><span>.+?href="(.+?)".+?>(.+?)<.+?src=.+? .+?="(.+?)"', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.theyidrh/?mode=Search10&query=%s)' %(name.strip())
        		cm.append(('[COLOR blue]R[/COLOR]elease Search', runstring))
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles3', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue]Next...[/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#--------------------------------------------------------------------------------com2dl------------------------------------------------------------------------------------------------#

def GetTitles4(section, url, startPage= '1', numOfPages= '1'):
    try:
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
                match = re.compile('shstory4-img.+?href="(.+?)"><img src="(.+?)" alt="(.+?)"', re.DOTALL).findall(html)
                for movieUrl, img, name in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.theyidrh/?mode=Search10&query=%s)' %(name.strip())
        		cm.append(('[COLOR blue]R[/COLOR]elease Search', runstring))
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles4', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')       
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#------------------------------------------------------------------------------------300mbmovies4u--------------------------------------------------------------------------------------------#

def GetTitles5(section, url, startPage= '1', numOfPages= '1'): 
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
                match = re.compile('<div class="cover"><a href="(.+?)".+?.+?<img src="(.+?)".+?alt="(.+?)"', re.DOTALL).findall(html)
                for movieUrl, img, name in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.theyidrh/?mode=Search10&query=%s)' %(name.strip().replace('300MB', '').replace('400MB', '').replace('1.1GB', '').replace('900MB', '').replace('1.2GB', '').replace('1.8GB', '').replace('800MB', '').replace('350MB', '').replace('700MB', '').replace('1.7GB', '').replace('x264', ''))
        		cm.append(('[COLOR blue]R[/COLOR]elease Search', runstring))
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles5', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view') 
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#----------------------------------------------------------------------------Scene down----------------------------------------------------------------------------------------------------#

def GetTitles6(section, url, startPage= '1', numOfPages= '1'): 
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
                match = re.compile('postTitle.+?href="(.+?)".+?>(.+?)<.+?src="(.+?)".+?', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.theyidrh/?mode=Search10&query=%s)' %(name.strip())
        		cm.append(('[COLOR blue]R[/COLOR]elease Search', runstring))
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles6', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')        
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#-----------------------------------------------------------------------------------Sceper---------------------------------------------------------------------------------------------#

def GetTitles7(section, url, startPage= '1', numOfPages= '1'): 
    try:
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
                match = re.compile('<h2.+?href="(.+?)">(.+?)<.+?src="(.+?)"', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.theyidrh/?mode=Search10&query=%s)' %(name.strip())
        		cm.append(('[COLOR blue]R[/COLOR]elease Search', runstring))
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles7', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')       
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#----------------------------------------------------------------------------------rls-tv----------------------------------------------------------------------------------------------#

def GetTitles8(section, url, startPage= '1', numOfPages= '1'): 
    try:
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + '/index.php?page=' + startPage + ''
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + '/index.php?page=' + str(page) + ''
                        html = net.http_GET(pageUrl).content
                match = re.compile("width='60%' style='text-align:left; font-size:12px;font-weight:bold;'><a href='(.+?)'>(.+?)-(.+?)</a></td><td", re.DOTALL).findall(html)
                for movieUrl, name, title, in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.theyidrh/?mode=Search10&query=%s)' %(name.strip().replace('X264', '').replace('x264', ''))
        		cm.append(('[COLOR blue]R[/COLOR]elease Search', runstring))
                        addon.add_directory({'mode': 'GetLinks1', 'section': section, 'url': movieUrl}, {'title':  name.strip() + '-' + title}, contextmenu_items= cm, img=IconPath + 'rlstv.png', fanart=FanartPath + 'fanart.png') 
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#-----------------------------------------------------------------------------wrzko---------------------------------------------------------------------------------------------------#

def GetTitles9(section, url, startPage= '1', numOfPages= '1'):
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
                match = re.compile('maintitle.+?href="(.+?)".+?>(.+?)<.+?src="(.+?)"', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.theyidrh/?mode=Search10&query=%s)' %(name.strip().replace('.', ' '))
        		cm.append(('[COLOR blue]R[/COLOR]elease Search', runstring))
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip().replace('.', ' ')}, contextmenu_items= cm, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles9', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')        
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))


#----------------------------------------------------------------------------scnsrc----------------------------------------------------------------------------------------------------#

def GetTitles1(section, url, startPage= '1', numOfPages= '1'): 
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
                match = re.compile('<h2>.+?href="(.+?)".+?>(.+?)<.+?.+?src="(.+?)"', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.theyidrh/?mode=Search10&query=%s)' %(name.strip())
        		cm.append(('[COLOR blue]R[/COLOR]elease Search', runstring))
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles1', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')        
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#------------------------------------------#

def GetTitles10(section, url, startPage= '1', numOfPages= '1'): #scnsrc tv
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
                match = re.compile('<h2 class="entry-title"><a href="(.+?)".+?>(.+?)<.+?.+?src=(.+?)', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.theyidrh/?mode=Search10&query=%s)' %(name.strip())
        		cm.append(('[COLOR blue]R[/COLOR]elease Search', runstring))
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles10', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')       
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------------------ddlv-----------------------------------------------------------------------------------------------#

def GetTitles11(section, url, startPage= '1', numOfPages= '1'): 
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
                match = re.compile('<h2>.+?href="(.+?)".+?>(.+?)<.+?src="(.+?)".+?', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.theyidrh/?mode=Search10&query=%s)' %(name.strip().replace('.', ' '))
        		cm.append(('[COLOR blue]R[/COLOR]elease Search', runstring))
                        addon.add_directory({'mode': 'GetLinks3', 'section': section, 'url': movieUrl}, {'title':  name.strip().replace('.', ' ')}, contextmenu_items= cm, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles11', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')        
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#--------------------------------------------------------------------------------rlsbb------------------------------------------------------------------------------------------------#

def GetTitles12(section, url, startPage= '1', numOfPages= '1'): 
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
                match = re.compile('postHeader.+?href="(.+?)".+?>(.+?)-(.+?)<.+?src=.+? src="(.+?)"', re.DOTALL).findall(html)
                for movieUrl, name, title, img in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.theyidrh/?mode=Search10&query=%s)' %(name.strip())
        		cm.append(('[COLOR blue]R[/COLOR]elease Search', runstring))
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip() + '-' + title}, contextmenu_items= cm, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles12', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#------------------------------------#

def GetTitles13(section, url, startPage= '1', numOfPages= '1'):  #rbbsport
    try:
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + 'page/' + startPage + ''
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + 'page/' + str(page) + ''
                        html = net.http_GET(pageUrl).content                      
                match = re.compile('postTitle.+?href="(.+?)".+?>(.+?)<.+?src=.+?src="(.+?)"', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')                        
                addon.add_directory({'mode': 'GetTitles13', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue]Come back soon[/COLOR]'}, img=IconPath + '', fanart=FanartPath + 'fanart.png')        
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------------------Extopia-----------------------------------------------------------------------------------------------#

def GetTitles14(section, url, startPage= '1', numOfPages= '1'): 
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
                match = re.compile('<h2><a.+?href="(.+?)".+?>(.+?)<.+?src="(.+?)".+?', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.theyidrh/?mode=Search10&query=%s)' %(name.strip())
        		cm.append(('[COLOR blue]R[/COLOR]elease Search', runstring))
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles14', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')       
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#--------------------------------------------------------------------------------fullmatch------------------------------------------------------------------------------------------------#

def GetTitles16(section, url, startPage= '1', numOfPages= '1'): 
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
                match = re.compile('<h2><a.+?href="(.+?)".+?>(.+?)<.+?src=.+?.+?', re.DOTALL).findall(html)
                for movieUrl, name in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.theyidrh/?mode=Search10&query=%s)' %(name.strip())
        		cm.append(('[COLOR blue]R[/COLOR]elease Search', runstring))
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img=IconPath + 'fullsport.png', fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles16', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------------- Fight-BB ----------------------------------------------------------------------------------------------------#

def GetTitles17(section, url, startPage= '1', numOfPages= '1'): 
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
                match = re.compile('<h2.+?href="(.+?)".+?>(.+?)<.+?', re.DOTALL).findall(html)
                for movieUrl, name in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.theyidrh/?mode=Search11&query=%s)' %(name.strip())
        		cm.append(('[COLOR blue]R[/COLOR]elease Search', runstring))
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img=IconPath + 'fbb.png', fanart=FanartPath + 'fanart.png') 
                addon.add_directory({'mode': 'GetTitles17', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#------------------------------------------------------------------------------------- Movie4download -------------------------------------------------------------------------------#

def GetTitles20(section, url, startPage= '1', numOfPages= '1'): 
    try:
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
                match = re.compile('excerpt-thumb.+?href="(.+?)" title=".+?" rel="bookmark">\s*?<img width="320" height="450" src="(.+?)" class="alignleft wp-post-image" alt="(.+?)" />', re.DOTALL).findall(html)
                for movieUrl, img, name in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.theyidrh/?mode=Search10&query=%s)' %(name.strip().replace('Full Movie', '').replace('_', ' '))
        		cm.append(('[COLOR blue]R[/COLOR]elease Search', runstring))
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip().replace('Full Movie', '').replace('_', ' ')}, contextmenu_items= cm, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles20', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------------------- rls1click --------------------------------------------------------------------------------------#

def GetTitles21(section, url, startPage= '1', numOfPages= '1'): 
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
                        pageUrl = url + 'page/' + startPage + '/'
                        html = net.http_GET(pageUrl).content                     
                match = re.compile('post-title.+?href="(.+?)">(.+?)<.+?src="(.+?)"', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.theyidrh/?mode=Search10&query=%s)' %(name.strip())
        		cm.append(('[COLOR blue]R[/COLOR]elease Search', runstring))
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles21', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')        
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------------------- irweb-dl --------------------------------------------------------------------------------------#

def GetTitles22(section, url, startPage= '1', numOfPages= '1'): 
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
                        pageUrl = url + 'page/' + startPage + '/'
                        html = net.http_GET(pageUrl).content                     
                match = re.compile('<h1 class="entry-title"><a href="(.+?)".+?>(.+?)<.+?src="(.+?)".+?', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.theyidrh/?mode=Search10&query=%s)' %(name.strip())
        		cm.append(('[COLOR blue]R[/COLOR]elease Search', runstring))
                        addon.add_directory({'mode': 'GetLinks4', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles22', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')        
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------------------- binflix --------------------------------------------------------------------------------------#

def GetTitles23(section, url, startPage= '1', numOfPages= '1'): 
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
                match = re.compile('entry-title.+?href="(.+?)".+?>(.+?)-(.+?)<.+?src="(.+?)"', re.DOTALL).findall(html)
                for movieUrl, name, title, img in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.theyidrh/?mode=Search10&query=%s)' %(name.strip().replace('x264', ''))
        		cm.append(('[COLOR blue]R[/COLOR]elease Search', runstring))
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip() + '-' + title}, contextmenu_items= cm, img= img, fanart=FanartPath + 'fanart.png')    
                addon.add_directory({'mode': 'GetTitles23', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------------------- dx-tv --------------------------------------------------------------------------------------#

def GetTitles24(section, url, startPage= '1', numOfPages= '1'): 
    try:
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + '?paged=' + startPage + ''
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + '?paged=' + startPage + ''
                        html = net.http_GET(pageUrl).content                         
                match = re.compile('entry-title.+?href="(.+?)">(.+?)<.+?src="(.+?)"', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.theyidrh/?mode=Search11&query=%s)' %(name.strip())
        		cm.append(('[COLOR blue]R[/COLOR]elease Search', runstring))
                        addon.add_directory({'mode': 'GetLinks5', 'section': section, 'url': movieUrl}, {'title':  name.strip().replace('.', ' ')}, contextmenu_items= cm, img= img, fanart=FanartPath + 'fanart.png')    
                addon.add_directory({'mode': 'GetTitles24', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------------------- github -----------------------------------------------------------------------------------#

def GetTitles27(url):
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('<>title="(.+?)" href="(.+?)" />< src="(.+?)"').findall(content)
        for name, url, img in match:
                addon.add_directory({'mode': 'PlayVideo3', 'url': url, 'listitem': listitem}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def PlayVideo3(url, listitem):
    try:
        print 'in PlayVideo %s' % url
        stream_url = urlresolver.HostedMediaFile(url).resolve()
        xbmc.Player().play(stream_url)
        addon.add_directory({'mode': 'help'}, {'title':  '[COLOR slategray][B]^^^ Press back ^^^[/B] [/COLOR]'},'','')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry Link may have been removed ![/B][/COLOR],[COLOR lime][B]Please try a different link/host !![/B][/COLOR],7000,"")")


#---------------------------------------------------------------------------------- moviesready --------------------------------------------------------------------------------------#

def Categories(url): 
        url = BASE_URL30
        html = net.http_GET(BASE_URL30).content
        match = re.compile('<li><a href="/(.+?)"><span>.+?</span></a></li>').findall(html)
        for url in match:
                addon.add_directory({'mode': 'GetTitles30', 'url': 'http://www.moviesready.com/' + url}, {'title': 'http://www.moviesready.com/' + url}, img=IconPath + 'mr.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetTitles30(section, url, startPage= '1', numOfPages= '1'): 
    try:
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + '/page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + '/page/' + startPage + '/'
                        html = net.http_GET(pageUrl).content                         
                match = re.compile('<div class="movieposter" title=".+?">\s*?<a href="(.+?)"><img src="(.+?)" width=".+?" height=".+?" alt=".+?" title=".+?"/></a>\s*?<div class="shortname">(.+?)</div', re.DOTALL).findall(html)
                for movieUrl, img, name in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.theyidrh/?mode=Search11&query=%s)' %(name.strip())
        		cm.append(('[COLOR blue]R[/COLOR]elease Search', runstring))
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip().replace('.', ' ')}, contextmenu_items= cm, img= 'http://www.moviesready.com/' + img, fanart=FanartPath + 'fanart.png')    
                addon.add_directory({'mode': 'GetTitles30', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))


###################################### index ################################## index ################################################# index ##########################################


#---------------------------------------------------------------------------- flixanity index ---------------------------------------------------------------------------------#

def GetTitles25(query):
    try:
        pageUrl = url
        html = net.http_GET(pageUrl).content                     
        match = re.compile('<li>\s*?<a href="(.+?)" class="item" title="">\s*?<img class="img-preview spec-border"  src=".+?src=(.+?)&amp;.+?" alt=" " style=".+?"/>\s*?</a>\s*?<div class="rating-pod">\s*?<div class="left">\s*?<p><strong>(.+?)</strong></p>',re.DOTALL).findall(html)
        for name, img, query in match:
                addon.add_directory({'mode': 'Search10', 'query': query}, {'title':  query}, img= img, fanart=FanartPath + 'fanart3.png')
        setView('tvshows', 'tvshows-view')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------------------- flixanity index TV -----------------------------------------------------------------------------------#

def GetTitles25a(query):
    try:
        pageUrl = url
        html = net.http_GET(pageUrl).content                     
        match = re.compile('img-preview spec-border.+?src=".+?src=(.+?)&amp;.+?".+?href="(.+?)".+?>.+?<.+?',re.DOTALL).findall(html)
        for img, query in match:
                addon.add_directory({'mode': 'Search10', 'query': query.replace('http://www.flixanity.com/show/', '').replace('-', ' ') + ' s'}, {'title':  query.replace('http://www.flixanity.com/show/', '').replace('-', ' ')}, img= img, fanart=FanartPath + 'fanart4.png')
        setView('tvshows', 'tvshows-view')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------------------- movie index  -----------------------------------------------------------------------------------#

def GetTitles28(query):
    try:
        pageUrl = url
        html = net.http_GET(pageUrl).content                     
        match = re.compile('<div class="thumb ph " title="(.+?)">\s*?<a class=".+?" href=".+?" title=".+?" target="_blank" style="" rel="nofollow"><img src=".+?" class="ph"/></a>\s*?<a href=".+?" title=".+?" target="_blank" rel="nofollow">\s*?<div class="thumb_img_wrapper"><img src="(.+?)" alt=".+?" style=".+?" class="ph"/></div>',re.DOTALL).findall(html)
        for query, img in match:
                addon.add_directory({'mode': 'Search10', 'query': query.replace('(', '').replace(')', '').replace('.', ' ').replace('[', '').replace(']', '').replace('-', ' ').replace('RARBG', '').replace('MAJESTiC', '').replace('ACAB', '').replace('MP3', '')}, {'title':  query.replace('.', ' ').replace('[', '').replace(']', '')}, img= img, fanart=FanartPath + 'fanart3.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#------------------------------------------------------------------------------- movierulz movie index ------------------------------------------------------------------------------#

def GetTitles29(section, query, startPage= '1', numOfPages= '1'):
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
                match = re.compile('<div class="entry clearfix">\s*?<a title=".+?" href=".+?"><img width="115" height="170" src="(.+?)" class="attachment-category-thumb wp-post-image" alt="(.+?)" /></a>', re.DOTALL).findall(html)
                for img, query in match:
                        addon.add_directory({'mode': 'Search10', 'section': section, 'query': query}, {'title':  query}, img= img, fanart=FanartPath + 'fanart3.png')    
                addon.add_directory({'mode': 'GetTitles29', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart3.png')
        setView('tvshows', 'tvshows-view')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))


##.replace('/', ' ')## \s*? ## 
#################################################################################getlinks###############################################################################################

def GetLinks(section, url): # Get Links
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        r = re.search('<strong>Links.*</strong>', html)
        if r:
                content = html[r.end():]

        r = re.search('commentblock', content)
        if r:
                content = content[:r.start()]
                
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

                if urlresolver.HostedMediaFile(url= url):
                        print 'in GetLinks if loop'
                        title = url.rpartition('/')
                        title = title[2].replace('.html', '')
                        title = title.replace('.htm', '')
                        title = title.replace('.rar', '[COLOR red][B][I]RAR no streaming[/B][/I][/COLOR]')
                        title = title.replace('rar', '[COLOR red][B][I]RAR no streaming[/B][/I][/COLOR]')
                        title = title.replace('sample', '[COLOR lime]Movie Trailer[/COLOR]')
                        title = title.replace('www.', '')
                        title = title.replace ('-',' ')
                        title = title.replace('_',' ')
                        title = title.replace('.',' ')
                        title = title.replace('gaz','')
                        title = title.replace('NTb','')
                        title = title.replace('1st','[COLOR coral][B]1st HALF[/B][/COLOR]')
                        title = title.replace('2nd','[COLOR coral][B]2nd HALF[/B][/COLOR]')
                        title = title.replace('fullmatches net','')
                        title = title.replace('.',' ')
                        title = title.replace('480p','[COLOR coral][B][I]480p[/B][/I][/COLOR]')
                        title = title.replace('720p','[COLOR gold][B][I]720p[/B][/I][/COLOR]')
                        title = title.replace('1080p','[COLOR orange][B][I]1080p[/B][/I][/COLOR]')
                        title = title.replace('mkv','[COLOR gold][B][I]MKV[/B][/I][/COLOR] ')
                        title = title.replace('avi','[COLOR pink][B][I]AVI[/B][/I][/COLOR] ')
                        title = title.replace('mp4','[COLOR purple][B][I]MP4[/B][/I][/COLOR] ')
                        title = title.replace('%20',' ')
                        host = host.replace('youtube.com','[COLOR lime]Movie Trailer[/COLOR]')
                        host = host.replace('k2s.cc','[COLOR red]Unsupported Link[/COLOR]')
                        host = host.replace('ryushare.com','[COLOR red]Unsupported Link[/COLOR]')
                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title':  host + ' [COLOR gold]:[/COLOR] ' + title }, img=IconPath + 'play.png', fanart=FanartPath + 'fanart.png')

        find = re.search('commentblock', html)
        if find:
                print 'in comments if'
                html = html[find.end():]
                match = re.compile('<a href="(.+?)" rel="nofollow"', re.DOTALL).findall(html)
                print len(match)
                for url in match:
                        host = GetDomain(url)
                        if 'Unknown' in host:
                                continue
                        
                        # ignore .rar files
                        r = re.search('\.rar[(?:\.html|\.htm)]*', url, re.IGNORECASE)
                        if r:
                                continue
                        try:
                                if urlresolver.HostedMediaFile(url= url):
                                        print 'in GetLinks if loop'
                                        title = url.rpartition('/')
                                        title = title[2].replace('.html', '')
                                        title = title.replace('.htm', '')
                                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title':  host + ' : ' + title}, img=IconPath + 'play.png', fanart=FanartPath + 'fanart.png')
                        except:
                                continue
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------------------RLStv-----------------------------------------------------------------------------------------------#

def GetLinks1(section, url): 
    try:
        html = net.http_GET(str(url)).content
        sources = []
        listitem = GetMediaInfo(html)
        print 'LISTITEM: '+str(listitem)
        content = html
        print'CONTENT: '+str(listitem)
        r = re.search('<strong>Links.*</strong>', html)
        if r:
                content = html[r.end():]
        match = re.compile("href='(.+?)'").findall(content)
        listitem = GetMediaInfo(content)
        for url in match:
                host = GetDomain(url)

                if 'Unknown' in host:
                        continue
                print '*****************************' + host + ' : ' + url
                title = url.rpartition('/')
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
        addon.add_directory({'mode': 'help'}, {'title':  '[COLOR slategray][B]^^^ Press back ^^^[/B] [/COLOR]'},'','')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry Link may have been removed ![/B][/COLOR],[COLOR lime][B]Please try a different link/host !![/B][/COLOR],7000,"")")

#-------------------------------------------------------------------------------ddlvalley-------------------------------------------------------------------------------------------------#

def GetLinks3(section, url): 
    try:
        html = net.http_GET(str(url)).content
        sources = []
        listitem = GetMediaInfo(html)
        print 'LISTITEM: '+str(listitem)
        content = html
        print'CONTENT: '+str(listitem)
        match = re.compile('href="(.+?)"').findall(content)
        listitem = GetMediaInfo(content)
        for url in match:
                host = GetDomain(url)
                if 'Unknown' in host:
                                continue
                r = re.search('\part1\part2\part3\part4\part5\.rar.html\.rar\.file[(?:\.html|\.htm)]*', url, re.IGNORECASE)
                if r:
                        continue
                print '*****************************' + host + ' : ' + url
                title = url.rpartition('/')
                title = title[2].replace('.html', '')
                title = title.replace('.htm', '')
                title = title.replace('.rar', '[COLOR red][B][I]RAR no streaming[/B][/I][/COLOR]')
                title = title.replace('DDLValley.net_', ' ')
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
        addon.add_directory({'mode': 'help'}, {'title':  '[COLOR slategray][B]^^^ Press back ^^^[/B] [/COLOR]'},'','')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry Link may have been removed ![/B][/COLOR],[COLOR lime][B]Please try a different link/host !![/B][/COLOR],7000,"")")

#------------------------------------------------------------------------------irweb-dl--------------------------------------------------------------------------------------#

def GetLinks4(section, url): 
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('<pre>(.+?)</pre>').findall(content)
        listitem = GetMediaInfo(content)
        for url in match:
                host = GetDomain(url)
                if 'Unknown' in host:
                                continue
                if urlresolver.HostedMediaFile(url= url):
                        print 'in GetLinks if loop'
                        title = url.rpartition('/')
                        title = title[2].replace('.html', '')
                        title = title.replace('.htm', '')
                        title = title.replace('480p','[COLOR coral][B][I]480p[/B][/I][/COLOR]')
                        title = title.replace('720p','[COLOR gold][B][I]720p[/B][/I][/COLOR]')
                        title = title.replace('1080p','[COLOR orange][B][I]1080p[/B][/I][/COLOR]')
                        title = title.replace('mkv','[COLOR gold][B][I]MKV[/B][/I][/COLOR] ')
                        title = title.replace('mp4','[COLOR purple][B][I]MP4[/B][/I][/COLOR] ')
                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title':  host + ' [COLOR gold]:[/COLOR] ' + title }, img=IconPath + 'play.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#-------------------------------------------------------------------------------dxtv--------------------------------------------------------------------------------------#

def GetLinks5(section, url): 
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('<p><span style="color: #008000;"><strong>(.+?)</strong></span></p>').findall(content)
        listitem = GetMediaInfo(content)
        for url in match:
                host = GetDomain(url)

                if 'Unknown' in host:
                                continue
                if urlresolver.HostedMediaFile(url= url):
                        print 'in GetLinks if loop'
                        title = url.rpartition('/')
                        title = title[2].replace('.html', '')
                        title = title.replace('.htm', '')
                        title = title.replace('480p','[COLOR coral][B][I]480p[/B][/I][/COLOR]')
                        title = title.replace('720p','[COLOR gold][B][I]720p[/B][/I][/COLOR]')
                        title = title.replace('1080p','[COLOR orange][B][I]1080p[/B][/I][/COLOR]')
                        title = title.replace('mkv','[COLOR gold][B][I]MKV[/B][/I][/COLOR] ')
                        title = title.replace('avi','[COLOR pink][B][I]AVI[/B][/I][/COLOR] ')
                        title = title.replace('mp4','[COLOR purple][B][I]MP4[/B][/I][/COLOR] ')
                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title':  host + ' [COLOR gold]:[/COLOR] ' + title }, img=IconPath + 'play.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#-------------------------------------------------------------------------------ufd--------------------------------------------------------------------------------------#

def GetLinks6(section, url): 
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('<p>(.+?)</p>').findall(content)
        listitem = GetMediaInfo(content)
        for url in match:
                host = GetDomain(url)

                if 'Unknown' in host:
                                continue
                if urlresolver.HostedMediaFile(url= url):
                        print 'in GetLinks if loop'
                        title = url.rpartition('/')
                        title = title[2].replace('.html', '')
                        title = title.replace('.htm', '')
                        title = title.replace('480p','[COLOR coral][B][I]480p[/B][/I][/COLOR]')
                        title = title.replace('720p','[COLOR gold][B][I]720p[/B][/I][/COLOR]')
                        title = title.replace('1080p','[COLOR orange][B][I]1080p[/B][/I][/COLOR]')
                        title = title.replace('mkv','[COLOR gold][B][I]MKV[/B][/I][/COLOR] ')
                        title = title.replace('avi','[COLOR pink][B][I]AVI[/B][/I][/COLOR] ')
                        title = title.replace('mp4','[COLOR purple][B][I]MP4[/B][/I][/COLOR] ')
                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title':  host + ' [COLOR gold]:[/COLOR] ' + title }, img=IconPath + 'play.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#-------------------------------------------------------------------------------tvshowpad--------------------------------------------------------------------------------------#

def GetLinks7(section, url): 
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('<p><a href=".+?" rel="nofollow">(.+?)</a></p>').findall(content)
        listitem = GetMediaInfo(content)
        for url in match:
                host = GetDomain(url)

                if 'Unknown' in host:
                                continue
                if urlresolver.HostedMediaFile(url= url):
                        print 'in GetLinks if loop'
                        title = url.rpartition('/')
                        title = title[2].replace('.html', '')
                        title = title.replace('.htm', '')
                        title = title.replace('480p','[COLOR coral][B][I]480p[/B][/I][/COLOR]')
                        title = title.replace('720p','[COLOR gold][B][I]720p[/B][/I][/COLOR]')
                        title = title.replace('1080p','[COLOR orange][B][I]1080p[/B][/I][/COLOR]')
                        title = title.replace('mkv','[COLOR gold][B][I]MKV[/B][/I][/COLOR] ')
                        title = title.replace('avi','[COLOR pink][B][I]AVI[/B][/I][/COLOR] ')
                        title = title.replace('mp4','[COLOR purple][B][I]MP4[/B][/I][/COLOR] ')
                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title':  host + ' [COLOR gold]:[/COLOR] ' + title }, img=IconPath + 'play.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#-------------------------------------------------------------------------------rlssource--------------------------------------------------------------------------------------#

def GetLinks8(section, url): 
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('href=(.+?) target=_blank>.+?<').findall(content)
        listitem = GetMediaInfo(content)
        for url in match:
                host = GetDomain(url)

                if 'Unknown' in host:
                                continue
                if urlresolver.HostedMediaFile(url= url):
                        print 'in GetLinks if loop'
                        title = url.rpartition('/')
                        title = title[2].replace('.html', '')
                        title = title.replace('.htm', '')
                        title = title.replace('480p','[COLOR coral][B][I]480p[/B][/I][/COLOR]')
                        title = title.replace('720p','[COLOR gold][B][I]720p[/B][/I][/COLOR]')
                        title = title.replace('1080p','[COLOR orange][B][I]1080p[/B][/I][/COLOR]')
                        title = title.replace('mkv','[COLOR gold][B][I]MKV[/B][/I][/COLOR] ')
                        title = title.replace('avi','[COLOR pink][B][I]AVI[/B][/I][/COLOR] ')
                        title = title.replace('mp4','[COLOR purple][B][I]MP4[/B][/I][/COLOR] ')
                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title':  host + ' [COLOR gold]:[/COLOR] ' + title }, img=IconPath + 'play.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------------- warezaz-------------------------------------------------------------------------------#

def GetLinks9(section, url): 
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        r = re.search('<strong>Links.*</strong>', html)
        if r:
                content = html[r.end():]

        r = re.search('commentblock', content)
        if r:
                content = content[:r.start()]
                
        match = re.compile('<pre style=".+?">(.+?)<').findall(content)
        match1 = re.compile('<pre style=".+?"><br /><br />(.+?)<').findall(content)
        listitem = GetMediaInfo(content)
        for url in match + match1:
                host = GetDomain(url)

                if 'Unknown' in host:
                                continue
                        
                # ignore .rar files
                r = re.search('\.rar[(?:\.html|\.htm)]*', url, re.IGNORECASE)
                if r:
                        continue

                if urlresolver.HostedMediaFile(url= url):
                        print 'in GetLinks if loop'
                        title = url.rpartition('/')
                        title = title[2].replace('.html', '')
                        title = title.replace('.htm', '')
                        title = title.replace('.rar', '[COLOR red][B][I]RAR no streaming[/B][/I][/COLOR]')
                        title = title.replace('rar', '[COLOR red][B][I]RAR no streaming[/B][/I][/COLOR]')
                        title = title.replace('sample', '[COLOR lime]Movie Trailer[/COLOR]')
                        title = title.replace('www.', '')
                        title = title.replace ('-',' ')
                        title = title.replace('_',' ')
                        title = title.replace('.',' ')
                        title = title.replace('gaz','')
                        title = title.replace('NTb','')
                        title = title.replace('1st','[COLOR coral][B]1st HALF[/B][/COLOR]')
                        title = title.replace('2nd','[COLOR coral][B]2nd HALF[/B][/COLOR]')
                        title = title.replace('fullmatches net','')
                        title = title.replace('.',' ')
                        title = title.replace('480p','[COLOR coral][B][I]480p[/B][/I][/COLOR]')
                        title = title.replace('720p','[COLOR gold][B][I]720p[/B][/I][/COLOR]')
                        title = title.replace('1080p','[COLOR orange][B][I]1080p[/B][/I][/COLOR]')
                        title = title.replace('mkv','[COLOR gold][B][I]MKV[/B][/I][/COLOR] ')
                        title = title.replace('avi','[COLOR pink][B][I]AVI[/B][/I][/COLOR] ')
                        title = title.replace('mp4','[COLOR purple][B][I]MP4[/B][/I][/COLOR] ')
                        title = title.replace('%20',' ')
                        host = host.replace('youtube.com','[COLOR lime]Movie Trailer[/COLOR]')
                        host = host.replace('k2s.cc','[COLOR red]Unsupported Link[/COLOR]')
                        host = host.replace('ryushare.com','[COLOR red]Unsupported Link[/COLOR]')
                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title':  host + ' [COLOR gold]:[/COLOR] ' + title }, img=IconPath + 'play.png', fanart=FanartPath + 'fanart.png')

        find = re.search('commentblock', html)
        if find:
                print 'in comments if'
                html = html[find.end():]
                match = re.compile('<a href="(.+?)" rel="nofollow"', re.DOTALL).findall(html)
                print len(match)
                for url in match:
                        host = GetDomain(url)
                        if 'Unknown' in host:
                                continue
                        
                        # ignore .rar files
                        r = re.search('\.rar[(?:\.html|\.htm)]*', url, re.IGNORECASE)
                        if r:
                                continue
                        try:
                                if urlresolver.HostedMediaFile(url= url):
                                        print 'in GetLinks if loop'
                                        title = url.rpartition('/')
                                        title = title[2].replace('.html', '')
                                        title = title.replace('.htm', '')
                                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title':  host + ' : ' + title}, img=IconPath + 'play.png', fanart=FanartPath + 'fanart.png')
                        except:
                                continue
        xbmcplugin.endOfDirectory(int(sys.argv[1]))


############################################################################# PlayVideo #################################################################################

def PlayVideo(url, listitem):
    try:
        stream_url = urlresolver.HostedMediaFile(url).resolve()
        xbmc.Player().play(stream_url)
        addon.add_directory({'mode': 'help'}, {'title':  '[COLOR slategray][B]^^^ Press back ^^^[/B] [/COLOR]'},'','')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry Link may have been removed ![/B][/COLOR],[COLOR lime][B]Please try a different link/host !![/B][/COLOR],7000,"")")

#---------------------------------------------------------------------------------------------------------------#

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

############################################################################# homescreen ################################################################################################

def MainMenu():        
        addon.add_directory({'mode': 'menu2'}, {'title': '[COLOR blue][B]Movies >>[/B] [/COLOR]>>'}, img=IconPath + 'films.png', fanart=FanartPath + 'fanart.png') 
        addon.add_directory({'mode': 'menu4'}, {'title': '[COLOR darkorange][B]Tv Shows >>[/B] [/COLOR]>>'}, img=IconPath + 'tv2.png', fanart=FanartPath + 'fanart.png') 
        addon.add_directory({'mode': 'menu6'}, {'title': '[COLOR lemonchiffon][B]Sport >>[/B] [/COLOR]>>'}, img=IconPath + 'sport1.png', fanart=FanartPath + 'fanart.png') 
        addon.add_directory({'mode': 'menu7'}, {'title': '[COLOR violet][B]Anime >>[/B] [/COLOR]>>'}, img=IconPath + 'anex.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'menu5'}, {'title': '[COLOR green][B]Searches >>[/B] [/COLOR]>>'}, img=IconPath + 'searches.png', fanart=FanartPath + 'fanart.png') 
        addon.add_directory({'mode': 'ResolverSettings'}, {'title':  '[COLOR red]Resolver Settings[/COLOR]'}, img=IconPath + 'resolver.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'HelpMenu'}, {'title':  '[COLOR aquamarine][B]News & Help  >[/B][/COLOR] >'}, img=IconPath + 'newshelp.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#------------------------------------------------------------------------------- help ----------------------------------------------------------------------------------------#

def HelpMenu():  
        addon.add_directory({'mode': 'Help'}, {'title':  '[COLOR lime]Whats New News >[/COLOR] >'}, img=IconPath + 'twit.png', fanart=FanartPath + 'fanart.png') 
        addon.add_directory({'mode': 'GetTitles27', 'url': BASE_URL27 + '/help.txt'}, {'title':  '[COLOR deeppink][B]Help & how to vids >[/COLOR][/B] >'}, img=IconPath + 'h2.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'HelpMenu'}, {'title':  '[B][COLOR gold]If you like this addon[/COLOR][/B]'}, img=IconPath + 'twit.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'HelpMenu'}, {'title':  '[B][COLOR gold]Please install Entertainment HUB from TheYids REPO[/COLOR][/B]'}, img= 'https://raw.githubusercontent.com/TheYid/My-Repo/master/plugin.video.allinone/icon.png', fanart= 'https://raw.githubusercontent.com/TheYid/My-Repo/master/plugin.video.allinone/fanart.jpg')
        addon.add_directory({'mode': 'HelpMenu'}, {'title':  '[B][COLOR gold]& if you like rave music install Rave player from TheYids REPO[/COLOR][/B]'}, img= 'https://raw.githubusercontent.com/TheYid/My-Repo/master/plugin.audio.raveplayer/icon.png', fanart= 'https://raw.githubusercontent.com/TheYid/My-Repo/master/plugin.audio.raveplayer/fanart.jpg')
        addon.add_directory({'mode': 'HelpMenu'}, {'title':  '[B][COLOR blue]System/Add-ons/Get Add-ons/TheYids REPO[/COLOR][/B]'}, img= 'https://raw.githubusercontent.com/TheYid/My-Repo/master/repository.TheYid/icon.png', fanart= 'https://raw.githubusercontent.com/TheYid/My-Repo/master/plugin.video.allinone/fanart.jpg')
        addon.add_directory({'mode': 'HelpMenu'}, {'title':  '[B][COLOR aqua]@TheYid009[/COLOR][/B] - [B][COLOR gold]Add me on twitter for all the latest news & updates..[/COLOR][/B]'}, img=IconPath + 'twit.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'HelpMenu'}, {'title':  '[B][COLOR red]This addon works best with a real-debrid.com premium account[/COLOR][/B]'}, img=IconPath + 'twit.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#------------------------------------------------------------------------------- movies -------------------------------------------------------------------------------------------------#

def Menu2():
        addon.add_directory({'mode': 'GetTitles30', 'section': 'ALL', 'url': BASE_URL30 + '/xfsearch/2014',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue][B]Latest Movies[/B] [/COLOR] [COLOR lavender](MoviesReady)[/COLOR] >>'}, img=IconPath + 'mr.png', fanart=FanartPath + 'fanart.png')
        #addon.add_directory({'mode': 'menu14'}, {'title': '[COLOR blue][B]Movie Genre[/B] [/COLOR] [COLOR lavender](MoviesReady)[/COLOR] >>'}, img=IconPath + 'mr.png', fanart=FanartPath + 'fanart.png') 
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL11 + '/category/movies/',
                             'startPage': '1', 'numOfPages': '2'}, {'title':  '[COLOR blue][B]Latest Movies[/B] [/COLOR] [COLOR gold](ReleaseBB)[/COLOR] >>'}, img=IconPath + 'moviebb.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles11', 'section': 'ALL', 'url': BASE_URL10 + '/category/movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue][B]Latest Movies[/B] [/COLOR] [COLOR powderblue](DDLvalley)[/COLOR] >>'}, img=IconPath + 'ddlmo.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL1 + '/films/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue][B]Latest Movies[/B] [/COLOR] [COLOR orangered](Scene Source)[/COLOR] >>'}, img=IconPath + 'ssmovies.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles7', 'section': 'ALL', 'url': BASE_URL8 + '/category/movies',
                             'startPage': '1', 'numOfPages': '2'}, {'title':  '[COLOR blue][B]Latest Movies[/B] [/COLOR] [COLOR mediumspringgreen](Sceper)[/COLOR] >>'}, img=IconPath + 'scmovie.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles6', 'section': 'ALL', 'url': BASE_URL9 + '/category/movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue][B]Latest Movies[/B] [/COLOR] [COLOR plum](Scene down)[/COLOR] >>'}, img=IconPath + 'sdmovies.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue][B]Latest Movies[/B] [/COLOR] [COLOR lime](Release Center)[/COLOR] >>'}, img=IconPath + 'rcmovies.png', fanart=FanartPath + 'fanart.png')
        #addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL7 + '/movies/',
                             #'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue][B]Latest Movies[/B] [/COLOR] [COLOR deepskyblue](wrzKO)[/COLOR] >>'}, img=IconPath + 'wmovies.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles21', 'section': 'ALL', 'url': BASE_URL21 + 'category/movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue][B]Latest Movies[/B] [/COLOR] [COLOR chocolate](Release 1-Click)[/COLOR] >>'}, img= 'https://raw.githubusercontent.com/TheYid/yidpics/master/icons/r1movies.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles14', 'section': 'ALL', 'url': BASE_URL5 + '/category/movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue][B]Latest Movies[/B] [/COLOR] [COLOR whitesmoke](The Extopia)[/COLOR] >>'}, img=IconPath + 'exmo.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'menu9'}, {'title': '[COLOR blue][B]Latest Movies[/B] [/COLOR] [COLOR crimson](300mb movies4u)[/COLOR] >>'}, img=IconPath + 'm4u1.png', fanart=FanartPath + 'fanart.png') 
        addon.add_directory({'mode': 'menu3'}, {'title': '[COLOR blue][B]Latest Movies[/B] [/COLOR] [COLOR powderblue](1080p Zone)[/COLOR] >>'}, img=IconPath + '10z.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles29', 'section': 'ALL', 'url': BASE_URL29 + '/category/hollywood-movie-2014/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue][B]New Released[/B] [/COLOR]: [COLOR greenyellow]Index Search[/COLOR]'}, img=IconPath + 'reto.png', fanart=FanartPath + 'fanart.png')
        #addon.add_directory({'mode': 'GetTitles25', 'url': BASE_URL25 + '/movies'}, {'title':  '[COLOR blue][B]Featured[/B] [/COLOR]: [COLOR greenyellow]Index Search[/COLOR]'}, img=IconPath + 'inf.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28', 'url': BASE_URL28 + '/'}, {'title':  '[COLOR blue][B]Released Today[/B] [/COLOR]: [COLOR greenyellow]Index Search[/COLOR]'}, img=IconPath + 'reto.png', fanart=FanartPath + 'fanart.png') 
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#------------------------------------------------------------------------------- MoviesReady -------------------------------------------------------------------------------------------------#

def Menu14():
        addon.add_directory({'mode': 'GetTitles30', 'section': 'ALL', 'url': BASE_URL30 + '/xfsearch/2014',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue][B]Latest Movies[/B] [/COLOR] [COLOR lavender](MoviesReady)[/COLOR] >>'}, img=IconPath + 'mr.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'Categories' },  {'title':  '[COLOR deepskyblue][B]Movie Genre[/B][/COLOR] >>'}, img=IconPath + 'mr.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------------------- 300mbmovies4u ----------------------------------------------------------------------------------------------#

def Menu9():   #300mbmovies4u
        addon.add_directory({'mode': 'GetTitles5', 'section': 'ALL', 'url': BASE_URL12 + '/category/hollywood-movie/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue][B]Latest Movies[/B][/COLOR] [COLOR crimson](Hollywood) [/COLOR] >>'}, img=IconPath + 'm4u1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles5', 'section': 'ALL', 'url': BASE_URL12 + '/category/hollywood-movie/english-1080p-movie/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue][B]HD 1080p Movies[/B][/COLOR] [COLOR crimson](Hollywood) [/COLOR] >>'}, img=IconPath + 'm4u1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles5', 'section': 'ALL', 'url': BASE_URL12 + '/category/bollywood-movie/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue][B]Latest Movies[/B][/COLOR] [COLOR crimson](Bollywood) [/COLOR] >>'}, img=IconPath + 'm4u1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles5', 'section': 'ALL', 'url': BASE_URL12 + '/category/tamil-movie/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue][B]Latest Movies[/B][/COLOR] [COLOR crimson](Tamil) [/COLOR] >>'}, img=IconPath + 'm4u1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles5', 'section': 'ALL', 'url': BASE_URL12 + '/category/hd-video/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue][B]HD Music video[/B][/COLOR] [COLOR crimson](International) [/COLOR] >>'}, img=IconPath + 'm4u1.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#--------------------------------------------------------------------------------- HD Zone movies ----------------------------------------------------------------------------------------------------------#

def Menu3():
        #addon.add_directory({'mode': 'GetTitles23', 'section': 'ALL', 'url': BASE_URL23 + '/category/movies/',
                             #'startPage': '1', 'numOfPages': '2'}, {'title':  '[COLOR steelblue][B]Latest Movies[/B][/COLOR] [COLOR darkseagreen](Binflix) [/COLOR]>>'}, img=IconPath + 'bf.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles22', 'section': 'ALL', 'url': BASE_URL22 + '/category/movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR steelblue][B]Latest Movies[/B] [/COLOR] [COLOR blue](irweb-dl)[/COLOR] >>'}, img=IconPath + 'ir.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles5', 'section': 'ALL', 'url': BASE_URL12 + '/category/hollywood-movie/english-3d-movie/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR steelblue][B]Latest 3D[/B][/COLOR] [COLOR crimson](300mb movies4u) [/COLOR] >>'}, img=IconPath + 'm4u1.png', fanart=FanartPath + 'fanart.png')
        #addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL7 + '/movies/yify-brrip-1080p/',
                             #'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR steelblue][B]Latest 1080p YIFY[/B] [/COLOR] [COLOR deepskyblue](wrzKO)[/COLOR] >>'}, img=IconPath + 'wmovies.png', fanart=FanartPath + 'fanart.png')
        #addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL7 + '/movies/yify-brrip-720p/',
                             #'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR steelblue][B]Latest 720p YIFY[/B] [/COLOR] [COLOR deepskyblue](wrzKO)[/COLOR] >>'}, img=IconPath + 'wmovies.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles11', 'section': 'ALL', 'url': BASE_URL10 + '/category/movies/yify-rips/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR steelblue][B]Latest YIFY[/B] [/COLOR] [COLOR powderblue](DDLvalley)[/COLOR] >>'}, img=IconPath + 'ddlmo.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles21', 'section': 'ALL', 'url': BASE_URL21 + '/category/movies/yify-brrip/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR steelblue][B]Latest YIFY[/B] [/COLOR] [COLOR chocolate](Release 1-Click)[/COLOR] >>'}, img= 'https://raw.githubusercontent.com/TheYid/yidpics/master/icons/r1movies.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL6 + '/movie/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue][B]Latest Movies[/B] [/COLOR] [COLOR darkorchid](Com2dl.com)[/COLOR] >>'}, img=IconPath + 'commovies.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles20', 'section': 'ALL', 'url': BASE_URL20 + '/movie',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue][B]Latest HD Movies[/B] [/COLOR] [COLOR magenta](Movie4download)[/COLOR] >>'}, img=IconPath + 'm4d.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL2 + '/movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue][B]Latest Movies[/B] [/COLOR] [COLOR powderblue](SceneLog)[/COLOR] >>'}, img=IconPath + 'slm1.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#------------------------------------------------------------------------------- tv -------------------------------------------------------------------------------------------------#

def Menu4():
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL11 + '/category/tv-shows/',
                             'startPage': '1', 'numOfPages': '2'}, {'title':  '[COLOR darkorange][B]Latest Tv Shows[/B] [/COLOR] [COLOR gold](ReleaseBB)[/COLOR] >>'}, img=IconPath + 'tvbb.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles11', 'section': 'ALL', 'url': BASE_URL10 + '/category/tv-shows/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Latest Tv Shows[/B] [/COLOR] [COLOR powderblue](DDLvalley)[/COLOR] >>'}, img=IconPath + 'ddltv.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles7', 'section': 'ALL', 'url': BASE_URL8 + '/category/tv-shows',
                             'startPage': '1', 'numOfPages': '2'}, {'title':  '[COLOR darkorange][B]Latest Tv Shows[/B] [/COLOR] [COLOR mediumspringgreen](Sceper)[/COLOR] >>'}, img=IconPath + 'setv.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles6', 'section': 'ALL', 'url': BASE_URL9 + '/category/tv-shows/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Latest Tv Shows[/B] [/COLOR] [COLOR plum](Scene down)[/COLOR] >>'}, img=IconPath + 'sdtv.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/tv-shows/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Latest Tv shows[/B] [/COLOR] [COLOR lime](Release Center) [/COLOR]>>'}, img=IconPath + 'rctv.png', fanart=FanartPath + 'fanart.png')
        #addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL7 + '/tv-shows/',
                             #'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Latest Tv Shows[/B] [/COLOR] [COLOR deepskyblue](wrzKO)[/COLOR] >>'}, img=IconPath + 'wtv.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL1 + '/tv/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Latest Tv Shows[/B] [/COLOR] [COLOR orangered](Scene Source)[/COLOR] >>'}, img=IconPath + 'sstv.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles14', 'section': 'ALL', 'url': BASE_URL5 + '/category/tvshow/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Latest Releases[/B] [/COLOR] [COLOR whitesmoke](The Extopia)[/COLOR] >>'}, img=IconPath + 'extv1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles21', 'section': 'ALL', 'url': BASE_URL21 + 'category/tv-shows/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Latest Tv Shows[/B] [/COLOR] [COLOR chocolate](Release 1-Click)[/COLOR] >>'}, img= 'https://raw.githubusercontent.com/TheYid/yidpics/master/icons/r1tv.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles5', 'section': 'ALL', 'url': BASE_URL12 + '/category/tv-shows/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Latest Tv Shows[/B][/COLOR] [COLOR crimson](300mb movies4u)[/COLOR] >>'}, img=IconPath + '3mb4.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL2 + '/tv-shows/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Latest Tv shows[/B] [/COLOR] [COLOR powderblue](SceneLog)[/COLOR] >>'}, img=IconPath + 'slt1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'menu11'}, {'title': '[COLOR darkorange][B]Latest Added[/B] [/COLOR] [COLOR blue](1080p zone)[/COLOR] >>'}, img=IconPath + '1080.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles25a', 'url': BASE_URL25 + '/tv-shows/date'}, {'title':  '[COLOR darkorange][B]TV Shows[/B] [/COLOR]: [COLOR green]Index Search[/COLOR]'}, img=IconPath + 'intvs.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#------------------------------------------------------------------------------------ hd zone tv --------------------------------------------------------------------------------------------#

def Menu11():
        #addon.add_directory({'mode': 'GetTitles23', 'section': 'ALL', 'url': BASE_URL23 + '/category/tv-shows/',
                             #'startPage': '1', 'numOfPages': '2'}, {'title':  '[COLOR darkorange][B]Latest Episodes 1080p/720p[/B][/COLOR] [COLOR darkseagreen](Binflix) [/COLOR]>>'}, img=IconPath + 'bf.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles22', 'section': 'ALL', 'url': BASE_URL22 + '/category/tv-shows/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Latest Tv shows 1080p/720p[/B] [/COLOR] [COLOR blue](irweb-dl)[/COLOR] >>'}, img=IconPath + 'ir.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/tv-show',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Latest 1080p Releases[/B] [/COLOR] [COLOR lightcyan](Crazy hd Source)[/COLOR] >>'}, img=IconPath + 'chd.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles14', 'section': 'ALL', 'url': BASE_URL5 + '/category/tvshow/web-dl/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Latest 1080p / 720p packs[/B] [/COLOR] [COLOR whitesmoke](The Extopia)[/COLOR] >>'}, img=IconPath + 'extv1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'menu12'}, {'title': '[COLOR darkorange][B]Latest 1080p / 720p[/B] [/COLOR] [COLOR red](Rls-TV)[/COLOR] >>'}, img=IconPath + 'rlstv.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#----------------------------------------------------------------------------------- rlstv ---------------------------------------------------------------------------------------------#

def Menu12():
        addon.add_directory({'mode': 'GetTitles8', 'section': 'ALL', 'url': BASE_URL16 + '/?cat=TV-720p',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Page 1[/B] [/COLOR]>>'}, img=IconPath + 'rlstv.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles8', 'section': 'ALL', 'url': BASE_URL16 + '/index.php?page=2&cat=TV-720p',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Page 2[/B] [/COLOR]>>'}, img=IconPath + 'rlstv.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles8', 'section': 'ALL', 'url': BASE_URL16 + '/index.php?page=3&cat=TV-720p',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Page 3[/B] [/COLOR]>>'}, img=IconPath + 'rlstv.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles8', 'section': 'ALL', 'url': BASE_URL16 + '/index.php?page=4&cat=TV-720p',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Page 4[/B] [/COLOR]>>'}, img=IconPath + 'rlstv.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles8', 'section': 'ALL', 'url': BASE_URL16 + '/index.php?page=5&cat=TV-720p',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Page 5[/B] [/COLOR]>>'}, img=IconPath + 'rlstv.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles8', 'section': 'ALL', 'url': BASE_URL16 + '/index.php?page=6&cat=TV-720p',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Page 6[/B] [/COLOR]>>'}, img=IconPath + 'rlstv.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles8', 'section': 'ALL', 'url': BASE_URL16 + '/index.php?page=7&cat=TV-720p',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Page 7[/B] [/COLOR]>>'}, img=IconPath + 'rlstv.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles8', 'section': 'ALL', 'url': BASE_URL16 + '/index.php?page=8&cat=TV-720p',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Page 8[/B] [/COLOR]>>'}, img=IconPath + 'rlstv.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles8', 'section': 'ALL', 'url': BASE_URL16 + '/index.php?page=9&cat=TV-720p',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Page 9[/B] [/COLOR]>>'}, img=IconPath + 'rlstv.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles8', 'section': 'ALL', 'url': BASE_URL16 + '/index.php?page=10&cat=TV-720p',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Page 10[/B] [/COLOR]>>'}, img=IconPath + 'rlstv.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#------------------------------------------------------------------------------------- sport -------------------------------------------------------------------------------------------#

def Menu6():
        addon.add_directory({'mode': 'GetTitles11', 'section': 'ALL', 'url': BASE_URL10 + '/category/tv-shows/sports/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lemonchiffon][B]Latest Sport[/B] [/COLOR] [COLOR powderblue](DDLvalley)[/COLOR] >>'}, img=IconPath + 'ddlsport.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles11', 'section': 'ALL', 'url': BASE_URL10 + '/category/tv-shows/sports/english-premier-league/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lemonchiffon][B]Latest EPL (HD)[/B] [/COLOR] [COLOR powderblue](DDLvalley)[/COLOR] >>'}, img=IconPath + 'ddlsport.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles11', 'section': 'ALL', 'url': BASE_URL10 + '/category/tv-shows/sports/nba/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lemonchiffon][B]Latest NBA[/B] [/COLOR] [COLOR powderblue](DDLvalley)[/COLOR] >>'}, img=IconPath + 'ddlsport.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles13', 'section': 'ALL', 'url': BASE_URL11 + '/page/1/?s=ufc&submit=Find',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lemonchiffon][B]Latest (7) UFC[/B] [COLOR gold](ReleaseBB)[/COLOR] >>'}, img=IconPath + 'bbsport.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles13', 'section': 'ALL', 'url': BASE_URL11 + '/?s=wwe&submit=Find',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lemonchiffon][B]Latest (7) WWE[/B] [COLOR gold](ReleaseBB)[/COLOR] >>'}, img=IconPath + 'bbsport.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles13', 'section': 'ALL', 'url': BASE_URL11 + '/?s=tna&submit=Find',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lemonchiffon][B]Latest (7) TNA[/B] [COLOR gold](ReleaseBB)[/COLOR] >>'}, img=IconPath + 'bbsport.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles13', 'section': 'ALL', 'url': BASE_URL11 + '/?s=boxing&submit=Find',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lemonchiffon][B]Latest (7) Boxing[/B] [COLOR gold](ReleaseBB)[/COLOR] >>'}, img=IconPath + 'bbsport.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles13', 'section': 'ALL', 'url': BASE_URL11 + '/?s=match+of+the+day&submit=Find',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lemonchiffon][B]Latest (7) Match Of The Day[/B] [COLOR gold](ReleaseBB)[/COLOR] >>'}, img=IconPath + 'bbsport.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'menu8'}, {'title': '[COLOR lightyellow][B]Football Full Matches[/B] [/COLOR]>>'}, img=IconPath + 'fullsport.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles24', 'section': 'ALL', 'url': BASE_URL24 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lemonchiffon][B]Latest Wrestling/MMA/Boxing[/B] [COLOR chartreuse](DX-TV)[/COLOR] >>'}, img=IconPath + 'dx.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles17', 'section': 'ALL', 'url': BASE_URL13 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lemonchiffon][B]Latest MMA/Wrestling/Boxing[/B] [COLOR orange](Fight-BB)[/COLOR] >>'}, img=IconPath + 'fbb.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#----------------------------------------------------------------------------------- fullmatch ---------------------------------------------------------------------------------------------#

def Menu8():
        addon.add_directory({'mode': 'GetTitles16', 'section': 'ALL', 'url': BASE_URL15 + '/category/full-matches/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lightyellow]Full Matches [/COLOR]>>'}, img=IconPath + 'fullsport.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles16', 'section': 'ALL', 'url': BASE_URL15 + '/category/full-matches/england-premier-league/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lightyellow]England Premier League [/COLOR]>>'}, img=IconPath + 'fullsport.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles16', 'section': 'ALL', 'url': BASE_URL15 + '/category/full-matches/la-liga/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lightyellow]La Liga [/COLOR]>>'}, img=IconPath + 'fullsport.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles16', 'section': 'ALL', 'url': BASE_URL15 + '/category/full-matches/serie-a/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lightyellow]Serie A [/COLOR]>>'}, img=IconPath + 'fullsport.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles16', 'section': 'ALL', 'url': BASE_URL15 + '/category/full-matches/bundesliga/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lightyellow]Bundesliga [/COLOR]>>'}, img=IconPath + 'fullsport.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles16', 'section': 'ALL', 'url': BASE_URL15 + '/category/full-matches/ligue-1/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lightyellow]Ligue 1 [/COLOR]>>'}, img=IconPath + 'fullsport.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles16', 'section': 'ALL', 'url': BASE_URL15 + '/category/full-matches/matches-other/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lightyellow]Matches Other [/COLOR]>>'}, img=IconPath + 'fullsport.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles16', 'section': 'ALL', 'url': BASE_URL15 + '/category/full-matches/uefa-champions-league/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lightyellow]Uefa Champions League [/COLOR]>>'}, img=IconPath + 'fullsport.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles16', 'section': 'ALL', 'url': BASE_URL15 + '/category/full-matches/uefa-europa-league/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lightyellow]Uefa Europa League [/COLOR]>>'}, img=IconPath + 'fullsport.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------------------- anime ----------------------------------------------------------------------------------------------#

def Menu7():
        addon.add_directory({'mode': 'GetTitles14', 'section': 'ALL', 'url': BASE_URL5 + '/category/anime/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR violet][B]Latest[/B] [/COLOR] [COLOR whitesmoke](The Extopia)[/COLOR] >>'}, img=IconPath + 'exan.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles14', 'section': 'ALL', 'url': BASE_URL5 + '/category/anime/movie/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR violet][B]Anime Movies[/B] [/COLOR] [COLOR whitesmoke](The Extopia)[/COLOR] >>'}, img=IconPath + 'exan.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles14', 'section': 'ALL', 'url': BASE_URL5 + '/category/anime/ovaspecial/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR violet][B]Anime Ova & Special[/B] [/COLOR] [COLOR whitesmoke](The Extopia)[/COLOR] >>'}, img=IconPath + 'exan.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles14', 'section': 'ALL', 'url': BASE_URL5 + '/category/anime/packs/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR violet][B]Anime Packs[/B] [/COLOR] [COLOR whitesmoke](The Extopia)[/COLOR] >>'}, img=IconPath + 'exan.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#-------------------------------------------------------------------------------- search ------------------------------------------------------------------------------------------------#

def Menu5():
        addon.add_directory({'mode': 'GetSearchQuery10'},  {'title':  '[COLOR khaki][B]M[/COLOR][COLOR blue]E[/COLOR][COLOR salmon]G[/COLOR][COLOR darkseagreen]A[/COLOR][/B] [COLOR blue][B]R[/B][/COLOR]elease [COLOR blue][B]HUB[/B][/COLOR] (Movies & Tv Episodes) : [COLOR green]Search[/COLOR]'}, img=IconPath + 'rhs.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetSearchQuery11'},  {'title':  '[COLOR khaki][B]M[/COLOR][COLOR blue]E[/COLOR][COLOR salmon]G[/COLOR][COLOR darkseagreen]A[/COLOR][/B] [COLOR blue][B]R[/B][/COLOR]elease [COLOR blue][B]HUB[/B][/COLOR] (Wrestling/MMA/Boxing) : [COLOR green]Search[/COLOR]'}, img=IconPath + 'rhs.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles25a', 'url': BASE_URL25 + '/tv-shows/date'}, {'title':  '[COLOR darkorange][B]TV Shows[/B] [/COLOR]: [COLOR greenyellow]Index Search[/COLOR]'}, img=IconPath + 'intvs.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles29', 'section': 'ALL', 'url': BASE_URL29 + '/category/hollywood-movie-2014/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue][B]New Released[/B] [/COLOR]: [COLOR greenyellow]Index Search[/COLOR]'}, img=IconPath + 'reto.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28', 'url': BASE_URL28 + '/'}, {'title':  '[COLOR blue][B]Released Today[/B] [/COLOR]: [COLOR greenyellow]Index Search[/COLOR]'}, img=IconPath + 'reto.png', fanart=FanartPath + 'fanart.png')
        #addon.add_directory({'mode': 'GetTitles25', 'url': BASE_URL25 + '/movies/favorites'}, {'title':  '[COLOR blue][B]Featured[/B] [/COLOR]: [COLOR greenyellow]Index Search[/COLOR]'}, img=IconPath + 'inf.png', fanart=FanartPath + 'fanart.png')
        #addon.add_directory({'mode': 'GetTitles25', 'url': BASE_URL25 + '/featuredmovies'}, {'title':  '[COLOR blue][B]Box office[/B] [/COLOR]: [COLOR greenyellow]Index Search[/COLOR]'}, img=IconPath + 'isbo.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetSearchQuery1'},  {'title':  '[COLOR gold][B]ReleaseBB[/COLOR][/B] : [COLOR green]Search[/COLOR]'}, img=IconPath + 'searches.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetSearchQuery2'},  {'title':  '[COLOR yellowgreen][B]Publizhare[/COLOR][/B] : [COLOR green]Search[/COLOR]'}, img=IconPath + 'searches.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

############################################################################## searches #############################################################################################

def GetSearchQuery10():
	last_search = addon.load_data('search')
	if not last_search: last_search = ''
	keyboard = xbmc.Keyboard()
        keyboard.setHeading('[COLOR green]MEGA ADDON SEARCH[/COLOR]')
	keyboard.setDefault(last_search)
	keyboard.doModal()
	if (keyboard.isConfirmed()):
                query = keyboard.getText()
                addon.save_data('search',query)
                Search10(query)
	else:
                return
def Search10(query):
    try:
        url = 'http://www.rlsbb.com/?s=' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('postHeader.+?href="(.+?)".+?>(.+?)<.+?src=.+? src="(.+?)"', re.DOTALL).findall(html)
        for movieUrl, title, img in match:
                addon.add_directory({'mode': 'GetLinks', 'url': movieUrl}, {'title':  title + ' [COLOR gold](ReleaseBB)[/COLOR]'}, img= img, fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry rlsbb search is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))
    try:
        url = 'http://www.ddlvalley.rocks/search/' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h2>.+?href="(.+?)".+?>(.+?)<.+?src="(.+?)".+?', re.DOTALL).findall(html)
        for movieUrl, title, img in match:
                title = title.replace('.', ' ')
                addon.add_directory({'mode': 'GetLinks3', 'url': movieUrl}, {'title':  title + ' [COLOR powderblue](DDLvalley)[/COLOR]'}, img= img, fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry ddlvalley search is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))
    #try:
    #    url = 'http://www.scnsrc.me/?s=' + query
    #    url = url.replace(' ', '+')
    #    print url
    #    html = net.http_GET(url).content
    #    match = re.compile('<h2> <a href="(.+?)" rel="bookmark" title=".+?">(.+?)</a></h2>', re.DOTALL).findall(html)
    #    for movieUrl, title in match:
    #            addon.add_directory({'mode': 'GetLinks', 'url': movieUrl}, {'title':  title + ' [COLOR orangered](Scene Source)[/COLOR]'}, img= 'https://raw.githubusercontent.com/TheYid/yidpics/8333f2912d71cc7ddd71a7cee9714dfe263ee543/icons/nopic.png', fanart=FanartPath + 'fanart.png')
    #except:
    #    xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry scnsrc search is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
    #   	xbmcplugin.endOfDirectory(int(sys.argv[1]))

    try:
        url = 'http://sceper.ws/search/' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h2.+?href="(.+?)">(.+?)<.+?src="(.+?)"', re.DOTALL).findall(html)
        for movieUrl, title, img in match:
                addon.add_directory({'mode': 'GetLinks', 'url': movieUrl}, {'title':  title + ' [COLOR mediumspringgreen](Sceper)[/COLOR]'}, img= img, fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry sceper search is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))
    try:
        url = 'http://rls-center.com/?s=' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h2 class="post-title"><a href="(.+?)".+?>(.+?)<.+?src="(.+?)"', re.DOTALL).findall(html)
        for movieUrl, title, img in match:
                title = title.replace('.', ' ')
                addon.add_directory({'mode': 'GetLinks', 'url': movieUrl}, {'title':  title + ' [COLOR lime](Release Center)[/COLOR]'}, img= img, fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry rls-center search is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))
    try:
        url = 'http://rls1click.com/?s=' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('post-title.+?href="(.+?)">(.+?)<.+?src="(.+?)"', re.DOTALL).findall(html)
        for movieUrl, title, img in match:
                addon.add_directory({'mode': 'GetLinks', 'url': movieUrl}, {'title':  title + ' [COLOR chocolate](Release 1-Click)[/COLOR]'}, img= img, fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry rls1click search is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

    try:
        url = 'http://irweb-dl.com/?s=' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h1 class="entry-title"><a href="(.+?)" title=".+?" rel="bookmark">(.+?)</a></h1>', re.DOTALL).findall(html)
        for movieUrl, title in match:
                addon.add_directory({'mode': 'GetLinks4', 'url': movieUrl}, {'title':  title + ' [COLOR blue](irweb-dl)[/COLOR]'}, img= 'https://raw.githubusercontent.com/TheYid/yidpics/8333f2912d71cc7ddd71a7cee9714dfe263ee543/icons/nopic.png', fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry irweb-dl search is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))
    try:
        url = 'http://300mbmovies4u.com/?s=' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<div class="cover"><a href="(.+?)".+?.+?<img src="(.+?)".+?alt="(.+?)"', re.DOTALL).findall(html)
        for movieUrl, img, title in match:
                addon.add_directory({'mode': 'GetLinks', 'url': movieUrl}, {'title':  title + ' [COLOR crimson](300mb movies4u)[/COLOR]'}, img= img, fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry 300mbmovies4u search is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))
    try:
        url = 'http://rlssource.net/?s=' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h2 class="entry-title"><a href="(.+?)" title=".+?" rel="bookmark">(.+?)</a></h2>', re.DOTALL).findall(html)
        for movieUrl, title in match:
                addon.add_directory({'mode': 'GetLinks8', 'url': movieUrl}, {'title':  title + ' [COLOR firebrick](rlssource)[/COLOR]'}, img= 'https://raw.githubusercontent.com/TheYid/yidpics/8333f2912d71cc7ddd71a7cee9714dfe263ee543/icons/nopic.png', fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry rlssource search is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))
    try:
        url = 'http://tv-release.net/?s='+query+'&cat='
        url = url.replace(' ', '%20')
        print url
        html = net.http_GET(url).content
        match = re.compile("width='60%' style='text-align:left; font-size:12px;font-weight:bold;'><a href='(.+?)'>(.+?)</a></td><td", re.DOTALL).findall(html)
        for movieUrl, title in match:
                title = title.replace('.', ' ')
                addon.add_directory({'mode': 'GetLinks1', 'url': movieUrl}, {'title':  title + ' [COLOR red](Rls-TV)[/COLOR]'}, img= 'https://raw.githubusercontent.com/TheYid/yidpics/8333f2912d71cc7ddd71a7cee9714dfe263ee543/icons/nopic.png', fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry RLSTV search is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))
    try:
        url = 'http://scnlog.eu/?s='+query+'&cat=4'
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('src=".+?" title=""/><a href="(.+?)" rel="bookmark" title=".+?">(.+?)</a>', re.DOTALL).findall(html)
        for movieUrl, title in match:
                title = title.replace('.', ' ')
                addon.add_directory({'mode': 'GetLinks', 'url': movieUrl}, {'title':  title + ' [COLOR blue](scnlog)[/COLOR]'}, img= 'https://raw.githubusercontent.com/TheYid/yidpics/8333f2912d71cc7ddd71a7cee9714dfe263ee543/icons/nopic.png', fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry scnlog search is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))
    try:
        url = 'http://www.srmovie.com/?s='+query 
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<div class="post-thumbnail">\s*?<a href="(.+?)" title=".+?" rel="bookmark">\s*?<img width="150" height="150" src="(.+?)" class="attachment-thumbnail wp-post-image" alt="(.+?)" />', re.DOTALL).findall(html)
        for url, img, title in match:
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title + ' [COLOR yellow](srmovie)[/COLOR]'}, img= img, fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry srmovie search is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))
    try:
        url = 'http://www.publizhare.com/?s='+query 
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h2 class="entry-title">\s*?<a href="(.+?)" title=".+?" rel="bookmark">(.+?)</a>\s*?</h2>', re.DOTALL).findall(html)
        for url, title in match:
                title = title.replace('.', ' ')
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title + ' [COLOR yellowgreen](publizhare)[/COLOR]'}, img= 'https://raw.githubusercontent.com/TheYid/yidpics/8333f2912d71cc7ddd71a7cee9714dfe263ee543/icons/nopic.png', fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry publizhare search is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))
    try:
        url = 'http://warezaz.com/?s='+query 
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<div class="clearfix entry-content">\s*?<p style="text-align:center"><img src="(.+?)" title="(.+?)" alt=".+?" /></p>\s*?<p> <a href="(.+?)" class=".+?">', re.DOTALL).findall(html)
        for img, title, url in match:
                title = title.replace('.', ' ')
                addon.add_directory({'mode': 'GetLinks9', 'url': url}, {'title':  title + ' [COLOR Indigo](warezaz)[/COLOR]'}, img= img, fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry warezaz search is down [/B][/COLOR],[COLOR olive][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))
    try:
        url = 'http://tv2show.com/?s='+query 
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h1.+?href="(.+?)">(.+?)<.+?src="(.+?)"', re.DOTALL).findall(html)
        for url, title, img in match:
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title + ' [COLOR peachpuff](tv2show)[/COLOR]'}, img= img, fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry tv2show search is down [/B][/COLOR],[COLOR olive][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))
    try:
        url = 'http://www.moviesready.com/index.php?do='+query 
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<div class="movieposter" title=".+?">\s*?<a href="(.+?)"><img src="(.+?)" width="110" height="150" alt=".+?" title=".+?"/></a>\s*?<div class="shortname">(.+?)</div', re.DOTALL).findall(html)
        for url, img, title in match:
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title + ' [COLOR lavender](moviesready)[/COLOR]'}, img= 'http://www.moviesready.com' + img, fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry moviesready search is down [/B][/COLOR],[COLOR olive][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))
    try:
        url = 'http://www.filestube.to/query.html?q='+ query + '&select=mkv'
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('target="_blank" rel="nofollow" href=".+?"><span id="/video/(.+?)">.+?</span></a>', re.DOTALL).findall(html)
        for url in match:
                addon.add_directory({'mode': 'GetLinks', 'url': 'http://www.filestube.to/video/' + url}, {'title': url.replace('-', ' ').replace('.html', ' ') + ' [COLOR lavender](filetube)[/COLOR]'}, img= 'https://raw.githubusercontent.com/TheYid/yidpics/8333f2912d71cc7ddd71a7cee9714dfe263ee543/icons/nopic.png', fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry filetube search is down [/B][/COLOR],[COLOR olive][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))


#------------------------------------------------------------------------------ sport search ----------------------------------------------------------------------------------#

def GetSearchQuery11():
	last_search = addon.load_data('search')
	if not last_search: last_search = ''
	keyboard = xbmc.Keyboard()
        keyboard.setHeading('[COLOR green]MEGA ADDON SEARCH[/COLOR]')
	keyboard.setDefault(last_search)
	keyboard.doModal()
	if (keyboard.isConfirmed()):
                query = keyboard.getText()
                addon.save_data('search',query)
                Search11(query)
	else:
                return

def Search11(query):
    try:
        url = 'http://dx-tv.com/?s=' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('entry-title.+?href="(.+?)">(.+?)<.+?src="(.+?)"', re.DOTALL).findall(html)
        for movieUrl, title, img in match:
                title = title.replace('.', ' ')
                addon.add_directory({'mode': 'GetLinks', 'url': movieUrl}, {'title':  title + ' [COLOR chartreuse](DX-TV)[/COLOR]'}, img= img, fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry DXTV search is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))
    try:
        url = 'http://shawnrebecca.com/?s=' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h2.+?href="(.+?)".+?>(.+?)<.+?', re.DOTALL).findall(html)
        for movieUrl, title in match:
                addon.add_directory({'mode': 'GetLinks3', 'url': movieUrl}, {'title':  title + ' [COLOR orange](Fight-BB)[/COLOR]'}, img= 'https://raw.githubusercontent.com/TheYid/yidpics/8333f2912d71cc7ddd71a7cee9714dfe263ee543/icons/nopic.png', fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry FIGHT BB search is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))
    try:
        url = 'http://uploaded-free-download.biz/?s=' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h1 class="entry-title"><a href="(.+?)" title=".+?" rel="bookmark">(.+?)</a></h1>', re.DOTALL).findall(html)
        for movieUrl, title in match:
                addon.add_directory({'mode': 'GetLinks6', 'url': movieUrl}, {'title':  title + ' [COLOR lavenderblush](UFD)[/COLOR]'}, img= 'https://raw.githubusercontent.com/TheYid/yidpics/8333f2912d71cc7ddd71a7cee9714dfe263ee543/icons/nopic.png', fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry UFD search is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))
    try:
        url = 'http://www.tvshowspad.com/?s=' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h2 id=".+?"><a href="(.+?)" rel="bookmark" title=".+?">(.+?)</a></h2', re.DOTALL).findall(html)
        for movieUrl, title in match:
                addon.add_directory({'mode': 'GetLinks7', 'url': movieUrl}, {'title':  title + ' [COLOR khaki](tvshowspad)[/COLOR]'}, img= 'https://raw.githubusercontent.com/TheYid/yidpics/8333f2912d71cc7ddd71a7cee9714dfe263ee543/icons/nopic.png', fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry tvshowspad search is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))
    try:
        url = 'http://tv-release.net/?s=' +query+'&cat='
        url = url.replace(' ', '%20')
        print url
        html = net.http_GET(url).content
        match = re.compile("width='60%' style='text-align:left; font-size:12px;font-weight:bold;'><a href='(.+?)'>(.+?)</a></td><td", re.DOTALL).findall(html)
        for movieUrl, title in match:
                title = title.replace('.', ' ')
                addon.add_directory({'mode': 'GetLinks1', 'url': movieUrl}, {'title':  title + ' [COLOR red](Rls-TV)[/COLOR]'}, img= 'https://raw.githubusercontent.com/TheYid/yidpics/8333f2912d71cc7ddd71a7cee9714dfe263ee543/icons/nopic.png', fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry RLSTV search is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

##.replace('/', ' ')## \s*? ## 
#-------------------------------------------------------------------------- rlsbb ----------------------------------------------------------------------------------------------#

def GetSearchQuery1():
	last_search = addon.load_data('search')
	if not last_search: last_search = ''
	keyboard = xbmc.Keyboard()
        keyboard.setHeading('[COLOR green]RLSBB SEARCH[/COLOR]')
	keyboard.setDefault(last_search)
	keyboard.doModal()
	if (keyboard.isConfirmed()):
                query = keyboard.getText()
                addon.save_data('search',query)
                Search1(query)
	else:
                return
def Search1(query):
    try:
        url = 'http://www.rlsbb.com/?s=' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('postHeader.+?href="(.+?)".+?>(.+?)<.+?src=.+? src="(.+?)"', re.DOTALL).findall(html)
        for movieUrl, title, img in match:
                addon.add_directory({'mode': 'GetLinks', 'url': movieUrl}, {'title':  title }, img= img, fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry rlsbb search is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#--------------------------------------------------------------------------  ----------------------------------------------------------------------------------------------#

def GetSearchQuery2():
	last_search = addon.load_data('search')
	if not last_search: last_search = ''
	keyboard = xbmc.Keyboard()
        keyboard.setHeading('[COLOR green]Publizhare SEARCH[/COLOR]')
	keyboard.setDefault(last_search)
	keyboard.doModal()
	if (keyboard.isConfirmed()):
                query = keyboard.getText()
                addon.save_data('search',query)
                Search2(query)
	else:
                return
def Search2(query):
    try:
        url = 'http://www.publizhare.com/?s='+query 
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h2 class="entry-title">\s*?<a href="(.+?)" title=".+?" rel="bookmark">(.+?)</a>\s*?</h2>', re.DOTALL).findall(html)
        for url, title in match:
                title = title.replace('.', ' ')
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title }, img= 'https://raw.githubusercontent.com/TheYid/yidpics/8333f2912d71cc7ddd71a7cee9714dfe263ee543/icons/nopic.png', fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry publizhare search is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))


#https://raw.githubusercontent.com/TheYid/yidpics/8333f2912d71cc7ddd71a7cee9714dfe263ee543/icons/nopic.png#
####################################################################### setViews #######################################################################################

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

#######################################################################################################################################################################

if mode == 'main': 
	MainMenu()
elif mode == 'HelpMenu':
        HelpMenu()
elif mode == 'GetTitles': 
	GetTitles(section, url, startPage, numOfPages)
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
elif mode == 'GetTitles9': 
	GetTitles9(section, url, startPage, numOfPages)
elif mode == 'GetTitles1': 
	GetTitles1(section, url, startPage, numOfPages)
elif mode == 'GetTitles10': 
	GetTitles10(section, url, startPage, numOfPages)
elif mode == 'GetTitles11': 
	GetTitles11(section, url, startPage, numOfPages)
elif mode == 'GetTitles12': 
	GetTitles12(section, url, startPage, numOfPages)
elif mode == 'GetTitles13': 
	GetTitles13(section, url, startPage, numOfPages)
elif mode == 'GetTitles14': 
	GetTitles14(section, url, startPage, numOfPages)
elif mode == 'GetTitles16': 
	GetTitles16(section, url, startPage, numOfPages)
elif mode == 'GetTitles17': 
	GetTitles17(section, url, startPage, numOfPages)
elif mode == 'GetTitles18': 
	GetTitles18(section, url, startPage, numOfPages)
elif mode == 'GetTitles19': 
	GetTitles19(section, url, startPage, numOfPages)
elif mode == 'GetTitles20': 
	GetTitles20(section, url, startPage, numOfPages)
elif mode == 'GetTitles21': 
	GetTitles21(section, url, startPage, numOfPages)
elif mode == 'GetTitles22': 
	GetTitles22(section, url, startPage, numOfPages)
elif mode == 'GetTitles23': 
	GetTitles23(section, url, startPage, numOfPages)
elif mode == 'GetTitles24': 
	GetTitles24(section, url, startPage, numOfPages)
elif mode == 'GetTitles25': 
	GetTitles25(query)
elif mode == 'GetTitles25a': 
	GetTitles25a(query)
elif mode == 'GetTitles26': 
	GetTitles26(query)
elif mode == 'GetTitles27': 
	GetTitles27(url)
elif mode == 'GetTitles28': 
	GetTitles28(query)
elif mode == 'GetTitles29': 
	GetTitles29(section, query, startPage, numOfPages)
elif mode == 'GetTitles30': 
	GetTitles30(section, url, startPage, numOfPages)
elif mode == 'GetLinks':
	GetLinks(section, url)
elif mode == 'GetLinks1':
	GetLinks1(section, url)
elif mode == 'GetLinks3':
	GetLinks3(section, url)
elif mode == 'GetLinks4':
	GetLinks4(section, url)
elif mode == 'GetLinks5':
	GetLinks5(section, url)
elif mode == 'GetLinks6':
	GetLinks6(section, url)
elif mode == 'GetLinks7':
	GetLinks7(section, url)
elif mode == 'GetLinks8':
	GetLinks8(section, url)
elif mode == 'GetLinks9':
	GetLinks9(section, url)
elif mode == 'Categories':
        Categories(url)
elif mode == 'GetSearchQuery1':
	GetSearchQuery1()
elif mode == 'Search1':
	Search1(query)
elif mode == 'GetSearchQuery2':
	GetSearchQuery2()
elif mode == 'Search2':
	Search2(query)
elif mode == 'GetSearchQuery10':
	GetSearchQuery10()
elif mode == 'Search10':
	Search10(query)
elif mode == 'GetSearchQuery11':
	GetSearchQuery11()
elif mode == 'Search11':
	Search11(query)
elif mode == 'PlayVideo':
	PlayVideo(url, listitem)
elif mode == 'PlayVideo3':
	PlayVideo3(url, listitem)	
elif mode == 'ResolverSettings':
        urlresolver.display_settings()
elif mode == 'Categories':
        Categories()
if mode == 'menu2':
       Menu2()
if mode == 'menu3':
       Menu3()
if mode == 'menu4':
       Menu4()
if mode == 'menu5':
       Menu5()
if mode == 'menu6':
       Menu6()
if mode == 'menu7':
       Menu7()
if mode == 'menu8':
       Menu8()
if mode == 'menu9':
       Menu9()
if mode == 'menu11':
       Menu11()
if mode == 'menu12':
       Menu12()
if mode == 'menu13':
       Menu13()
if mode == 'menu14':
       Menu14()
elif mode == 'Help':
    import helpbox
    helpbox.HelpBox()

xbmcplugin.endOfDirectory(int(sys.argv[1]))