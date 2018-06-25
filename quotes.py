# -*- coding: utf-8 -*-
import copy
import random
import hashlib

quotes=[]
quote={}
minlen=3
searches={}


def load(config):
  with open(config['quotesfile'],'r') as f:
    rawquotes = f.readlines()
  #sample data format
  #5426#2517#cops Never trade luck for skill (c), added by FBI
  c=0
  for line in rawquotes:
    tmp = line.split(' ')
    qinfo = tmp[0].split('#')
    quote['number']=int(qinfo[0])
    quote['lnumber']=int(qinfo[1])
    quote['channel']=qinfo[2]
    quote['text']=' '.join(tmp[1:])
    quotes.append(copy.copy(quote))
    c=c+1
  return c>0 #true or false



def getquote(id):
  for quote in quotes:
    if quote['number']==int(id):
      return quote
  return {}

def getrandomquote():
  return getquote(random.randint(0,len(quotes))) #this is incorrect - TODO - as quotes may have holes, it's not monotonic array

def findquotes(text):
#TODO - check for minimal length
#TODO - limit total number of active searches as it consumes memory
#TODO - keep this data inside config file
  c=0
  thash = gethash(text.lower()) 
  print(thash)
  if not thash in searches:
    searches[thash]={}
    searches[thash]['quotes']=[]
  for quote in quotes:
    if quote['text'].lower().find(text.lower()) is not -1:
      searches[thash]['quotes'].append(copy.copy(quote))
      c=c+1
  if c > 0:
    searches[thash]['count']=c
    return searches
  return None

def findquote(text):
  thash = gethash(text.lower()) 
  if not thash in searches:
    if findquotes(text) == None:
      #nothing was found for the text
      return None
  if len(searches[thash]['quotes']) > 0:
    qinfo={'quote':searches[thash]['quotes'].pop(0), 'nleft': len(searches[thash]['quotes']), 'total':searches[thash]['count']}
    if len(searches[thash]['quotes']) == 0:
      #let's cleanup that hash
      searches.pop(thash, None)
    return qinfo


def gethash(text):
  return hashlib.md5(text.encode('utf-8')).hexdigest()
