# Intro
Simple quotes bot for Telegram network.
shows quotes created by QuoteBot for eggdrop.

# Setup
## Quotes database
Requires manual change of quotebot db to have
* convert to utf8
* remove 1st line

## Environment
### Debian 9
#### System setup
```sudo apt-get install python3 python3-pip python3-setuptools dbus```
#### to be run under dedicated user
```
pip3 install wheel
pip3 install pytelegrambotapi

python3 bot.py -c config/zaykax.ini
```
#### Runing as a service
refer to contrib dir to check about systemd sample unit to run as systemd service

# implementation details
Refer to simple telegram bot creation script - https://groosha.gitbooks.io/telegram-bot-lessons/content/chapter1.html




