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

        print("Starting Loop")

	# Loop through Tweets
        for line in tweets:
		# Get Current Time
		currentTime = init(time.strftime("%H"))

		# Check if it's daytime
		if currentTime < 6: # If it's before 0600
			wait = 6 - currentTime
			print(currentTime + " o'clock. Waiting until 6AM")
			pause.hours(wait)
		else if currentTime >= 21:
			wait = 6 + 24 - currentTime
			print(currentTime + " o'clock. Waiting until 6AM")
			pause.hours(wait)

		# Update Status
		status = time.strftime("%d %b %Y %H:%M") + " and still #ThisIsNotNormal...DT is not normal! Please Help! " + line
		api.update_status(status)
		pause.hours(1) # Wait 1 hour

	print("End Loop, restarting")

# Start the bot
tweetNow('tweets.txt')
