import tweepy
import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

auth = tweepy.OAuthHandler('VYzNi6fe7UTHWto3Fv8q8s3tP','bZLPr1GazWNaryi7MFi0VrUB6mcvW8bfGtQUC6mPX2e1IkuqLQ')

auth.set_access_token('1261756287626260480-SRODrK4AuZm6E28h3S0FqH2Vt3jL8m','GHf9ZhawcMurBr8vZa0nhgewGVDxXwI2ZJPBThcSbRR9o')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()


def get_tweets(username): 
    # tweets = api.user_timeline(screen_name=username) 
    for tweet in tweepy.Cursor(api.user_timeline,screen_name=username).items(100):
        if not tweet.favorited:
            # Mark it as Liked, since we have not done it yet
            try:
                tweet.favorite()
            except Exception as e:
                logger.error("Error on fav", exc_info=True)
        if not tweet.retweeted:
            # Retweet, since we have not retweeted it yet
            try:
                tweet.retweet()
            except Exception as e:
                logger.error("Error on fav and retweet", exc_info=True)

if __name__ == '__main__': 
  
    # Here goes the twitter handle for the user 
    # whose tweets are to be extracted and liked. 
    get_tweets("insert name of person whose tweets you want to like")  
