# Kool London XBMC Plugin
# Developer: Android TV Boxes reworked by TheYid
# Support: www.xbmchub.com or @TheYid009
# Disclaimer: Android TV Boxes or TheYid do not own or publish the content delivered by the plugin
# streams and content is owned by Koollondon

import sys
import xbmcgui
import xbmcplugin
 
addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'audio')
url = 'http://uk1-pn.webcast-server.net:8698'
li = xbmcgui.ListItem('[COLOR dodgerblue][B]Kool London[/B][/COLOR] [COLOR red][B][I](Live)[/B][/I][/COLOR]  [COLOR yellow][B] >>[/B][/COLOR] >>    [COLOR lime](Stream 1)[/COLOR]', iconImage='http://s30.postimg.org/5r870dash/icon.png')
li.setProperty('fanart_image', 'http://koollondon.com/images/stories/kool-timetable-march-2014.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

xbmcplugin.setContent(addon_handle, 'audio')
url = 'http://uk1-pn.mixstream.net/8698.m3u'
li = xbmcgui.ListItem('[COLOR dodgerblue][B]Kool London[/B][/COLOR] [COLOR red][B][I](Live)[/B][/I][/COLOR]  [COLOR yellow][B] >>[/B][/COLOR] >>    [COLOR lime](Stream 2)[/COLOR]', iconImage='http://s30.postimg.org/5r870dash/icon.png')
li.setProperty('fanart_image', 'http://s2.postimg.org/4jtfmw5qx/fanart2.jpg')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
xbmcplugin.endOfDirectory(addon_handle)

