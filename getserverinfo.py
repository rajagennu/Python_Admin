#!/usr/bin/python3


import subprocess
import socket
import os
import platform
import shutil
import netifaces_IP

subprocess.call("clear")
print ('Hello Please find server information below')
hostname = socket.gethostname()
fqdn = socket.getfqdn()
arch = platform.architecture()
macarch = platform.machine()
sizetuple = shutil.disk_usage('/')
Totalsize=round((sizetuple.total/(1024*1024*1000)),2)
Usedsize=round((sizetuple.used/(1024*1024*1000)),2)
Freesize=round((sizetuple.free/(1024*1024*1000)),2)


print ("#########################################################################")
print ("Server Hostname: ",hostname)
print ("Server FQDN:",fqdn)
#print ("Server Uname:",uname)
print ("Server Architecture:",arch," and Machine Architecture: ",macarch)
print ("Server Kernel and OS:",platform.platform())
print ("#########################################################################")
print ("Total size of root partition is :{} GB".format(Totalsize))
print ("Used space: %d GB "%Usedsize)
print ("Freesize:{} GB".format(Freesize))
print ("#########################################################################")
netifaces_IP.IPLIST()
