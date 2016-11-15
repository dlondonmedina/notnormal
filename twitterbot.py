#!/usr/bin/evn python
# -*- coding: utf-8 -*-

# Original script (kept up to date): https://github.com/robincamille/bot-tutorial/blob/master/mybot.py
# NEW SCRIPT modified for NotNormal bot: https://github.com/dlondonmedina/notnormal/twitterbot.py


# Twitter Bot Starter Kit: Bot 1

# This bot tweets three times, waiting 15 seconds between tweets.

# If you haven't changed credentials.py yet with your own Twitter
# account settings, this script will tweet at twitter.com/lacunybot



import tweepy, time
from credentials import *
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)
count = 0

def tweetNow(f):
    # What the bot will tweet
    filename = open(f, 'r')
    tweets = filename.readlines()
    filename.close()

    currentTime = time.hour()
    endTime = 1579478400
    currentTick = time.time()

    for line in tweets:
        if currentTime >= 9 and currentTime < 21:
            status = "This isn't normal! DT isn't normal. Don't give up! Visit: " + line
            api.update_status(status)
            time.sleep(3600)
        else:
            time.sleep(43200)
    if currentTick < endTime:
        tweetNow('tweets.txt')

tweetNow('tweets.txt')
