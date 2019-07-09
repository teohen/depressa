from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import credenciais

class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)

if __name__ == "__main__":

    listener = StdOutListener()
    auth = OAuthHandler(credenciais.CONSUMER_KEY, credenciais.CONSUMER_SECRET)
    auth.set_access_token(credenciais.ACCESS_TOKEN, credenciais.ACCESS_TOKEN_SECRET)

    stream = Stream(auth, listener)

    stream.filter(track=['Daltan Dallagnol', 'Sergio Moro'])
