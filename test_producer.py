import configparser, argparse, logging, socket, tweepy, socket, sys

from confluent_kafka import Producer
from tweepy.streaming import Stream
import time

# Auxiliary classes
#
class TwitterStreamListener(tweepy.Stream):

    _kafka_producer = None
    _topic = None
    
    def connect_to_kafka(self, broker, topic):
        conf = {'bootstrap.servers': broker,
                'client.id': socket.gethostname()}        
        self._kafka_producer = Producer(conf)
        self._topic = topic
        
    def on_data(self, data):
        if self._kafka_producer!=None:
            self._kafka_producer.produce(self._topic, value=data)
            self._kafka_producer.flush()
            logging.debug(f"tweet: {data}")
        else:
            print(data)

    def on_error(self, status):
        logging.error(status)
        sys.exit(-1)

    def verify_credentials(self):
        try:
            self.verify_credentials()
            return True
        except:
            return False

# Body of the scripts       
#
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser()
    parser.add_argument("credentials_file", help="path to the file with info to access the service")
    parser.add_argument("filters", help="provide the filters matching the tweets you want to get specified as comma separated values (ex. btc,eth,#ada")
    parser.add_argument("-b", "--broker",
                        help="server:port of the Kafka broker where messages will be published")
    parser.add_argument("-t", "--topic",
                        help="topic where messages will be published")  
    args = parser.parse_args()

  # Read credentials to connect to the Twitter Stream
  #
    credentials = configparser.ConfigParser()
    credentials.read(args.credentials_file)
        
    API_key = credentials['DEFAULT']['API_key']
    API_secret = credentials['DEFAULT']['API_secret']
    access_token = credentials['DEFAULT']['access_token']
    access_secret = credentials['DEFAULT']['access_secret']

  # Twitter connection and Kafka producer initialization
  #  
    print("the credentials are: ")
    print("\tAPI_key: ", API_key)
    print("\tAPI_secret: ", API_secret)
    print("\taccess_token: ", access_token)
    print("\taccess_secret: ", access_secret )

    twitter_conn = TwitterStreamListener(API_key, API_secret,
                                         access_token, access_secret)
    
  # Initialize the Kafka producer if broker and topic was specified
if args.broker != None and args.topic != None:
    twitter_conn.connect_to_kafka(args.broker, args.topic)
    # Start the filtering
    twitter_conn.filter(track=args.filters.split(","), locations= [-17.1278, 21.4153, -1.1533, 37.0922], stall_warnings=True)
    twitter_conn.sample()

else:
    print("\n/\ Trying to connect to Twitter without Kafka")
    # check if the connection to Twitter is working
    if twitter_conn.verify_credentials():
        print("Connection OK\n")
    else:
        print("Error during authentication\n")
        sys.exit(-1)

    twitter_conn.filter(track=args.filters.split(","), locations= [-17.1278, 21.4153, -1.1533, 37.0922], stall_warnings=True)
    twitter_conn.sample()
    time.sleep(5)
    
    # the sample method returns a lot of tweets, so we need to filter them
