NotNormal Twitter Bot
I. File list
credentials.py.default        Contains the Twitter Authentication settings.
tweets.txt                    List of tweets to cycle through
twitterbot.py                 Main program


To setup your Twitterbot:
1. Create a Twitter account
2. Login to apps.twitter.com
3. Create App Following On Screen instructions
4. Copy credentials.py.default and rename credentials.py
5. Replace constants in crendentials.py with your credentials from step 3
6. Run the application from command line.

Description
This twitter bot posts a line from the tweets.txt file once per hour between 0900 and 2100.
It repeats this process recursively until January 20, 2020.
