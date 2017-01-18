#clean version of code

#Required packages
import tweepy
import argparse
import json
import ijson
import os
import re
import pandas as pd
import time
import numpy
#set up working directory
os.getcwd()
os.chdir("/Users/nicolekelly/Documents/ft_aggregate/")



#Setting up Twitter API
#twitterkeys.py is a file that contains my consumer_key, consumer_secret, access_token and access_token_secret
import twitterkeys

auth = tweepy.OAuthHandler(twitterkeys.consumer_key, twitterkeys.consumer_secret)
auth.set_access_token(twitterkeys.access_token, twitterkeys.access_token_secret)

api = tweepy.API(auth)



#second method from David
#Pull in most recent 20 tweets
ArepaZone_timeline=api.user_timeline("ArepaZone")
arepa_tweets=[]
for tweet in ArepaZone_timeline:
    tweet_parts = {
        "id":tweet.id,
        "created_at":tweet.created_at,
        "text":tweet.text
    }
    arepa_tweets.append(tweet_parts)

ArepaZone_df = pd.DataFrame(arepa_tweets)
ArepaZone_df



#doesn't work yet, something with the pd.DataFrame line syntax
trucks=['captaincookiedc']
for food_truck_twitter_handle in trucks:
    food_truck_twitter_handle_timeline=api.user_timeline('{}'.format(food_truck_twitter_handle))
    food_truck_twitter_handle_tweets=[]
    for tweet in food_truck_twitter_handle_timeline:
        tweet_parts = {
            "id":tweet.id,
            "created_at":tweet.created_at,
            "text":tweet.text
        }
        food_truck_twitter_handle_tweets.append(tweet_parts)
    food_truck_twitter_handle_df = pd.DataFrame(food_truck_twitter_handle_tweets)
    return food_truck_twitter_handle_df



#doesn't work yet, something with the pd.DataFrame line syntax
def tweets_to_dataframe(food_truck_twitter_handle, food_truck_twitter_handle_string):
    food_truck_twitter_handle_timeline=api.user_timeline('{}'.format(food_truck_twitter_handle_string))
    food_truck_twitter_handle_tweets=[]
    for tweet in food_truck_twitter_handle_timeline:
        tweet_parts = {
            "id":tweet.id,
            "created_at":tweet.created_at,
            "text":tweet.text
        }
        food_truck_twitter_handle_tweets.append(tweet_parts)
    food_truck_twitter_handle_df = pd.DataFrame(food_truck_twitter_handle_string_tweets)
    return food_truck_twitter_handle_df



tweets_to_dataframe('captaincookiedc','captaincookiedc')



