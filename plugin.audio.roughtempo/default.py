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
li = xbmcgui.ListItem('[COLOR lightsteelblue][B]Rough Tempo [/B][/COLOR]  [COLOR red](Video Streaming)[/COLOR]  [COLOR lime](((LIVE)))[/COLOR]', iconImage='http://www.roughtempo.com/fbimage.jpg', thumbnailImage= 'http://www.roughtempo.com/fbimage.jpg')
li.setProperty('fanart_image', 'http://i1.ytimg.com/vi/UwCoz9kGJAs/maxresdefault.jpg')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

xbmcplugin.endOfDirectory(addon_handle)

