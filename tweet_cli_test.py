#! c:/python27/python.exe
# -*- coding: utf-8 -*-

'''
Created on 2012/08/22

@author: Damofujiki
'''



import random


import sys
import tweepy



CONSUMER_KEY        = ''
CONSUMER_SECRET     = ''
ACCES_TOKEN         = ''
ACCES_TOKEN_SECRET  = ''


if(len(sys.argv))>1:
    if(len(sys.argv[1])>1):
        print sys.argv[1]
        if(len(sys.argv[1])>12 and len(sys.argv)<3):
            print u"too many strings,fuck off（文字多すぎ）"
            print len(sys.argv)
            sys.exit()



else:
    print "no args"
    sys.exit()



ln=0
tweetlist=[]
tweeted_num=[]
tweet=""
chk = False
wh=0
num = random.randint(0,370)


auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCES_TOKEN, ACCES_TOKEN_SECRET)
api = tweepy.API(auth)
#dt_rp=api.mentions()[1].created_at
#tweet = raw_input('?')

tweet = sys.argv[1]
tweet=tweet.decode('shift-jis')


api.update_status(tweet)