from autenticador import Autenticador
from twitter_listener import TwitterListener
from tweepy import Stream

class TwitterStreamer():

    def __init__(self):
        self.auth = Autenticador()
    
    def stream_tweets(self, fetched_tweets_filename, users_list = None):
        auth = self.auth.autenticar()   

        listener = TwitterListener(fetched_tweets_filename)
        stream = Stream(auth, listener)
        stream.filter(track=users_list)    