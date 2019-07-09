from tweepy.streaming import StreamListener
from tweepy import OAuthHandler 
from tweepy import Stream

class TwitterStreamer():
    
    def stream_tweets(self, fetched_tweets_filename, users_list):
        listener = StdOutListener()
        auth = OAuthHandler(credenciais.CONSUMER_KEY, credenciais.CONSUMER_SECRET)
        auth.set_access_token(credenciais.ACCESS_TOKEN, credenciais.ACCESS_TOKEN_SECRET)

        stream = Stream(auth, listener)

        stream.filter(track=users_list)    

import credenciais

class StdOutListener(StreamListener):

    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, data):
        try:
            print(data)
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("Erro na busca %s" % str(e))
        return True

    def on_error(self, status):
        print(status)

if __name__ == "__main__":

    users_list = ['Daltan', 'Sergio Moro']
    fetched_tweets_filename = "tweets.json"

    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, users_list)
