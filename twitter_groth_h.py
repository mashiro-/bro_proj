#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 14:13:40 2019

@author: paolomenna
"""
'''
TWEEPY DOCS: 
    https://media.readthedocs.org/pdf/tweepy/latest/tweepy.pdf
    https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/user-object.html
    https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object
'''

import time
import tweepy
from tweepy import OAuthHandler
 
consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

for user in tweepy.Cursor(api.followers, screen_name="albertosettimo").items(2):
    print("lo user ",user.screen_name, " ha scritto i seguenti tweets: \n")
    for tweet in tweepy.Cursor(api.user_timeline, screen_name = user.screen_name).items(2):
         print("tweet_id: ", tweet.id," tweet testo: ", tweet.text, "\n")




'''
API.retweet(id)
Retweets a tweet. Requires the id of the tweet you are retweeting.
Parameters id – The numerical ID of the status.
Return type Status object
''' 

# https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/user-object.html

'''
crea like usando il tweet_id
'''

api.create_favorite(tweet.id)












