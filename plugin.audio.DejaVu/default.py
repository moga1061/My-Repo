# Flight FM London XBMC Plugin
# Developer: Android TV Boxes
# Support: support@androidtvboxes.co.uk
# Disclaimer: Android TV Boxes do not own or publish the content delivered by the plugin
# streams and content is owned by DejaVu FM

import sys
import xbmcgui
import xbmcplugin
 
addon_handle = int(sys.argv[1])
 
xbmcplugin.setContent(addon_handle, 'audio')
 
url = 'http://176.31.239.83:9136/'
li = xbmcgui.ListItem('Studio 1 = Deja Classic >>', iconImage='http://s2.postimg.org/eg7k51z3t/icon.png', thumbnailImage='http://www.urbanreadyuk.co.uk/deja%20vu%20icon.jpg')
li.setProperty('fanart_image', 'http://s18.postimg.org/fnbfwgw3d/fanart.jpg')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://176.31.239.83:9041/'
li = xbmcgui.ListItem('Studio 2 = DejaVuLive >>', iconImage='http://s2.postimg.org/eg7k51z3t/icon.png', thumbnailImage= 'http://s2.postimg.org/eg7k51z3t/icon.png')
li.setProperty('fanart_image', 'http://s18.postimg.org/fnbfwgw3d/fanart.jpg')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)


xbmcplugin.endOfDirectory(addon_handle)