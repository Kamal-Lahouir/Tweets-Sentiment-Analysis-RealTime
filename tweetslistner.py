import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
import socket
import json
import time 

# Set up your credentials
bearer_token = "AAAAAAAAAAAAAAAAAAAAAEP1lAEAAAAAMnS4dYk4hA9jXzzq%2BlwbgBscqk0%3DQU4DALAYbqpHtytqUmzObEzJ6briMuqisg9ygy1oE0ROQez05C"
consumer_key = "BLt10eTfBXELqwGZF1S67Vy8x"
consumer_secret = "KlHEQyNLcfHN5b5g5slkoRNgp5klxvtTRAKRXUq7xZBSqRqyIxp" 
access_token = "1547915644678463488-f4tHSXv6WTpzjYIc1yIynI09nWxB1g"
access_secret = "azydtIKhJM37cmHsYcCaXOSKOwKzkIOzh8pkDlIspWu9V" 


# Gainaing access and connecting to Twitter API using Credentials
client = tweepy.Client()

auth = tweepy.OAuth1UserHandler(
    consumer_key,
    consumer_secret,
    access_token,
    access_secret
)
api = tweepy.API(auth)

search_terms = "#morocco #trading OR morocco trading finance"
tags = ["trading, finance"]

# Bot searches for tweets containing certain keywords
class MyStream(tweepy.StreamingClient):        
    # This function gets called when the stream is working
    def on_connect(self):
        print("Connected")


    # This function gets called when a tweet passes the stream
    def on_tweet(self, tweet):
        try:
            # Displaying tweet in console
            for term in tags:
                if term in tweet.text: 
                    sockett.send(tweet.text.encode('utf-8'))
                    print(tweet.text)
            # Delay between tweets
            time.sleep(5)
        except Exception as e:
            print(e)
            pass

    def on_exception(self, exception):
        print(exception)
        return super().on_exception(exception)
        

# Creating Stream object
def sendData(c):
    # while True:
    stream = MyStream(bearer_token)
    stream.add_rules(tweepy.StreamRule(search_terms))

    # Starting stream
    stream.filter()

if __name__ == "__main__":
    s = socket.socket()         # Create a socket object
    host = "127.0.0.1"     # Get local machine name
    port = 5553        # Reserve a port for your service.
    s.bind((host, port))        # Bind to the port

    print(f"Listening on port: {str(port)}")

    s.listen(5)                 # Now wait for client connection.
    sockett, addr = s.accept()        # Establish connection with client.

    print("Received request from: " + str(addr))

    stream = MyStream(bearer_token)
    stream.add_rules(tweepy.StreamRule(search_terms))

    # Starting stream
    stream.filter()