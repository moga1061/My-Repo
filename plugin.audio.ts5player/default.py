import xbmc, xbmcgui, xbmcaddon, xbmcplugin
import re, string, sys, os
from t0mm0.common.addon import Addon
from t0mm0.common.net import Net

addon_id = 'plugin.audio.ts5player'
plugin = xbmcaddon.Addon(id=addon_id)
DB = os.path.join(xbmc.translatePath("special://database"), 'ts5player.db')
BASE_URL = 'http://www.ts5.com/'
net = Net()
addon = Addon('plugin.audio.ts5player', sys.argv)
mode = addon.queries['mode']
url = addon.queries.get('url', None)
content = addon.queries.get('content', None)
listitem = addon.queries.get('listitem', None)

############################################################################### Get links #############################################################################################

def GetLinks(url):
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
        li = xbmcgui.ListItem('[COLOR dodgerblue][B]PLAY STREAM[/B][/COLOR]  [COLOR darkorchid][B] >>[/B][/COLOR] >> ', iconImage='https://pbs.twimg.com/media/BTsytR2IAAA5b2g.jpg', thumbnailImage= 'https://pbs.twimg.com/media/BTsytR2IAAA5b2g.jpg')
        li.setProperty('fanart_image', 'http://i.vimeocdn.com/video/466480811_640.jpg')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
        xbmcplugin.endOfDirectory(addon_handle)

################################################################################ ListItem #################################################################################

def GetMediaInfo(html):
        listitem = xbmcgui.ListItem()
        match = re.search('og:title" content="(.+?) \((.+?)\)', html)
        if match:
                print match.group(1) + ' : '  + match.group(2)
                listitem.setInfo('video', {'Title': match.group(1), 'Year': int(match.group(2)) } )
        return listitem

################################################################################# menus ####################################################################################################

def MainMenu():    #homescreen
        addon_handle = int(sys.argv[1]) 
        xbmcplugin.setContent(addon_handle, 'audio')
        url = 'http://media-ice.musicradio.com/CapitalXTRALondonMP3.m3u'
        li = xbmcgui.ListItem('[COLOR blue][B]Capital Xtra[/B][/COLOR] [COLOR lime] (((LIVE))) [/COLOR] >>', iconImage='http://www.musicweek.com/cimages/a6ff7aa07ec100c4cc84ab4148817d44.jpg', thumbnailImage= 'http://www.musicweek.com/cimages/a6ff7aa07ec100c4cc84ab4148817d44.jpg')
        li.setProperty('fanart_image', 'http://s29.postimg.org/u0cwxr30n/fanart.jpg')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

        addon.add_directory({'mode': 'GetLinks', 'url': BASE_URL + '/'}, {'title':  '[COLOR darkorchid][B]TS5 Music Player[/B] [/COLOR]'}, img = 'http://img.youtube.com/vi/MExnrzr7Pa8/0.jpg', fanart = 'http://s29.postimg.org/u0cwxr30n/fanart.jpg')
        xbmcplugin.endOfDirectory(addon_handle)


################################################################################# mode #########################################################################################

if mode == 'main': 
	MainMenu()
elif mode == 'GetLinks':
	GetLinks(url)
elif mode == 'PlayVideo':
	PlayVideo(url, listitem)	
