import os, dotenv 
from requests_oauthlib import OAuth1Session

dotenv.load_dotenv('.env')

consumer_key = os.environ.get('CONSUMER_KEY')
consumer_secret = os.environ.get('CONSUMER_SECRET')
access_token = os.environ.get('ACCESS_TOKEN')
access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')

session = OAuth1Session(consumer_key, consumer_secret, access_token, access_token_secret)

url = 'https://api.twitter.com/2/tweets'

def tweet(message):
  res = session.post(url, json={'text': message})
  return res.text

