import tweepy
from time import sleep


consumer_key = 'djqF9ATn9TabaAGqJ6v4NvO40'
consumer_secret = 'lzVGLc2b7pkrerCVtol9kbepGWec4JH97opY1DkRK6W6H5d8de'
access_token = '1022124674623463424-0oIYTbhS0rGC2j7jmQqdg2n7Nsy5U9'
access_token_secret = 'yEPSAcJkzJsKMVnhpfm2eqPTo54MoZyTJlm4SwZgUG067'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

count = 0
for tweet in tweepy.Cursor(api.search, q='#backpack').items():
  
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
    
  


