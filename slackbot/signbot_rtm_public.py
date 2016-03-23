#!/usr/bin/env python

import time
from slackclient import SlackClient
from subprocess import call

#token = "xoxb-16569788000-v0QkD3YyVNA1NoLql6M4Phsu"
token = "xoxb-16569788000-NoXWhsDU4WyPOnw1w6w8huOt"
sc = SlackClient(token)
if sc.rtm_connect():
    while True:
        msg = sc.rtm_read()
        for x in msg:
           if "text" in x:
               args = "\"-t " + x["text"] + "\""
               print args
               call("/home/pi/led_sign/sign.py " + args, shell=True)
        time.sleep(1)
    else:
        print "Connection Failed, invalid token?"
