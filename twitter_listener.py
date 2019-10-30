from tweepy.streaming import StreamListener

class TwitterListener(StreamListener):
    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, data):
        try:
            print(type(data))
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("Erro na busca %s" % str(e))
        return True

    def on_error(self, status):
        if status == 420:
            return False
            
        print(status)