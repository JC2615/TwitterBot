import tweepy
from time import sleep
import nltk
from PIL import Image
import requests
from io import BytesIO

response = requests.get('https://s3.amazonaws.com/cdn-origin-etr.akc.org/wp-content/uploads/2017/11/13001000/Beagle-On-White-01-400x267.jpg')
img = Image.open(BytesIO(response.content))
img.save("temp.jpg", "JPEG")

auth = tweepy.OAuthHandler("djqF9ATn9TabaAGqJ6v4NvO40", "lzVGLc2b7pkrerCVtol9kbepGWec4JH97opY1DkRK6W6H5d8de")
auth.set_access_token("1022124674623463424-0oIYTbhS0rGC2j7jmQqdg2n7Nsy5U9", "yEPSAcJkzJsKMVnhpfm2eqPTo54MoZyTJlm4SwZgUG067")

api = tweepy.API(auth)

myFile = open('Twitter_Sayings.txt', 'a+', )
fileLines = myFile.readlines()
myFile.close()

def tweetLine():
    for line in fileLines:
        try:
            if line != '\n':
                api.update_status(line)
            else:
                pass
        except tweepy.TweepError as e:
            print(e.reason)
            sleep(2)