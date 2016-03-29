#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from slackclient import SlackClient
from subprocess import call
import fileinput

<<<<<<< HEAD

#token = "xoxb-16569788000-v0QkD3YyVNA1NoLql6M4Phsu"
=======
#testKanal = "C0FJTRJM6"
#signKanal = "C0GGN4D0T"
>>>>>>> a6edadebac8455c7fcbb14d80a53e2d527d79da6
token = "xoxb-16569788000-NoXWhsDU4WyPOnw1w6w8huOt"
sc = SlackClient(token)
if sc.rtm_connect():
    while True:
        msg = sc.rtm_read()
        for x in msg:
            atext = ""
            
            if "text" in x and x["text"]:
                atext = x["text"].encode('utf-8')
            elif "attachments" in x:
                for attachment in x["attachments"]:
                    #No text in message check in attachments...
                    if "text" in attachment and attachment["text"]:
                        #First for a text in attachment....
                        atext = attachment["text"]
                        #Then for a pretext...
                    elif "pretext" in attachment and attachment["pretext"]:
                        atext = attachment["pretext"]
                    elif "fallback" in attachment and attachment["fallback"] and attachment["fallback"] != "NO FALLBACK DEFINED":
                        #Then for a fallback....
                        atext = attachment["fallback"]
            if atext:
                args = "\"-t " + atext + "\""
                print args
                call("/home/pi/led_sign/sign.py " + args, shell=True)
        time.sleep(1)
    else:
        print "Connection Failed, invalid token?"
