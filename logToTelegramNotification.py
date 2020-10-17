#!/usr/bin/python

# imports
import tailer
import telegram_send

# blocklist
blocklist = open("blocklist.txt", "r").read().split()

# Follow the file as it grows
for line in tailer.follow(open('squid.txt')):
    # check against blocklist
    for unwantedUrl in blocklist:
        # if there exist a line with a entry on the blocklist, do 'telegram-send'
        if unwantedUrl in line:
            # disabling potential links to be clickable by putting the dot between brackets
            safeUrl = line.replace(".", "[.]")
            telegram_send.send(messages=[safeUrl], conf=None, disable_web_page_preview="true")
