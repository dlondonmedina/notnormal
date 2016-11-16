#!/usr/bin/evn python
# -*- coding: utf-8 -*-

# Original script (kept up to date): https://github.com/robincamille/bot-tutorial/blob/master/mybot.py
# NEW SCRIPT modified for NotNormal bot: https://github.com/dlondonmedina/notnormal/twitterbot.py

# Not Normal Bot
# This bot tweets once per hour between 0900 and 2100
# Continues tweeting until January 20, 2020

import tweepy
import time
import pause
import datetime
from credentials import *
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)
endTime = 1579478400

##############
# Main function
# @param f filename list with tweets

def tweetNow(f):

    currentTick = time.time()
    while currentTick < endTime:
        currentTick = time.time()

        # Open file and get lines
        filename = open(f, 'r')
        tweets = filename.readlines()
        filename.close()

        # Get Current Time
        currentTime = int(time.strftime("%H"))

        # Loop through Tweets
        for line in tweets:
            if currentTime >= 6 and currentTime < 21: # If it's day, tweet.
                status = time.strftime("%d %b %Y %H:%M") + " and still #ThisIsNotNormal...DT is not normal! Please Help! " + line
                api.update_status(status)
                pause.hours(1) # Wait 1 hour
            else: # If it's not day sleep all night
                today = int(time.strftime("%d"))
                dt = datetime.datetime.today()
                dt = dt.replace(day=today+1, hour=6, minute=0, second=0, microsecond=0)
                pause.until(dt) # Wait until 8AM tomorrow


# Start the bot
tweetNow('tweets.txt')
