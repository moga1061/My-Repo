import xbmc, xbmcgui, xbmcaddon, xbmcplugin
import urllib, urllib2
import re, string, sys, os
import urlresolver
from TheYid.common.addon import Addon
from TheYid.common.net import Net
from htmlentitydefs import name2codepoint as n2cp
import HTMLParser

try:
	from sqlite3 import dbapi2 as sqlite
	print "Loading sqlite3 as DB engine"
except:
	from pysqlite2 import dbapi2 as sqlite
	print "Loading pysqlite2 as DB engine"

addon_id = 'plugin.video.1080ptvseries'
plugin = xbmcaddon.Addon(id=addon_id)

DB = os.path.join(xbmc.translatePath("special://database"), '1080ptvseries.db')
BASE_URL = 'http://www.blue1city.net/'
net = Net()
addon = Addon('plugin.video.1080ptvseries', sys.argv)

#PATHS#
AddonPath = addon.get_path()
IconPath = AddonPath + "/icons/"
FanartPath = AddonPath + "/icons/"

##### Queries ##########
mode = addon.queries['mode']
url = addon.queries.get('url', None)
content = addon.queries.get('content', None)
query = addon.queries.get('query', None)
startPage = addon.queries.get('startPage', None)
numOfPages = addon.queries.get('numOfPages', None)
listitem = addon.queries.get('listitem', None)
urlList = addon.queries.get('urlList', None)
section = addon.queries.get('section', None)
##### Queries ##########


def GetTitles(section, url, startPage= '1', numOfPages= '1'): # Get Movie Titles
        print '1080ptvseries get Movie Titles Menu %s' % url
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + 'page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + 'page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content
                match = re.compile('<p><img alt=.+? src=.+? rel="nofollow" href="(.+?)" target=.+? class=.+?>(.+?)</a></p>', re.DOTALL).findall(html)
                for movieUrl, name in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img = 'http://pretwerk.nl/wp-content/uploads/blog_tvseries.jpg', fanart = 'http://www.bubblews.com/assets/images/news/254376144_1377377439.jpg')
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#############---------------------------------------------------#############################################

def GetTitles2(section, url, startPage= '1', numOfPages= '1'): # Get Movie Titles
        print '1080ptvseries get Movie Titles Menu %s' % url
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + 'page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + 'page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content
                match = re.compile('<p><a rel="nofollow" href="(.+?)" target="_blank" class="external">Direct Download(.+?)</a></p>', re.DOTALL).findall(html)
                for movieUrl, name in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img = 'http://pretwerk.nl/wp-content/uploads/blog_tvseries.jpg', fanart = 'http://www.bubblews.com/assets/images/news/254376144_1377377439.jpg')
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

##############################################################################################################

def GetLinks(section, url): # Get Links
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(str(url)).content
        sources = []
        listitem = GetMediaInfo(html)
        print 'LISTITEM: '+str(listitem)
        content = html
        print'CONTENT: '+str(listitem)
        r = re.search('<strong>Links.*</strong>', html)
        if r:
                content = content[:r.start()]

        match = re.compile('href="(.+?)"').findall(content)
        listitem = GetMediaInfo(content)
        for url in match:
                host = GetDomain(url)

                if 'Unknown' in host:
                                continue

                print '*****************************' + host + ' : ' + url
                title = url.rpartition('/')
                title = title[2].replace('.html', '')
                title = title.replace('.htm', '')
                title = title.replace('www.', '')
                title = title.replace ('-','')
                title = title.replace('_',' ')
                title = title.replace('.',' ')
                title = title.replace('720p','[COLOR gold][B][I]720p[/B][/I][/COLOR]')
                title = title.replace('1080p','[COLOR orange][B][I]1080p[/B][/I][/COLOR]')
                title = title.replace('mkv','[COLOR gold][B][I]MKV[/B][/I][/COLOR] ')
                name = host+'-'+title
                hosted_media = urlresolver.HostedMediaFile(url=url, title=name)
                sources.append(hosted_media)


        source = urlresolver.choose_source(sources)
        if source: stream_url = source.resolve()
        else: stream_url = ''
        xbmc.Player().play(stream_url)
                       
####################################################################################################################################


def GetDomain(url):
        tmp = re.compile('//(.+?)/').findall(url)
        domain = 'Unknown'
        if len(tmp) > 0 :
            domain = tmp[0].replace('www.', '')
        return domain


def GetMediaInfo(html):
        listitem = xbmcgui.ListItem()
        match = re.search('og:title" content="(.+?) \((.+?)\)', html)
        if match:
                print match.group(1) + ' : '  + match.group(2)
                listitem.setInfo('video', {'Title': match.group(1), 'Year': int(match.group(2)) } )
        return listitem

        
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

###################################################################################################################################################

def MainMenu():    #homescreen  
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/the-walking-dead-s01-s02-complete-bluray-1080p-x264/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'The Walking Dead S01 to S03 BluRay 1080p x264'}, img = 'http://collider.com/wp-content/uploads/The-Walking-Dead-01-poster.jpg', fanart = 'http://www.geekosystem.com/wp-content/uploads/2013/10/dead.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/breaking-bad-s01-s05-complete-1080p-bluray-x264/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Breaking Bad S01 to S05 Bluray 1080p x264'}, img = 'http://static2.businessinsider.com/image/51c9e1afecad04ab7000001f-960/breaking-bad-season-5.jpg', fanart = 'http://sites.psu.edu/rclnataliasolar/wp-content/uploads/sites/4987/2014/01/breaking-bad.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/lost-s01-s06-complete-720p-bluray-x264-tvt/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Lost S01 to S06 720p BluRay x264'}, img = 'http://www.sorozatguru.info/wp-content/uploads/2010/05/Lost-Season-6-Blu-ray-art-1.jpg', fanart = 'http://www.scifiheaven.net/wp-content/uploads/2010/01/lost-season-5-promo.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/supernatural-s01-s08-complete-720p-bluray-web-dl-hdtv/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Supernatural S01 to S08 Bluray 720p x264'}, img = 'http://static2.wikia.nocookie.net/__cb20120926135917/supernatural/images/e/e6/Supernatural_Season_7_BRCover.jpg', fanart = 'http://images5.fanpop.com/image/photos/30500000/Supernatural-supernatural-30545991-1680-1050.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/true-blood-s01-s05-complete-720p-bluray-x264/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'True Blood S01 to S05 BluRay 720p x264'}, img = 'http://yokedesign.com.au/wp-content/uploads/2013/04/true-blood-eric-northman-poster.jpg', fanart = 'http://kingbritt.com/wp-content/uploads/2010/09/True-Blood.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/mentalist-s01-s05-complete-720p-bluray-web-dl/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'The Mentalist S01 to S05 BluRay 720p x264'}, img = 'http://whatculture.com/wp-content/uploads/2012/08/217954_389118961155453_762368379_n.jpg', fanart = 'http://smokedhss.files.wordpress.com/2013/12/the-mentalist-the-mentalist-8522362-1280-800.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + 'haven-s01-s03-720p-bluray-x264/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Haven S01 to S03 Bluray 720p x264'}, img = 'http://www.blue1city.net/Upload/images/21608front.jpg', fanart = 'http://photos.imageevent.com/afap/wallpapers/televisionshows/haven//Eric%20Balfour%20-%20Haven.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/primeval-new-world-s01-2080p-bluray-x264-bia/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Primeval New World S01 1080p Bluray x264'}, img = 'http://fanart.tv/fanart/tv/253042/tvposter/primeval-new-world-52129839bce31.jpg', fanart = 'http://cultfix.co.uk/wp-content/uploads/Primeval-New-World-poster-s1.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/ripper-street-s01-720p-bluray-x264-shortbrehd/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Ripper Street S01 720p Bluray x264'}, img = 'http://ecx.images-amazon.com/images/I/91fOLrla0bL._SL1500_.jpg', fanart = 'http://the-southern-cross.com/awordortwo/wp-content/uploads/2014/02/Ripper-Street-ripper-street-33161902-1190-824.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/the-vampire-diaries-s01-s03-complete-720p-bluray-x264/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'The Vampire Diaries S01 to S04 720p BluRay x264'}, img = 'http://justpic.info/images1/ff53/10897front.jpg', fanart = 'http://images6.fanpop.com/image/photos/33200000/new-TVD-season-4-promo-wallpaper-the-vampire-diaries-33254359-1023-768.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/mad-men-s01-s05-complete-720p-bluray-x264/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Mad Men S01 to S05 720p Bluray x264'}, img = 'http://www.blue1city.net/Upload/images/41114front.jpg', fanart = 'http://img845.imageshack.us/img845/1034/t9nb.jpg')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL + '/mad-men-s06-720p-web-dl-dd5-1-h-264-tvt/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Mad Men S06 720p WEB-DL DD5.1'}, img = 'http://s2.thcdn.com/productimg/0/600/600/91/10828891-1379679174-403951.jpg', fanart = 'http://images.amcnetworks.com/amctv.com/wp-content/uploads/2013/03/mm-s6-key-art-nologo-980.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/supernatural-s01-s08-complete-720p-bluray-web-dl-hdtv/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Supernatural S01 to S08 720p Bluray x264'}, img = 'http://images2.fanpop.com/image/photos/10200000/S5-DVD-offical-cover-supernatural-10291987-499-700.jpg', fanart = 'http://images5.fanpop.com/image/photos/28000000/Sam-Dean-angels-supernatural-28070046-1280-800.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/30-rock-s01-s07-complete-720p-web-dl/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '30 Rock S01 to S07 720p'}, img = 'http://upload.wikimedia.org/wikipedia/en/3/30/30_Rock_Season_7_DVD.jpg', fanart = 'http://0.tqn.com/d/tvcomedies/1/0/F/E/-/-/30-rock-season-7.jpg')

        #addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '',
                             #'startPage': '1', 'numOfPages': '1'}, {'title':  ''}, img = '', fanart = '')
        addon.add_directory({'mode': 'ResolverSettings'}, {'title':  '[COLOR red][B]Real-Debird[/B] Settings[/COLOR]'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'help'}, {'title':  '[COLOR aqua][B]@TheYid009[/B][/COLOR] [COLOR gold][B][I]FOLLOW ME ON TWITTER FOR UPDATES [/B][/I][/COLOR] '}, img=IconPath + 'twit.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view')   
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

######################################################################################################################################################

def setView(content, viewType):

	if content:
		xbmcplugin.setContent(int(sys.argv[1]), content)
	if addon.get_setting('auto-view') == 'true':
		xbmc.executebuiltin("Container.SetViewMode(%s)" % addon.get_setting(viewType) )


	xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_UNSORTED )
	xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_LABEL )
	xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_VIDEO_RATING )
	xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_DATE )
	xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_PROGRAM_COUNT )
	xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_VIDEO_RUNTIME )
	xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_GENRE )

######################################################################################################################################################

if mode == 'main': 
	MainMenu()
elif mode == 'GetTitles': 
	GetTitles(section, url, startPage, numOfPages)
elif mode == 'GetTitles2': 
	GetTitles2(section, url, startPage, numOfPages)
elif mode == 'GetLinks':
	GetLinks(section, url)
elif mode == 'PlayVideo':
	PlayVideo(url, listitem)	
elif mode == 'ResolverSettings':
        urlresolver.display_settings()

