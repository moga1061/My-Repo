# Rough Tempo XBMC Plugin
# Developer: Android TV Boxes reworked by TheYid
# Support: www.xbmchub.com or @TheYid009
# Disclaimer: Android TV Boxes or TheYid do not own or publish the content delivered by the plugin
# streams and content is owned by Rough Tempo

import sys
import xbmcgui
import xbmcplugin
 
addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'audio')
url = 'http://213.229.108.96/RTB'
li = xbmcgui.ListItem('[COLOR lightsteelblue][B]Rough Tempo [/B][/COLOR]  [COLOR red](Video Stream)[/COLOR]  [COLOR lime](((LIVE)))[/COLOR]', iconImage='http://www.roughtempo.com/fbimage.jpg', thumbnailImage= 'http://www.roughtempo.com/fbimage.jpg')
li.setProperty('fanart_image', 'http://s18.postimg.org/wxt9kuvpl/maxresdefault.jpg')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'audio')
url = 'http://213.229.108.96:8000/'
li = xbmcgui.ListItem('[COLOR deepskyblue][B]Rough Tempo [/B][/COLOR]  [COLOR red](Audio Stream)[/COLOR]  [COLOR lime](((LIVE)))[/COLOR]', iconImage='http://www.roughtempo.com/fbimage.jpg', thumbnailImage= 'http://www.roughtempo.com/fbimage.jpg')
li.setProperty('fanart_image', 'http://s18.postimg.org/wxt9kuvpl/maxresdefault.jpg')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

xbmcplugin.setContent(addon_handle, 'audio')
url = 'http://213.229.108.96/RAVETV'
li = xbmcgui.ListItem('[COLOR lightsteelblue][B]Rave:TV [/B][/COLOR]  [COLOR red](Video Stream)[/COLOR]  [COLOR gold](((NOT 24/7 check site to see when live)))[/COLOR]', iconImage='https://fbcdn-profile-a.akamaihd.net/hprofile-ak-ash3/t1.0-1/c28.28.345.345/s160x160/562599_139408172908462_1152825309_n.jpg', thumbnailImage= 'https://fbcdn-profile-a.akamaihd.net/hprofile-ak-ash3/t1.0-1/c28.28.345.345/s160x160/562599_139408172908462_1152825309_n.jpg')
li.setProperty('fanart_image', 'http://archive-media.nyafuu.org/wg/image/1367/08/1367087842578.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'audio')
url = 'http://213.229.108.96:8000/'
li = xbmcgui.ListItem('Message The Studio Direct: +44 (0) 7766680280. Twitter: @RoughTempo. BEST RADIO STATION - DRUM & BASS AWARDS 2014 Live from the UK to the WORLD! - inc Multi-Cam Video Stream, www.roughtempo.com ', iconImage='http://www.roughtempo.com/fbimage.jpg', thumbnailImage= 'http://www.roughtempo.com/fbimage.jpg')
li.setProperty('fanart_image', 'http://s18.postimg.org/wxt9kuvpl/maxresdefault.jpg')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

xbmcplugin.endOfDirectory(addon_handle)

