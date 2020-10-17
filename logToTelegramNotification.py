#!/usr/bin/python

# imports
#  install 'tailer' with 'pip install tailer'
import tailer
#  install 'telegram-send' with 'pip install telegram-send'
import telegram_send

# blocklist
blocklist = open("blocklist.txt", "r").read().split()

# Follow the file as it grows
for line in tailer.follow(open('squid.txt')):
    # check against blocklist
    for unwantedUrl in blocklist:
        # if there exist a line with a entry on the blocklist, do 'telegram-send'
        if unwantedUrl in line:
            safeUrl = line.replace(".", "[.]")
            telegram_send.send(messages=[safeUrl], conf=None, disable_web_page_preview="true")