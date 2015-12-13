#!/usr/local/bin/python3

import subprocess
import socket
import os
import platform

subprocess.call("clear")
print ('Hello Please find server information below')
hostname = socket.gethostname()
fqdn = socket.getfqdn()
arch = platform.architecture()
macarch = platform.machine()

print ("#########################################################################")
print ("Server Hostname: ",hostname)
print ("Server FQDN:",fqdn)
#print ("Server Uname:",uname)
print ("Server Architecture:",arch," and Machine Architecture: ",macarch)
print ("Server Kernel and OS:",platform.platform())
print ("#########################################################################")


