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

########### url's ###########
BASE_URL = 'http://rls-center.com/'
BASE_URL1 = 'http://www.scnsrc.me/'
BASE_URL2 = 'http://scenelog.eu/'
BASE_URL3 = 'http://crazyhdsource.com/'
BASE_URL5 = 'http://www.theextopia.com/'
BASE_URL6 = 'http://com2dl.com/'
BASE_URL7 = 'http://www.wrzko.eu/'
BASE_URL8 = 'http://sceper.ws/'
BASE_URL9 = 'http://scenedown.in/'
BASE_URL10 = 'http://www.ddlvalley.eu/'
BASE_URL11 = 'http://www.rlsbb.com/'
BASE_URL12 = 'http://300mbmovies4u.com/'
BASE_URL13 = 'http://shawnrebecca.com/'
BASE_URL15 = 'http://www.fullmatches.net/'
BASE_URL16 = 'http://tv-release.net/'
BASE_URL17 = 'http://www.tribalmixes.com/'
BASE_URL18 = 'http://www.freshremix.org/'

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

############################################################################### Movie Titles #######################################################################################

def GetTitles(section, url, startPage= '1', numOfPages= '1'):   # Release Center
    try:
        print 'theyidrh get Movie Titles Menu %s' % url
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
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')        
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site mite be down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def GetTitles2(section, url, startPage= '1', numOfPages= '1'): # scenelog
    try:
        print 'theyidrh get Movie Titles Menu %s' % url
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
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img=IconPath + 'sl.png', fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles2', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site mite be down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def GetTitles3(section, url, startPage= '1', numOfPages= '1'): #crazyhdsource
    try:
        print 'theyidrh get Movie Titles Menu %s' % url
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
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles3', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue]Next...[/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site mite be down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def GetTitles4(section, url, startPage= '1', numOfPages= '1'): #com2dl
    try:
        print 'theyidrh get Movie Titles Menu %s' % url
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
                match = re.compile('shstory-img.+?href="(.+?)"><img src="(.+?)" alt="(.+?)"', re.DOTALL).findall(html)
                for movieUrl, img, name in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles4', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')       
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site mite be down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def GetTitles5(section, url, startPage= '1', numOfPages= '1'): #300mbmovies4u
    try:
        print 'theyidrh get Movie Titles Menu %s' % url
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
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles5', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view') 
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site mite be down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def GetTitles6(section, url, startPage= '1', numOfPages= '1'): #Scene down
    try:
        print 'theyidrh get Movie Titles Menu %s' % url
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
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles6', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')        
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site mite be down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def GetTitles7(section, url, startPage= '1', numOfPages= '1'): # Sceper
    try:
        print 'theyidrh get Movie Titles Menu %s' % url
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
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles7', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')       
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site mite be down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def GetTitles8(section, url, startPage= '1', numOfPages= '1'): # rls-tv
    try:
        print 'theyidrh get Movie Titles Menu %s' % url
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + '/index.php?page=' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + '/index.php?page=' + str(page) + '/'
                        html = net.http_GET(pageUrl).content
                match = re.compile("<td width=.+? style=.+?><a href='(.+?)'>(.+?)</a></td><td", re.DOTALL).findall(html)
                for movieUrl, name in match:
                        addon.add_directory({'mode': 'GetLinks1', 'section': section, 'url': 'http://tv-release.net/' + movieUrl}, {'title':  name.strip()}, img=IconPath + 'rlstv.png', fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site mite be down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def GetTitles9(section, url, startPage= '1', numOfPages= '1'): #wrzko
    try:
        print 'theyidrh get Movie Titles Menu %s' % url
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
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles9', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')        
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site mite be down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def GetTitles1(section, url, startPage= '1', numOfPages= '1'): #scnsrc movies
    try:
        print 'theyidrh get Movie Titles Menu %s' % url
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
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles1', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')        
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site mite be down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#------------------------------------------#

def GetTitles10(section, url, startPage= '1', numOfPages= '1'): #scnsrc tv
    try:
        print 'theyidrh get Movie Titles Menu %s' % url
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
                match = re.compile('<h2.+?href="(.+?)".+?>(.+?)<.+?.+?src=(.+?)', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles10', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')       
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site mite be down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def GetTitles11(section, url, startPage= '1', numOfPages= '1'): #ddlv
    try:
        print 'theyidrh get Movie Titles Menu %s' % url
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
                        addon.add_directory({'mode': 'GetLinks3', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles11', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')        
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site mite be down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def GetTitles12(section, url, startPage= '1', numOfPages= '1'): #rbb
    try:
        print 'theyidrh get Movie Titles Menu %s' % url
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
                match = re.compile('postHeader.+?href="(.+?)".+?>(.+?)<.+?src=.+? src="(.+?)"', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles12', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site mite be down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#------------------------------------#

def GetTitles13(section, url, startPage= '1', numOfPages= '1'):  #rbb2
    try:
        print 'theyidrh get Movie Titles Menu %s' % url
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
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site mite be down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def GetTitles14(section, url, startPage= '1', numOfPages= '1'): # Extopia
    try:
        print 'theyidrh get Movie Titles Menu %s' % url
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
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles14', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')       
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site mite be down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def GetTitles16(section, url, startPage= '1', numOfPages= '1'): # fullmatch
    try:
        print 'theyidrh get Movie Titles Menu %s' % url
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
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img=IconPath + 'fullsport.png', fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles16', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site mite be down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def GetTitles17(section, url, startPage= '1', numOfPages= '1'): # Fight-BB
    try:
        print 'theyidrh get Movie Titles Menu %s' % url
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
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img=IconPath + 'fbb.png', fanart=FanartPath + 'fanart.png') 
                addon.add_directory({'mode': 'GetTitles17', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site mite be down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def GetTitles18(section, url, startPage= '1', numOfPages= '1'): #house
    try:
        print 'theyidrh get Movie Titles Menu %s' % url
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
                match = re.compile('width=100%><a href="(.+?)" class=.+? ><.+?>(.+?)</font>(.+?)</a></td>', re.DOTALL).findall(html)
                for movieUrl, name, name in match:
                        addon.add_directory({'mode': 'GetLinks2', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img=IconPath + 'tm.png', fanart=FanartPath + 'fanart.png') 
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site mite be down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def GetTitles19(section, url, startPage= '1', numOfPages= '1'): # freshremix
    try:
        print 'theyidrh get Movie Titles Menu %s' % url
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
                match = re.compile('<h2.+?href="(.+?)">(.+?)<.+?src="(.+?)".+?', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles19', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site mite be down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#################################################################################getlinks###############################################################################################

def GetLinks(section, url): # Get Links
        print 'GETLINKS FROM URL: '+url
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
                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title':  host + ' [COLOR gold]:[/COLOR] ' + title}, img=IconPath + 'play.png', fanart=FanartPath + 'fanart.png')

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

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def GetLinks1(section, url): #RLStv
    try:
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

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def GetLinks2(section, url): # #house
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('width=150 > (.+?)<').findall(content)
        listitem = GetMediaInfo(content)
        for url in match:
                host = GetDomain(url)
                if urlresolver.HostedMediaFile(url= url):
                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title':  host }, img=IconPath + 'play.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def GetLinks3(section, url): # Get Links ddlvalley
    try:
        print 'GETLINKS FROM URL: '+url
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

############################################################################# PlayVideo #################################################################################

def PlayVideo(url, listitem):
    try:
        print 'in PlayVideo %s' % url
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

############################################################################# Menus ################################################################################################

def MainMenu():    #homescreen        
        addon.add_directory({'mode': 'menu2'}, {'title': '[COLOR blue][B]Movies >>[/B] [/COLOR]>>'}, img=IconPath + 'films.png', fanart=FanartPath + 'fanart.png') 
        addon.add_directory({'mode': 'menu4'}, {'title': '[COLOR darkorange][B]Tv Shows >>[/B] [/COLOR]>>'}, img=IconPath + 'tv2.png', fanart=FanartPath + 'fanart.png') 
        addon.add_directory({'mode': 'menu6'}, {'title': '[COLOR lemonchiffon][B]Sport >>[/B] [/COLOR]>>'}, img=IconPath + 'sport1.png', fanart=FanartPath + 'fanart.png') 
        addon.add_directory({'mode': 'menu7'}, {'title': '[COLOR violet][B]Anime >>[/B] [/COLOR]>>'}, img=IconPath + 'anex.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'menu13'}, {'title':  '[COLOR cadetblue][B]Music >[/B][/COLOR] >'}, img=IconPath + 'music.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'menu5'}, {'title': '[COLOR green][B]Searches >>[/B] [/COLOR]>>'}, img=IconPath + 'searches.png', fanart=FanartPath + 'fanart.png') 
        addon.add_directory({'mode': 'ResolverSettings'}, {'title':  '[COLOR red]Resolver Settings[/COLOR]'}, img=IconPath + 'resolver.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'HelpMenu'}, {'title':  '[COLOR pink][B]PLEASE CLICK HERE FOR INFO ON TheYids REPO[/B][/COLOR] >>'}, img=IconPath + 'helphub.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'HelpMenu'}, {'title':  '[COLOR gold][B]FOLLOW ME ON TWITTER... [/B][/COLOR] [COLOR aqua][B][I]@TheYid009 [/B][/I][/COLOR] '}, img=IconPath + 'twit.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def HelpMenu():   
        dialog = xbmcgui.Dialog()
        dialog.ok("TheYid's REPO", "I now have a donation button setup at xbmcHUB", "please help keep TheYid's REPO alive more info @","http://www.xbmchub.com/forums/")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def Menu13():   #music
        addon.add_directory({'mode': 'GetTitles18', 'section': 'ALL', 'url': BASE_URL17 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue][B]House Music mixes[/B] [/COLOR] [COLOR crimson](tribalmixes.com)[/COLOR] >>'}, img=IconPath + 'tm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles19', 'section': 'ALL', 'url': BASE_URL18 + '/video',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue][B]1080p Music videos[/B] [/COLOR] [COLOR darkorchid](freshremix.org)[/COLOR] >>'}, img=IconPath + 'fm.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def Menu2():   #movies
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
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL7 + '/movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue][B]Latest Movies[/B] [/COLOR] [COLOR deepskyblue](wrzKO)[/COLOR] >>'}, img=IconPath + 'wmovies.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL6 + '/movie/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue][B]Latest Movies[/B] [/COLOR] [COLOR darkorchid](Com2dl.com)[/COLOR] >>'}, img=IconPath + 'commovies.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles14', 'section': 'ALL', 'url': BASE_URL5 + '/category/movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue][B]Latest Movies[/B] [/COLOR] [COLOR whitesmoke](The Extopia)[/COLOR] >>'}, img=IconPath + 'exmo.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL2 + '/movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue][B]Latest Movies[/B] [/COLOR] [COLOR powderblue](SceneLog)[/COLOR] >>'}, img=IconPath + 'slm1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'menu9'}, {'title': '[COLOR blue][B]Latest Movies[/B] [/COLOR] [COLOR crimson](300mb movies4u)[/COLOR] >>'}, img=IconPath + 'm4u1.png', fanart=FanartPath + 'fanart.png') 
        addon.add_directory({'mode': 'menu3'}, {'title': '[COLOR steelblue][B]YIFY Movies >>[/B] [/COLOR]>>'}, img=IconPath + 'yify.png', fanart=FanartPath + 'fanart.png') 
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def Menu9():   #300mb movies4u
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

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def Menu3():   #yify
        addon.add_directory({'mode': 'GetTitles5', 'section': 'ALL', 'url': BASE_URL12 + '/category/hollywood-movie/english-yify-movie/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR steelblue][B]Latest YIFY[/B][/COLOR] [COLOR crimson](300mb movies4u) [/COLOR] >>'}, img=IconPath + 'm4u1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL7 + '/movies/yify-brrip-1080p/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR steelblue][B]Latest 1080p YIFY[/B] [/COLOR] [COLOR deepskyblue](wrzKO)[/COLOR] >>'}, img=IconPath + 'wmovies.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL7 + '/movies/yify-brrip-720p/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR steelblue][B]Latest 720p YIFY[/B] [/COLOR] [COLOR deepskyblue](wrzKO)[/COLOR] >>'}, img=IconPath + 'wmovies.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles11', 'section': 'ALL', 'url': BASE_URL10 + '/category/movies/yify-rips/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR steelblue][B]Latest YIFY[/B] [/COLOR] [COLOR powderblue](DDLvalley)[/COLOR] >>'}, img=IconPath + 'ddlmo.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def Menu4():    #tv
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
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL7 + '/tv-shows/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Latest Tv Shows[/B] [/COLOR] [COLOR deepskyblue](wrzKO)[/COLOR] >>'}, img=IconPath + 'wtv.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles10', 'section': 'ALL', 'url': BASE_URL1 + '/tv/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Latest Tv Shows[/B] [/COLOR] [COLOR orangered](Scene Source)[/COLOR] >>'}, img=IconPath + 'sstv.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles14', 'section': 'ALL', 'url': BASE_URL5 + '/category/tvshow/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Latest Releases[/B] [/COLOR] [COLOR whitesmoke](The Extopia)[/COLOR] >>'}, img=IconPath + 'extv1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles5', 'section': 'ALL', 'url': BASE_URL12 + '/category/tv-shows/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Latest Tv Shows[/B][/COLOR] [COLOR crimson](300mb movies4u)[/COLOR] >>'}, img=IconPath + '3mb4.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL2 + '/tv-shows/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Latest Tv shows[/B] [/COLOR] [COLOR powderblue](SceneLog)[/COLOR] >>'}, img=IconPath + 'slt1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'menu11'}, {'title': '[COLOR darkorange][B]Latest Added[/B] [/COLOR] [COLOR blue](1080p zone)[/COLOR] >>'}, img=IconPath + '1080.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def Menu11():    #Crazy hd
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/tv-show',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Latest 1080p Releases[/B] [/COLOR] [COLOR lightcyan](Crazy hd Source)[/COLOR] >>'}, img=IconPath + 'chd.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles14', 'section': 'ALL', 'url': BASE_URL5 + '/category/tvshow/web-dl/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Latest 1080p / 720p packs[/B] [/COLOR] [COLOR whitesmoke](The Extopia)[/COLOR] >>'}, img=IconPath + 'extv1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'menu12'}, {'title': '[COLOR darkorange][B]Latest 1080p / 720p[/B] [/COLOR] [COLOR red](Rls-TV)[/COLOR] >>'}, img=IconPath + 'rlstv.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def Menu12():    #rlstv
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

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def Menu5():   #search
        addon.add_directory({'mode': 'GetSearchQuery8'},  {'title':  '[COLOR green][B]Search[/B] [/COLOR] [COLOR powderblue](DDLvalley)[/COLOR]'}, img=IconPath + 'searches.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetSearchQuery'},  {'title':  '[COLOR green][B]Search[/B] [/COLOR] [COLOR lime](Release Center)[/COLOR]'}, img=IconPath + 'searches.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetSearchQuery5'},  {'title':  '[COLOR green][B]Search[/B] [/COLOR] [COLOR mediumspringgreen](Sceper)[/COLOR]'}, img=IconPath + 'searches.png', fanart=FanartPath + 'fanart.png')
        #addon.add_directory({'mode': 'GetSearchQuery4'},  {'title':  '[COLOR green][B]Search[/B] [/COLOR] [COLOR plum](Scene down)[/COLOR]'}, img=IconPath + 'searches.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetSearchQuery2'},  {'title':  '[COLOR green][B]Search[/B] [/COLOR] [COLOR skyblue](Newdownload.net)[/COLOR]'}, img=IconPath + 'searches.png', fanart=FanartPath + 'fanart.png')
        #addon.add_directory({'mode': 'GetSearchQuery3'},  {'title':  '[COLOR green][B]Search[/B] [/COLOR] [COLOR deepskyblue](wrzKO)[/COLOR]'}, img=IconPath + 'searches.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetSearchQuery6'},  {'title':  '[COLOR green][B]Search[/B] [/COLOR] [COLOR orangered](Scene Source)[/COLOR]'}, img=IconPath + 'searches.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetSearchQuery7'},  {'title':  '[COLOR green][B]Search[/B] [/COLOR] [COLOR orange](Release 1 click)[/COLOR]'}, img=IconPath + 'searches.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetSearchQuery9'},  {'title':  '[COLOR green][B]Search[/B] [/COLOR] [COLOR gold](ReleaseBB)[/COLOR]'}, img=IconPath + 'searches.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def Menu6():   #sport

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
        addon.add_directory({'mode': 'GetTitles17', 'section': 'ALL', 'url': BASE_URL13 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lemonchiffon][B]Latest MMA/Wrestling/Boxing[/B] [COLOR orange](Fight-BB)[/COLOR] >>'}, img=IconPath + 'fbb.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'menu8'}, {'title': '[COLOR lightyellow][B]Football Full Matches[/B] [/COLOR]>>'}, img=IconPath + 'fullsport.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def Menu8():   #fullmatch
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

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def Menu7():   #anime
        addon.add_directory({'mode': 'GetTitles14', 'section': 'ALL', 'url': BASE_URL5 + '/category/anime/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR violet][B]Latest[/B] [/COLOR] [COLOR whitesmoke](The Extopia)[/COLOR] >>'}, img=IconPath + 'exan.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles14', 'section': 'ALL', 'url': BASE_URL5 + '/category/anime/movie/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR violet][B]Anime Movies[/B] [/COLOR] [COLOR whitesmoke](The Extopia)[/COLOR] >>'}, img=IconPath + 'exan.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles14', 'section': 'ALL', 'url': BASE_URL5 + '/category/anime/ovaspecial/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR violet][B]Anime Ova & Special[/B] [/COLOR] [COLOR whitesmoke](The Extopia)[/COLOR] >>'}, img=IconPath + 'exan.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles14', 'section': 'ALL', 'url': BASE_URL5 + '/category/anime/packs/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR violet][B]Anime Packs[/B] [/COLOR] [COLOR whitesmoke](The Extopia)[/COLOR] >>'}, img=IconPath + 'exan.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

############################################################################## searches #############################################################################################

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
        url = 'http://www.google.com/search?q=site:rls-center.com ' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h3 class="r"><a href="(.+?)".+?onmousedown=".+?">(.+?)</a>').findall(html)
        for url, title in match:
                title = title.replace('<b>...</b>', '').replace('<em>', '').replace('</em>', '')
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title})
	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def GetSearchQuery2():
	last_search = addon.load_data('search')
	if not last_search: last_search = ''
	keyboard = xbmc.Keyboard()
        keyboard.setHeading('[COLOR green]Search[/COLOR]')
	keyboard.setDefault(last_search)
	keyboard.doModal()
	if (keyboard.isConfirmed()):
                query = keyboard.getText()
                addon.save_data('search',query)
                Search2(query)
	else:
                return
def Search2(query):
        url = 'http://www.google.com/search?q=site:newdownload.net ' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h3 class="r"><a href="(.+?)".+?onmousedown=".+?">(.+?)</a>').findall(html)
        for url, title in match:
                title = title.replace('<b>...</b>', '').replace('<em>', '').replace('</em>', '')
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title})
	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def GetSearchQuery3():
	last_search = addon.load_data('search')
	if not last_search: last_search = ''
	keyboard = xbmc.Keyboard()
        keyboard.setHeading('[COLOR green]Search[/COLOR]')
	keyboard.setDefault(last_search)
	keyboard.doModal()
	if (keyboard.isConfirmed()):
                query = keyboard.getText()
                addon.save_data('search',query)
                Search3(query)
	else:
                return
def Search3(query):
        url = 'http://www.google.com/search?q=site:wrzko.eu ' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h3 class="r"><a href="(.+?)".+?onmousedown=".+?">(.+?)</a>').findall(html)
        for url, title in match:
                title = title.replace('<b>...</b>', '').replace('<em>', '').replace('</em>', '')
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title})
	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def GetSearchQuery4():
	last_search = addon.load_data('search')
	if not last_search: last_search = ''
	keyboard = xbmc.Keyboard()
        keyboard.setHeading('[COLOR green]Search[/COLOR]')
	keyboard.setDefault(last_search)
	keyboard.doModal()
	if (keyboard.isConfirmed()):
                query = keyboard.getText()
                addon.save_data('search',query)
                Search4(query)
	else:
                return
def Search4(query):
        url = 'http://www.google.com/search?q=site:scenedown.me ' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h3 class="r"><a href="(.+?)".+?onmousedown=".+?">(.+?)</a>').findall(html)
        for url, title in match:
                title = title.replace('<b>...</b>', '').replace('<em>', '').replace('</em>', '')
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title})
	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def GetSearchQuery5():
	last_search = addon.load_data('search')
	if not last_search: last_search = ''
	keyboard = xbmc.Keyboard()
        keyboard.setHeading('[COLOR green]Search[/COLOR]')
	keyboard.setDefault(last_search)
	keyboard.doModal()
	if (keyboard.isConfirmed()):
                query = keyboard.getText()
                addon.save_data('search',query)
                Search5(query)
	else:
                return
def Search5(query):
        url = 'http://www.google.com/search?q=site:sceper.ws ' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h3 class="r"><a href="(.+?)".+?onmousedown=".+?">(.+?)</a>').findall(html)
        for url, title in match:
                title = title.replace('<b>...</b>', '').replace('<em>', '').replace('</em>', '')
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title})
	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def GetSearchQuery6():
	last_search = addon.load_data('search')
	if not last_search: last_search = ''
	keyboard = xbmc.Keyboard()
        keyboard.setHeading('[COLOR green]Search[/COLOR]')
	keyboard.setDefault(last_search)
	keyboard.doModal()
	if (keyboard.isConfirmed()):
                query = keyboard.getText()
                addon.save_data('search',query)
                Search6(query)
	else:
                return 
def Search6(query):
        url = 'http://www.google.com/search?q=site:scnsrc.me ' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h3 class="r"><a href="(.+?)".+?onmousedown=".+?">(.+?)</a>').findall(html)
        for url, title in match:
                title = title.replace('<b>...</b>', '').replace('<em>', '').replace('</em>', '')
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title})
	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def GetSearchQuery7():
	last_search = addon.load_data('search')
	if not last_search: last_search = ''
	keyboard = xbmc.Keyboard()
        keyboard.setHeading('[COLOR green]Search[/COLOR]')
	keyboard.setDefault(last_search)
	keyboard.doModal()
	if (keyboard.isConfirmed()):
                query = keyboard.getText()
                addon.save_data('search',query)
                Search7(query)
	else:
                return
def Search7(query):
        url = 'http://www.google.com/search?q=site:rls1click.com ' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h3 class="r"><a href="(.+?)".+?onmousedown=".+?">(.+?)</a>').findall(html)
        for url, title in match:
                title = title.replace('<b>...</b>', '').replace('<em>', '').replace('</em>', '')
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title})
	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def GetSearchQuery8():
	last_search = addon.load_data('search')
	if not last_search: last_search = ''
	keyboard = xbmc.Keyboard()
        keyboard.setHeading('[COLOR green]Search[/COLOR]')
	keyboard.setDefault(last_search)
	keyboard.doModal()
	if (keyboard.isConfirmed()):
                query = keyboard.getText()
                addon.save_data('search',query)
                Search8(query)
	else:
                return
def Search8(query):
        url = 'http://www.google.com/search?q=site:ddlvalley.eu ' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h3 class="r"><a href="(.+?)".+?onmousedown=".+?">(.+?)</a>').findall(html)
        for url, title in match:
                title = title.replace('<b>...</b>', '').replace('<em>', '').replace('</em>', '')
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title})
	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def GetSearchQuery9():
	last_search = addon.load_data('search')
	if not last_search: last_search = ''
	keyboard = xbmc.Keyboard()
        keyboard.setHeading('[COLOR green]Search[/COLOR]')
	keyboard.setDefault(last_search)
	keyboard.doModal()
	if (keyboard.isConfirmed()):
                query = keyboard.getText()
                addon.save_data('search',query)
                Search9(query)
	else:
                return
def Search9(query):
        url = 'http://www.google.com/search?q=site:rlsbb.com ' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h3 class="r"><a href="(.+?)".+?onmousedown=".+?">(.+?)</a>').findall(html)
        for url, title in match:
                title = title.replace('<b>...</b>', '').replace('<em>', '').replace('</em>', '')
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title})
	xbmcplugin.endOfDirectory(int(sys.argv[1]))

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
elif mode == 'GetLinks':
	GetLinks(section, url)
elif mode == 'GetLinks1':
	GetLinks1(section, url)
elif mode == 'GetLinks2':
	GetLinks2(section, url)
elif mode == 'GetLinks3':
	GetLinks3(section, url)
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
elif mode == 'GetSearchQuery5':
	GetSearchQuery5()
elif mode == 'Search5':
	Search5(query)
elif mode == 'GetSearchQuery6':
	GetSearchQuery6()
elif mode == 'Search6':
	Search6(query)
elif mode == 'GetSearchQuery7':
	GetSearchQuery7()
elif mode == 'Search7':
	Search7(query)
elif mode == 'GetSearchQuery8':
	GetSearchQuery8()
elif mode == 'Search8':
	Search8(query)
elif mode == 'GetSearchQuery9':
	GetSearchQuery9()
elif mode == 'Search9':
	Search9(query)
elif mode == 'PlayVideo':
	PlayVideo(url, listitem)	
elif mode == 'ResolverSettings':
        urlresolver.display_settings()
elif mode == 'Categories':
        Categories(section)
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

xbmcplugin.endOfDirectory(int(sys.argv[1]))