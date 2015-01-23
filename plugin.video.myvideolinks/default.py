import xbmc, xbmcgui, xbmcaddon, xbmcplugin
import re, string, sys, os
import urlresolver
import HTMLParser
from TheYid.common.addon import Addon
from TheYid.common.net import Net

addon_id = 'plugin.video.myvideolinks'
plugin = xbmcaddon.Addon(id=addon_id)
DB = os.path.join(xbmc.translatePath("special://database"), 'myvideolinks.db')
BASE_URL1 = 'http://tv.myvideolinks.eu/'
net = Net()
addon = Addon('plugin.video.myvideolinks', sys.argv)

BASE_URL = addon.get_setting('custurl')
if not BASE_URL.endswith("/"):
    BASE_URL = BASE_URL + "/"

###### PATHS ##########
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

############################################################################## Get titles ###############################################################################

def GetTitles(section, url, startPage= '1', numOfPages= '1'): # Get Movie Titles
        print 'myvideolinks get Movie Titles Menu %s' % url
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
                match = re.compile('<div class="entry">\s*?<a href="(.+?)" rel="bookmark" title=".+?"> <img src="(.+?)" title="(.+?)"  alt=".+?"/></a>', re.DOTALL).findall(html)
                for movieUrl, img, name in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')   
                match1 = re.compile('<div class="archive">.+?<a href="(.+?)" rel="bookmark" title=".+?"> <img src="(.+?)"  title="(.+?)" class="alignleft" alt=".+?" /></a>.+?<h4><a href=".+?" rel="bookmark" title=".+?">.+?</a></h4>', re.DOTALL).findall(html)
                for movieUrl, img, name in match1:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')    
                addon.add_directory({'mode': 'GetTitles', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view')        
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetTitles2(section, url, startPage= '1', numOfPages= '1'): # Get Movie Titles 2
        print 'myvideolinks get Movie Titles Menu %s' % url
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
                match = re.compile('<div class="archive">\s*?<a href="(.+?)" rel="bookmark" title=".+?"> <img src="(.+?)" title="(.+?)" class="alignleft" alt=".+?" /></a>', re.DOTALL).findall(html)
                for movieUrl, img, name in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')      
                addon.add_directory({'mode': 'GetTitles2', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view')        
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def GetTitles1(section, url, startPage= '1', numOfPages= '1'): # Get tv Titles
        print 'myvideolinks get Movie Titles Menu %s' % url
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
                match = re.compile('rel="bookmark" title=".+?">\s*?<img src="(.+?)"  title="(.+?)" class="alignleft" alt=".+?" /></a>\s*?<h4><a href="(.+?)" rel="bookmark"', re.DOTALL).findall(html)
                for img, name, movieUrl in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')      
                addon.add_directory({'mode': 'GetTitles1', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view')        
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

############################################################################## Get Links ###############################################################################

def GetLinks(section, url): # Get Links
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('<li><a href="(.+?)">.+?</a></li>').findall(content)
        match1 = re.compile("Watch=window.+?'(.+?)'").findall(content)
        match2 = re.compile("Watch=window.+?'(.+?)'").findall(content)
        listitem = GetMediaInfo(content)
        for url in match1:
                addon.add_directory({'mode': 'GetLinks1', 'url': url, 'listitem': listitem}, {'title':  'V-Vids'}, img=IconPath + 'vids.png', fanart=FanartPath + 'fanart.png')
        for url in match + match2:
                host = GetDomain(url)
                if 'Unknown' in host:
                                continue
                print '*****************************' + host + ' : ' + url
                if urlresolver.HostedMediaFile(url= url):
                        print 'in GetLinks if loop'
                        title = url.rpartition('/')
                        title = title[2].replace('.html', '')
                        title = title.replace('.htm', '')
                        host = host.replace('youtube.com','[COLOR lime]Movie Trailer[/COLOR]')
                        host = host.replace('youtu.be','[COLOR lime]Movie Trailer[/COLOR]')
                        host = host.replace('.net','')
                        host = host.replace('.com','')
                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title':  host }, img=IconPath + 'play.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))



def GetLinks1(url):                                            
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('onclick=".+?" href="(.+?)" title=".+?"').findall(content)
        match2 = re.compile('<embed type="video/divx" src="(.+?)"').findall(content)
        listitem = GetMediaInfo(content)
        for url in match + match2:
                addon.add_directory({'mode': 'PlayVideo1', 'url': url, 'listitem': listitem}, {'title':  'load stream'}, img=IconPath + 'watch.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

############################################################################## PlayVideo ###############################################################################

def PlayVideo(url, listitem):
    try:
        print 'in PlayVideo %s' % url
        stream_url = urlresolver.HostedMediaFile(url).resolve()
        xbmc.Player().play(stream_url)
        addon.add_directory({'mode': 'help'}, {'title':  '[COLOR slategray][B]^ Press back ^[/B] [/COLOR]'},'','')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry Link may have been removed ![/B][/COLOR],[COLOR lime][B]Please try a different link/host !![/B][/COLOR],7000,"")")


def PlayVideo1(url, listitem):
        addon_handle = int(sys.argv[1])
        xbmcplugin.setContent(addon_handle, 'video')
        li = xbmcgui.ListItem('[COLOR dodgerblue][B]PLAY STREAM[/B][/COLOR]  >> ', iconImage='https://lh5.googleusercontent.com/-p2h0tx7Trgs/Uzu-3kxzKuI/AAAAAAAAOsU/sVJKqxSMY-4/s319/watch2.jpg', thumbnailImage= 'http://s29.postimg.org/8z8jd5x5j/logo1.png')
        li.setProperty('fanart_image', '')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
        xbmcplugin.endOfDirectory(addon_handle)

########################################################################################################################################################################

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

############################################################################## categories ###############################################################################

def Categories(section):  #categories

        url = BASE_URL + '/category/' + section
        html = net.http_GET(BASE_URL).content
        match = re.compile('<li class=.+?/category/' + section + '(.+?)".+?>(.+?)<').findall(html)
        for cat, title in match:
                url = url + cat
                addon.add_directory({'mode': 'GetTitles', 'section': section, 'url': url,
                                     'startPage': '1', 'numOfPages': '1'}, {'title':  title}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

############################################################################## Menus ######################################################################################

def MainMenu():    #homescreen
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue]Latest Movies added [/COLOR]>>'}, img=IconPath + 'newmovies.png', fanart=FanartPath + 'fanart.png')
        #addon.add_directory({'mode': 'Categories', 'section': 'movies'},  {'title':  '[COLOR blue]Movie by year & release group [/COLOR]>>'}, img=IconPath + 'date.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'releaseMenu'}, {'title':  '[COLOR blue]Movie by year & release group [/COLOR]>>'}, img=IconPath + 'date.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GenreMenu'}, {'title':  '[COLOR blue]Movies by genre [/COLOR]>>'}, img=IconPath + 'mg.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL1 + '/category/tv-shows/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue]Latest Tv shows added [/COLOR]>>'}, img=IconPath + 'newtvs.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/uncategorized/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue]Uncategorized Movies[/COLOR]>>'}, img=IconPath + '66a.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/movies/3-d-movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Latest 3D movies [/COLOR]>>'}, img=IconPath + '3d1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetSearchQuery9'},  {'title':  '[COLOR green]Movie Search[/COLOR]'}, img=IconPath + 'searchse.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetSearchQuery'},  {'title':  '[COLOR green]Movie Search[/COLOR]  (backup)'}, img=IconPath + 'searchse.png', fanart=FanartPath + 'fanart.png')

        addon.add_directory({'mode': 'ResolverSettings'}, {'title':  '[COLOR red]Resolver Settings[/COLOR]'}, img=IconPath + 'resolvere.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'HelpMenu'}, {'title':  '[COLOR pink][B]PLEASE CLICK HERE FOR INFO ON TheYids REPO[/B][/COLOR] >>'}, img=IconPath + 'helps3.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'HelpMenu'}, {'title':  '[COLOR gold][B]FOLLOW ME ON TWITTER [/B][/COLOR] [COLOR aqua][B][I]@TheYid009 [/B][/I][/COLOR] '}, img=IconPath + 'theyid.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def HelpMenu():   
        dialog = xbmcgui.Dialog()
        dialog.ok("TheYid's REPO", "I now have a donation button setup at xbmcHUB", "please help keep TheYid's REPO alive more info @","http://forums.tvaddons.ag/")

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def releaseMenu():   #homescreen
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/movies/2013-and-older/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]2013 and older >>[/COLOR]'}, img=IconPath + 'date.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/movies/2014/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]2014 >>[/COLOR]'}, img=IconPath + 'date.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/movies/2013-and-older/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]2013 and older >>[/COLOR]'}, img=IconPath + 'date.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/movies/2015/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]2015 >>[/COLOR]'}, img=IconPath + 'date.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/movies/3-d-movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]3D movies >>[/COLOR]'}, img=IconPath + 'date.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/movies/bdrip/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]BDRip >>[/COLOR]'}, img=IconPath + 'date.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/movies/bluray/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]BluRay >>[/COLOR]'}, img=IconPath + 'date.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/movies/dvdrips/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]DVDRip >>[/COLOR]'}, img=IconPath + 'date.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/movies/tagalog/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Tagalog >>[/COLOR]'}, img=IconPath + 'date.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/uncategorized/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Uncategorized Movies[/COLOR]>>'}, img=IconPath + 'date.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def GenreMenu():   #homescreen
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/movies/3-d-movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]3D >>[/COLOR]'}, img=IconPath + '3d1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL + '/tag/family/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Family >>[/COLOR]'}, img=IconPath + 'fam.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL + '/tag/animation/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Animation >>[/COLOR]'}, img=IconPath + 'an.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL + '/tag/action/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Action >>[/COLOR]'}, img=IconPath + 'ac.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL + '/tag/adventure/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Adventure >>[/COLOR]'}, img=IconPath + 'ad.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL + '/tag/biography/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Biography >>[/COLOR]'}, img=IconPath + 'bm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL + '/tag/comedy/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Comedy >>[/COLOR]'}, img=IconPath + 'com.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL + '/tag/documentary-2/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Documentary >>[/COLOR]'}, img=IconPath + 'doc1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL + '/tag/fantasy/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Fantasy >>[/COLOR]'}, img=IconPath + 'fan.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL + '/tag/horror/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Horror >>[/COLOR]'}, img=IconPath + 'ho.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL + '/tag/sci-fi/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Sci-fi >>[/COLOR]'}, img=IconPath + 'sci.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL + '/tag/mystery/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Mystery >>[/COLOR]'}, img=IconPath + 'ms.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL + '/tag/music/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Music >>[/COLOR]'}, img=IconPath + 'mus.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL + '/tag/war/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]War >>[/COLOR]'}, img=IconPath + 'war.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL + '/tag/western/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Western >>[/COLOR]'}, img=IconPath + 'west.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

######################################################################### Search ##########################################################################################

def GetSearchQuery9():
	last_search = addon.load_data('search')
	if not last_search: last_search = ''
	keyboard = xbmc.Keyboard()
        keyboard.setHeading('[COLOR green]Search[/COLOR]')
	keyboard.setDefault(last_search)
	keyboard.doModal()
	if (keyboard.isConfirmed()):
                query = keyboard.getText()
                addon.save_data('search',query)
                Search9(query)
	else:
                return
def Search9(query):
        url = BASE_URL + '/?s=' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h4><a href="(.+?)" rel="bookmark" title="(.+?)">.+?</a></h4>', re.DOTALL).findall(html)
        for url, title in match:
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title}, img ='newmovies.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))


def GetSearchQuery():
	last_search = addon.load_data('search')
	if not last_search: last_search = ''
	keyboard = xbmc.Keyboard()
        keyboard.setHeading('[COLOR green]Search[/COLOR]')
	keyboard.setDefault(last_search)
	keyboard.doModal()
	if (keyboard.isConfirmed()):
                query = keyboard.getText()
                addon.save_data('search',query)
                Search(query)
	else:
                return  
def Search(query):
        url = 'http://www.google.com/search?q=site:movies.myvideolinks.xyz/ ' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h3 class="r"><a href="(.+?)".+?onmousedown=".+?">(.+?)</a>').findall(html)
        for url, title in match:
                title = title.replace('<b>...</b>', '').replace('<em>', '').replace('</em>', '')
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title}, img ='newmovies.png', fanart=FanartPath + 'fanart.png')
	xbmcplugin.endOfDirectory(int(sys.argv[1]))


############################################################################# set View ####################################################################################

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

#########################################################################################################################################################################

if mode == 'main': 
	MainMenu()
elif mode == 'HelpMenu':
        HelpMenu()
elif mode == 'GenreMenu':
        GenreMenu()
elif mode == 'releaseMenu':
        releaseMenu()
elif mode == 'GetTitles': 
	GetTitles(section, url, startPage, numOfPages)
elif mode == 'GetTitles1': 
	GetTitles1(section, url, startPage, numOfPages)
elif mode == 'GetTitles2': 
	GetTitles2(section, url, startPage, numOfPages)
elif mode == 'GetLinks':
	GetLinks(section, url)
elif mode == 'GetLinks1':
	GetLinks1(url)
elif mode == 'GetSearchQuery9':
	GetSearchQuery9()
elif mode == 'Search9':
	Search9(query)
elif mode == 'GetSearchQuery':
	GetSearchQuery()
elif mode == 'Search':
	Search(query)
elif mode == 'PlayVideo':
	PlayVideo(url, listitem)
elif mode == 'PlayVideo1':
	PlayVideo1(url, listitem)	
elif mode == 'ResolverSettings':
        urlresolver.display_settings()
elif mode == 'Categories':
        Categories(section)

xbmcplugin.endOfDirectory(int(sys.argv[1]))