import tweepy
from time import sleep


consumer_key = 'djqF9ATn9TabaAGqJ6v4NvO40'
consumer_secret = 'lzVGLc2b7pkrerCVtol9kbepGWec4JH97opY1DkRK6W6H5d8de'
access_token = '1022124674623463424-0oIYTbhS0rGC2j7jmQqdg2n7Nsy5U9'
access_token_secret = 'yEPSAcJkzJsKMVnhpfm2eqPTo54MoZyTJlm4SwZgUG067'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

person = api.user_timeline(screenname = 'Curry2615')

public_tweets = api.home_timeline()

test = [
    "potato",
    "pie",
    "1+1+1"
]
# my_file=open('sample20.txt','r')
# file_lines=my_file.readlines()
# my_file.close()



# for line in test:
# # Add try ... except block to catch and output errors
#     try:
#         print(line)
#         if line != '\n':
#             #this line tweets the input
#             api.send_direct_message(person)
#         else:
#             pass
#     except tweepy.TweepError as e:
#         print(e.reason)
#     sleep(5)
count = 0
for tweet in tweepy.Cursor(api.search, q='#soccer').items():
  
    try:
        # Add \n escape character to print() to organize tweets
        print('\nTweet by: @' + tweet.user.screen_name)

        # Retweet tweets as they are found
        tweet.retweet()
        print('Retweeted the tweet')

        count += 1
        if count == 5:
            break
        sleep(5)
    
    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break
    
  


