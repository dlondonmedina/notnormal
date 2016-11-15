#!/usr/bin/evn python
# -*- coding: utf-8 -*-

# Original script (kept up to date): https://github.com/robincamille/bot-tutorial/blob/master/mybot.py
# NEW SCRIPT modified for NotNormal bot: https://github.com/dlondonmedina/notnormal/twitterbot.py

# Not Normal Bot
# This bot tweets once per hour between 0900 and 2100
# Continues tweeting until January 20, 2020

import tweepy, time
from credentials import *
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)
endTime = 1579478400

##############
# Main function
# @param f filename list with tweets

def tweetNow(f):
    # Open file and get lines
    filename = open(f, 'r')
    tweets = filename.readlines()
    filename.close()

    # Get Current Time
    currentTime = time.hour()
    currentTick = time.time()
    # Loop through Tweets
    for line in tweets:
        if currentTime >= 9 and currentTime < 21: # If it's day, tweet.
            status = "This isn't normal! DT isn't normal. Don't give up! Visit: " + line
            api.update_status(status)
            time.sleep(3600) # Wait 1 hour
        else: # If it's not day sleep all night
            time.sleep(43200) # Wait 12 hours
    # End of loop, start over again if it's before the end of time.
    if currentTick < endTime:
        tweetNow('tweets.txt')

# Start the bot
tweetNow('tweets.txt')
