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

addon_id = 'plugin.video.allinone'
plugin = xbmcaddon.Addon(id=addon_id)
net = Net()
addon = Addon('plugin.video.allinone', sys.argv)
DB = os.path.join(xbmc.translatePath("special://database"), 'allinone.db')
BASE_URL = 'http://oneclickwatch.org/'
BASE_URL1 = 'http://watchthetapes.com/'
BASE_URL2 = 'http://www.watchtvshowz.org/'
BASE_URL3 = 'http://viooz.pw/'
BASE_URL4 = 'http://www.ultra-vid.com/'
BASE_URL5 = 'http://moviesall4u.com/'
BASE_URL6 = 'http://www1.zmovie.tw/'
BASE_URL7 = 'http://www.movie-kingdom.com/'
BASE_URL8 = 'http://watchseriesus.com/'
BASE_URL9 = 'http://www.oneclickmoviez.ag/'
BASE_URL10 = 'http://www.myvideolinks.eu/'
BASE_URL11 = 'http://www.ddlvalley.eu/'
BASE_URL12 = 'http://before2000.com/'
BASE_URL13 = 'http://fullepisode.info/'
BASE_URL14 = 'http://www.channelcut.me/'
BASE_URL15 = 'http://putseries.com/'
BASE_URL16 = 'http://putlocker.bz/'
BASE_URL17 = 'http://tv-junky.eu/'
BASE_URL19 = 'http://all4youz.com/'
BASE_URL20 = 'http://world4ufree.com/'
BASE_URL21 = 'http://movies2k.eu/'
BASE_URL22 = 'http://www.cinemadivx.com/'
BASE_URL23 = 'http://300mbmovies4u.com/'
BASE_URL24 = 'http://www.hotnewhiphop.com/'
BASE_URL25 = 'http://www.rapgrid.com/'
BASE_URL26 = 'http://www.2kmusic.com/'

#### PATHS ##########
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

###############################################################################################                 #################################################################

def GetTitles(section, url, startPage= '1', numOfPages= '1'): # Get Movie Titles    #oneclickwatch
        print 'allinone get Movie Titles Menu %s' % url
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
                match = re.compile('<h2.+?href="(.+?)".+?>(.+?)<.+?src="(.+?)"', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')    
                addon.add_directory({'mode': 'GetTitles', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#################################################################################################################################################################################

def GetTitles1(section, url, startPage= '1', numOfPages= '1'): # Get Movie Titles  #WTT
        print 'allinone get Movie Titles Menu %s' % url
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
                match = re.compile('entry-title.+?href="(.+?)".+?>(.+?)<.+?src=.+?', re.DOTALL).findall(html)
                for movieUrl, name in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles1', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')        
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

###############################################################################################################################################################################


def GetTitles2(section, url, startPage= '1', numOfPages= '1'): # Get Movie Titles  #WTShows
        print 'allinone get Movie Titles Menu %s' % url
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
                match = re.compile('entry.+?href="(.+?)" .+?=(.+?)>.+?<.+?src="(.+?)"', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles2', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')        
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

####################################################################################################################################################################

def GetTitles3(section, url, startPage= '1', numOfPages= '1'): # Get Movie Titles    #viooz
        print 'allinone get Movie Titles Menu %s' % url 
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
                match = re.compile('postsbody.+?href="(.+?)".+?="(.+?)">.+?src="(.+?)"', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles3', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view')           
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#################################################################################################################################################################################

def GetTitles4(section, url, startPage= '1', numOfPages= '1'): # Get Movie Titles  #Uv
        print 'allinone get Movie Titles Menu %s' % url
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
                match = re.compile('itemdets.+?href="(.+?)" title="(.+?)".+?.+?src="(.+?)".+?', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles4', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view')       
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

##################################################################################################################################################################################


def GetTitles5(section, url, startPage= '1', numOfPages= '1'): # Get Movie Titles  #moviesall4u
        print 'allinone get Movie Titles Menu %s' % url
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
                match = re.compile('entry-title.+?href="(.+?)".+?>(.+?)<.+?src="(.+?)".+?', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles5', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view')             
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))


####################################################################################################################################################################

def GetTitles6(section, url, startPage= '1', numOfPages= '1'): # Get Movie Titles #ZMOVIES
        print 'allinone get Movie Titles Menu %s' % url
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
                match = re.compile('width: 68px; height: 100px; position: relative;.+?href="(.+?)" title="(.+?)">.+?src=.+?src="(.+?)"', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles6', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view')          
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

###############             ########################               #######################            ##################            ######################        ####################


def GetTitles6a(section, url, startPage= '1', numOfPages= '1'): # Get Movie Titles #z2
        print 'allinone get Movie Titles Menu %s' % url
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
                match = re.compile('width: 68px; height: 100px; position: relative;.+?href="(.+?)" title="(.+?)">.+?src=.+?src="(.+?)"', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view')          
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))


##############################################################################################################################################################

def GetTitles7(section, url, startPage= '1', numOfPages= '1'): # Get Movie Titles #moviekingdom
        print 'allinone get Movie Titles Menu %s' % url
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
                match = re.compile('img-preview spec-border.+?src="(.+?)".+?href="(.+?)".+?>(.+?)<.+?', re.DOTALL).findall(html)
                for img, movieUrl, name in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles7', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view')          
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#####################              ##################              #####################            #####################            ########################

def GetTitles7a(section, url, startPage= '1', numOfPages= '1'): # Get Movie Titles #moviekingdom
        print 'allinone get Movie Titles Menu %s' % url
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
                match = re.compile('img-preview spec-border.+?src="(.+?)".+?href="(.+?)".+?>(.+?)<.+?', re.DOTALL).findall(html)
                for img, movieUrl, name in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view')          
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))


####################################################################################################################################################################################


def GetTitles8(section, url, startPage= '1', numOfPages= '1'): # Get Movie Titles  ##wsus
        print 'allinone get Movie Titles Menu %s' % url
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
                match = re.compile('moviefilm.+?href="(.+?)".+?src="(.+?)".+?=(.+?)height=.+?', re.DOTALL).findall(html)
                for movieUrl, img, name in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles8', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')        
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#############################################################################################################################################################################################

def GetTitles9(section, url, startPage= '1', numOfPages= '1'): # Get Movie Titles  #oneclickmoviez
        print 'allinone get Movie Titles Menu %s' % url
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
                match = re.compile('text-align:center.+?href="(.+?)".+?>.+?<.+?src="(.+?)" .+?=.+? .+?=.+? .+?=.+? .+?=.+? title="(.+?)">', re.DOTALL).findall(html)
                for movieUrl, img, name in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')                        
                addon.add_directory({'mode': 'GetTitles9', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png') 
        setView('tvshows', 'tvshows-view')          
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#############################################################################################################################################################################################

def GetTitles10(section, url, startPage= '1', numOfPages= '1'): # Get Movie Titles #mvl
        print 'allinone get Movie Titles Menu %s' % url
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
                match = re.compile('<img src="(.+?)"  title="(.+?)" class=".+?" alt=".+?" /></a>\r\n\t\t\r\n<h3><a href="(.+?)" rel=".+?"', re.DOTALL).findall(html)
                for img, name, movieUrl in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')      
                addon.add_directory({'mode': 'GetTitles10', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view')         
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))


#################################################################################################################################################################################

def GetTitles11(section, url, startPage= '1', numOfPages= '1'): # Get Movie Titles #ddlvalley
        print 'allinone get Movie Titles Menu %s' % url
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
                        addon.add_directory({'mode': 'GetLinks3', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles11', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')        
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

##################################################################################################################################################################################

def GetTitles12(section, url, startPage= '1', numOfPages= '1'): # Get Movie Titles #omp
        print 'allinone get Movie Titles Menu %s' % url
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
                match = re.compile('<h2 class="title"><a href="(.+?)" rel=.+? title=.+?>(.+?)</a>', re.DOTALL).findall(html)
                for movieUrl, name in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img=IconPath + 'omp.png', fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles12', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')      
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#################            ####################            ##########################            ########################        ##########################       ##########

def GetTitles12a(section, url, startPage= '1', numOfPages= '1'): # Get Movie Titles #omp2
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
                match = re.compile('><h2 class="title" id=.+?><a href="(.+?)" rel=.+? title=.+?>(.+?)</a></h2>', re.DOTALL).findall(html)
                for movieUrl, name in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img=IconPath + 'omp.png', fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles12a', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR darkorchid][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')       
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

################################################################################################################################################################################

def GetTitles13(section, url, startPage= '1', numOfPages= '1'): # Get Movie Titles  #fullepisode.info
        print 'allinone get Movie Titles Menu %s' % url
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
                match = re.compile('<h2.+?href="(.+?)".+?>(.+?)<.+?src="(.+?)"', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles13', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')        
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#############################################################################################################################################################

def GetTitles14(section, url, startPage= '1', numOfPages= '1'): # Get Movie Titles   #channelcut
        print 'allinone get Movie Titles Menu %s' % url
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
                match = re.compile('<h2><a.+?href="(.+?)".+?>(.+?)<.+?', re.DOTALL).findall(html)
                for movieUrl, name in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img=IconPath + 'cc.png', fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles14', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')        
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

######################################################################################################################################################


def GetTitles15(section, url, startPage= '1', numOfPages= '1'): #putseries movies
        print 'allinone get Movie Titles Menu %s' % url

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
                match = re.compile('text-align:center.+?href="(.+?)".+?>.+?<.+?src="(.+?)" .+?=.+? .+?=.+? .+?=.+? .+?=.+? title="(.+?)">', re.DOTALL).findall(html)
                for movieUrl, img, name in match:
                        addon.add_directory({'mode': 'GetLinks1', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png') 
                addon.add_directory({'mode': 'GetTitles15', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')

       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------------------------------------------------------#

def GetTitles15a(section, url, startPage= '1', numOfPages= '1'): #putseries tv shows
        print 'allinone get Movie Titles Menu %s' % url

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
                match = re.compile('<a class="link" href="(.+?)" title="(.+?)">.+?<span', re.DOTALL).findall(html)
                for movieUrl, name in match:
                        addon.add_directory({'mode': 'GetLinks1', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')

       	xbmcplugin.endOfDirectory(int(sys.argv[1]))



def GetTitles15b(section, url, startPage= '1', numOfPages= '1'): #putseries tv menu
        print 'rls-center get Movie Titles Menu %s' % url

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
                match = re.compile('<a class="link" href="(.+?)" title="(.+?)">', re.DOTALL).findall(html)
                for movieUrl, title in match:
                        addon.add_directory({'mode': 'GetTitles15a', 'section': section, 'url': movieUrl, 'startPage': '1', 'numOfPages': '1'}, {'title':  title}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png') 
                addon.add_directory({'mode': 'GetTitles15b', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')  
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

###############################################################################################################################################################################

def GetTitles16(section, url, startPage= '1', numOfPages= '1'): # Get putlocker. Titles
        print 'allinone get Movie Titles Menu %s' % url
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + '/' + startPage
        print pageUrl
        html = net.http_GET(pageUrl).content
        CLEAN(html)
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + '/' + str(page)
                        html = net.http_GET(pageUrl).content
                        CLEAN(html)  
                match = re.compile('<td width=.+? valign=.+? style=.+?><a href="(.+?)" title="(.+?)"><img src="(.+?)" border=.+?', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')
                #addon.add_directory({'mode': 'GetTitles16', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view')       
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#############################################################################################################################################################

def GetTitles17(section, url, startPage= '1', numOfPages= '1'): #Tv-junky
        print 'fight-bb get Movie Titles Menu %s' % url
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
                match = re.compile('posttitle.+?href="(.+?)".+?>(.+?)<.+?', re.DOTALL).findall(html)
                for movieUrl, name in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img=IconPath + 'tvj.png', fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles17', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

################################################################################################################################################################################

def GetTitles18(section, url, startPage= '1', numOfPages= '1'): #2nd list oneclickmoviez tv url 9
        print 'allinone get Movie Titles Menu %s' % url

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
                match = re.compile('item.+?href="(.+?)".+?>.+?<.+?src="(.+?)" title="(.+?)">', re.DOTALL).findall(html)
                for movieUrl, img, name in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img=img, fanart=FanartPath + 'fanart.png')
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))



def GetTitles18a(section, url, startPage= '1', numOfPages= '1'): # 1st list oneclickmoviez tv url 9
        print 'allinone get Movie Titles Menu %s' % url

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
                match = re.compile('text-align:center.+?href="(.+?)".+?>.+?<.+?src=.+? title="(.+?)">', re.DOTALL).findall(html)
                for movieUrl, title in match:
                        addon.add_directory({'mode': 'GetTitles18', 'section': section, 'url': movieUrl, 'startPage': '1', 'numOfPages': '1'}, {'title':  title}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png') 
                addon.add_directory({'mode': 'GetTitles18a', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')  
       	xbmcplugin.endOfDirectory(int(sys.argv[1])) 

###############################################################################################################################################################################

def GetTitles19(section, url, startPage= '1', numOfPages= '1'): #all4u
        print 'allinone get Movie Titles Menu %s' % url

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
                match = re.compile('posttitle.+?href="(.+?)".+?>(.+?)<.+?src=.+?.+?', re.DOTALL).findall(html)
                for movieUrl, name in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img=IconPath + 'a4u.png', fanart=FanartPath + 'fanart.png') 
                addon.add_directory({'mode': 'GetTitles19', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')       
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#################################################################################################################################################################################

def GetTitles20(section, url, startPage= '1', numOfPages= '1'): #world4ufree
        print 'allinone get Movie Titles Menu %s' % url

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
                match = re.compile('<div class="cover"><a href="(.+?)" title="(.+?)"><img src="(.+?)" alt=.+? class=.+? width=.+? height=.+? /></a></div>', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png') 
                addon.add_directory({'mode': 'GetTitles20', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png') 
        setView('tvshows', 'tvshows-view')        
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#################################################################################################################################################################################

def GetTitles21(section, url, startPage= '1', numOfPages= '1'): # Get Movie Titles
        print 'myZmovies get Movie Titles Menu %s' % url

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
                match = re.compile('<h2.+?href="(.+?)".+?>(.+?)<.+?src="(.+?)".+?', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png') 
                addon.add_directory({'mode': 'GetTitles21', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png') 
        setView('tvshows', 'tvshows-view')  
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#########################################################################################################################################################################################

def GetTitles22(section, url, startPage= '1', numOfPages= '1'): # Get Movie Titles
        print 'allinone get Movie Titles Menu %s' % url

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
                match = re.compile('class="entry-thumbnails-link" href="(.+?)"><img src="(.+?)" alt=.+? title="(.+?)"', re.DOTALL).findall(html)
                for movieUrl, img, name in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png') 
                addon.add_directory({'mode': 'GetTitles22', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view')  
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#################################################################################################################################################################################

def GetTitles23(section, url, startPage= '1', numOfPages= '1'): # 300mbmovies4u
        print 'allinone get Movie Titles Menu %s' % url
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
                match = re.compile('cover.+?href="(.+?)".+?.+?<img src="(.+?)".+?alt="(.+?)"', re.DOTALL).findall(html)
                for movieUrl, img, name in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles23', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view') 
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))


#############################################################################################################################################################################

def GetTitles24(section, url, startPage= '1', numOfPages= '1'): # hiphop
        print 'allinone get Movie Titles Menu %s' % url
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
                match = re.compile('http://schema.org/VideoObject.+?href="(.+?)".+?>.+?<.+?src="(.+?)" alt="(.+?)"', re.DOTALL).findall(html)
                for movieUrl, img, name in match:
                        addon.add_directory({'mode': 'GetLinks4', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')
        
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#############################################################################################################################################################################

def GetTitles25(section, url, startPage= '1', numOfPages= '1'): # Get Movie Titles
        print 'allinone get Movie Titles Menu %s' % url
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
                match = re.compile('<div class="battleTeaserPhoto"><a href="(.+?)" title="(.+?)"><img src="(.+?)" width="150" height="113"/></a></div>', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        addon.add_directory({'mode': 'GetLinks5', 'section': section, 'url': 'http://www.rapgrid.com/' + movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

###############################################################################################################################################################################

def GetTitles26(section, url, startPage= '1', numOfPages= '1'): # Get Movie Titles
        print 'allinone get Movie Titles Menu %s' % url
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
                match = re.compile('http://schema.org/VideoObject"><a title="(.+?)" href="(.+?)" itemprop=.+?><span class=.+?><img src="(.+?)" ', re.DOTALL).findall(html)
                for name, movieUrl, img in match:
                        addon.add_directory({'mode': 'GetLinks6', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')
        
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

###############################################################################links#############################################################################################


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
        if r:
                content = content[:r.start()]
        match = re.compile('href="(.+?)"').findall(content)
        listitem = GetMediaInfo(content)
        for url in match:
                host = GetDomain(url)
                if 'Unknown' in host:
                        continue
                print '*****************************' + host + ' : ' + url
                title = url.rpartition('/')
                title = title[2].replace('.html', '')
                host = host.replace('youtube.com','[COLOR lime]Movie Trailer[/COLOR]')
                name = host
                hosted_media = urlresolver.HostedMediaFile(url=url, title=name)
                sources.append(hosted_media)
                print len(match)
                for url in match:
                        host = GetDomain(url)
                        if 'Unknown' in host:
                                continue
        source = urlresolver.choose_source(sources)
        if source: stream_url = source.resolve()
        else: stream_url = ''
        xbmc.Player().play(stream_url)

#---------------------------------------------------------------------------------#

def GetLinks1(section, url): # Get Links #putseries
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
        if r:
                content = content[:r.start()]
        match = re.compile('src="(.+?)"').findall(content)
        listitem = GetMediaInfo(content)
        for url in match:
                host = GetDomain(url)
                if 'Unknown' in host:
                        continue
                print '*****************************' + host + ' : ' + url
                title = url.rpartition('/')
                title = title[2].replace('.html', '')
                host = host.replace('embed.','')
                name = host
                hosted_media = urlresolver.HostedMediaFile(url=url, title=name)
                sources.append(hosted_media)
                print len(match)
                for url in match:
                        host = GetDomain(url)
                        if 'Unknown' in host:
                                continue
        source = urlresolver.choose_source(sources)
        if source: stream_url = source.resolve()
        else: stream_url = ''
        xbmc.Player().play(stream_url)

#-------------------------------------------------------------------------------#

def GetLinks3(section, url): # Get Links
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(str(url)).content
        CLEAN(html)
        sources = []
        listitem = GetMediaInfo(html)
        print 'LISTITEM: '+str(listitem)
        content = html
        print'CONTENT: '+str(listitem)
        r = re.search('<strong>Links.*</strong>', html)
                
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
                print '*****************************' + host + ' : ' + url
                title = url.rpartition('/')
                title = title[2].replace('.html', '')
                title = title.replace('.htm', '')
                title = title.replace('www.', '')
                title = title.replace ('-',' ')
                title = title.replace('_',' ')
                title = title.replace('.',' ')
                title = title.replace('.',' ')
                name = host+'-'+title
                hosted_media = urlresolver.HostedMediaFile(url=url, title=name)
                sources.append(hosted_media)

                
        find = re.search('commentblock', html)
        if find:
                print 'in comments if'
                html = html[find.end():]
                CLEAN(html)###
                match1 = re.compile(r'comment-page-numbers(.+?)<!--comments form -->', re.DOTALL).findall(html)
                match = re.compile('<a href="(htt.+?)" rel="nofollow"', re.DOTALL).findall(str(match1))
                print 'MATCH IS: '+str(match)
                print len(match)
                for url in match:
                        host = GetDomain(url)
                        if 'Unknown' in host:
                                continue
                        # ignore .srt files
                        r = re.search('\.srt[(?:\.html|\.htm)]*$', url, re.IGNORECASE)
                        if r:

                                continue

                        # ignore .rar files
                        r = re.search('\.rar[(?:\.html|\.htm)]*', url, re.IGNORECASE)
                        if r:
                                continue

        source = urlresolver.choose_source(sources)
        if source: stream_url = source.resolve()
        else: stream_url = ''
        xbmc.Player().play(stream_url)

#----------------------------------------------------------------------#

def GetLinks4(section, url): # Get Links
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

        match = re.compile('content="(.+?)"').findall(content)
        listitem = GetMediaInfo(content)
        for url in match:
                host = GetDomain(url)

                if 'Unknown' in host:
                        continue

                print '*****************************' + host
                title = url.rpartition('/')
                name = host
                hosted_media = urlresolver.HostedMediaFile(url=url, title=name)
                sources.append(hosted_media)


        source = urlresolver.choose_source(sources)
        if source: stream_url = source.resolve()
        else: stream_url = ''
        xbmc.Player().play(stream_url)

#-----------------------------------------------------------------------#

def GetLinks5(section, url): # Get Links
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

        match = re.compile("file: '(.+?)'").findall(content)
        listitem = GetMediaInfo(content)
        for url in match:
                host = GetDomain(url)
                if 'Unknown' in host:
                        continue
                print '*****************************' + host + ' : ' + url
                title = url.rpartition('/')
                title = title[2].replace('.html', '')
                host = host.replace('embed.','')
                name = host
                hosted_media = urlresolver.HostedMediaFile(url=url, title=name)
                sources.append(hosted_media)
                print len(match)
                for url in match:
                        host = GetDomain(url)
                        if 'Unknown' in host:
                                continue
        source = urlresolver.choose_source(sources)
        if source: stream_url = source.resolve()
        else: stream_url = ''
        xbmc.Player().play(stream_url)

#------------------------------------------------------------------------------#

def GetLinks6(section, url): # Get Links
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
        if r:
                content = content[:r.start()]
        match = re.compile('content="(.+?)"').findall(content)
        listitem = GetMediaInfo(content)
        for url in match:
                host = GetDomain(url)
                if 'Unknown' in host:
                        continue
                print '*****************************' + host + ' : ' + url
                title = url.rpartition('/')
                title = title[2].replace('.html', '')
                title = title.replace('.htm', '')
                title = title.replace('www.', '')
                title = title.replace ('-','')
                title = title.replace('_',' ')
                title = title.replace('x1ct',' ')
                title = title.replace('?',' ')
                title = title.replace('=','')
                title = title.replace('1','')
                title = title.replace('autoplay','[COLOR blue]this link to play video     [/COLOR]')
                name = host+'-'+title
                hosted_media = urlresolver.HostedMediaFile(url=url, title=name)
                sources.append(hosted_media)
                print len(match)
                for url in match:
                        host = GetDomain(url)
                        if 'Unknown' in host:
                                continue
        source = urlresolver.choose_source(sources)
        if source: stream_url = source.resolve()
        else: stream_url = ''
        xbmc.Player().play(stream_url)
 

#####################################################################################           ##################################################################################


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


######################################################################menu####################################################################################################



def MainMenu():    #homescreen
        addon.add_directory({'mode': 'MovieMenu'}, {'title':  '[COLOR cornflowerblue][B]Movies >[/B][/COLOR] >'}, img=IconPath + 'films.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'TvMenu'}, {'title':  '[COLOR darkorange][B]Tv Shows >[/B][/COLOR] >'}, img=IconPath + 'tv2.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'SportMenu'}, {'title':  '[COLOR lemonchiffon][B]Sport >[/B][/COLOR] >'}, img=IconPath + 'sport1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'MusicMenu'}, {'title':  '[COLOR cadetblue][B]Music >[/B][/COLOR] >'}, img=IconPath + 'music.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'SearchMenu'}, {'title':  '[COLOR green][B]Searches [/B] [/COLOR]'}, img=IconPath + 'searches.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'ResolverSettings'}, {'title':  '[COLOR red]Resolver Settings[/COLOR]'}, img=IconPath + 'resolver.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'Help'}, {'title':  '[COLOR pink]FOR HELP PLEASE GOTO...[/COLOR] [COLOR gold][B][I]www.xbmchub.com[/B][/I][/COLOR]'}, img=IconPath + 'helphub.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'help'}, {'title':  '[COLOR aqua][B]FOLLOW ME ON TWITTER [/B][/COLOR] [COLOR gold][B][I]@TheYid009 [/B][/I][/COLOR] '}, img=IconPath + 'twit.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def MusicMenu():   #Music
        addon.add_directory({'mode': 'GetTitles24', 'section': 'ALL', 'url': BASE_URL24 + '/videos/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cadetblue][B]Latest Rap videos[/B][/COLOR] [COLOR crimson](HotNewHipHop) [/COLOR]>>'}, img=IconPath + 'hiphop.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles25', 'section': 'ALL', 'url': BASE_URL25 + '/battles',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cadetblue][B]Rap Battle videos[/B][/COLOR] [COLOR springgreen](Rap Grid) [/COLOR]>>'}, img=IconPath + 'rg.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles26', 'section': 'ALL', 'url': BASE_URL26 + '/en/music/videos',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cadetblue][B]Latest Music videos[/B][/COLOR] [COLOR red](2kmusic) [/COLOR]>>'}, img=IconPath + '2km.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def SportMenu():   #sport
        #addon.add_directory({'mode': 'GetTitles12a', 'section': 'ALL', 'url': BASE_URL12 + '/category/boxing/',
                             #'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lemonchiffon][B]Latest Sports[/B][/COLOR] [COLOR darkorchid](OMP) [/COLOR]>>'}, img=IconPath + 'omp.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles14', 'section': 'ALL', 'url': BASE_URL14 + '/category/ufc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lemonchiffon][B]Latest UFC list[/B][/COLOR] [COLOR tomato](ChannelCut) [/COLOR]>>'}, img=IconPath + 'cc.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles14', 'section': 'ALL', 'url': BASE_URL14 + '/category/wwe',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lemonchiffon][B]Latest WWE list[/B][/COLOR] [COLOR tomato](ChannelCut) [/COLOR]>>'}, img=IconPath + 'cc.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles14', 'section': 'ALL', 'url': BASE_URL14 + '/category/impact-wrestling',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lemonchiffon][B]Latest TNA list[/B][/COLOR] [COLOR tomato](ChannelCut) [/COLOR]>>'}, img=IconPath + 'cc.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))


def MovieMenu():   #movies 
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Latest Movies[/B][/COLOR] [COLOR blue](OCW) [/COLOR]>>'}, img=IconPath + 'ocw.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL1 + '/category/movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Latest Movies[/B][/COLOR] [COLOR salmon](WTT) [/COLOR]>>'}, img=IconPath + 'wtt.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles10', 'section': 'ALL', 'url': BASE_URL10 + '/category/movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Latest Movies[/B][/COLOR] [COLOR khaki](MyVideoLinks) [/COLOR]>>'}, img=IconPath + 'mvl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles16', 'section': 'ALL', 'url': BASE_URL16 + '/featured/1',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR steelblue][B]Featured Movies[/B][/COLOR] [COLOR moccasin](Putlocker.bz) [/COLOR]>>'}, img=IconPath + 'pl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'OcmMenu'}, {'title':  '[COLOR deepskyblue][B]Movie Genre[/B][/COLOR] [COLOR peru](OneClickMoviez) [/COLOR]>>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'PutMenu'}, {'title':  '[COLOR deepskyblue][B]Movie Genre[/B][/COLOR] [COLOR teal](Putlocker Series) [/COLOR]>>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'OmpMenu'}, {'title':  '[COLOR deepskyblue][B]Movie Genre[/B][/COLOR] [COLOR darkorchid](OMP) [/COLOR]>>'}, img=IconPath + 'omp.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'MovMenu'}, {'title':  '[COLOR deepskyblue][B]Movie Genre[/B][/COLOR] [COLOR lightslategray](ViooZ) [/COLOR]>>'}, img=IconPath + 'vu1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'UvMenu'}, {'title':  '[COLOR deepskyblue][B]Movie Genre[/B][/COLOR] [COLOR floralwhite](Ultra-Vid) [/COLOR]>>'}, img=IconPath + 'uv1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'MkMenu'}, {'title':  '[COLOR deepskyblue][B]Movie Genre[/B][/COLOR] [COLOR gold](Movie-Kingdom) [/COLOR]>>'}, img=IconPath + 'mk.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'ZmMenu'}, {'title':  '[COLOR deepskyblue][B]Movie Genre[/B][/COLOR] [COLOR plum](Zmovies) [/COLOR]>>'}, img=IconPath + 'ze1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'WtMenu'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR lightsteelblue][B]International Movies Zone[/B][/COLOR] >>'}, img=IconPath + 'iz.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'RgMenu'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR mediumturquoise][B]Full HD Zone[/B][/COLOR] >>'}, img=IconPath + 'fhz.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def RgMenu():   #yify  #mvl rg #HD zone
        addon.add_directory({'mode': 'GetTitles20', 'section': 'ALL', 'url': BASE_URL20 + '/category/trailers/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Trailers [/B][/COLOR] [COLOR darkorchid](World4UFree) [/COLOR]>>'}, img=IconPath + 'w4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles23', 'section': 'ALL', 'url': BASE_URL23 + '/category/hollywood-movie/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Hollywood[/B][/COLOR] [COLOR crimson](300mb movies4u) [/COLOR] >>'}, img=IconPath + 'm4u1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles23', 'section': 'ALL', 'url': BASE_URL23 + '/category/hollywood-movie/english-yify-movie/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Movies by Yify[/B][/COLOR] [COLOR crimson](300mb movies4u) [/COLOR] >>'}, img=IconPath + 'm4u1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles20', 'section': 'ALL', 'url': BASE_URL20 + '/category/hollywood/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Hollywood [/B][/COLOR][COLOR darkorchid](World4UFree) [/COLOR]>>'}, img=IconPath + 'w4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles5', 'section': 'ALL', 'url': BASE_URL5 + '/category/english-movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Hollywood [/B][/COLOR] [COLOR fuchsia](Moviesall4u) [/COLOR]>>'}, img=IconPath + 'm4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles10', 'section': 'ALL', 'url': BASE_URL10 + '/category/movies/yify/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Movies by Yify[/B][/COLOR] [COLOR khaki](MyVideoLinks) [/COLOR]>>'}, img=IconPath + 'mvl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles10', 'section': 'ALL', 'url': BASE_URL10 + '/category/movies/ganool/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Movies by Ganool[/B][/COLOR] [COLOR khaki](MyVideoLinks) [/COLOR]>>'}, img=IconPath + 'mvl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles10', 'section': 'ALL', 'url': BASE_URL10 + '/category/movies/msd/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Movies by Msd[/B][/COLOR] [COLOR khaki](MyVideoLinks) [/COLOR]>>'}, img=IconPath + 'mvl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles10', 'section': 'ALL', 'url': BASE_URL10 + '/category/movies/anoxmous/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Movies by Anoxmous[/B][/COLOR] [COLOR khaki](MyVideoLinks) [/COLOR]>>'}, img=IconPath + 'mvl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles10', 'section': 'ALL', 'url': BASE_URL10 + '/category/movies/judas/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Movies by Judas[/B][/COLOR] [COLOR khaki](MyVideoLinks) [/COLOR]>>'}, img=IconPath + 'mvl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles11', 'section': 'ALL', 'url': BASE_URL11 + '/category/movies/yify-rips/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Movies by Yify[/B][/COLOR] [COLOR mediumblue](DDLvalley) [/COLOR]>>'}, img=IconPath + 'ddl1.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def WtMenu():   #Moviesall4u  #all4youz #world4ufree #cinemadivx
        addon.add_directory({'mode': 'CineMenu'}, {'title':  '[COLOR cornflowerblue][B](Spanish) Movie Genre[/B][/COLOR] [COLOR orangered](Cinemadivx) [/COLOR]>>'}, img=IconPath + 'cin.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles20', 'section': 'ALL', 'url': BASE_URL20 + '/category/trailers/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Trailers [/B][/COLOR] [COLOR darkorchid](World4UFree) [/COLOR]>>'}, img=IconPath + 'w4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles23', 'section': 'ALL', 'url': BASE_URL23 + '/category/hollywood-movie/english-movie-dual-audio/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Dual Audio[/B][/COLOR] [COLOR crimson](300mb movies4u) [/COLOR] >>'}, img=IconPath + 'm4u1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles23', 'section': 'ALL', 'url': BASE_URL23 + '/category/tamil-movie/tamil-hindi-dubbed-movie/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Tamil hindi Dubbed[/B][/COLOR] [COLOR crimson](300mb movies4u) [/COLOR] >>'}, img=IconPath + 'm4u1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles23', 'section': 'ALL', 'url': BASE_URL23 + '/category/bollywood-movie/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Bollywood[/B][/COLOR] [COLOR crimson](300mb movies4u) [/COLOR] >>'}, img=IconPath + 'm4u1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles23', 'section': 'ALL', 'url': BASE_URL23 + '/category/tamil-movie/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Tamil[/B][/COLOR] [COLOR crimson](300mb movies4u) [/COLOR] >>'}, img=IconPath + 'm4u1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles19', 'section': 'ALL', 'url': BASE_URL19 + '/category/hollywood/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Hollywood [/B][/COLOR] [COLOR bisque](All4Youz) [/COLOR]>>'}, img=IconPath + 'a4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles20', 'section': 'ALL', 'url': BASE_URL20 + '/category/bollywood/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Bollywood [/B][/COLOR] [COLOR darkorchid](World4UFree) [/COLOR]>>'}, img=IconPath + 'w4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles20', 'section': 'ALL', 'url': BASE_URL20 + '/category/hindi-dubbed-movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Hindi Dubbed [/B][/COLOR] [COLOR darkorchid](World4UFree) [/COLOR]>>'}, img=IconPath + 'w4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles20', 'section': 'ALL', 'url': BASE_URL20 + '/category/songs/indian-videos/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Indian Music Videos [/B][/COLOR] [COLOR darkorchid](World4UFree) [/COLOR]>>'}, img=IconPath + 'w4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles5', 'section': 'ALL', 'url': BASE_URL5 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Latest Added [/B][/COLOR] [COLOR fuchsia](Moviesall4u) [/COLOR]>>'}, img=IconPath + 'm4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles5', 'section': 'ALL', 'url': BASE_URL5 + '/category/hindi-movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Hindi [/B][/COLOR] [COLOR fuchsia](Moviesall4u) [/COLOR]>>'}, img=IconPath + 'm4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles5', 'section': 'ALL', 'url': BASE_URL5 + '/category/indian-bangla-movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Indian & Bangla Movies [/B][/COLOR] [COLOR fuchsia](Moviesall4u) [/COLOR]>>'}, img=IconPath + 'm4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles5', 'section': 'ALL', 'url': BASE_URL5 + '/category/dual-audio-movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Dual Audio [/B][/COLOR] [COLOR fuchsia](Moviesall4u) [/COLOR]>>'}, img=IconPath + 'm4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles19', 'section': 'ALL', 'url': BASE_URL19 + '/category/box-office-hit/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Box Office [/B][/COLOR] [COLOR bisque](All4Youz) [/COLOR]>>'}, img=IconPath + 'a4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles19', 'section': 'ALL', 'url': BASE_URL19 + '/category/bollywood/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Bollywood [/B][/COLOR] [COLOR bisque](All4Youz) [/COLOR]>>'}, img=IconPath + 'a4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles19', 'section': 'ALL', 'url': BASE_URL19 + '/category/hiindi-dubbed/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Hindi Dubbed [/B][/COLOR] [COLOR bisque](All4Youz) [/COLOR]>>'}, img=IconPath + 'a4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles19', 'section': 'ALL', 'url': BASE_URL19 + '/category/dual-audio/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Dual Audio [/B][/COLOR] [COLOR bisque](All4Youz) [/COLOR]>>'}, img=IconPath + 'a4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles21', 'section': 'ALL', 'url': BASE_URL21 + '/category/hollywood-movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cornflowerblue][B]Hollywood [/B][/COLOR] [COLOR lawngreen](movies2k.eu) [/COLOR]>>'}, img=IconPath + '2k.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles21', 'section': 'ALL', 'url': BASE_URL21 + '/category/hindi-movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cornflowerblue][B]Hindi [/B][/COLOR] [COLOR lawngreen](movies2k.eu) [/COLOR]>>'}, img=IconPath + '2k.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles21', 'section': 'ALL', 'url': BASE_URL21 + '/category/hindi-dubbed/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cornflowerblue][B]Hindi Dubbed [/B][/COLOR] [COLOR lawngreen](movies2k.eu) [/COLOR]>>'}, img=IconPath + '2k.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles21', 'section': 'ALL', 'url': BASE_URL21 + '/category/malayalam-movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cornflowerblue][B]Malayalam [/B][/COLOR] [COLOR lawngreen](movies2k.eu) [/COLOR]>>'}, img=IconPath + '2k.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles21', 'section': 'ALL', 'url': BASE_URL21 + '/category/tamil-movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cornflowerblue][B]Tamil [/B][/COLOR] [COLOR lawngreen](movies2k.eu) [/COLOR]>>'}, img=IconPath + '2k.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles21', 'section': 'ALL', 'url': BASE_URL21 + '/category/telugu-movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cornflowerblue][B]Telugu [/B][/COLOR] [COLOR lawngreen](movies2k.eu) [/COLOR]>>'}, img=IconPath + '2k.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def CineMenu():  #cinemadivx
        addon.add_directory({'mode': 'GetTitles22', 'section': 'ALL', 'url': BASE_URL22 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR orangered]Pagina principal[/COLOR] >>'}, img=IconPath + 'cin.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles22', 'section': 'ALL', 'url': BASE_URL22 + '/category/estrenos/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR orangered]Estrenos[/COLOR] >>'}, img=IconPath + 'cin.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles22', 'section': 'ALL', 'url': BASE_URL22 + '/category/clasicas/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR orangered]Clasicas[/COLOR] >>'}, img=IconPath + 'cin.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles22', 'section': 'ALL', 'url': BASE_URL22 + '/category/accion/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR orangered]Accion[/COLOR] >>'}, img=IconPath + 'cin.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles22', 'section': 'ALL', 'url': BASE_URL22 + '/category/cine/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR orangered]Cine[/COLOR] >>'}, img=IconPath + 'cin.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles22', 'section': 'ALL', 'url': BASE_URL22 + '/category/latino/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR orangered]Latino[/COLOR] >>'}, img=IconPath + 'cin.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles22', 'section': 'ALL', 'url': BASE_URL22 + '/category/musical/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR orangered]Musical[/COLOR] >>'}, img=IconPath + 'cin.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles22', 'section': 'ALL', 'url': BASE_URL22 + '/category/animacion/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR orangered]Animacion[/COLOR] >>'}, img=IconPath + 'cin.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles22', 'section': 'ALL', 'url': BASE_URL22 + '/category/aventura/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR orangered]Aventura[/COLOR] >>'}, img=IconPath + 'cin.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles22', 'section': 'ALL', 'url': BASE_URL22 + '/category/ciencia-ficcion/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR orangered]Ciencia Ficcion[/COLOR] >>'}, img=IconPath + 'cin.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles22', 'section': 'ALL', 'url': BASE_URL22 + '/category/thriller/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR orangered]Thriller[/COLOR] >>'}, img=IconPath + 'cin.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles22', 'section': 'ALL', 'url': BASE_URL22 + '/category/terror/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR orangered]Terror[/COLOR] >>'}, img=IconPath + 'cin.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles22', 'section': 'ALL', 'url': BASE_URL22 + '/category/subtitulos/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR orangered]Subtitulos[/COLOR] >>'}, img=IconPath + 'cin.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles22', 'section': 'ALL', 'url': BASE_URL22 + '/category/comedia/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR orangered]Comedia[/COLOR] >>'}, img=IconPath + 'cin.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles22', 'section': 'ALL', 'url': BASE_URL22 + '/category/espanol/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR orangered]Espanol[/COLOR] >>'}, img=IconPath + 'cin.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles22', 'section': 'ALL', 'url': BASE_URL22 + '/category/drama/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR orangered]Drama[/COLOR] >>'}, img=IconPath + 'cin.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles22', 'section': 'ALL', 'url': BASE_URL22 + '/category/fantastico/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR orangered]Fantastico[/COLOR] >>'}, img=IconPath + 'cin.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles22', 'section': 'ALL', 'url': BASE_URL22 + '/category/romance/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR orangered]Romance[/COLOR] >>'}, img=IconPath + 'cin.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles22', 'section': 'ALL', 'url': BASE_URL22 + '/category/sin-categoria/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR orangered]Sin Categoria[/COLOR] >>'}, img=IconPath + 'cin.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))




def MovMenu():   #moviesviooz
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cornflowerblue][B]Latest Movies[/B][/COLOR] [COLOR lightslategray](ViooZ) [/COLOR]>>'}, img=IconPath + 'vu1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/category/hd-movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'HD Movies >>'}, img=IconPath + 'vu1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/category/hollywood/action',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Action >>'}, img=IconPath + 'vu1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/category/hollywood/adventure',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Adventure >>'}, img=IconPath + 'vu1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/category/hollywood/animation',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Animation >>'}, img=IconPath + 'vu1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/category/hollywood/comedy',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Comedy >>'}, img=IconPath + 'vu1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/category/hollywood/crime',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Crime >>'}, img=IconPath + 'vu1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/category/hollywood/drama',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Drama >>'}, img=IconPath + 'vu1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/category/hollywood/fantasy',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Fantasy >>'}, img=IconPath + 'vu1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/category/hollywood/horror',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Horror >>'}, img=IconPath + 'vu1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/category/hollywood/romance',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Romance >>'}, img=IconPath + 'vu1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/category/hollywood/sci-Fi',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sci Fi >>'}, img=IconPath + 'vu1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/category/hollywood/sport',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sport >>'}, img=IconPath + 'vu1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/category/hollywood/thriller',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Thriller >>'}, img=IconPath + 'vu1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/category/hollywood/western',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Western >>'}, img=IconPath + 'vu1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/category/hollywood/war',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'War >>'}, img=IconPath + 'vu1.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))


def UvMenu():   #moviesUv
        addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL4 + '/category/movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cornflowerblue][B]Latest Movies[/B][/COLOR] [COLOR floralwhite](Ultra-Vid) [/COLOR]>>'}, img=IconPath + 'uv1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL4 + '/category/hd',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'HD Movies >>'}, img=IconPath + 'uv1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL4 + '/category/movies/action',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Action >>'}, img=IconPath + 'uv1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL4 + '/category/adventure',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Adventure>>'}, img=IconPath + 'uv1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL4 + '/category/movies/animation',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Animation >>'}, img=IconPath + 'uv1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL4 + '/category/movies/comedy',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Comedy >>'}, img=IconPath + 'uv1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL4 + '/category/movies/crime',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Crime >>'}, img=IconPath + 'uv1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL4 + '/category/movies/documentary',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Documentary >>'}, img=IconPath + 'uv1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL4 + '/category/movies/fantasy',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Fantasy >>'}, img=IconPath + 'uv1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL4 + '/category/movies/horror',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Horror >>'}, img=IconPath + 'uv1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL4 + '/category/movies/drama',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Mystery drama >>'}, img=IconPath + 'uv1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL4 + '/category/movies/romance-movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Romance >>'}, img=IconPath + 'uv1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL4 + '/category/movies/comedy/romantic-comedy',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Romantic comedy>>'}, img=IconPath + 'uv1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL4 + '/category/movies/sci-fi',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sci-fi >>'}, img=IconPath + 'uv1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL4 + '/category/movies/thriller',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Thriller >>'}, img=IconPath + 'uv1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL4 + '/category/movies/family/holiday',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Family >>'}, img=IconPath + 'uv1.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))


def ZmMenu():
        addon.add_directory({'mode': 'GetTitles6a', 'section': 'ALL', 'url': BASE_URL6 + '/movies/new',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cornflowerblue][B]Latest Movies[/B][/COLOR] [COLOR plum](Zmovies) [/COLOR]>>'}, img=IconPath + 'ze1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles6', 'section': 'ALL', 'url': BASE_URL6 + '/search/genre/action',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Action >>'}, img=IconPath + 'ze1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles6', 'section': 'ALL', 'url': BASE_URL6 + '/search/genre/adventure',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Adventure >>'}, img=IconPath + 'ze1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles6', 'section': 'ALL', 'url': BASE_URL6 + '/search/genre/animation',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Animation >>'}, img=IconPath + 'ze1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles6', 'section': 'ALL', 'url': BASE_URL6 + '/search/genre/Comedy',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Comedy >>'}, img=IconPath + 'ze1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles6', 'section': 'ALL', 'url': BASE_URL6 + '/search/genre/crime',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Crime >>'}, img=IconPath + 'ze1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles6', 'section': 'ALL', 'url': BASE_URL6 + '/search/genre/documentary',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Documentary >>'}, img=IconPath + 'ze1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles6', 'section': 'ALL', 'url': BASE_URL6 + '/search/genre/drama',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Drama >>'}, img=IconPath + 'ze1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles6', 'section': 'ALL', 'url': BASE_URL6 + '/search/genre/fantasy',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Fantasy >>'}, img=IconPath + 'ze1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles6', 'section': 'ALL', 'url': BASE_URL6 + '/search/genre/horror',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Horror >>'}, img=IconPath + 'ze1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles6', 'section': 'ALL', 'url': BASE_URL6 + '/search/genre/romance',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Romance >>'}, img=IconPath + 'ze1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles6', 'section': 'ALL', 'url': BASE_URL6 + '/search/genre/sci-Fi',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sci Fi >>'}, img=IconPath + 'ze1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles6', 'section': 'ALL', 'url': BASE_URL6 + '/search/genre/thriller',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Thriller >>'}, img=IconPath + 'ze1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles6', 'section': 'ALL', 'url': BASE_URL6 + '/search/genre/sport',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sport >>'}, img=IconPath + 'ze1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles6', 'section': 'ALL', 'url': BASE_URL6 + '/search/genre/western',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Western >>'}, img=IconPath + 'ze1.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))



def MkMenu():
        addon.add_directory({'mode': 'GetTitles7a', 'section': 'ALL', 'url': BASE_URL7 + '/new-movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cornflowerblue][B]Latest Movies[/B][/COLOR] [COLOR gold](Movie-Kingdom) [/COLOR]>>'}, img=IconPath + 'mk.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles7', 'section': 'ALL', 'url': BASE_URL7 + '/movie-tags/action',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Action >>'}, img=IconPath + 'mk.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles7', 'section': 'ALL', 'url': BASE_URL7 + '/movie-tags/adventure',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Adventure >>'}, img=IconPath + 'mk.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles7', 'section': 'ALL', 'url': BASE_URL7 + '/movie-tags/animation',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Animation >>'}, img=IconPath + 'mk.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles7', 'section': 'ALL', 'url': BASE_URL7 + '/movie-tags/biography',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Biography >>'}, img=IconPath + 'mk.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles7', 'section': 'ALL', 'url': BASE_URL7 + '/movie-tags/comedy',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Comedy >>'}, img=IconPath + 'mk.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles7', 'section': 'ALL', 'url': BASE_URL7 + '/movie-tags/crime',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Crime >>'}, img=IconPath + 'mk.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles7', 'section': 'ALL', 'url': BASE_URL7 + '/movie-tags/documentary',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Documentary >>'}, img=IconPath + 'mk.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles7', 'section': 'ALL', 'url': BASE_URL7 + '/movie-tags/drama',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Drama >>'}, img=IconPath + 'mk.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles7', 'section': 'ALL', 'url': BASE_URL7 + '/movie-tags/family',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Family >>'}, img=IconPath + 'mk.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles7', 'section': 'ALL', 'url': BASE_URL7 + '/movie-tags/fantasy',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Fantasy >>'}, img=IconPath + 'mk.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles7', 'section': 'ALL', 'url': BASE_URL7 + '/movie-tags/history',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'History >>'}, img=IconPath + 'mk.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles7', 'section': 'ALL', 'url': BASE_URL7 + '/movie-tags/horror',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Horror >>'}, img=IconPath + 'mk.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles7', 'section': 'ALL', 'url': BASE_URL7 + '/movie-tags/music',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Music >>'}, img=IconPath + 'mk.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles7', 'section': 'ALL', 'url': BASE_URL7 + '/movie-tags/musical',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'musical >>'}, img=IconPath + 'mk.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles7', 'section': 'ALL', 'url': BASE_URL7 + '/movie-tags/mystery',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Mystery >>'}, img=IconPath + 'mk.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles7', 'section': 'ALL', 'url': BASE_URL7 + '/movie-tags/romance',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Romance >>'}, img=IconPath + 'mk.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles7', 'section': 'ALL', 'url': BASE_URL7 + '/movie-tags/sci-fi',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sci-fi >>'}, img=IconPath + 'mk.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles7', 'section': 'ALL', 'url': BASE_URL7 + '/movie-tags/short',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Short >>'}, img=IconPath + 'mk.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#-------------------------------------------------------------omp-----------------------------------------------------------------------------------------------------#

def OmpMenu():
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorchid]LATEST ADDED [/COLOR]>>'}, img=IconPath + 'omp.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'OmpazMenu'}, {'title':  '[COLOR darkorchid]A-Z [/COLOR]>>'}, img=IconPath + 'omp.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12a', 'section': 'ALL', 'url': BASE_URL12 + '/tag/action',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Action >>'}, img=IconPath + 'omp.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12a', 'section': 'ALL', 'url': BASE_URL12 + '/tag/adventure',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Adventure >>'}, img=IconPath + 'omp.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12a', 'section': 'ALL', 'url': BASE_URL12 + '/tag/animation',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Animation >>'}, img=IconPath + 'omp.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12a', 'section': 'ALL', 'url': BASE_URL12 + '/tag/comedy',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Comedy >>'}, img=IconPath + 'omp.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12a', 'section': 'ALL', 'url': BASE_URL12 + '/tag/crime',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Crime >>'}, img=IconPath + 'omp.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12a', 'section': 'ALL', 'url': BASE_URL12 + '/tag/drama',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Drama >>'}, img=IconPath + 'omp.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12a', 'section': 'ALL', 'url': BASE_URL12 + '/tag/fantasy',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Fantasy >>'}, img=IconPath + 'omp.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12a', 'section': 'ALL', 'url': BASE_URL12 + '/tag/horror',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Horror >>'}, img=IconPath + 'omp.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12a', 'section': 'ALL', 'url': BASE_URL12 + '/tag/romance',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Romance >>'}, img=IconPath + 'omp.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12a', 'section': 'ALL', 'url': BASE_URL12 + '/tag/sci-Fi',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sci Fi >>'}, img=IconPath + 'omp.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12a', 'section': 'ALL', 'url': BASE_URL12 + '/tag/thriller',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Thriller >>'}, img=IconPath + 'omp.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12a', 'section': 'ALL', 'url': BASE_URL12 + '/tag/western',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Western >>'}, img=IconPath + 'omp.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def OmpazMenu():
        addon.add_directory({'mode': 'GetTitles12a', 'section': 'ALL', 'url': BASE_URL12 + '/tag/a',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'A >>'}, img=IconPath + 'omp.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12a', 'section': 'ALL', 'url': BASE_URL12 + '/tag/b',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'B >>'}, img=IconPath + 'omp.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12a', 'section': 'ALL', 'url': BASE_URL12 + '/tag/c',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'C >>'}, img=IconPath + 'omp.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12a', 'section': 'ALL', 'url': BASE_URL12 + '/tag/d',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'D >>'}, img=IconPath + 'omp.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12a', 'section': 'ALL', 'url': BASE_URL12 + '/tag/e',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'E >>'}, img=IconPath + 'omp.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12a', 'section': 'ALL', 'url': BASE_URL12 + '/tag/f',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'F >>'}, img=IconPath + 'omp.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12a', 'section': 'ALL', 'url': BASE_URL12 + '/tag/g',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'G >>'}, img=IconPath + 'omp.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12a', 'section': 'ALL', 'url': BASE_URL12 + '/tag/h',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'H >>'}, img=IconPath + 'omp.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12a', 'section': 'ALL', 'url': BASE_URL12 + '/tag/i',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'I >>'}, img=IconPath + 'omp.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12a', 'section': 'ALL', 'url': BASE_URL12 + '/tag/j',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'J >>'}, img=IconPath + 'omp.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12a', 'section': 'ALL', 'url': BASE_URL12 + '/tag/k',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'K >>'}, img=IconPath + 'omp.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12a', 'section': 'ALL', 'url': BASE_URL12 + '/tag/l',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'L >>'}, img=IconPath + 'omp.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12a', 'section': 'ALL', 'url': BASE_URL12 + '/tag/m',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'M >>'}, img=IconPath + 'omp.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12a', 'section': 'ALL', 'url': BASE_URL12 + '/tag/n',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'N >>'}, img=IconPath + 'omp.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12a', 'section': 'ALL', 'url': BASE_URL12 + '/tag/o',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'O >>'}, img=IconPath + 'omp.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12a', 'section': 'ALL', 'url': BASE_URL12 + '/tag/p',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'P >>'}, img=IconPath + 'omp.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12a', 'section': 'ALL', 'url': BASE_URL12 + '/tag/q',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Q >>'}, img=IconPath + 'omp.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12a', 'section': 'ALL', 'url': BASE_URL12 + '/tag/r',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'R >>'}, img=IconPath + 'omp.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12a', 'section': 'ALL', 'url': BASE_URL12 + '/tag/s',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'S >>'}, img=IconPath + 'omp.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12a', 'section': 'ALL', 'url': BASE_URL12 + '/tag/t',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'T >>'}, img=IconPath + 'omp.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12a', 'section': 'ALL', 'url': BASE_URL12 + '/tag/u',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'U >>'}, img=IconPath + 'omp.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12a', 'section': 'ALL', 'url': BASE_URL12 + '/tag/v',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'V >>'}, img=IconPath + 'omp.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12a', 'section': 'ALL', 'url': BASE_URL12 + '/tag/w',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'W >>'}, img=IconPath + 'omp.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12a', 'section': 'ALL', 'url': BASE_URL12 + '/tag/x',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'X >>'}, img=IconPath + 'omp.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12a', 'section': 'ALL', 'url': BASE_URL12 + '/tag/y',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Y >>'}, img=IconPath + 'omp.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12a', 'section': 'ALL', 'url': BASE_URL12 + '/tag/z',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Z >>'}, img=IconPath + 'omp.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#----------------------------------------------------------------------------------------------------------------------------------------------------------------#

def PutMenu():          #put
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/new-movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cornflowerblue][B]Latest Added [/B][/COLOR] >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movies/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cornflowerblue][B]ABC [/B][/COLOR] >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movies/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cornflowerblue][B]Top IMDB [/B][/COLOR] >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'Put1Menu'}, {'title':  '[COLOR deepskyblue][B]Movie Genre[/B][/COLOR] [COLOR teal](Latest added) [/COLOR]>>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png') 
        addon.add_directory({'mode': 'Put2Menu'}, {'title':  '[COLOR deepskyblue][B]Movie Genre[/B][/COLOR] [COLOR teal](IMDB rating) [/COLOR]>>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png') 
        addon.add_directory({'mode': 'Put3Menu'}, {'title':  '[COLOR deepskyblue][B]Movie Genre[/B][/COLOR] [COLOR teal](A/Z) [/COLOR]>>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png') 
        xbmcplugin.endOfDirectory(int(sys.argv[1]))


def Put1Menu():          #put
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/action',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Action >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/adventure',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Adventure >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/animation',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Animation >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/biography',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Biography >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/comedy',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Comedy >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/crime',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Crime >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/drama',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Drama >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/documentary',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Documentary >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/fantasy',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Fantasy >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/family',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Family >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/horror',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Horror >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/musical',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Musical >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/mystery',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Mystery >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/romance',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Romance >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/sci-fi',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sci Fi >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/sport',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sport >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/thriller',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Thriller >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/war',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'War >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/western',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Western >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#-------------------------------------------------------#

def Put2Menu():          #put imdb
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/action/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Action >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/adventure/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Adventure >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/animation/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Animation >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/biography/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Biography >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/comedy/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Comedy >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/crime/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Crime >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/drama/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Drama >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/documentary/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Documentary >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/fantasy/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Fantasy >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/family/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Family >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/horror/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Horror >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/musical/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Musical >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/mystery/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Mystery >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/romance/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Romance >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/sci-fi/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sci Fi >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/sport/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sport >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/thriller/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Thriller >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/war/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'War >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/western/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Western >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------#

def Put3Menu():          #put abc
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/action/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Action >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/adventure/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Adventure >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/animation/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Animation >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/biography/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Biography >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/comedy/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Comedy >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/crime/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Crime >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/drama/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Drama >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/documentary/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Documentary >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/fantasy/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Fantasy >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/family/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Family >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/horror/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Horror >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/musical/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Musical >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/mystery/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Mystery >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/romance/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Romance >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/sci-fi/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sci Fi >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/sport/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sport >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/thriller/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Thriller >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/warv',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'War >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/western/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Western >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def OcmMenu():          #one click moviez
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cornflowerblue][B]Latest Added [/B][/COLOR] >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/featuredmovies/date/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cornflowerblue][B]Featured [/B][/COLOR] >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movies/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cornflowerblue][B]Top IMDB [/B][/COLOR] >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'Ocm1Menu'}, {'title':  '[COLOR deepskyblue][B]Movie Genre[/B][/COLOR] [COLOR peru](Latest added) [/COLOR]>>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png') 
        addon.add_directory({'mode': 'Ocm2Menu'}, {'title':  '[COLOR deepskyblue][B]Movie Genre[/B][/COLOR] [COLOR peru](IMDB rating) [/COLOR]>>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png') 
        addon.add_directory({'mode': 'Ocm3Menu'}, {'title':  '[COLOR deepskyblue][B]Movie Genre[/B][/COLOR] [COLOR peru](A/Z) [/COLOR]>>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png') 
        xbmcplugin.endOfDirectory(int(sys.argv[1]))


def Ocm1Menu():          #one click movies
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/action',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Action >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/adventure',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Adventure >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/animation',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Animation >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/biography',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Biography >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/comedy',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Comedy >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/crime',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Crime >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/drama',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Drama >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/documentary',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Documentary >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/fantasy',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Fantasy >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/family',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Family >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/horror',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Horror >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/musical',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Musical >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/mystery',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Mystery >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/romance',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Romance >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/sci-fi',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sci Fi >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/sport',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sport >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/thriller',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Thriller >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/war',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'War >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/western',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Western >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#-------------------------------------------------------#

def Ocm2Menu():          #one click moviez imdb
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/action/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Action >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/adventure/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Adventure >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/animation/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Animation >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/biography/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Biography >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/comedy/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Comedy >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/crime/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Crime >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/drama/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Drama >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/documentary/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Documentary >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/fantasy/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Fantasy >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/family/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Family >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/horror/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Horror >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/musical/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Musical >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/mystery/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Mystery >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/romance/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Romance >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/sci-fi/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sci Fi >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/sport/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sport >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/thriller/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Thriller >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/war/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'War >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/western/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Western >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------#

def Ocm3Menu():          #one click watch abc
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/action/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Action >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/adventure/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Adventure >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/animation/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Animation >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/biography/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Biography >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/comedy/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Comedy >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/crime/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Crime >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/drama/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Drama >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/documentary/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Documentary >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/fantasy/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Fantasy >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/family/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Family >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/horror/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Horror >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/musical/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Musical >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/mystery/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Mystery >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/romance/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Romance >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/sci-fi/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sci Fi >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/sport/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sport >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/thriller/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Thriller >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/warv',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'War >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/western/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Western >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

############################################################################---tv---##########################################################################################################

def TvMenu():       #tv
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/tv-shows/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR darkorange][B]Latest Episodes[/B][/COLOR] [COLOR blue](OCW) [/COLOR]>>'}, img=IconPath + 'ocw.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL1 + '/category/tvshows',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR darkorange][B]Latest Episodes[/B][/COLOR] [COLOR salmon](WTT) [/COLOR]>>'}, img=IconPath + 'wtt.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles10', 'section': 'ALL', 'url': BASE_URL10 + '/category/tv-shows/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR darkorange][B]Latest Episodes[/B][/COLOR] [COLOR khaki](MyVideoLinks) [/COLOR]>>'}, img=IconPath + 'mvl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles11', 'section': 'ALL', 'url': BASE_URL11 + '/category/tv-shows/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR darkorange][B]Latest Episodes[/B][/COLOR] [COLOR mediumblue](DDLvalley) [/COLOR]>>'}, img=IconPath + 'ddl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles8', 'section': 'ALL', 'url': BASE_URL8 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Latest Episodes[/B][/COLOR] [COLOR yellowgreen](WatchSeriesUs) [/COLOR]>>'}, img=IconPath + 'wsu.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL4 + '/category/tv',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Latest Episodes[/B][/COLOR] [COLOR floralwhite](Ultra-Vid) [/COLOR]>>'}, img=IconPath + 'uv1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL2 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Latest Episodes[/B][/COLOR] [COLOR darkslateblue](WTS) [/COLOR]>>'}, img=IconPath + 'wts1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles7', 'section': 'ALL', 'url': BASE_URL7 + '/new-shows',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Latest Episodes[/B][/COLOR] [COLOR gold](Movie-Kingdom) [/COLOR]>>'}, img=IconPath + 'mk.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles13', 'section': 'ALL', 'url': BASE_URL13 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Latest Episodes list[/B][/COLOR] [COLOR cadetblue](FullEpisode) [/COLOR]>>'}, img=IconPath + 'fei.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles14', 'section': 'ALL', 'url': BASE_URL14 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Latest Episodes list[/B][/COLOR] [COLOR tomato](ChannelCut) [/COLOR]>>'}, img=IconPath + 'cc.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles17', 'section': 'ALL', 'url': BASE_URL17 + '/category/shows/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Latest Episodes list[/B][/COLOR] [COLOR sienna](Tv-Junky) [/COLOR]>>'}, img=IconPath + 'tvj.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'TvocmMenu'}, {'title':  '[COLOR orange][B]Full Seasons[/B][/COLOR] [COLOR peru](OneClickMoviez) [/COLOR]>>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'TvputMenu'}, {'title':  '[COLOR orange][B]Full Seasons[/B][/COLOR] [COLOR teal](Putlocker Series) [/COLOR]>>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def TvocmMenu():
        addon.add_directory({'mode': 'GetTitles18a', 'section': 'ALL', 'url': BASE_URL9 + '/tv-shows',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR orange][B]Full Seasons[/B][/COLOR] [COLOR peru](Latest added) [/COLOR]>>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles18a', 'section': 'ALL', 'url': BASE_URL9 + '/tv-shows/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR orange][B]Full Seasons[/B][/COLOR] [COLOR peru](Top IMDB) [/COLOR]>>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles18a', 'section': 'ALL', 'url': BASE_URL9 + '/tv-shows/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR orange][B]Full Seasons[/B][/COLOR] [COLOR peru](ABC) [/COLOR]>>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'Tvocm1Menu'}, {'title':  '[COLOR orange][B]Tv Show Genre[/B][/COLOR] [COLOR peru](Top IMDB ) [/COLOR]>>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def Tvocm1Menu():
        addon.add_directory({'mode': 'GetTitles18a', 'section': 'ALL', 'url': BASE_URL9 + '/tv-tags/action/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Action >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles18a', 'section': 'ALL', 'url': BASE_URL9 + '/tv-tags/adventure/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Adventure >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles18a', 'section': 'ALL', 'url': BASE_URL9 + '/tv-tags/animation/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Animation >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles18a', 'section': 'ALL', 'url': BASE_URL9 + '/tv-tags/biography/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Biography >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles18a', 'section': 'ALL', 'url': BASE_URL9 + '/tv-tags/comedy/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Comedy >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles18a', 'section': 'ALL', 'url': BASE_URL9 + '/tv-tags/crime/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Crime >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles18a', 'section': 'ALL', 'url': BASE_URL9 + '/tv-tags/drama/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Drama >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles18a', 'section': 'ALL', 'url': BASE_URL9 + '/tv-tags/documentary/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Documentary >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles18a', 'section': 'ALL', 'url': BASE_URL9 + '/tv-tags/fantasy/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Fantasy >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles18a', 'section': 'ALL', 'url': BASE_URL9 + '/tv-tags/family/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Family >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles18a', 'section': 'ALL', 'url': BASE_URL9 + '/tv-tags/horror/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Horror >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles18a', 'section': 'ALL', 'url': BASE_URL9 + '/tv-tags/musical/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Musical >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles18a', 'section': 'ALL', 'url': BASE_URL9 + '/tv-tags/mystery/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Mystery >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles18a', 'section': 'ALL', 'url': BASE_URL9 + '/tv-tags/romance/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Romance >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles18a', 'section': 'ALL', 'url': BASE_URL9 + '/tv-tags/sci-fi/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sci Fi >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles18a', 'section': 'ALL', 'url': BASE_URL9 + '/tv-tags/sport/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sport >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles18a', 'section': 'ALL', 'url': BASE_URL9 + '/tv-tags/thriller/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Thriller >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles18a', 'section': 'ALL', 'url': BASE_URL9 + '/tv-tags/war/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'War >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles18a', 'section': 'ALL', 'url': BASE_URL9 + '/tv-tags/western/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Western >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def TvputMenu():  #put
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-shows',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR orange][B]Full Seasons[/B][/COLOR] [COLOR teal](Latest added) [/COLOR]>>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-shows/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR orange][B]Full Seasons[/B][/COLOR] [COLOR teal](Top IMDB) [/COLOR]>>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-shows/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR orange][B]Full Seasons[/B][/COLOR] [COLOR teal](ABC) [/COLOR]>>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'Tvput1Menu'}, {'title':  '[COLOR orange][B]Tv Show Genre[/B][/COLOR] [COLOR teal](ABC) [/COLOR]>>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def Tvput1Menu():    #put
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/action/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Action >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/adventure/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Adventure >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/animation/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Animation >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/biography/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Biography >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/comedy/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Comedy >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/crime/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Crime >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/drama/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Drama >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/documentary/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Documentary >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/fantasy/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Fantasy >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/family/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Family >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/horror/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Horror >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/musical/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Musical >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/mystery/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Mystery >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/romance/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Romance >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/sci-fi/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sci Fi >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/sport/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sport >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/thriller/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Thriller >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/war/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'War >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/western/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Western >>'}, img=IconPath + 'ps.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

################################################################################searchmenu###############################################################################################

def SearchMenu():
        addon.add_directory({'mode': 'GetSearchQuery9'},  {'title':  '[COLOR blue][B]OneClickWatch[/B][/COLOR] [COLOR green]Search[/COLOR]'}, img=IconPath + 'searches.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetSearchQuery1'},  {'title':  '[COLOR salmon][B]WatchTheTapes[/B][/COLOR] [COLOR green]Search[/COLOR]'}, img=IconPath + 'searches.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetSearchQuery2'},  {'title':  '[COLOR darkslateblue][B]WatchTvShows[/B][/COLOR] [COLOR green]Search Tv Shows[/COLOR] '}, img=IconPath + 'searches.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetSearchQuery3'},  {'title':  '[COLOR coral][B]TV junky[/B][/COLOR] [COLOR green]Search Tv Shows[/COLOR] '}, img=IconPath + 'searches.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetSearchQuery4'},  {'title':  '[COLOR tomato][B]ChannelCut[/B][/COLOR] [COLOR green]Search Tv Shows[/COLOR] '}, img=IconPath + 'searches.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))



########################################################################search#################################################################################################

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
        url = 'http://www.google.com/search?q=site:oneclickwatch.org ' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        CLEAN(html)
        match = re.compile('<h3 class="r"><a href="(.+?)".+?onmousedown=".+?">(.+?)</a>').findall(html)
        for url, title in match:
                title = title.replace('<b>...</b>', '').replace('<em>', '').replace('</em>', '')
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title})
	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#######################################################################################################


def GetSearchQuery2():
	last_search = addon.load_data('search')
	if not last_search: last_search = ''
	keyboard = xbmc.Keyboard()
        keyboard.setHeading('[COLOR green]Search TV Shows[/COLOR]')
	keyboard.setDefault(last_search)
	keyboard.doModal()
	if (keyboard.isConfirmed()):
                query = keyboard.getText()
                addon.save_data('search',query)
                Search2(query)
	else:
                return

        
def Search2(query):
        url = 'http://www.google.com/search?q=site:watchtvshowz.org ' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        CLEAN(html)
        match = re.compile('<h3 class="r"><a href="(.+?)".+?onmousedown=".+?">(.+?)</a>').findall(html)
        for url, title in match:
                title = title.replace('<b>...</b>', '').replace('<em>', '').replace('</em>', '').replace('Watch', '')
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title})
	xbmcplugin.endOfDirectory(int(sys.argv[1]))


###########################################################################

def GetSearchQuery1():
	last_search = addon.load_data('search')
	if not last_search: last_search = ''
	keyboard = xbmc.Keyboard()
        keyboard.setHeading('[COLOR green]Search[/COLOR]')
	keyboard.setDefault(last_search)
	keyboard.doModal()
	if (keyboard.isConfirmed()):
                query = keyboard.getText()
                addon.save_data('search',query)
                Search1(query)
	else:
                return

        
def Search1(query):
        url = 'http://www.google.com/search?q=site:watchthetapes.com ' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        CLEAN(html)
        match = re.compile('<h3 class="r"><a href="(.+?)".+?onmousedown=".+?">(.+?)</a>').findall(html)
        for url, title in match:
                title = title.replace('<b>...</b>', '').replace('<em>', '').replace('</em>', '').replace('Watch', '')
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title})
	xbmcplugin.endOfDirectory(int(sys.argv[1]))

###############################################################################

def GetSearchQuery3():
	last_search = addon.load_data('search')
	if not last_search: last_search = ''
	keyboard = xbmc.Keyboard()
        keyboard.setHeading('[COLOR green]Search TV Shows[/COLOR]')
	keyboard.setDefault(last_search)
	keyboard.doModal()
	if (keyboard.isConfirmed()):
                query = keyboard.getText()
                addon.save_data('search',query)
                Search3(query)
	else:
                return

        
def Search3(query):
        url = 'http://www.google.com/search?q=site:tv-junky.eu ' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        CLEAN(html)
        match = re.compile('<h3 class="r"><a href="(.+?)".+?onmousedown=".+?">(.+?)</a>').findall(html)
        for url, title in match:
                title = title.replace('<b>...</b>', '').replace('<em>', '').replace('</em>', '').replace('Watch', '')
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title})
	xbmcplugin.endOfDirectory(int(sys.argv[1]))

######################################################################################

def GetSearchQuery4():
	last_search = addon.load_data('search')
	if not last_search: last_search = ''
	keyboard = xbmc.Keyboard()
        keyboard.setHeading('[COLOR green]Search TV Shows[/COLOR]')
	keyboard.setDefault(last_search)
	keyboard.doModal()
	if (keyboard.isConfirmed()):
                query = keyboard.getText()
                addon.save_data('search',query)
                Search4(query)
	else:
                return

        
def Search4(query):
        url = 'http://www.google.com/search?q=site:channelcut.me ' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        CLEAN(html)
        match = re.compile('<h3 class="r"><a href="(.+?)".+?onmousedown=".+?">(.+?)</a>').findall(html)
        for url, title in match:
                title = title.replace('<b>...</b>', '').replace('<em>', '').replace('</em>', '').replace('Watch', '')
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title})
	xbmcplugin.endOfDirectory(int(sys.argv[1]))


######################################################################################

def GetSearchQuery5():
	last_search = addon.load_data('search')
	if not last_search: last_search = ''
	keyboard = xbmc.Keyboard()
        keyboard.setHeading('[COLOR green]Search OneClickMoviez[/COLOR]')
	keyboard.setDefault(last_search)
	keyboard.doModal()
	if (keyboard.isConfirmed()):
                query = keyboard.getText()
                addon.save_data('search',query)
                Search5(query)
	else:
                return

        
def Search5(query):
        url = 'http://www.google.com/search?q=site:oneclickmoviez.ag ' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        CLEAN(html)
        match = re.compile('<h3 class="r"><a href="(.+?)".+?onmousedown=".+?">(.+?)</a>').findall(html)
        for url, title in match:
                title = title.replace('<b>...</b>', '').replace('<em>', '').replace('</em>', '').replace('Watch', '').replace('ONE CLICK MOVIEZ ', '')
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title})
	xbmcplugin.endOfDirectory(int(sys.argv[1]))


######################################################################################              ##########################################################################

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

##############################################################################################################################################################################

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
elif mode == 'GetTitles6a': 
	GetTitles6a(section, url, startPage, numOfPages)
elif mode == 'GetTitles7': 
	GetTitles7(section, url, startPage, numOfPages)
elif mode == 'GetTitles7a': 
	GetTitles7a(section, url, startPage, numOfPages)
elif mode == 'GetTitles8': 
	GetTitles8(section, url, startPage, numOfPages)
elif mode == 'GetTitles9': 
	GetTitles9(section, url, startPage, numOfPages)
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
elif mode == 'GetTitles12a': 
	GetTitles12a(section, url, startPage, numOfPages)
elif mode == 'GetTitles15': 
	GetTitles15(section, url, startPage, numOfPages)
elif mode == 'GetTitles15a': 
	GetTitles15a(section, url, startPage, numOfPages)
elif mode == 'GetTitles15b': 
	GetTitles15b(section, url, startPage, numOfPages)
elif mode == 'GetTitles16': 
	GetTitles16(section, url, startPage, numOfPages)
elif mode == 'GetTitles17': 
	GetTitles17(section, url, startPage, numOfPages)
elif mode == 'GetTitles18': 
	GetTitles18(section, url, startPage, numOfPages)
elif mode == 'GetTitles18a': 
	GetTitles18a(section, url, startPage, numOfPages)
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
	GetTitles25(section, url, startPage, numOfPages)
elif mode == 'GetTitles26': 
	GetTitles26(section, url, startPage, numOfPages)
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
elif mode == 'GetSearchQuery9':
	GetSearchQuery9()
elif mode == 'Search9':
	Search9(query)
elif mode == 'GetSearchQuery2':
	GetSearchQuery2()
elif mode == 'Search2':
	Search2(query)
elif mode == 'GetSearchQuery3':
	GetSearchQuery3()
elif mode == 'Search3':
	Search3(query)
elif mode == 'GetSearchQuery1':
	GetSearchQuery1()
elif mode == 'Search1':
	Search1(query)
elif mode == 'GetSearchQuery4':
	GetSearchQuery4()
elif mode == 'Search4':
	Search4(query)
elif mode == 'GetSearchQuery5':
	GetSearchQuery5()
elif mode == 'Search5':
	Search5(query)
elif mode == 'PlayVideo':
	PlayVideo(url, listitem)	
elif mode == 'ResolverSettings':
        urlresolver.display_settings()
elif mode == 'SearchMenu':
        SearchMenu()
elif mode == 'MovieMenu':
        MovieMenu()
elif mode == 'TvMenu':
        TvMenu()
elif mode == 'MusicMenu':
        MusicMenu()
elif mode == 'MovMenu':
        MovMenu()
elif mode == 'UvMenu':
        UvMenu()
elif mode == 'WtMenu':
        WtMenu()
elif mode == 'ZmMenu':
        ZmMenu()
elif mode == 'MkMenu':
        MkMenu()
elif mode == 'RgMenu':
        RgMenu()
elif mode == 'OmpMenu':
        OmpMenu()
elif mode == 'SportMenu':
        SportMenu()
elif mode == 'OmpazMenu':
        OmpazMenu()
elif mode == 'OcmMenu':
        OcmMenu()
elif mode == 'Ocm1Menu':
        Ocm1Menu()
elif mode == 'Ocm2Menu':
        Ocm2Menu()
elif mode == 'Ocm3Menu':
        Ocm3Menu()
elif mode == 'TvocmMenu':
        TvocmMenu()
elif mode == 'Tvocm1Menu':
        Tvocm1Menu()
elif mode == 'PutMenu':
        PutMenu()
elif mode == 'Put1Menu':
        Put1Menu()
elif mode == 'Put2Menu':
        Put2Menu()
elif mode == 'Put3Menu':
        Put3Menu()
elif mode == 'TvputMenu':
        TvputMenu()
elif mode == 'Tvput1Menu':
        Tvput1Menu()
elif mode == 'CineMenu':
        CineMenu()
