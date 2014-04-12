import xbmc, xbmcgui, xbmcaddon, xbmcplugin
import re, string, sys, os
from t0mm0.common.addon import Addon
from t0mm0.common.net import Net

addon_id = 'plugin.audio.ts5'
plugin = xbmcaddon.Addon(id=addon_id)
DB = os.path.join(xbmc.translatePath("special://database"), 'ts5.db')
BASE_URL = 'http://www.ts5.com/'
net = Net()
addon = Addon('plugin.audio.ts5', sys.argv)

###### PATHS ###########
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

############################################################################### Get links #############################################################################################

def GetLinks(section, url):
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('data-track-name="(.+?)" data-track-url="(.+?)">').findall(content)
        listitem = GetMediaInfo(content)
        for name, url in match:
                addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title':  name.strip()}, img = 'https://pbs.twimg.com/media/BTsytR2IAAA5b2g.jpg', fanart = 'http://assets2.capitalfm.com/2013/36/craig-david-capital-fm-1378707484-large-article-0.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

############################################################################# Play Video #####################################################################################

def PlayVideo(url, listitem):
        addon_handle = int(sys.argv[1])
        xbmcplugin.setContent(addon_handle, 'audio')
        li = xbmcgui.ListItem('[COLOR dodgerblue][B]PLAY STREAM[/B][/COLOR]  [COLOR darkorchid][B] >>[/B][/COLOR] >> ', iconImage='https://pbs.twimg.com/media/BTsytR2IAAA5b2g.jpg')
        li.setProperty('fanart_image', 'http://www.kissfmuk.com/wp-content/uploads/2013/03/craigdavid.jpg')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
        xbmcplugin.endOfDirectory(addon_handle)

##########################################################################################################################################################################

def GetMediaInfo(html):
        listitem = xbmcgui.ListItem()
        match = re.search('og:title" content="(.+?) \((.+?)\)', html)
        if match:
                print match.group(1) + ' : '  + match.group(2)
                listitem.setInfo('video', {'Title': match.group(1), 'Year': int(match.group(2)) } )
        return listitem

###################################################################### menus ####################################################################################################

def MainMenu():    #homescreen
        addon.add_directory({'mode': 'GetLinks', 'section': 'ALL', 'url': BASE_URL + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorchid][B]TS5 Music Player[/B] [/COLOR]>>'}, img = 'https://pbs.twimg.com/media/BTsytR2IAAA5b2g.jpg', fanart = 'http://assets2.capitalfm.com/2013/36/craig-david-capital-fm-1378707484-large-article-0.jpg')
 
        addon_handle = int(sys.argv[1]) 
        xbmcplugin.setContent(addon_handle, 'audio')
        url = 'http://media-ice.musicradio.com/CapitalXTRALondonMP3.m3u'
        li = xbmcgui.ListItem('[COLOR darkorchid][B]Capital Xtra[/B][/COLOR] [COLOR red] (((LIVE))) [/COLOR] >>', iconImage='http://www.musicweek.com/cimages/7ec1c3e8cda116edcba97d259933f288.jpg')
        li.setProperty('fanart_image', 'http://londonist.com/wp-content/uploads/2013/11/Capital-XTRA.jpg')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
        xbmcplugin.endOfDirectory(addon_handle)


#################################################################################################################################################################################

if mode == 'main': 
	MainMenu()
elif mode == 'GetLinks':
	GetLinks(section, url)
elif mode == 'PlayVideo':
	PlayVideo(url, listitem)	
