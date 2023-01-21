import tweepy
import socket
import json
import time 

# Set up your credentials
consumer_key = "AT6J5mcjRy2Qqz1ylKkRxo9pF"
consumer_secret = "pKqMudgkx6knqdBVwjFavFgYfPN0FAYxHvX5khPCwpz2PMfUD5" 
access_token = "1547915644678463488-HgmrWQrjLANhFDGyoy0qdeBwvZQpo6"
access_secret = "lw4TzM6PhwTeNsy3eI2zDhXbGDCwYoWl8b2WIdo7yF3xt" 

# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

# Creating the API object
api = tweepy.API(auth)

# Search terms
search_terms = ["#crypto", "#morocco"]

# Bot searches for tweets containing certain keywords
class MyStream(tweepy.Stream(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_secret, daemon=False)):

    def on_connect(self):
        print("Connected")

    def on_status(self, status):
        try:
            # Displaying tweet in console
            if status.referenced_tweets == None:
                print(status.text)
                sockett.send(status.text.encode('utf-8'))
                # client.like(status.id)

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
    # Creating Stream object
    stream = MyStream(auth=api.auth, listener=MyStream())
    
    # Adding terms to search rules
    for term in search_terms:
        stream.filter(track=[term]) 

    # Starting stream and adding filter for location
    # Morocco coordinates: [-17.03, 21.37, -1.12, 37.09]
    stream.filter(locations=[-17.03, 21.37, -1.12, 37.09])

if __name__ == "__main__":
    s = socket.socket()         # Create a socket object
    host = "127.0.0.1"     # Get local machine name
    port = 5553        # Reserve a port for your service.
    s.bind((host, port))        # Bind to the port
    s.listen(5)                 # Now wait for client connection
    while True:
        sockett, addr = s.accept() # Establish connection with client.
        print ('Got connection from', addr)
        sendData(sockett)
        sockett.close() # Close the connection