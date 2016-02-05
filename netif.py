#!/usr/bin/python3

import netifaces 

a=netifaces.interfaces()
print (a)
netifaces.ifaddresses('a[1]')

print (a[1])
