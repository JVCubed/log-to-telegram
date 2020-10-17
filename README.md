# log-to-telegram-notifications
A python script for reading growing log files and sending notifications via the telegram API based on items in a blocklist.

# Dependencies:
- tailer; see https://pypi.org/project/tailer/ for more information about this module.
- telegram-send; see https://pypi.org/project/telegram-send/ for more information about this module.

# Requirements:
- Create a Telegram bot (https://core.telegram.org/bots).
- Make sure to use 'telegram-send --configure' to configure telegram-send with your telegram API
- Create a blocklist file or modify the path to use an existing file
- Modify the path of the logfile to the locations of the log file you want to follow.

# About this script
This script uses the 'tailer' module to read the appended lines of a log file. 'tailer' is a python implementation of the GNU tail and head commands. The script will then check those lines against the blocklist and if there is a match it will use telegram-send to send the entire line via the Telegram API to your configured chat or group. Be aware of the Telegram API limitations as described in https://core.telegram.org/bots/faq#my-bot-is-hitting-limits-how-do-i-avoid-this
