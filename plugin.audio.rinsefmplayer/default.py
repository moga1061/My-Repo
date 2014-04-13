import xbmc, xbmcgui, xbmcaddon, xbmcplugin
import re, string, sys, os
from t0mm0.common.addon import Addon
from t0mm0.common.net import Net

addon_id = 'plugin.audio.rinsefmplayer'
plugin = xbmcaddon.Addon(id=addon_id)
DB = os.path.join(xbmc.translatePath("special://database"), 'rinsefmplayer.db')
BASE_URL = 'http://rinse.fm/'
net = Net()
addon = Addon('plugin.audio.rinsefmplayer', sys.argv)
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
        match = re.compile('<a href="(.+?)" download="http://podcast.dgen.net/rinsefm/podcast/(.+?)"').findall(content)
        listitem = GetMediaInfo(content)
        for url, name in match:
                addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title':  name.strip()}, img = 'http://s16.postimg.org/kdlyi29j9/icon.png', fanart = 'http://s29.postimg.org/rsd7ep7gn/fanart.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

############################################################################# Play Video #####################################################################################

def PlayVideo(url, listitem):
        addon_handle = int(sys.argv[1])
        xbmcplugin.setContent(addon_handle, 'audio')
        li = xbmcgui.ListItem('[COLOR dodgerblue][B]PLAY STREAM[/B][/COLOR]  [COLOR powderblue][B] >>[/B][/COLOR] >> ', iconImage='http://s16.postimg.org/kdlyi29j9/icon.png')
        li.setProperty('fanart_image', 'http://s29.postimg.org/rsd7ep7gn/fanart.jpg')
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

def MainMenu():   
        addon_handle = int(sys.argv[1]) 
        xbmcplugin.setContent(addon_handle, 'audio')
        url = 'http://podcast.dgen.net/rinsefm'
        li = xbmcgui.ListItem('[COLOR powderblue][B]Rinse FM[/B][/COLOR] [COLOR red] (((LIVE))) [/COLOR] >>', iconImage='http://s16.postimg.org/kdlyi29j9/icon.png')
        li.setProperty('fanart_image', 'http://s29.postimg.org/rsd7ep7gn/fanart.jpg')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

        addon.add_directory({'mode': 'GetLinks', '': '', 'url': BASE_URL + '/podcasts/',
                             '': '', '': ''}, {'title':  '[COLOR dodgerblue][B]Latest shows (Music Player)[/B] [/COLOR]>>'}, img = 'http://s16.postimg.org/kdlyi29j9/icon.png', fanart = 'http://s29.postimg.org/rsd7ep7gn/fanart.jpg')

        addon.add_directory({'mode': 'GetLinks', '': '', 'url': BASE_URL + '/podcasts/?showID=265',
                             '': '', '': ''}, {'title':  '[COLOR cadetblue][B]Uncle Dugs (shows)[/B] [/COLOR]>>'}, img = 'http://rinse.fm/wp-content/uploads/2012/09/artistprofile_uncledugs.jpg', fanart = 'http://s29.postimg.org/rsd7ep7gn/fanart.jpg')
        addon.add_directory({'mode': 'GetLinks', '': '', 'url': BASE_URL + '/podcasts/?showID=187',
                             '': '', '': ''}, {'title':  '[COLOR cadetblue][B]Dappa (shows)[/B] [/COLOR]>>'}, img = 'http://rinse.fm/wp-content/uploads/2012/09/artistprofile_dappa2.jpg', fanart = 'http://s29.postimg.org/rsd7ep7gn/fanart.jpg')
        addon.add_directory({'mode': 'GetLinks', '': '', 'url': BASE_URL + '/podcasts/?showID=11361',
                             '': '', '': ''}, {'title':  '[COLOR cadetblue][B]Flight (shows)[/B] [/COLOR]>>'}, img = 'https://pbs.twimg.com/profile_images/378800000033780049/8585048820bc918b88594175e528d057.jpeg', fanart = 'http://s29.postimg.org/rsd7ep7gn/fanart.jpg')
        addon.add_directory({'mode': 'GetLinks', '': '', 'url': BASE_URL + '/podcasts/?showID=249',
                             '': '', '': ''}, {'title':  '[COLOR cadetblue][B]Marcus Nasty (shows)[/B] [/COLOR]>>'}, img = 'http://rinse.fm/wp-content/uploads/2012/09/artistprofile_marcusnasty3.jpg', fanart = 'http://s29.postimg.org/rsd7ep7gn/fanart.jpg')
        addon.add_directory({'mode': 'GetLinks', '': '', 'url': BASE_URL + '/podcasts/?showID=5661',
                             '': '', '': ''}, {'title':  '[COLOR cadetblue][B]Metalheadz (shows)[/B] [/COLOR]>>'}, img = 'http://rinse.fm/wp-content/uploads/2013/04/artistprofile_metalheadz_1-460x508.jpg', fanart = 'http://s29.postimg.org/rsd7ep7gn/fanart.jpg')
        addon.add_directory({'mode': 'GetLinks', '': '', 'url': BASE_URL + '/podcasts/?showID=272',
                             '': '', '': ''}, {'title':  '[COLOR cadetblue][B]Mark Radford (shows)[/B] [/COLOR]>>'}, img = 'http://rinse.fm/wp-content/uploads/2012/09/artistprofile_markradford1.jpg', fanart = 'http://s29.postimg.org/rsd7ep7gn/fanart.jpg')
        addon.add_directory({'mode': 'GetLinks', '': '', 'url': BASE_URL + '/podcasts/?showID=224',
                             '': '', '': ''}, {'title':  '[COLOR cadetblue][B]Sam Supplier (shows)[/B] [/COLOR]>>'}, img = 'http://rinse.fm/wp-content/uploads/2012/09/artistprofile_supplier2.jpg', fanart = 'http://s29.postimg.org/rsd7ep7gn/fanart.jpg')
        addon.add_directory({'mode': 'GetLinks', '': '', 'url': BASE_URL + '/podcasts/?showID=166',
                             '': '', '': ''}, {'title':  '[COLOR cadetblue][B]Zinc (shows)[/B] [/COLOR]>>'}, img = 'http://rinse.fm/wp-content/uploads/2012/09/artistprofile_zincv3-460x508.jpg', fanart = 'http://s29.postimg.org/rsd7ep7gn/fanart.jpg')
        addon.add_directory({'mode': 'GetLinks', '': '', 'url': BASE_URL + '/podcasts/?showID=2853',
                             '': '', '': ''}, {'title':  '[COLOR cadetblue][B]The Garage Hour (shows)[/B] [/COLOR]>>'}, img = 'http://s16.postimg.org/kdlyi29j9/icon.png', fanart = 'http://s29.postimg.org/rsd7ep7gn/fanart.jpg')
        addon.add_directory({'mode': 'GetLinks', '': '', 'url': BASE_URL + '/podcasts/?showID=7592',
                             '': '', '': ''}, {'title':  '[COLOR cadetblue][B]The Grime Show (shows)[/B] [/COLOR]>>'}, img = 'http://s16.postimg.org/kdlyi29j9/icon.png', fanart = 'http://s29.postimg.org/rsd7ep7gn/fanart.jpg')
        xbmcplugin.endOfDirectory(addon_handle)

################################################################################# mode #########################################################################################

if mode == 'main': 
	MainMenu()
elif mode == 'GetLinks':
	GetLinks(url)
elif mode == 'PlayVideo':
	PlayVideo(url, listitem)	
