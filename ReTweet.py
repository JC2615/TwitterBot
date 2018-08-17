import tweepy
from time import sleep


consumer_key = YOUR_KEY
consumer_secret = YOUR_SECRET
access_token = YOUR_ACCESS_TOKEN
access_token_secret = YOUR_SECRET


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

count = 0
for tweet in tweepy.Cursor(api.search, q='#corgi').items():
  
    try:
        # Add \n escape character to print() to organize tweets
        print('\nTweet by: @' + tweet.user.screen_name)

        # Retweet tweets as they are found
        tweet.retweet()
        print('Retweeted the tweet')

        count += 1
        if count == 5:
            break
    
    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break
    
  


