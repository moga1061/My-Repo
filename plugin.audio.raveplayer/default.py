import xbmc, xbmcgui, xbmcaddon, xbmcplugin
import urllib, urllib2
import re, string, sys, os
import urlresolver
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
BASE_URL5 = 'http://www.rave-archive.com/'
BASE_URL6 = 'http://ratpack.podomatic.com/'

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

def GetLinks(url):                                             #oneinthejungle
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('<td><a href="(.+?)">(.+?)</a></td>').findall(content)
        listitem = GetMediaInfo(content)
        for url, name in match:
                addon.add_directory({'mode': 'PlayVideo', 'url': 'http://www.oneinthejungle.co.uk/' + url, 'listitem': listitem}, {'title':  name.strip()}, img = 'http://www.oneinthejungle.net/images/home/fb.png', fanart = 'http://www.allcrew.co.uk/pages/cartgifs/party.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def GetLinks2(url):                                            #20bensons
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('href="(.+?)">(.+?)</a>').findall(content)
        listitem = GetMediaInfo(content)
        for url, name in match:
                addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title':  name.strip()}, img = 'http://www.zigsam.at/l07/B_Cig/BensonHedgesSpeciaF-20fJP197.jpg', fanart = 'http://cs11180.vk.me/u19162043/47140284/x_977c8c97.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


def GetLinks3(url):                                             #ravetapepacks1
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('<li class=".+?"><a href="(.+?)" title=".+?">(.+?)</a>').findall(content)
        listitem = GetMediaInfo(content)
        for url, name in match:
                addon.add_directory({'mode': 'GetLinks3a', 'url': url, 'listitem': listitem}, {'title':  name.strip()}, img = 'http://fc09.deviantart.net/fs25/f/2008/111/a/8/Cassette_tape_by_Quick_Stop.png', fanart = 'http://24.media.tumblr.com/tumblr_md33y3uDzM1qkcj9ro4_1280.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))


def GetLinks3a(url):                                             #ravetapepacks1a
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        CLEAN(html)
        content = html
        match = re.compile('<a href="(.+?)" rel="bookmark">(.+?)</a>').findall(content)
        listitem = GetMediaInfo(content)
        for url, name in match:
                addon.add_directory({'mode': 'GetLinks3b', 'url':  url, 'listitem': listitem}, {'title':  name.strip()}, img = 'http://fc09.deviantart.net/fs25/f/2008/111/a/8/Cassette_tape_by_Quick_Stop.png', fanart = 'http://24.media.tumblr.com/tumblr_md33y3uDzM1qkcj9ro4_1280.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))


def GetLinks3b(url):                                             #ravetapepacks2a
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('<p style="text-align: left;"><a href="(.+?)">(.+?)</a></p>').findall(content)
        listitem = GetMediaInfo(content)
        for url, name in match:
                addon.add_directory({'mode': 'PlayVideo', 'url':  url, 'listitem': listitem}, {'title':  name.strip()}, img = 'http://fc09.deviantart.net/fs25/f/2008/111/a/8/Cassette_tape_by_Quick_Stop.png', fanart = 'http://24.media.tumblr.com/tumblr_md33y3uDzM1qkcj9ro4_1280.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


def GetLinks4(url):                                             #deepinsidetheoldskool1
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile("<a dir='ltr' href='(.+?)'>(.+?)</a>").findall(content)
        listitem = GetMediaInfo(content)
        for url, name in match:
                addon.add_directory({'mode': 'GetLinks4a', 'url': url, 'listitem': listitem}, {'title':  name.strip()}, img = 'http://www.djsoundhire.co.uk/stock-photos/22-1289478980.jpg', fanart = 'https://phaven-prod.s3.amazonaws.com/files/image_part/asset/376411/zJiIP2IgvAoFrWjDxG6FfyZosnE/medium_abbfabb_03.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))


def GetLinks4a(url):                                             #deepinsidetheoldskoola
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile("<a href='(.+?)'>(.+?-)").findall(content)
        listitem = GetMediaInfo(content)
        for url, name in match:
                addon.add_directory({'mode': 'GetLinks4b', 'url':  url, 'listitem': listitem}, {'title':  name.strip()}, img = 'http://www.djsoundhire.co.uk/stock-photos/22-1289478980.jpg', fanart = 'https://phaven-prod.s3.amazonaws.com/files/image_part/asset/376411/zJiIP2IgvAoFrWjDxG6FfyZosnE/medium_abbfabb_03.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))


def GetLinks4b(url):                                             #deepinsidetheoldskoola
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile(' <a href="(.+?)">.+?<').findall(content)
        if not match:
            match = re.compile('<a href="(.+?)">.+?<',re.DOTALL).findall(html)
        listitem = GetMediaInfo(content)
        for url in match:
                addon.add_directory({'mode': 'PlayVideo', 'url':  url, 'listitem': listitem},  {'title':  url}, img = 'http://www.djsoundhire.co.uk/stock-photos/22-1289478980.jpg', fanart = 'https://phaven-prod.s3.amazonaws.com/files/image_part/asset/376411/zJiIP2IgvAoFrWjDxG6FfyZosnE/medium_abbfabb_03.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))


#--------------------------------------------------------------------------------------------------------------------------------------#


def GetTitles(section, url, startPage= '1', numOfPages= '1'):    #rave-archive
        print 'raveplayer get Movie Titles Menu %s' % url
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + 'page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        CLEAN(html)
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + 'page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content
                        CLEAN(html)
                match = re.compile('img-wrapper.+?href="(.+?)" rel="bookmark" title="(.+?)" class="img-bevel video">', re.DOTALL).findall(html)
                for movieUrl, name in match:
                        addon.add_directory({'mode': 'GetLinks5', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img = 'https://pbs.twimg.com/profile_images/3335360596/3d9ebe5623ae5be2bab14a54625a2537.jpeg', fanart = 'http://img820.imageshack.us/img820/3836/flyercollage.jpg')
                #addon.add_directory({'mode': 'GetTitles', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img = 'http://www.cloudforge.com/sites/default/files/codesion/images/com-next.jpg', fanart = 'http://img820.imageshack.us/img820/3836/flyercollage.jpg')
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetLinks5(url):                                             #rave-archive
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        CLEAN(html)
        content = html
        match = re.compile('<a href="(.+?)">Download</a></p>').findall(content)
        listitem = GetMediaInfo(content)
        for url in match:
                addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title':  url}, img = 'https://pbs.twimg.com/profile_images/3335360596/3d9ebe5623ae5be2bab14a54625a2537.jpeg', fanart = 'http://img820.imageshack.us/img820/3836/flyercollage.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def GetLinks6(url):                                            #ratpack
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('<a href="(.+?)" class="podcast-title header2" target="_blank" title=".+?">(.+?)</a>').findall(content)
        listitem = GetMediaInfo(content)
        for url, name in match:
                addon.add_directory({'mode': 'GetLinks6a', 'url': url, 'listitem': listitem}, {'title':  name.strip()}, img = 'http://media.ents24network.com/image/000/000/527/942171df2ccf89033bf2454012f1cb47b817fa9d.jpg', fanart = 'http://www.mixmag.net/sites/default/files/u10/sun2.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetLinks6a(url):                                            #ratpack
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('<a href="(.+?)">Download episode</a>').findall(content)
        listitem = GetMediaInfo(content)
        for url in match:
                addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title':  url}, img = 'http://media.ents24network.com/image/000/000/527/942171df2ccf89033bf2454012f1cb47b817fa9d.jpg', fanart = 'http://hardcorewillneverdie.com/eswe/pagez/flyerz/helter2.jpg')
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
        url = 'http://www.ravetaperadio.com/listen/listen.asx'
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

        addon.add_directory({'mode': 'GetLinks', 'url': BASE_URL + '/'}, {'title':  '[COLOR green][B]One In The Jungle [/COLOR][COLOR palegreen]Archive[/B] [/COLOR]>>'}, img = 'http://www.oneinthejungle.net/images/home/fb.png', fanart = 'http://img193.imageshack.us/img193/4990/dsc09956tx.jpg')
        addon.add_directory({'mode': 'GetLinks3', 'url': BASE_URL3 + '/'}, {'title':  '[COLOR green][B]Rave tape packs [/COLOR][COLOR palegreen]Archive[/B] [/COLOR]>>'}, img = 'http://fc09.deviantart.net/fs25/f/2008/111/a/8/Cassette_tape_by_Quick_Stop.png', fanart = 'http://img200.imageshack.us/img200/9097/dsc007484.jpg')
        addon.add_directory({'mode': 'GetLinks2', 'url': BASE_URL2 + '/soundmanager2/demo/page-player/20bensons.html'}, {'title':  '[COLOR green][B]20bensons rave [/COLOR][COLOR palegreen]Archive[/B] [/COLOR]>>'}, img = 'http://www.zigsam.at/l07/B_Cig/BensonHedgesSpeciaF-20fJP197.jpg', fanart = 'http://torontoravemixtapearchive.com/images/promo/DavidRyanTapes.jpg')
        addon.add_directory({'mode': 'GetLinks4', 'url': BASE_URL4 + '/'}, {'title':  '[COLOR green][B]Oldskool [/COLOR][COLOR palegreen]Archive[/B] [/COLOR]>>'}, img = 'http://www.djsoundhire.co.uk/stock-photos/22-1289478980.jpg', fanart = 'https://phaven-prod.s3.amazonaws.com/files/image_part/asset/376411/zJiIP2IgvAoFrWjDxG6FfyZosnE/medium_abbfabb_03.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL5 + '/desire/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR chartreuse][B]Desire [/COLOR][COLOR palegreen]Archive[/B] [/COLOR]>>'}, img = 'http://i712.photobucket.com/albums/ww126/wigsoldskool/scan0127-1.jpg?t=1253343015', fanart = 'http://img820.imageshack.us/img820/3836/flyercollage.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL5 + '/stevie-hyper-d-sets/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR chartreuse][B]Stevie Hyper D [/COLOR][COLOR palegreen]Archive[/B] [/COLOR]>>'}, img = 'http://i1.ytimg.com/vi/kfHcSw8cw4Y/hqdefault.jpg', fanart = 'http://img820.imageshack.us/img820/3836/flyercollage.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL5 + '/awol/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR chartreuse][B]AWOL [/COLOR][COLOR palegreen]Archive[/B] [/COLOR]>>'}, img = 'http://i1.sndcdn.com/artworks-000021177481-q21i03-crop.jpg?77d7a69', fanart = 'http://img820.imageshack.us/img820/3836/flyercollage.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL5 + '/kool-london/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR chartreuse][B]Kool fm [/COLOR][COLOR palegreen]Archive[/B] [/COLOR]>>'}, img = 'http://i5.photobucket.com/albums/y158/Paul_M_86/98af59b4.jpg', fanart = 'http://img820.imageshack.us/img820/3836/flyercollage.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL5 + '/jungle-fever/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR chartreuse][B]Jungle Fever [/COLOR][COLOR palegreen]Archive[/B] [/COLOR]>>'}, img = 'http://phatmedia.co.uk/media/assets/large/dde6ba0896a9a772805e17098b414f5d657c3b0b.jpg', fanart = 'http://img820.imageshack.us/img820/3836/flyercollage.jpg')
        addon.add_directory({'mode': 'GetLinks6', 'url': BASE_URL6 + '/'}, {'title':  '[COLOR chartreuse][B]RatPack [/COLOR][COLOR mediumseagreen]Podcasts[/B] [/COLOR]>>'}, img = 'http://strictlyoldskool.net/wp-content/gallery/ratpack/ratpack-pic-1.jpg', fanart = 'http://static.inlog.org/wp-content/uploads/2013/04/front-590x390.jpg')
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
elif mode == 'GetTitles': 
	GetTitles(section, url, startPage, numOfPages)
elif mode == 'GetLinks5':
	GetLinks5(url)
elif mode == 'GetLinks6':
	GetLinks6(url)
elif mode == 'GetLinks6a':
	GetLinks6a(url)
elif mode == 'PlayVideo':
	PlayVideo(url, listitem)	