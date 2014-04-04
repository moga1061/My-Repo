# Kool London XBMC Plugin
# Developer: Android TV Boxes reworked by TheYid
# Support: www.xbmchub.com
# Disclaimer: Android TV Boxes or TheYid do not own or publish the content delivered by the plugin
# streams and content is owned by Koollondon

import sys
import xbmcgui
import xbmcplugin
 
addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'audio')
url = 'http://uk1-pn.webcast-server.net:8698'
li = xbmcgui.ListItem('[COLOR blue][B][I]Kool London[/B][/I][/COLOR] [COLOR red][B][I](Live)[/B][/I][/COLOR]  [COLOR yellow][B] >>[/B][/COLOR]', iconImage='http://s1.postimg.org/fko2kyu9b/icon.png')
li.setProperty('fanart_image', 'http://s27.postimg.org/47ti3qg6b/fanart.jpg')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
xbmcplugin.endOfDirectory(addon_handle)
