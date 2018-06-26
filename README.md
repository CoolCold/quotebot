simple quotebot - can show quotes created by QuoteBot for eggdrop. Requires manual change of quotebot db to have
* convert to utf8
* remove 1st line

Setup

on Debian 9, under separate user
```apt-get install python3 python3-pip python3-setuptools dbus
pip3 install wheel
pip3 install pytelegrambotapi

python3 bot.py -c config/zaykax.ini
```
refer to contrib dir to check about systemd sample unit
Requirements
TBD, but refer to simple telegram bot creation script - https://groosha.gitbooks.io/telegram-bot-lessons/content/chapter1.html

Runing as a service


