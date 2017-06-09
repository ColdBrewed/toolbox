#!/usr/bin/python2.7
# Black Hat Python: Sniff email creds with Scapy

from scapy.all import *
#our packet callback
def packet_callback(packet):
	print packet.show()

#fire up our sniffer
sniff(prn=packet_callback,count=1)

