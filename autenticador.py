from tweepy import OAuthHandler 
import credenciais

class Autenticador():
    def autenticar(self):
        auth = OAuthHandler(credenciais.CONSUMER_KEY, credenciais.CONSUMER_SECRET)
        auth.set_access_token(credenciais.ACCESS_TOKEN, credenciais.ACCESS_TOKEN_SECRET)
        return auth