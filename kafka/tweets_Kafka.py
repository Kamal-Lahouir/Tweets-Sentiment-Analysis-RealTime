import tweepy
from kafka import KafkaProducer

# Twitter API credentials
consumer_key = "P6nEoctXBkchpj9AEuvGRkiJU"
consumer_secret = "FRN2AokYmRox2byaMlgSkcCWgkGs2oIskxG1tVQpKByeoVvFS0"
access_token = "1548953019672305664-tzU0ynvJ66TyQbmKqsrVGwY6z6Jivj"
access_token_secret = "C0Jyhr0kgEPvJ15EobeE20cLwLcqnk7OqgFZukwWLw5fN"

# Kafka topic name
topic_name = "tweets"

# Authentication and connection to Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Kafka producer
producer = KafkaProducer(bootstrap_servers='localhost:9092')

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        # Send tweet to Kafka topic
        producer.send(topic_name, status.text.encode())
        print(status.text)

# Create a stream object
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

# Start streaming tweets
# List of hashtags to track
hashtags = ["#Crypto", "#Cryptocurrency", "#"]

myStream.filter(locations=[-17.1278, 21.4153, -1.1533, 37.0922])

