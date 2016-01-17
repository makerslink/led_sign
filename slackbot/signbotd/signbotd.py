#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from slackclient import SlackClient
from subprocess import call
import fileinput


token = "xoxb-16569788000-v0QkD3YyVNA1NoLql6M4Phsu"
sc = SlackClient(token)
if sc.rtm_connect():
    while True:
        msg = sc.rtm_read()
        for x in msg:
           if "text" in x:
               atext = x["text"].encode('utf-8')
               args = "\"-t " + atext + "\""
               print args
               call("/home/pi/led_sign/sign.py " + args, shell=True)
        time.sleep(1)
    else:
        print "Connection Failed, invalid token?"
