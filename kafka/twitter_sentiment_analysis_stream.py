from pyspark import SparkConf, SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from pyspark.sql import SQLContext
import string
from nltk.corpus import stopwords


# Create Spark configuration and context
conf = SparkConf().setAppName("TwitterSentimentAnalysis")
sc = SparkContext(conf=conf)

# Create a SQL context
sql_context = SQLContext(sc)

# Create a streaming context with a batch interval of 1 second
ssc = StreamingContext(sc, 1)

# Read tweets from the Kafka topic
kafkaStream = kafkaUtils.createStream(ssc, "localhost:2181", "twitter_sentiment_analysis", {"tweets":1})

# Perform sentiment analysis on the tweets
def sentimentAnalysis(rdd):
    # Convert RDD to DataFrame
    tweets_df = sql_context.read.json(rdd)
    # Preprocess the tweets
    preprocessed_tweets = tweets_df.select("text").rdd.map(lambda x: x[0].lower())
    # Remove punctuation and stopwords
    
    stopwords = set(stopwords.words('english'))
    preprocessed_tweets = preprocessed_tweets.map(lambda x: ' '.join([word for word in x.translate(str.maketrans('','',string.punctuation)).split() if word.lower() not in stopwords]))
    # Perform sentiment analysis on the tweets
    sentiments = preprocessed_tweets.map(lambda x: TextBlob(x).sentiment.polarity)
    # Write the results to another kafka topic
    from kafka import KafkaProducer
    from json import dumps
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'],value_serializer=lambda x: dumps(x).encode('utf-8'))
    for sentiment in sentiments:
        producer.send("sentiment_result", sentiment)


kafkaStream.foreachRDD(sentimentAnalysis)

# Start the streaming context
ssc.start()
ssc.awaitTermination()
