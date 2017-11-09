import unittest
import tweepy
import requests
import json
import twitter_info

consumer_key = twitter_info.consumer_key
consumer_secret = twitter_info.consumer_secret
access_token = twitter_info.access_token
access_token_secret = twitter_info.access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

term = input("Please enter a search term: ")

results = api.search(term)

tweets = api.home_timeline()
print(tweets)

# for a in results["statuses"]:
#     print("TEXT: ", a['text'])
#     print("CREATED AT: : ", a['created_at'])
#     print("USERNAME: ", a['user']['screen_name'])
#     print("\n")
#
# for x in results["statuses"]:
#     if x['user']['screen_name'] == "livywiesnerd":
#         print(x['text'])
#         print("BY: " + x['user']['screen_name'])
