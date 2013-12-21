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

addon_id = 'plugin.video.singlelinkmoviez'
plugin = xbmcaddon.Addon(id=addon_id)

DB = os.path.join(xbmc.translatePath("special://database"), 'singlelinkmoviez.db')
BASE_URL = 'http://singlelinkmoviez.com/'
net = Net()
addon = Addon('plugin.video.singlelinkmoviez', sys.argv)
showAllParts = True
showPlayAll = True

######PATHS########
AddonPath = addon.get_path()
IconPath = AddonPath + "/icons/"
FanartPath = AddonPath + "/icons/"

if plugin.getSetting('showAllParts') == 'false':
	showAllParts = False

if plugin.getSetting('showPlayAll') == 'false':
	showPlayAll = False

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




def GetTitles(section, url, startPage= '1', numOfPages= '1'): # Get Movie Titles
	print 'singlelinkmoviez get Movie Titles Menu %s' % url

        # handle paging
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
                        
                match = re.compile('entry-title.+?href="(.+?)".+?>(.+?)<.+? .+?src="(.+?)".+?', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        cm  = []
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img)
		

      
		addon.add_directory({'mode': 'GetTitles', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR red][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'page.png', fanart=FanartPath + 'fanart.png')

	
	xbmcplugin.endOfDirectory(int(sys.argv[1]))


def GetLinks(section, url): # Get Links
	print 'GETLINKS FROM URL: '+url
	html = net.http_GET(str(url)).content
	CLEAN(html)
	sources = []
	listitem = GetMediaInfo(html)
	print 'LISTITEM: '+str(listitem)
	content = html
	print'CONTENT: '+str(listitem)
	r = re.search('<strong>Links.*</strong>', html)
	if r:
		content = html[r.end():]

	match = re.compile('href="(.+?)"').findall(content)
	listitem = GetMediaInfo(content)
	for url in match:
		host = GetDomain(url)

		if 'Unknown' in host:

			continue
		print '*****************************' + host
		title = url.rpartition('/')
		host = host.replace('','')
		host = host.replace('33b1ad22','xbmc link')
		host = host.replace('.miniurls.co','')
		host = host.replace('rapidgator.net','rapidgator')
		host = host.replace('extabit.com','extabit')
		host = host.replace('ul.to','uploaded')
		host = host.replace('letitbit.net','letitbit')
		host = host.replace('www.sockshare.com','sockshare')
		host = host.replace('www.share-online.biz','share-online')
		host = host.replace('www.putlocker.com','putlocker')
		host = host.replace('turbobit.net','turbobit')
		host = host.replace('ryushare.com','[COLOR red]ryushare[/COLOR]')
		name = host
		hosted_media = urlresolver.HostedMediaFile(url=url, title=name)
		sources.append(hosted_media)

		
	find = re.search('commentblock', html)
	if find:
		print 'in comments if'
		html = html[find.end():]
		CLEAN(html)###
		print 'MATCH IS: '+str(match)
		print len(match)
		for url in match:
			host = GetDomain(url)
			if 'Unknown' in host:
				continue

	source = urlresolver.choose_source(sources)
	if source: stream_url = source.resolve()
	else: stream_url = ''
	xbmc.Player().play(stream_url)



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


def GetDomain(url):
	tmp = re.compile('//(.+?)/').findall(url)
	domain = 'Unknown'
	if len(tmp) > 0 :
	    domain = tmp[0].replace('www.', '')
	    domain = tmp[0].replace('http://33b1ad22.miniurls.co/url/.', '')
	return domain


def GetMediaInfo(html):
	listitem = xbmcgui.ListItem()
	match = re.search('og:title" content="(.+?) \((.+?)\)', html)
	if match:
		print match.group(1) + ' : '  + match.group(2)
		listitem.setInfo('video', {'Title': match.group(1), 'Year': int(match.group(2)) } )
	return listitem

def Categories(section):  #categories

	url = BASE_URL + '/category/' + section
	html = net.http_GET(BASE_URL).content
	CLEAN(html)
	match = re.compile('<li class=.+?/category/' + section + '(.+?)".+?>(.+?)<').findall(html)
	for cat, title in match:
		url = url + cat
		addon.add_directory({'mode': 'GetTitles', 'section': section, 'url': url,
				     'startPage': '1', 'numOfPages': '1'}, {'title':  title})
	xbmcplugin.endOfDirectory(int(sys.argv[1]))

def MainMenu():    #homescreen
	addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/latest-movies/',
			     'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue]Latest movies >>[/COLOR]'}, img=IconPath + '1.png', fanart=FanartPath + 'fanart.png')
	addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/animated-movies/',
			     'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue]Animated Movies >>[/COLOR]'}, img=IconPath + '2.png', fanart=FanartPath + 'fanart.png')
	addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/asian-movies/',
			     'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue]Asian Movies >>[/COLOR]'}, img=IconPath + '3.png', fanart=FanartPath + 'fanart.png')
	addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/indian-movies/',
			     'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue]Indian Movies  >>[/COLOR]'}, img=IconPath + '4.png', fanart=FanartPath + 'fanart.png')
	addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/documentary/',
			     'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue]Documentary	>>[/COLOR]'}, img=IconPath + '5.png', fanart=FanartPath + 'fanart.png')
	addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/concerts/',
			     'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue]Concerts  >>[/COLOR]'}, img=IconPath + '6.png', fanart=FanartPath + 'fanart.png')
	addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/uncategorized/',
			     'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue]Web-dl,WEBrip,HDrip	>>[/COLOR]'}, img=IconPath + '7.png', fanart=FanartPath + 'fanart.png')
	addon.add_directory({'mode': 'Categories', 'section': 'dvd'},  {'title':  '[COLOR blue]DVDRips,SCR,DVDR  >>[/COLOR]'}, img=IconPath + '8.png', fanart=FanartPath + 'fanart.png')
	addon.add_directory({'mode': 'Categories', 'section': 'b'},  {'title':	'[COLOR blue]BRRip,BDRip >>[/COLOR]'}, img=IconPath + '9.png', fanart=FanartPath + 'fanart.png')
	addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/r5/',
			     'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue]R5 >>[/COLOR]'}, img=IconPath + '10.png', fanart=FanartPath + 'fanart.png')
	addon.add_directory({'mode': 'GetSearchQuery'},  {'title':  '[COLOR green]Search Moviez[/COLOR]'}, img=IconPath + 's.png', fanart=FanartPath + 'fanart.png')
	addon.add_directory({'mode': 'ResolverSettings'}, {'title':  '[COLOR red]Resolver Settings[/COLOR]'}, img=IconPath + 'r.png', fanart=FanartPath + 'fanart.png')
	addon.add_directory({'mode': 'help'}, {'title':  '[COLOR pink]FOR HELP PLEASE GOTO...[/COLOR] [COLOR gold][B][I]www.xbmchub.com[/B][/I][/COLOR]'}, img=IconPath + 'h.png', fanart=FanartPath + 'fanart.png')
	addon.add_directory({'mode': 'help'}, {'title':  '[COLOR aqua][B]FOLLOW ME ON TWITTER [/B][/COLOR] [COLOR gold][B][I]@TheYid009 [/B][/I][/COLOR] [COLOR aqua][B]AND SHOW YOUR SUPPORT... [/B][/COLOR] '}, img=IconPath + 'theyid.png', fanart=FanartPath + 'fanart.png')
	xbmcplugin.endOfDirectory(int(sys.argv[1]))


def GetSearchQuery():
	last_search = addon.load_data('search')
	if not last_search: last_search = ''
	keyboard = xbmc.Keyboard()
	keyboard.setHeading('[COLOR green]Search Single Link Moviez[/COLOR]')
	keyboard.setDefault(last_search)
	keyboard.doModal()
	if (keyboard.isConfirmed()):
		query = keyboard.getText()
		addon.save_data('search',query)
		Search(query)
	else:
		return

	
def Search(query):
	url = 'http://www.google.com/search?q=site:singlelinkmoviez.com/ ' + query
	url = url.replace(' ', '+')
	print url
	html = net.http_GET(url).content
	CLEAN(html)
	match = re.compile('<h3 class="r"><a href="(.+?)".+?onmousedown=".+?">(.+?)</a>').findall(html)
	for url, title in match:
		title = title.replace('<b>...</b>', '').replace('<em>', '').replace('</em>', '')
		addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title})
	xbmcplugin.endOfDirectory(int(sys.argv[1]))


if mode == 'main': 
	MainMenu()
elif mode == 'GetTitles': 
	GetTitles(section, url, startPage, numOfPages)
elif mode == 'GetLinks':
	GetLinks(section, url)
elif mode == 'GetSearchQuery':
	GetSearchQuery()
elif mode == 'Search':
	Search(query)
elif mode == 'PlayVideo':
	PlayVideo(url, listitem)	
elif mode == 'ResolverSettings':
	urlresolver.display_settings()
elif mode == 'Categories':
	Categories(section)
