#!/usr/bin/python3

import netifaces



def IPLIST():
	LIST_IF=netifaces.interfaces()
	print ("Current System Interfaces and Their IPAddress")		
	for i in range(len(LIST_IF)):
			INET_i=netifaces.ifaddresses(LIST_IF[i])
			ADDR_INET_i=INET_i[netifaces.AF_INET]
			print (LIST_IF[i],"=",ADDR_INET_i[0]['addr'])




IPLIST()

