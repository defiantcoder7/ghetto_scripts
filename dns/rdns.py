#!/usr/bin/env python
#
# Resolves domain name from IP address
# takes a file with ip addresses and externally resolve the domain name via dns lookup.

import socket

inFilePath = input("Please enter path to Input File: ")
inFile = open(inFilePath,'r')
for ip in inFile.readlines():
    dns = socket.gethostbyaddr(ip)
    print (dns)
inFile.close()
