#!/usr/bin/python

from slackclient import SlackClient

#token = "xoxb-16552072721-O4wnMMfwFhuIpIk8DkcozlFO"
token = "xoxb-16569788000-NoXWhsDU4WyPOnw1w6w8huOt"
sc = SlackClient(token)
print sc.api_call("api.test")
#print sc.api_call("channels.list")
#print sc.api_call("im.open", user="U04JVU36K")

print sc.api_call("chat.postMessage", as_user="true:", channel="C0FJTRJM6", attachments='[{"pretext": "Test", "fallback": "Please ignore"}]')
#print sc.api_call("channels.history", channel="C0GGN4D0T")
