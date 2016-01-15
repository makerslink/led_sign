#!/usr/bin/python

from slackclient import SlackClient

token = "xoxb-16552072721-O4wnMMfwFhuIpIk8DkcozlFO"
sc = SlackClient(token)
print sc.api_call("api.test")
print sc.api_call("im.open", user="U04JVU36K")

print sc.api_call("chat.postMessage", as_user="true:", channel="D0GG8PQDC", text="whohoo :-D")
print sc.api_call("im.history", channel="D0GG8PQDC")
