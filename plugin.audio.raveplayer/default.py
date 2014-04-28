'''
    Rave player XBMC Addon
    Copyright (C) 2014 tcz009 @TheYid009 TheYid's REPO

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
#############################################################-Rave player-########################################################################################

import xbmc, xbmcgui, xbmcaddon, xbmcplugin
import urllib, urllib2
import re, string, sys, os
from TheYid.common.addon import Addon
from TheYid.common.net import Net
from htmlentitydefs import name2codepoint as n2cp
import HTMLParser

addon_id = 'plugin.audio.raveplayer'
plugin = xbmcaddon.Addon(id=addon_id)
DB = os.path.join(xbmc.translatePath("special://database"), 'raveplayer.db')

BASE_URL = 'http://www.oneinthejungle.co.uk/'
BASE_URL2 = 'http://20bensons.com/'
BASE_URL3 = 'http://www.ravetapepacks.com/'
BASE_URL4 = 'http://deepinsidetheoldskool.blogspot.co.uk/'
BASE_URL5 = 'http://www.thebeatsanctuary.co.uk/'
BASE_URL6 = 'http://ratpack.podomatic.com/'
BASE_URL7 = 'http://www.ukraves.co.uk/'
BASE_URL8 = 'http://oldskool.podomatic.com/'
BASE_URL9 = 'http://mikusmusik.blogspot.co.uk/'
BASE_URL10 = 'http://drumandbass.ch/'
BASE_URL11 = 'http://mixtapes.demodulated.com/'
BASE_URL12 = 'http://www.shitmixtapes.com/'
BASE_URL13 = 'http://www.rave-archive.com/'
BASE_URL14 = 'http://www.thewire.co.uk/'
BASE_URL15 = 'https://raw.githubusercontent.com/TheYid/yidpics/master'
BASE_URL17 = 'https://archive.org/'
BASE_URL18 = 'http://torontoravemixtapearchive.com/'
BASE_URL19 = 'http://jungletechno.tumblr.com/'
BASE_URL20 = 'http://www.dj-jedi.com/'
BASE_URL21 = 'http://175bpm.pl/'

net = Net()
addon = Addon('plugin.audio.raveplayer', sys.argv)
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

#---------------------------------------------------------------------------- oneinthejungle ----------------------------------------------------------------------------#

def GetLinks(url):                                             
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('<td><a href="(.+?)">(.+?)</a>').findall(content)
        for url, name in match:
                addon.add_directory({'mode': 'PlayVideo', 'url': 'http://www.oneinthejungle.co.uk/' + url, 'listitem': listitem}, {'title':  name.strip()}, img = 'http://www.oneinthejungle.net/images/home/fb.png', fanart = 'http://www.allcrew.co.uk/pages/cartgifs/party.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#------------------------------------------------------------------------------ 20bensons ----------------------------------------------------------------------------#

def GetLinks2(url):                                           
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('href="(.+?)">(.+?)</a>').findall(content)
        for url, name in match:
                url = url.replace(' ','%20')
                addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title':  name.strip()}, img = 'http://www.zigsam.at/l07/B_Cig/BensonHedgesSpeciaF-20fJP197.jpg', fanart = 'http://cs11180.vk.me/u19162043/47140284/x_977c8c97.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#------------------------------------------------------------------------------- ravetapepacks -------------------------------------------------------------------------------------#

def GetLinks3(url):  
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html                                          
        match = re.compile('<li class=".+?"><a href="(.+?)" title=".+?">(.+?)</a>').findall(content)
        for url, name in match:
                addon.add_directory({'mode': 'GetLinks3a', 'url': url, 'listitem': listitem}, {'title':  name.strip()}, img = 'http://fc09.deviantart.net/fs25/f/2008/111/a/8/Cassette_tape_by_Quick_Stop.png', fanart = 'http://24.media.tumblr.com/tumblr_md33y3uDzM1qkcj9ro4_1280.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetLinks3a(url):                                           
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        CLEAN(html)
        content = html
        match = re.compile('<h1 class="entry-title">\n\t\t\t\t<a href="(.+?)" rel="bookmark">(.+?)</a>').findall(content)
        for url, name in match:
                addon.add_directory({'mode': 'GetLinks3b', 'url':  url, 'listitem': listitem}, {'title':  name.strip()}, img = 'http://fc09.deviantart.net/fs25/f/2008/111/a/8/Cassette_tape_by_Quick_Stop.png', fanart = 'http://24.media.tumblr.com/tumblr_md33y3uDzM1qkcj9ro4_1280.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetLinks3b(url):                                            
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('<p style="text-align: left;"><a href="(.+?)">(.+?)</a></p>').findall(content)
        match2 = re.compile('<p><a href="http://www.ravetapepacks.com/music/(.+?)">(.+?)</a></p>').findall(content)
        for url, name in match:
                addon.add_directory({'mode': 'PlayVideo', 'url':  url, 'listitem': listitem}, {'title':  name.strip()}, img = 'http://fc09.deviantart.net/fs25/f/2008/111/a/8/Cassette_tape_by_Quick_Stop.png', fanart = 'http://24.media.tumblr.com/tumblr_md33y3uDzM1qkcj9ro4_1280.jpg')
        for url, name in match2:
                addon.add_directory({'mode': 'PlayVideo', 'url':  'http://www.ravetapepacks.com/music/' + url, 'listitem': listitem}, {'title':  name.strip()}, img = 'http://fc09.deviantart.net/fs25/f/2008/111/a/8/Cassette_tape_by_Quick_Stop.png', fanart = 'http://24.media.tumblr.com/tumblr_md33y3uDzM1qkcj9ro4_1280.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#------------------------------------------------------------------------ deepinsidetheoldskool -------------------------------------------------------------------------------------#

def GetLinks4(url):                                          
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile("<a dir='ltr' href='(.+?)'>(.+?)</a>").findall(content)
        for url, name in match:
                addon.add_directory({'mode': 'GetLinks4a', 'url': url, 'listitem': listitem}, {'title':  name.strip()}, img = 'http://www.djsoundhire.co.uk/stock-photos/22-1289478980.jpg', fanart = 'https://phaven-prod.s3.amazonaws.com/files/image_part/asset/376411/zJiIP2IgvAoFrWjDxG6FfyZosnE/medium_abbfabb_03.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetLinks4a(url):                                             
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile("<h3 class='post-title entry-title' itemprop='.+?'>\s*?<a href='(.+?)'>(.+?)</a>").findall(content)
        for url, name in match:
                addon.add_directory({'mode': 'GetLinks4b', 'url':  url, 'listitem': listitem}, {'title':  name.strip()}, img = 'http://www.djsoundhire.co.uk/stock-photos/22-1289478980.jpg', fanart = 'https://phaven-prod.s3.amazonaws.com/files/image_part/asset/376411/zJiIP2IgvAoFrWjDxG6FfyZosnE/medium_abbfabb_03.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetLinks4b(url):                                             
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('<a href="http://deepinside.demodulated.com/(.+?)">.+?</a>').findall(content)
        for url in match:
                addon.add_directory({'mode': 'PlayVideo', 'url':  'http://deepinside.demodulated.com/' + url, 'listitem': listitem},  {'title':  url.replace('%20', ' ').replace('_', ' ')}, img = 'http://www.djsoundhire.co.uk/stock-photos/22-1289478980.jpg', fanart = 'https://phaven-prod.s3.amazonaws.com/files/image_part/asset/376411/zJiIP2IgvAoFrWjDxG6FfyZosnE/medium_abbfabb_03.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#------------------------------------------------------------------------------ ratpack ---------------------------------------------------------------------------------#

def GetLinks6(url):                                            
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('<a href="(.+?)" class="podcast-title header2" target="_blank" title=".+?">(.+?)</a>').findall(content)
        for url, name in match:
                addon.add_directory({'mode': 'GetLinks6a', 'url': url, 'listitem': listitem}, {'title':  name.strip()}, img = 'http://media.ents24network.com/image/000/000/527/942171df2ccf89033bf2454012f1cb47b817fa9d.jpg', fanart = 'http://www.mixmag.net/sites/default/files/u10/sun2.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetLinks6a(url):                                            
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('<a href="(.+?)">Download episode</a>').findall(content)
        for url in match:
                addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title':  url}, img = 'http://media.ents24network.com/image/000/000/527/942171df2ccf89033bf2454012f1cb47b817fa9d.jpg', fanart = 'http://hardcorewillneverdie.com/eswe/pagez/flyerz/helter2.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#--------------------------------------------------------------------------- ukraves -------------------------------------------------------------------------------------#

def GetLinks7(url):                                            
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('<h2><a href="(.+?)" target="new">(.+?)</a></h2>').findall(content)
        for url, name in match:
                addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title':  name.strip()}, img = 'http://image.spreadshirt.com/image-server/v1/compositions/19412958/views/1,width=280,height=280,appearanceId=1.png/ecstasy-pill-dove-generation-t-shirt_design.png', fanart = 'http://i383.photobucket.com/albums/oo273/Senbonzakura_8/takeecstesyyoumaydiebutitllbefunalo.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#----------------------------------------------------------------------------- mikusmusik ----------------------------------------------------------------------------------#

def GetLinks9a(url):                                            
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        CLEAN(html)
        content = html
        match = re.compile("<a dir='ltr' href='(.+?)'>(.+?)</a>").findall(content)
        for url, name in match:
                addon.add_directory({'mode': 'GetLinks9b', 'url': url, 'listitem': listitem}, {'title':  name.strip()}, img = 'http://static.tvtropes.org/pmwiki/pub/images/Pirate_radio_station_5417.jpg', fanart = 'http://s29.postimg.org/xwiy1he6f/fanart.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetLinks9b(url):                                            
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        CLEAN(html)
        content = html
        match = re.compile("<h3 class='post-title entry-title' itemprop='name'>\s*?<a href='(.+?)'>(.+?)</a>").findall(content)
        for url, name in match:
                addon.add_directory({'mode': 'GetLinks9c', 'url': url, 'listitem': listitem}, {'title':  name.strip()}, img = 'http://static.tvtropes.org/pmwiki/pub/images/Pirate_radio_station_5417.jpg', fanart = 'http://s29.postimg.org/xwiy1he6f/fanart.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetLinks9c(url):                                            
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        CLEAN(html)
        content = html
        match = re.compile('<a href="http://www.terraincognita.co.uk/(.+?)"').findall(content)
        for url in match:
                addon.add_directory({'mode': 'PlayVideo', 'url': 'http://www.terraincognita.co.uk/' + url, 'listitem': listitem}, {'title':  url.replace('%20', ' ').replace('_', ' ').replace('musik/', '').replace('pirate radio/', '')}, img = 'http://static.tvtropes.org/pmwiki/pub/images/Pirate_radio_station_5417.jpg', fanart = 'http://s29.postimg.org/xwiy1he6f/fanart.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#------------------------------------------------------------------------------ drumandbass --------------------------------------------------------------------------------#

def GetLinks10(url):                                           
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        CLEAN(html)
        content = html
        match = re.compile('<a href="(.+?)" target="_blank">(.+?)</a><br />').findall(content)
        for url, name in match:
                addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title':  name.strip()}, img = 'http://whatishousemusic.co.uk/wp-content/uploads/2013/10/History_of_house.jpg', fanart = 'http://www.mixmag.net/sites/default/files/imagecache/article/images/Foot_shuffling.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#--------------------------------------------------------------------------------- demodulated -----------------------------------------------------------------------------#

def GetLinks11(url):                                            
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        CLEAN(html)
        content = html
        match = re.compile('<li class=".+?"><a href="(.+?)" title=".+?">(.+?)</a>').findall(content)
        for url, name in match:
                addon.add_directory({'mode': 'GetLinks11a', 'url': url, 'listitem': listitem}, {'title':  name.strip()}, img = 'http://urbanlegendkampala.com/wp-content/uploads/2013/11/Mixtape-Image.jpg', fanart = 'https://chronicle-vitae-production.s3.amazonaws.com/uploads/user_article/photo/133/full_11112013-mixtapes.gif')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetLinks11a(url):                                            
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        CLEAN(html)
        content = html
        match = re.compile('<h2><a href="(.+?)" rel="bookmark" title=".+?">(.+?)</a></h2>').findall(content)
        for url, name in match:
                addon.add_directory({'mode': 'GetLinks11b', 'url': url, 'listitem': listitem}, {'title':  name.strip()}, img = 'http://urbanlegendkampala.com/wp-content/uploads/2013/11/Mixtape-Image.jpg', fanart = 'http://img.wallpaperstock.net:81/vintage-cassette-retro-player-wallpapers_36465_1920x1080.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetLinks11b(url):                                          
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        CLEAN(html)
        content = html
        match = re.compile('href="http://www.demodulated.com/music/mixsets/(.+?)">.+?</a></strong>').findall(content)
        for url in match:
                addon.add_directory({'mode': 'PlayVideo', 'url': 'http://www.demodulated.com/music/mixsets/' + url, 'listitem': listitem}, {'title':  url}, img = 'http://urbanlegendkampala.com/wp-content/uploads/2013/11/Mixtape-Image.jpg', fanart = 'http://img.wallpaperstock.net:81/vintage-cassette-retro-player-wallpapers_36465_1920x1080.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#------------------------------------------------------------------------------- shitmixtapes ---------------------------------------------------------------------------------------#

def GetLinks12(url):                                            
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        CLEAN(html)
        content = html
        match = re.compile('<li><a href="(.+?)">(.+?)</a></li>').findall(content)
        for url, name in match:
                addon.add_directory({'mode': 'GetLinks12a', 'url': 'http://www.shitmixtapes.com/' + url, 'listitem': listitem}, {'title':  name.strip()}, img = 'http://www.shitmixtapes.com/storage/shitmixtapes1024x600_netbook.jpg?__SQUARESPACE_CACHEVERSION=1310509037820', fanart = 'http://www.keepingtheravealive.com/images/KEEPING-THE-RAVE-ALIVE_01.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetLinks12a(url):                                            
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        CLEAN(html)
        content = html
        match = re.compile('<a href="(.+?)" target="_blank">(.+?)</a></strong></p>').findall(content)
        match1 = re.compile('<p style="text-align: center;"><a href="(.+?)" target="_blank"><strong>(.+?)</strong></a').findall(content)
        for url, name in match + match1:
                addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title':  name.strip()}, img = 'http://www.shitmixtapes.com/storage/shitmixtapes1024x600_netbook.jpg?__SQUARESPACE_CACHEVERSION=1310509037820', fanart = 'http://www.keepingtheravealive.com/images/KEEPING-THE-RAVE-ALIVE_01.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#------------------------------------------------------------------------- rave-archive ---------------------------------------------------------------------------------#

def GetLinks13(url):                                            
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        CLEAN(html)
        content = html
        match = re.compile("<a href='(.+?)' class='.+?' title='.+?' style='.+?'>(.+?)</a>").findall(content)
        for url, name in match:
                addon.add_directory({'mode': 'GetLinks13a', 'url': url, 'listitem': listitem}, {'title':  name.strip()}, img = 'https://pbs.twimg.com/profile_images/3335360596/3d9ebe5623ae5be2bab14a54625a2537.jpeg', fanart = 'http://junglejunglesound.files.wordpress.com/2013/04/jungle_logo_net.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetLinks13a(url):                                            
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        CLEAN(html)
        content = html
        match = re.compile('<a href="(.+?)" rel="bookmark" title="(.+?)" class="img-bevel video">\s*?<img width="200" height="200" src="(.+?)" class="attachment-article-thumb wp-post-image"').findall(content)
        for url, name, img in match:
                addon.add_directory({'mode': 'GetLinks13b', 'url': url, 'listitem': listitem}, {'title':  name.strip()}, img =img, fanart = 'http://wallpapersus.com/wp-content/uploads/2012/02/music-animals-audio-jungle.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetLinks13b(url):                                           
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        CLEAN(html)
        content = html
        match = re.compile('<a href="http://ravearchive.mediafire.com/file/(.+?)" target="_blank">.+?</a>').findall(content)
        match2 = re.compile('<p style="text-align: center;"><a href="http://ravearchive.mediafire.com/listen/(.+?)" target="_blank">.+?</a></p>').findall(content)
        match3 = re.compile('<a href="http://ravearchive.mediafire.com/file/(.+?)">.+?</a>').findall(content)
        match4 = re.compile('<iframe class=".+?" style=".+?" src="(.+?)"></iframe>').findall(content)
        for url in match:
                addon.add_directory({'mode': 'PlayVideo', 'url': 'http://ravearchive.mediafire.com/file/' + url, 'listitem': listitem}, {'title':  url.replace('_', ' ').replace('/', ' ').replace('%26', ' ')}, img = 'https://pbs.twimg.com/profile_images/3335360596/3d9ebe5623ae5be2bab14a54625a2537.jpeg', fanart = 'http://aerosoul.co.uk/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/j/u/junglist_logo_on_dark_navy_jm_hoodie.png')
        for url in match2:
                addon.add_directory({'mode': 'GetLinks13c', 'url': 'http://ravearchive.mediafire.com/listen/' + url, 'listitem': listitem}, {'title':  url.replace('_', ' ').replace('/', ' ').replace('%26', ' ')}, img = 'https://pbs.twimg.com/profile_images/3335360596/3d9ebe5623ae5be2bab14a54625a2537.jpeg', fanart = 'http://aerosoul.co.uk/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/j/u/junglist_logo_on_dark_navy_jm_hoodie.png')
        for url in match3:
                addon.add_directory({'mode': 'PlayVideo', 'url': 'http://ravearchive.mediafire.com/file/' + url, 'listitem': listitem}, {'title':  url.replace('_', ' ').replace('/', ' ').replace('%26', ' ')}, img = 'https://pbs.twimg.com/profile_images/3335360596/3d9ebe5623ae5be2bab14a54625a2537.jpeg', fanart = 'http://aerosoul.co.uk/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/j/u/junglist_logo_on_dark_navy_jm_hoodie.png')
        for url in match4:
                addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title': 'video links not supported'}, img = 'https://pbs.twimg.com/profile_images/3335360596/3d9ebe5623ae5be2bab14a54625a2537.jpeg', fanart = 'http://aerosoul.co.uk/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/j/u/junglist_logo_on_dark_navy_jm_hoodie.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetLinks13c(url):                                            
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        CLEAN(html)
        content = html
        match = re.compile('id="audioControlGroup">   <a href="(.+?)" target="_blank"><div').findall(content)
        for url in match:
                addon.add_directory({'mode': 'PlayVideo', 'url': 'https://www.mediafire.com/' + url, 'listitem': listitem}, {'title':  '[COLOR blue][B]LOAD STREAM[/B][/COLOR] ' + url}, img = 'https://pbs.twimg.com/profile_images/3335360596/3d9ebe5623ae5be2bab14a54625a2537.jpeg', fanart = 'http://junglejunglesound.files.wordpress.com/2013/04/jungle_logo_net.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#------------------------------------------------------------------------------- the beat sanctuary -------------------------------------------------------------------------------------#

def GetLinks5(url):                                            
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('class="level2 item4 first"><a href="(.+?)" class="level2 item4 first"><span>(Frog and Nightgown)</span>').findall(content)
        match1 = re.compile('class="level2 item5"><a href="(.+?)" class="level2 item5"><span>(The Gass Club)</span>').findall(content)
        match2 = re.compile('class="level2 item7"><a href="(.+?)" class="level2 item7"><span>(MOS Demo Tapes)</span>').findall(content)
        match4 = re.compile('class="level3 item2"><a href="(.+?)" class="level3 item2"><span>(Risk FM)</span>').findall(content)
        match5 = re.compile('class="level3 item3"><a href="(.+?)" class="level3 item3"><span>(Pleasure FM)</span').findall(content)
        match6 = re.compile('class="level3 item4"><a href="(.+?)" class="level3 item4"><span>(Friction FM)</span>').findall(content)
        match7 = re.compile('class="level3 item5 last"><a href="(.+?)" class="level3 item5 last"><span>(Soundz FM)</span>').findall(content)
        for url, name in match + match1 + match2 + match4 + match5 + match6 + match7:
                addon.add_directory({'mode': 'GetLinks5a', 'url': 'http://www.thebeatsanctuary.co.uk/' + url, 'listitem': listitem}, {'title':  name.strip()}, img = 'http://i2.wp.com/musicyouneed.net/wp-content/uploads/2013/03/MYN-The-Underground.jpg?resize=290%2C290', fanart = 'https://googledrive.com/host/0B99lcOwdwe5MUDRsdkgyWS1Kems/dj-bass-music-wallpaper.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetLinks5a(url):                                            
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('<a target=".+?" href="https://dl.dropboxusercontent.com/u/(.+?)">').findall(content)
        for url in match:
                addon.add_directory({'mode': 'PlayVideo', 'url': 'https://dl.dropboxusercontent.com/u/' + url, 'listitem': listitem}, {'title':  url}, img = 'http://i2.wp.com/musicyouneed.net/wp-content/uploads/2013/03/MYN-The-Underground.jpg?resize=290%2C290', fanart = 'https://lh6.ggpht.com/clu-N-hZ_xyCgGm5JwtVLRXX59eSMfl59RXf9MQd23lZVvQgoa2aQNdGHU-eEfaYZMeO=h900')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#------------------------------------------------------------------------------- thewire -------------------------------------------------------------------------------------#

def GetLinks14(url):                                            
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        CLEAN(html)
        content = html
        match = re.compile('<a href=".+?" data-file="(.+?)" class=".+?" title=".+?" rel="nofollow">(.+?)</a>').findall(content)
        for url, name in match:
                addon.add_directory({'mode': 'PlayVideo', 'url': 'http://www.thewire.co.uk/' + url, 'listitem': listitem}, {'title':  name.strip()}, img = 'http://www.hcmf.co.uk/uploads/images/197wirelogoblockurlcopy.jpg?1253097636', fanart = 'http://alicepettey.com/wp-content/uploads/2012/03/The_Wire_Logo.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#------------------------------------------------------------------------------- github -------------------------------------------------------------------------------------#

def GetLinks15(url):                                            
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        CLEAN(html)
        content = html
        match = re.compile('<>title="(.+?)" href="(.+?)" />< src="(.+?)"').findall(content)
        for name, url, img in match:
                addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title':  name.strip()}, img=img , fanart = 'http://i1.sndcdn.com/artworks-000047576476-bckt74-original.jpg?77d7a69')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetLinks16(url):                                            
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        CLEAN(html)
        content = html
        match = re.compile('<>title="(.+?)" href="(.+?)" /><').findall(content)
        for name, url in match:
                addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title':  name.strip()}, img = 'http://hackneyhistory.files.wordpress.com/2013/01/piratees.jpg' , fanart = 'http://s29.postimg.org/ipshtqvx3/fanart.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#------------------------------------------------------------------------------- ltj Bukem Mixtapes Collection -------------------------------------------------------------------------------------#

def GetLinks17(url):                                            
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        CLEAN(html)
        content = html
        match = re.compile('<a href="/download/175bpm.plLtjBukemMixtapesCollection/(.+?)mp3">').findall(content)
        for url in match:
                addon.add_directory({'mode': 'PlayVideo', 'url': 'https://archive.org/download/175bpm.plLtjBukemMixtapesCollection/' + url + 'mp3', 'listitem': listitem}, {'title':  url}, img = 'http://www.djsets.co.uk/Compilations/ltjbukem/ltj-bukem.jpg', fanart = 'http://musicwithsubstance.files.wordpress.com/2009/12/goodlooking.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#a------------------------------------------------------------------------------- Helter Skelter Collection -----######

def GetLinks17a(url):                                            
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        CLEAN(html)
        content = html
        match = re.compile('<a href="/download/175bpm.pl-HelterSkelterCollection/(.+?)mp3">').findall(content)
        for url in match:
                addon.add_directory({'mode': 'PlayVideo', 'url': 'https://archive.org/download/175bpm.pl-HelterSkelterCollection/' + url + 'mp3', 'listitem': listitem}, {'title':  url.replace('_', ' ')}, img = 'http://www.djsets.co.uk/Compilations/helterskelter/hs3.jpg', fanart = 'http://www.oldskoolanthemz.com/forum/attachments/file-sharing/27640d1224888916-dj-warlock-helter-skelter-zoom-9-12-95-untitled.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#------------------------------------------------------------------------------- toronto rave mixtape archive -------------------------------------------------------------------------------------#

def GetLinks18(url):                                            
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        CLEAN(html)
        content = html
        match = re.compile('<li><a href="(.+?)"><span>(Jungle / Hardcore)</span></a></li>').findall(content)
        match1 = re.compile('<li><a href="(.+?)"><span>(House / Techno)</span></a></li>').findall(content)
        match2 = re.compile('<li><a href="(.+?)"><span>(Studio)</span></a></li>').findall(content)
        match3 = re.compile('<li><a href="(.+?)"><span>(X-Static)</span></a></li>').findall(content)
        for url, name in match + match1 + match2 + match3:
                addon.add_directory({'mode': 'GetLinks18a', 'url': 'http://torontoravemixtapearchive.com/' + url, 'listitem': listitem}, {'title':  name.strip()}, img = 'http://www.torontoravemixtapearchive.com/images/promo/trma.jpg', fanart = 'http://dropthebeatz.com/wp-content/uploads/2013/08/EDMcrowd.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetLinks18a(url):                                            
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        CLEAN(html)
        content = html
        match = re.compile('>.+?<a href="http://www.torontoravemixtapearchive.com/files/(.+?)">').findall(content)
        match1 = re.compile('>.+?-.+?- <a href="http://www.torontoravemixtapearchive.com/files/(.+?)">').findall(content)
        match2 = re.compile('>Download </a><br />\s*?<a href="http://www.torontoravemixtapearchive.com/files/(.+?)">').findall(content)
        match4 = re.compile('N.+?<a href="http://www.torontoravemixtapearchive.com/files/(.+?)">').findall(content)
        match3 = re.compile('Andy.+?<a href="http://www.torontoravemixtapearchive.com/files/(.+?)">').findall(content)
        match5 = re.compile('k.+?<a href="http://www.torontoravemixtapearchive.com/files/(.+?)">').findall(content)
        match6 = re.compile(' 1.+?<a href="http://www.torontoravemixtapearchive.com/files/(.+?)">').findall(content)
        for url in match + match1 + match2 + match3 + match4 + match5 + match6:
                url = url.replace(' ','%20')
                url = url.replace('_','%20')
                addon.add_directory({'mode': 'PlayVideo', 'url': 'http://www.torontoravemixtapearchive.com/files/' + url, 'listitem': listitem}, {'title': url.replace('%20', ' ').replace('mixtapes/', ' ').replace('%', ' ').replace('x-static/', ' ')}, img = 'http://www.torontoravemixtapearchive.com/images/promo/trma.jpg', fanart = 'http://b.vimeocdn.com/ts/437/750/437750726_1280.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#------------------------------------------------------------------------------- jungletechno -------------------------------------------------------------------------------------#

def GetLinks19(url):                                            
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        CLEAN(html)
        content = html
        match = re.compile('<p>(.+?)<a href="(.+?)" target="_blank">.+?</a>.+?</p>').findall(content)
        for name, url in match:
                addon.add_directory({'mode': 'GetLinks19a', 'url': url, 'listitem': listitem}, {'title':  name.strip().replace('_', ' ')}, img = 'https://pbs.twimg.com/profile_images/1430963248/Hardcore_Jungle_Techno_-_001.jpg', fanart = 'http://images4.alphacoders.com/133/133336.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetLinks19a(url):                                            
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        CLEAN(html)
        content = html
        match = re.compile('kNO = "http://download(.+?)"').findall(content)
        for url in match:
                addon.add_directory({'mode': 'PlayVideo', 'url': 'http://download' + url, 'listitem': listitem}, {'title':  url.replace('_', ' ')}, img = 'https://pbs.twimg.com/profile_images/1430963248/Hardcore_Jungle_Techno_-_001.jpg', fanart = 'http://i1.ytimg.com/vi/Busq9tROYlo/maxresdefault.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#------------------------------------------------------------------------------- dj jedi -------------------------------------------------------------------------------------#

def GetLinks20(url):                                            
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        CLEAN(html)
        content = html
        match = re.compile('<p><a href="(.+?)" onClick=".+?"><strong>(.+?)</strong></a></p>').findall(content)
        for url, name in match:
                addon.add_directory({'mode': 'PlayVideo', 'url': 'http://www.dj-jedi.com/' + url, 'listitem': listitem}, {'title':  name.strip()}, img = 'http://www.dj-jedi.com/images/dj_jedi_logo.gif', fanart = 'http://andberlin.com/wp-content/uploads/2013/05/Lights-at-Berlin-Summer-Rave-2013.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))


#------------------------------------------------------------------------------- 180 -------------------------------------------------------------------------------------#

def GetLinks21(url):                                            
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        CLEAN(html)
        content = html
        match = re.compile('<li id=".+?" class=".+?"><a href="(.+?)">(.+?)</a></li>').findall(content)
        for url, name in match:
                addon.add_directory({'mode': 'GetLinks21a', 'url': url, 'listitem': listitem}, {'title':  name.strip()}, img = 'http://i1.sndcdn.com/artworks-000040491089-ibo2zb-crop.jpg?164b459', fanart = 'http://i1.ytimg.com/vi/eY2ceXfW1FU/maxresdefault.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetLinks21a(url):                                            
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        CLEAN(html)
        content = html
        match = re.compile('<h2 class="entry-title"><a href="(.+?)" title=".+?" rel="bookmark">(.+?)</a></h2>').findall(content)
        for url, name in match:
                addon.add_directory({'mode': 'GetLinks21b', 'url': url, 'listitem': listitem}, {'title':  name.strip()}, img = 'http://i1.sndcdn.com/artworks-000040491089-ibo2zb-crop.jpg?164b459', fanart = 'http://i1.ytimg.com/vi/eY2ceXfW1FU/maxresdefault.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetLinks21b(url):                                            
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        CLEAN(html)
        content = html
        match = re.compile('ref="(.+?)">(.+?)</a></strong>').findall(content)
        for url, name in match:
                addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title':  name.strip()}, img = 'http://i1.sndcdn.com/artworks-000040491089-ibo2zb-crop.jpg?164b459', fanart = 'http://i1.ytimg.com/vi/eY2ceXfW1FU/maxresdefault.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

######################################################################### clean ###########################################################################################

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

############################################################################# Play Video #####################################################################################

def PlayVideo(url, listitem):
        addon_handle = int(sys.argv[1])
        xbmcplugin.setContent(addon_handle, 'audio')
        li = xbmcgui.ListItem('[COLOR dodgerblue][B]PLAY STREAM[/B][/COLOR]  [COLOR lime][B] >>[/B][/COLOR] >> ', iconImage='http://www.sayerhamilton.com/resources/images/hear/tape.png', thumbnailImage= 'http://www.sayerhamilton.com/resources/images/hear/tape.png')
        li.setProperty('fanart_image', 'http://www.papermashmusic.com/filess/Feb/5/rave-babie-blue-lights.jpg')
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
        url = 'http://192.99.11.97:8000'
        li = xbmcgui.ListItem('[COLOR blue][B]Rave Tape Radio[/B][/COLOR] [COLOR lime] (((LIVE))) [/COLOR] >>', thumbnailImage= 'http://d1i6vahw24eb07.cloudfront.net/s182965d.png')
        li.setProperty('fanart_image', 'http://s12.postimg.org/rkd8gen7h/fanart.jpg')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

        xbmcplugin.setContent(addon_handle, 'audio')
        url = 'http://www.livegigstream.co.uk:8040/'
        li = xbmcgui.ListItem('[COLOR dodgerblue][B]Oldskool Anthemz Radio[/B][/COLOR] [COLOR lime](((Live)))[/COLOR] >>', thumbnailImage= 'http://www.oldskoolanthemz.com/images/cms/osafacebookconnect.jpg')
        li.setProperty('fanart_image', 'http://s12.postimg.org/rkd8gen7h/fanart.jpg')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

        xbmcplugin.setContent(addon_handle, 'audio')
        url = 'http://178.33.237.151:8004'
        li = xbmcgui.ListItem('[COLOR dodgerblue][B]Only Oldskool Radio[/B][/COLOR] [COLOR lime](((Live)))[/COLOR] >>', thumbnailImage= 'http://i1.sndcdn.com/artworks-000074359327-1jmjy6-original.jpg?435a760')
        li.setProperty('fanart_image', 'http://s12.postimg.org/rkd8gen7h/fanart.jpg')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

        addon.add_directory({'mode': 'GetLinks15', 'url': BASE_URL15 + '/dnb.txt'}, {'title':  '[COLOR gold][B]Rave player Specials [/COLOR] (Rave Dj Sets)[/B]'}, img = 'http://s28.postimg.org/uwfyuzepp/cassettetdk.jpg', fanart = 'http://amgroup.com/news/wp-content/uploads/2013/04/IMG_4470-Custom.jpg')
        addon.add_directory({'mode': 'GetLinks16', 'url': BASE_URL15 + '/radioshows.txt'}, {'title':  '[COLOR gold][B]Rave player Specials [/COLOR] (the lost tapes)[/B]'}, img = 'http://s12.postimg.org/3szbuobot/icon.png', fanart = 'http://4.bp.blogspot.com/_8V97VYqI3Po/S7Md-Sd5OcI/AAAAAAAABGk/haepgezjFqw/s1600/24897_410278471302_133985331302_5619646_2569052_n.jpg')
        addon.add_directory({'mode': 'GetLinks', 'url': BASE_URL + '/'}, {'title':  '[COLOR green][B]One In The Jungle [/COLOR](Archive)[/B]'}, img = 'http://www.oneinthejungle.net/images/home/fb.png', fanart = 'http://img193.imageshack.us/img193/4990/dsc09956tx.jpg')
        addon.add_directory({'mode': 'GetLinks3', 'url': BASE_URL3 + '/'}, {'title':  '[COLOR green][B]Rave tape packs [/COLOR](Archive)[/B]'}, img = 'http://fc09.deviantart.net/fs25/f/2008/111/a/8/Cassette_tape_by_Quick_Stop.png', fanart = 'http://s27.postimg.org/3qdp1snnn/hhhgggg.jpg')
        addon.add_directory({'mode': 'GetLinks4', 'url': BASE_URL4 + '/'}, {'title':  '[COLOR green][B]Deepinside the oldskool [/COLOR](Archive)[/B]'}, img = 'http://www.djsoundhire.co.uk/stock-photos/22-1289478980.jpg', fanart = 'https://phaven-prod.s3.amazonaws.com/files/image_part/asset/376411/zJiIP2IgvAoFrWjDxG6FfyZosnE/medium_abbfabb_03.jpg')
        addon.add_directory({'mode': 'GetLinks13', 'url': BASE_URL13 + '/'}, {'title':  '[COLOR green][B]Rave-archive [/COLOR](Archive)[/B]'}, img = 'https://pbs.twimg.com/profile_images/3335360596/3d9ebe5623ae5be2bab14a54625a2537.jpeg', fanart = 'http://s11.postimg.org/vhd2897k3/fanart.jpg')
        addon.add_directory({'mode': 'GetLinks18', 'url': BASE_URL18 + '/'}, {'title':  '[COLOR green][B]Toronto rave mixtape [/COLOR](Archive)[/B]   [COLOR red] *[/COLOR]'}, img = 'http://www.torontoravemixtapearchive.com/images/promo/trma.jpg', fanart = 'http://torontoravemixtapearchive.com/images/promo/DavidRyanTapes.jpg')
        addon.add_directory({'mode': 'GetLinks19', 'url': BASE_URL19 + ''}, {'title':  '[COLOR green][B]jungletechno [/COLOR](Archive)[/B][COLOR red]   *[/COLOR]'}, img = 'https://pbs.twimg.com/profile_images/1430963248/Hardcore_Jungle_Techno_-_001.jpg', fanart = 'http://thebowlerfirm.com/wp-content/uploads/2012/05/stevie.jpg')
        addon.add_directory({'mode': 'GetLinks2', 'url': BASE_URL2 + '/soundmanager2/demo/page-player/20bensons.html'}, {'title':  '[COLOR green][B]20bensons rave [/COLOR](Archive)[/B]'}, img = 'http://www.zigsam.at/l07/B_Cig/BensonHedgesSpeciaF-20fJP197.jpg', fanart = 'http://bigghostlimited.com/wp-content/uploads/2013/09/MIxtape.gif')
        addon.add_directory({'mode': 'GetLinks7', 'url': BASE_URL7 + '/category_Event_Mixes_1.htm'}, {'title':  '[COLOR green][B]UK raves [/COLOR](Archive)[/B]'}, img = 'https://pbs.twimg.com/profile_images/3337802286/571a3ecdec1efb53e30cf19c00f45212.jpeg', fanart = 'http://www.fantazia.org.uk/Event%20info/Pics/11fantaziasummertime.jpg')
        addon.add_directory({'mode': 'GetLinks11', 'url': BASE_URL11 + '/'}, {'title':  '[COLOR green][B]Demodulated mixtapes [/COLOR](Archive)[/B]'}, img = 'http://urbanlegendkampala.com/wp-content/uploads/2013/11/Mixtape-Image.jpg', fanart = 'http://bigghostlimited.com/wp-content/uploads/2013/09/MIxtape.gif')
        addon.add_directory({'mode': 'GetLinks9a', 'url': BASE_URL9 + '/'}, {'title':  '[COLOR green][B]mikus Musik [/COLOR](Archive)[/B]'}, img = 'http://3.bp.blogspot.com/-iDTTgsZBiBA/TwHRQBfrEKI/AAAAAAAAATs/8lTy5Va4_is/s1600/MIKUS.gif', fanart = 'http://s23.postimg.org/4sn8qcp8b/fanart.jpg')
        addon.add_directory({'mode': 'GetLinks12', 'url': BASE_URL12 + '/'}, {'title':  '[COLOR green][B]Shitmixtapes [/COLOR](Archive)[/B]'}, img = 'http://www.shitmixtapes.com/storage/shitmixtapes-white.jpg?__SQUARESPACE_CACHEVERSION=1310920306487', fanart = 'http://farm3.staticflickr.com/2814/11285947406_690a1a7a92_z.jpg')
        addon.add_directory({'mode': 'GetLinks21', 'url': BASE_URL21 + '/'}, {'title':  '[COLOR green][B]175BPM [/COLOR] (Archive)[/B]   [COLOR red] *[/COLOR]'}, img = 'http://i1.sndcdn.com/artworks-000040491089-ibo2zb-crop.jpg?164b459', fanart = 'http://i1.ytimg.com/vi/eY2ceXfW1FU/maxresdefault.jpg')
        addon.add_directory({'mode': 'GetLinks17', 'url': BASE_URL17 + '/details/175bpm.plLtjBukemMixtapesCollection'}, {'title':  '[COLOR mediumseagreen][B]L T J Bukem [/COLOR](Mixtapes Collection)[/B]'}, img = 'http://i1.wp.com/www.mostlyjunkfood.com/treats/2013/05/image002.jpg', fanart = 'http://www.htbackdrops.org/v2/albums/userpics/10257/orig_LTJ_Bukem.jpg')
        addon.add_directory({'mode': 'GetLinks17a', 'url': BASE_URL17 + '/details/175bpm.pl-HelterSkelterCollection'}, {'title':  '[COLOR mediumseagreen][B]Helter Skelter [/COLOR] (Mixtapes Collection)[/B]'}, img = 'http://rave.space.net.au/graphics/hskelter.jpg', fanart = 'http://www.fantazia.org.uk/flyerlibrary/images/HelterSkelter_170993_f.jpg')
        addon.add_directory({'mode': 'GetLinks20', 'url': BASE_URL20 + 'dj_jedi_audio.php'}, {'title':  '[COLOR mediumseagreen][B]Dj jedi [/COLOR](Mixtapes Collection)[/B]'}, img = 'http://www.dj-jedi.com/images/dj_jedi_logo.gif', fanart = 'http://archive-media.nyafuu.org/wg/image/1367/08/1367087842578.png')
        addon.add_directory({'mode': 'GetLinks6', 'url': BASE_URL6 + '/'}, {'title':  '[COLOR chartreuse][B]RatPack [/COLOR](Podcasts)[/B]'}, img = 'http://strictlyoldskool.net/wp-content/gallery/ratpack/ratpack-pic-1.jpg', fanart = 'http://static.inlog.org/wp-content/uploads/2013/04/front-590x390.jpg')
        addon.add_directory({'mode': 'GetLinks10', 'url': BASE_URL10 + '/showthread.php?3752-mal-was-anderes-oldskool-history-of-edm-mix'}, {'title':  '[COLOR chartreuse][B]In the beginning there was Jack[/COLOR] (podcast)[/B]'}, img = 'http://sd.keepcalm-o-matic.co.uk/i/in-the-beginning-there-was-jack-9.png', fanart = 'http://galiofficial.com/wp-content/uploads/2013/03/house-music-design-nation.jpg')
        addon.add_directory({'mode': 'GetLinks5', 'url': BASE_URL5 + '/'}, {'title':  '[COLOR turquoise][B]The beat sanctuary [/COLOR] (oldskool H&G)[/B]'}, img = 'http://i2.wp.com/musicyouneed.net/wp-content/uploads/2013/03/MYN-The-Underground.jpg?resize=290%2C290', fanart = 'http://www.crownbc.com/wp-content/uploads/2013/06/Bunker-Rave.jpg')
        addon.add_directory({'mode': 'GetLinks14', 'url': BASE_URL14 + 'audio/tracks/a-brief-history-of-grime-tapes'}, {'title':  '[COLOR turquoise][B]The wire [/COLOR] (oldskool H&G)[/B]'}, img = 'http://www.hcmf.co.uk/uploads/images/197wirelogoblockurlcopy.jpg?1253097636', fanart = 'http://alicepettey.com/wp-content/uploads/2012/03/The_Wire_Logo.jpg')
        #addon.add_directory({'mode': 'GetLinks', 'url': BASE_URL + ''}, {'title':  '[COLOR mediumseagreen][B] [/COLOR] ()[/B]'}, img = '', fanart = '')
        xbmcplugin.endOfDirectory(addon_handle)

################################################################################# mode #########################################################################################

if mode == 'main': 
	MainMenu()
elif mode == 'GetLinks':
	GetLinks(url)
elif mode == 'GetLinks2':
	GetLinks2(url)
elif mode == 'GetLinks3':
	GetLinks3(url)
elif mode == 'GetLinks3a':
	GetLinks3a(url)
elif mode == 'GetLinks3b':
	GetLinks3b(url)
elif mode == 'GetLinks4':
	GetLinks4(url)
elif mode == 'GetLinks4a':
	GetLinks4a(url)
elif mode == 'GetLinks4b':
	GetLinks4b(url)
elif mode == 'GetLinks5':
	GetLinks5(url)
elif mode == 'GetLinks5a':
	GetLinks5a(url)
elif mode == 'GetLinks6':
	GetLinks6(url)
elif mode == 'GetLinks6a':
	GetLinks6a(url)
elif mode == 'GetLinks7':
	GetLinks7(url)
elif mode == 'GetLinks7a':
	GetLinks7a(url)
elif mode == 'GetLinks9a':
	GetLinks9a(url)
elif mode == 'GetLinks9b':
	GetLinks9b(url)
elif mode == 'GetLinks9c':
	GetLinks9c(url)
elif mode == 'GetLinks10':
	GetLinks10(url)
elif mode == 'GetLinks11':
	GetLinks11(url)
elif mode == 'GetLinks11a':
	GetLinks11a(url)
elif mode == 'GetLinks11b':
	GetLinks11b(url)
elif mode == 'GetLinks12':
	GetLinks12(url)
elif mode == 'GetLinks12a':
	GetLinks12a(url)
elif mode == 'GetLinks13':
	GetLinks13(url)
elif mode == 'GetLinks13a':
	GetLinks13a(url)
elif mode == 'GetLinks13b':
	GetLinks13b(url)
elif mode == 'GetLinks13c':
	GetLinks13c(url)
elif mode == 'GetLinks14':
	GetLinks14(url)
elif mode == 'GetLinks15':
	GetLinks15(url)
elif mode == 'GetLinks16':
	GetLinks16(url)
elif mode == 'GetLinks17':
	GetLinks17(url)
elif mode == 'GetLinks17a':
	GetLinks17a(url)
elif mode == 'GetLinks18':
	GetLinks18(url)
elif mode == 'GetLinks18a':
	GetLinks18a(url)
elif mode == 'GetLinks19':
	GetLinks19(url)
elif mode == 'GetLinks19a':
	GetLinks19a(url)
elif mode == 'GetLinks20':
	GetLinks20(url)
elif mode == 'GetLinks21':
	GetLinks21(url)
elif mode == 'GetLinks21a':
	GetLinks21a(url)
elif mode == 'GetLinks21b':
	GetLinks21b(url)
elif mode == 'PlayVideo':
	PlayVideo(url, listitem)