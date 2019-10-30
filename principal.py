from autenticador import Autenticador
from twitter_streamer import TwitterStreamer
from twitter_cliente import TwitterClient

import credenciais

if __name__ == "__main__":

    users_list = ['Daltan', 'Sergio Moro']
    fetched_tweets_filename = "tweets.json"

    cliente = TwitterClient("teohen")
    # print(cliente.get_user_timeline(1))
    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, users_list)
