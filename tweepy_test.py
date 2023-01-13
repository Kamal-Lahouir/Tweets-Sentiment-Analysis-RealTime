import tweepy
import json

# Set up your Twitter API credentials
consumer_key = "P6nEoctXBkchpj9AEuvGRkiJU"
consumer_secret = "FRN2AokYmRox2byaMlgSkcCWgkGs2oIskxG1tVQpKByeoVvFS0"
access_token = "1548953019672305664-tzU0ynvJ66TyQbmKqsrVGwY6z6Jivj"
access_token_secret = "C0Jyhr0kgEPvJ15EobeE20cLwLcqnk7OqgFZukwWLw5fN"

# Authenticate with the Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Search for tweets from a specific location (Morocco)
tweets = tweepy.Cursor(api.search_tweets,q= "#crypto", geocode="31.7917,-7.0926,300km", lang="en").items(1000)

# get the first tweet out of tweets
