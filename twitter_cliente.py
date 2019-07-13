from autenticador import Autenticador
from tweepy import API
from tweepy import Cursor
class TwitterClient():
    def __init__(self, usuario=None):
        self.auth = Autenticador().autenticar()
        self.twitter_client = API(self.auth)
        self.usuario = usuario

    def get_user_timeline(self, num_tweets):
        tweets = []
        for tweet in Cursor(self.twitter_client.user_timeline, id = self.usuario).items(num_tweets):
            tweets.append(tweet)
        return tweets