from kafka import KafkaProducer
import tweepy

# Twitter API credentials
consumer_key = "P6nEoctXBkchpj9AEuvGRkiJU"
consumer_secret = "FRN2AokYmRox2byaMlgSkcCWgkGs2oIskxG1tVQpKByeoVvFS0"
access_token = "1548953019672305664-tzU0ynvJ66TyQbmKqsrVGwY6z6Jivj"
access_token_secret = "C0Jyhr0kgEPvJ15EobeE20cLwLcqnk7OqgFZukwWLw5fN"
# Create Twitter API connection
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Create Kafka producer
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Kafka topic name
topic_name = "tweets"

# List of hashtags to track
hashtags = ["#Python", "#DataScience", "#BigData"]

# A variable to count the number of tweets streamed
tweet_count = 0
class MyStream(tweepy.Stream):
    def on_data(self, data):
        global tweet_count
        # Send tweet to kafka topic
        producer.send(topic_name, data.encode())
        tweet_count += 1
        print(data)
        # Stop streaming after 500 tweets
        if tweet_count >= 500:
            self.disconnect()

while True:
    myStream = MyStream(consumer_key, consumer_secret, access_token,access_token_secret)
    myStream.filter(track=hashtags,locations=[-17.1278, 21.4153, -1.1533, 37.0922],stall_warnings=True)
    producer.flush()
