# -*- coding: utf-8 -*-
import logging
import time

import argparse

parser = argparse.ArgumentParser(description='Simple reimplementation of Zayka/ZaykaX bot from XNet irc network')
parser.add_argument('-c', '--config', help='path to config file')

args = parser.parse_args()

import configparser
config = configparser.ConfigParser()
config.read(args.config)
token=config['telegram'].get('token') #TODO - add check it's not empty / or fail
if token == None:
  raise RuntimeError('failed to load token for telegram auth')

import telebot
logger = telebot.logger
telebot.logger.setLevel(logging.INFO) # Outputs debug messages to console.

#TODO - read modules and phrase bindings to be loaded from ini file, not hardcoded - PRETEND TO BE EGGDROP!!! MVAHAHAHAHA!!!
import quotes
if not quotes.load(config['quotebot']):
  raise RuntimeError('failed to load configuration for quotes') 


bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    bot.send_message(message.chat.id, "this is help " + message.text)
@bot.message_handler(commands=['test'])
def handle_start_help(message):
    bot.send_message(message.chat.id, "@" + message.from_user.username + " test passed, all nishtyak!")

@bot.message_handler(commands=['quote'])
def handle_quote(message):
    quote = {}
    quoteid = None
    print(message)
    tokens = message.text.split(" ")
    if len(tokens)>1:
      #need to strip spaces, TODO
      quoteid = tokens[1]
#      print(quoteid)
      if quoteid.isdigit(): #quote id
        print("quote is a digit " + quoteid)
        quote = quotes.getquote(quoteid)
        if quote != {}:
            bot.send_message(message.chat.id, "quote #%i (#%i for #%s): %s" % (quote['number'], quote['lnumber'], quote['channel'], quote['text']) )
        else:
            bot.send_message(message.chat.id, "wasn't able to get quote %s ;(" % (quoteid))
      else: #need to lookup for subphrase
        phrase = ' '.join(tokens[1:])
        print("phrase is" + phrase)
        qinfo=quotes.findquote(phrase)
        if qinfo == None :
          bot.send_message(message.chat.id, "wasn't able to find quotes for %s ;(" % (phrase))
        else:
          bot.send_message(message.chat.id, "quote #%i (#%i for #%s, %i left): %s" % (qinfo['quote']['number'], qinfo['quote']['lnumber'], qinfo['quote']['channel'], qinfo['nleft'], qinfo['quote']['text']))
    else:
      quote = quotes.getrandomquote()
      if quote != {}:
          bot.send_message(message.chat.id, "quote #%i (#%i for #%s): %s" % (quote['number'], quote['lnumber'], quote['channel'], quote['text']) )
      else:
          bot.send_message(message.chat.id, "wasn't able to get quote %s ;(" % (quoteid))

if __name__ == '__main__':
  pass
  logging.info("---- starting polling sleeping 1 second before retry...")
  while True:
    try:
      bot.polling(none_stop=True)
    except:
      logging.warning("some error occured during polling")
    logging.info("sleeping 1 second before retry...") #no idea why it doesn't work with logging.INFO level
    time.sleep(5)
