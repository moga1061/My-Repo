import xbmc, xbmcgui, xbmcaddon, xbmcplugin
import re, string, sys, os
import urlresolver
import HTMLParser
from TheYid.common.addon import Addon
from TheYid.common.net import Net

addon_id = 'plugin.video.myvideolinks'
plugin = xbmcaddon.Addon(id=addon_id)
DB = os.path.join(xbmc.translatePath("special://database"), 'myvideolinks.db')
BASE_URL = 'http://www.myvideolinks.eu/'
net = Net()
addon = Addon('plugin.video.myvideolinks', sys.argv)

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
                match = re.compile(' <img src="(.+?)"  title="(.+?)" class=".+?" alt=".+?" /></a>\r\n\t\t\r\n<h4><a href="(.+?)" rel=".+?"', re.DOTALL).findall(html)
                if not match:
                    match = re.compile(' <img src="(.+?)" title="(.+?)" class=".+?" alt=".+?" /></a>\r\n\t\t\r\n<h4><a href="(.+?)" rel=".+?"',re.DOTALL).findall(html)
                for img, name, movieUrl in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')      
                addon.add_directory({'mode': 'GetTitles', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view')        
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

############################################################################## Get Links ###############################################################################

def GetLinks(section, url): # Get Links
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('<li><a href="(.+?)">.+?</a></li>').findall(content)
        listitem = GetMediaInfo(content)
        for url in match:
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

############################################################################## PlayVideo ###############################################################################

def PlayVideo(url, listitem):
    try:
        print 'in PlayVideo %s' % url
        stream_url = urlresolver.HostedMediaFile(url).resolve()
        xbmc.Player().play(stream_url)
        addon.add_directory({'mode': 'help'}, {'title':  '[COLOR slategray][B]^ Press back ^[/B] [/COLOR]'},'','')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry Link may have been removed ![/B][/COLOR],[COLOR lime][B]Please try a different link/host !![/B][/COLOR],7000,"")")

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
        addon.add_directory({'mode': 'Categories', 'section': 'movies'},  {'title':  '[COLOR blue]Movie by year & release group [/COLOR]>>'}, img=IconPath + 'date.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GenreMenu'}, {'title':  '[COLOR blue]Movies by genre [/COLOR]>>'}, img=IconPath + 'mg.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/tv-shows/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue]Latest Tv shows added [/COLOR]>>'}, img=IconPath + 'newtvs.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/uncategorized/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue]Uncategorized Movies & TV Shows [/COLOR]>>'}, img=IconPath + '66a.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/movies/3-d-movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Latest 3D movies [/COLOR]>>'}, img=IconPath + '3d1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetSearchQuery9'},  {'title':  '[COLOR green]Search[/COLOR]'}, img=IconPath + 'searchse.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'ResolverSettings'}, {'title':  '[COLOR red]Resolver Settings[/COLOR]'}, img=IconPath + 'resolvere.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'HelpMenu'}, {'title':  '[COLOR pink][B]PLEASE CLICK HERE FOR INFO ON TheYids REPO[/B][/COLOR] >>'}, img=IconPath + 'helps.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'HelpMenu'}, {'title':  '[COLOR gold][B]FOLLOW ME ON TWITTER [/B][/COLOR] [COLOR aqua][B][I]@TheYid009 [/B][/I][/COLOR] '}, img=IconPath + 'he.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def HelpMenu():   
        dialog = xbmcgui.Dialog()
        dialog.ok("TheYid's REPO", "I now have a donation button setup at xbmcHUB", "please help keep TheYid's REPO alive more info @","http://www.xbmchub.com/forums/")

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def GenreMenu():   #homescreen
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/movies/3-d-movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]3D >>[/COLOR]'}, img=IconPath + '3d1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/tag/family/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Family >>[/COLOR]'}, img=IconPath + 'fam.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/tag/animation/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Animation >>[/COLOR]'}, img=IconPath + 'an.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/tag/action/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Action >>[/COLOR]'}, img=IconPath + 'ac.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/tag/adventure/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Adventure >>[/COLOR]'}, img=IconPath + 'ad.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/tag/biography/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Biography >>[/COLOR]'}, img=IconPath + 'bm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/tag/comedy/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Comedy >>[/COLOR]'}, img=IconPath + 'com.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/tag/documentary-2/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Documentary >>[/COLOR]'}, img=IconPath + 'doc1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/tag/fantasy/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Fantasy >>[/COLOR]'}, img=IconPath + 'fan.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/tag/horror/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Horror >>[/COLOR]'}, img=IconPath + 'ho.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/tag/sci-fi/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Sci-fi >>[/COLOR]'}, img=IconPath + 'sci.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/tag/mystery/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Mystery >>[/COLOR]'}, img=IconPath + 'ms.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/tag/music/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Music >>[/COLOR]'}, img=IconPath + 'mus.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/tag/war/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]War >>[/COLOR]'}, img=IconPath + 'war.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/tag/western/',
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
        url = 'http://www.google.com/search?q=site:myvideolinks.eu  ' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h3 class="r"><a href="(.+?)".+?onmousedown=".+?">(.+?)</a>').findall(html)
        for url, title in match:
                title = title.replace('<b>...</b>', '').replace('<em>', '').replace('</em>', '').replace('Category Archives', '').replace('Myvideolinks.eu', '').replace('BluRay', '').replace(':', '')
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title})
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
elif mode == 'GetTitles': 
	GetTitles(section, url, startPage, numOfPages)
elif mode == 'GetLinks':
	GetLinks(section, url)
elif mode == 'GetSearchQuery9':
	GetSearchQuery9()
elif mode == 'Search9':
	Search9(query)
elif mode == 'PlayVideo':
	PlayVideo(url, listitem)	
elif mode == 'ResolverSettings':
        urlresolver.display_settings()
elif mode == 'Categories':
        Categories(section)

xbmcplugin.endOfDirectory(int(sys.argv[1]))