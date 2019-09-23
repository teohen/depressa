from tweepy import  OAuthHandler
from tweepy.streaming import StreamListener
from tweepy import Stream
  
# Fill the X's with the credentials obtained by  
# following the above mentioned procedure. 
consumer_key = "mujD286ILQ1Mk3FYr5MKkOygo"
consumer_secret = "mls6OQku9sJfTQBqAlD4Li7BCuNStSJiHWEBHHaWT8mh9J7agN"
access_key = "1148305857458913280-pwv9zqsW8qxP6O5EHhh590gBitHGPO"
access_secret = "1148305857458913280-pwv9zqsW8qxP6O5EHhh590gBitHGPO"


class StdOutListener(StreamListener):
    def on_data(self, data):
        print(data)
        return True
    def on_error(self, status):
        print (status)
        return False

if __name__ == "main":
    listener = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    stream = Stream(auth, listener)
    