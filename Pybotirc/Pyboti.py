#-------------------------------------------------------------------------------
# Name:        Pybot(Integrated IRC)
# Purpose:     To create Pybot with an integrated IRC
#
# Author:      kickguy223
#
# Created:     04/12/2014
# Copyright:   (c) kickguy223 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import socket
import os
import time
import sys
import datetime
import string

twitchIp = b"irc.twitch.tv"

#Settings
oauth = b"PASS oauth:t3a1yw3lvu9fe44j9a696vgq73umii"

botname = b"Pybottest"
ident = botname.lower()
rname = b"Pybot"
rbuff = b""

streamer = b"kickguy223"

channeltoJoin = b"kickguy223"
debug = 1
password = []

#password = "PASS"
#password.append(oauth)
#Pass = ''.join(password)

def debug(message):
    if debug == 1:
        print(message)

def init_irc():
    global irc
    irc = socket.socket( )
    irc.connect((twitchIp,6667))
    time.sleep(2)
    irc.send(oauth)
    time.sleep(.4)
    irc.send(b"NICK " + botname)
    irc.send(b"USER " +ident+ b" "+ident+b' '+ident+b' '+rname)
    irc.send(b"JOIN #"+channeltoJoin)

    #do intro
    irc.send(b"say There is no"+streamer+b", Only Zuel")

def ping():
    irc.send(b"PONG :pingis \n")

def basic_rall_hook(chat):

    global lSplitLine
    sInLine = chat
    debug(sInLine)
    sStripLine = string.rstrip(sInLine)
    debug(sStripLine)
    lSplitLine = string.split(sStripLine)
    debug(lSplitLine)

    #Split line Definition: [0] = nick, [1] = text(?), [2] = ?
    #TODO: TEST THIS


#Initialize IRC
init_irc()

#Exec loop
while 1:
    rbuff=rbuff+irc.recv(1024)
    #temp=string.split(rbuff, "\n")
    temp=rbuff.strip(b'\n\r')
    #rbuff = temp.pop( )
    print(temp)

    if temp.find(b"PING :" != -1):
        ping()

    for line in temp:
        debug(line)
        if line:
            basic_rall_hook(line)

   #     line=string.rstrip(line)
   #     line=string.split(line)
   #     debug(line)






