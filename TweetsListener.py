import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
import socket
import json
import time 

# Set up your credentials
bareerer_tok = "AAAAAAAAAAAAAAAAAAAAAEP1lAEAAAAACNC%2Bp%2Bw0SsduR3pRbD3VqyIWwkw%3DCOmGzkbFPt1qJnrRdAprIhTgiTS0Q6so4hOVCF66xkR2crKH3w"
consumer_key = "AT6J5mcjRy2Qqz1ylKkRxo9pF"
consumer_secret = "pKqMudgkx6knqdBVwjFavFgYfPN0FAYxHvX5khPCwpz2PMfUD5" 
access_token = "1547915644678463488-HgmrWQrjLANhFDGyoy0qdeBwvZQpo6"
access_secret = "lw4TzM6PhwTeNsy3eI2zDhXbGDCwYoWl8b2WIdo7yF3xt" 



# Gainaing access and connecting to Twitter API using Credentials
client = tweepy.Client()

auth = tweepy.OAuth1UserHandler(
    consumer_key,
    consumer_secret,
    access_token,
    access_secret
)
api = tweepy.API(auth)

search_terms = ["#crypto", "#morocco"]

# Bot searches for tweets containing certain keywords
class MyStream(tweepy.StreamingClient):

        # self.user_agent = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0"
        # self.bearer_token = "AAAAAAAAAAAAAAAAAAAAAIi1fQEAAAAAMBjc%2BVoXDftuUMV6cPXVjhkAPfc%3DcoAxHa5U3S1vKJF6lSCgqG6zXdPc75XWZbu2c1OdfqZ2t3ilBF"
        

    # This function gets called when the stream is working
    def on_connect(self):

        print("Connected")


    # This function gets called when a tweet passes the stream
    def on_tweet(self, tweet):
        try:
            # Displaying tweet in console
            if tweet.referenced_tweets == None:
                print(tweet.text)
                sockett.send( tweet.text.encode('utf-8') )
                # client.like(tweet.id)

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
        stream = MyStream(bareerer_tok)
        # try:
            

            # Adding terms to search rules
            # It's important to know that these rules don't get deleted when you stop the
            # program, so you'd need to use stream.get_rules() and stream.delete_rules()
            # to change them, or you can use the optional parameter to stream.add_rules()
            # called dry_run (set it to True, and the rules will get deleted after the bot
            # stopped running).
        for term in search_terms:
            stream.add_rules(tweepy.StreamRule(term))

        # Starting stream and add a filter of Morocco

        stream.filter(tweet_fields=["referenced_tweets"])
        # except Exception as e:
        #     print(e)
        #     time.sleep(5)
        #     pass


if __name__ == "__main__":
    s = socket.socket()         # Create a socket object
    host = "127.0.0.1"     # Get local machine name
    port = 5553        # Reserve a port for your service.
    s.bind((host, port))        # Bind to the port

    print("Listening on port: %s" % str(port))

    s.listen(5)                 # Now wait for client connection.
    sockett, addr = s.accept()        # Establish connection with client.

    print( "Received request from: " + str( addr ) )

    stream = MyStream(bareerer_tok)

    for term in search_terms:
        stream.add_rules(tweepy.StreamRule(term))

        # Starting stream
    
    stream.filter(tweet_fields=["referenced_tweets"])
    



