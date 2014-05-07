# Freek fm Live XBMC Plugin
# Developer: @TheYid009
# Support: www.xbmchub.com or @TheYid009
# Disclaimer: @TheYid009 dose not own or publish the content delivered by the plugin
# streams and content is owned by Freek fm live

import sys
import xbmcgui
import xbmcplugin
 
addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'audio')
url = 'http://xfreekfmx.api.channel.livestream.com/3.0/playlist.m3u8'
li = xbmcgui.ListItem('[COLOR blue][B]Freek fm [/B][/COLOR]  [COLOR gold](Video)[/COLOR]  [COLOR lime](((LIVE)))[/COLOR]', thumbnailImage= 'http://s30.postimg.org/d68bagf29/icon.png')
li.setProperty('fanart_image', 'http://s4.postimg.org/jr0kzygil/fanart.jpg')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

xbmcplugin.setContent(addon_handle, 'audio')
url = 'http://208.167.236.13:8230/;'
li = xbmcgui.ListItem('[COLOR lightsteelblue][B]Freek fm [/B][/COLOR]  [COLOR gold](Audio)[/COLOR]  [COLOR lime](((LIVE)))[/COLOR]', thumbnailImage= 'http://s30.postimg.org/d68bagf29/icon.png')
li.setProperty('fanart_image', 'http://s4.postimg.org/jr0kzygil/fanart.jpg')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

xbmcplugin.setContent(addon_handle, 'audio')
url = 'http://webstreamer.co.uk:2199/tunein/sc_51100/playlist.pls'
li = xbmcgui.ListItem('IF YOU WOULD LIKE TO ADVERTISE ON OUR MULTI-AWARD WINNING NETWORK, PLEASE EMAIL OUR SALES TEAM NOW : FREEKFMOFFICIAL@GMAIL.COM // TEXT THE STUDIO +447501 347 440 @FREEKFMOFFICIAL', thumbnailImage= 'http://s30.postimg.org/d68bagf29/icon.png')
li.setProperty('fanart_image', 'http://s4.postimg.org/jr0kzygil/fanart.jpg')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)


xbmcplugin.endOfDirectory(addon_handle)

