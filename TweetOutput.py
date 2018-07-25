global userImage, userTranslateLanguage, transLang
transLang = ""
# Imports the Google Cloud client library
from google.cloud import translate

#Imports necessary libraries for google vision API
import io
import os
from google.cloud import vision
from google.cloud.vision import types

import tweepy
from time import sleep
import nltk
from PIL import Image
import requests
from io import BytesIO

auth = tweepy.OAuthHandler("djqF9ATn9TabaAGqJ6v4NvO40", "lzVGLc2b7pkrerCVtol9kbepGWec4JH97opY1DkRK6W6H5d8de")
auth.set_access_token("1022124674623463424-0oIYTbhS0rGC2j7jmQqdg2n7Nsy5U9", "yEPSAcJkzJsKMVnhpfm2eqPTo54MoZyTJlm4SwZgUG067")
api = tweepy.API(auth)
myFile = open('Twitter_Sayings.txt', 'w', encoding="utf-8")

userImage = input("Enter and image url: ")
userTranslateLanguage = input("Enter a number that corresponds to the language you'd like the output to be translated to - [1] Spanish, [2] Japanese, [3] French, [4] Italian, [5] German, [6] English: ")



if userTranslateLanguage == "1":
    userTranslateLanguage = "es-US"
elif userTranslateLanguage == "2":
    userTranslateLanguage = "ja-JP"
elif userTranslateLanguage == "3":
    userTranslateLanguage = "fr-FR"
elif userTranslateLanguage == "4":
    userTranslateLanguage = "it-IT"
elif userTranslateLanguage == "5":
    userTranslateLanguage = "de-DE"
elif userTranslateLanguage == "6":
    userTranslateLanguage = "en-US"

transLang = userTranslateLanguage[0:2]

response = requests.get(userImage)
img = Image.open(BytesIO(response.content))
img.save("temp.jpg", "JPEG")


def translateStuff(targetLanguage, text):
    global userTranslateLanguage
    translate_client = translate.Client()
    translation = translate_client.translate(text, target_language = targetLanguage)
    translatedText = translation["translatedText"]
    myFile.write(" Translation: " + translatedText)

def labelsUrl(uri):
    """Detects labels in the file located in Google Cloud Storage or on the
    Web."""
    client = vision.ImageAnnotatorClient()
    image = types.Image()
    image.source.image_uri = uri

    response = client.label_detection(image=image)
    labels = response.label_annotations
    print('Labels:')

    for label in labels:
        myFile.write(label.description)
        translateStuff(transLang, label.description)
        break

def searchFace(uri):
    client = vision.ImageAnnotatorClient()
    image = vision.types.Image()
    image.source.image_uri = uri

    response = client.face_detection(image=image)
    faces = response.face_annotations

    # Names of likelihood from google.cloud.vision.enums
    chances = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY')
    print('Faces:')

    for face in faces:
        myFile.write('anger: {}'.format(chances[face.anger_likelihood]))
        myFile.write('joy: {}'.format(chances[face.joy_likelihood]))
        myFile.write('surprise: {}'.format(chances[face.surprise_likelihood]))
        myFile.write('sorrow: {}'.format(chances[face.sorrow_likelihood]))
        myFile.write('headwear: {}'.format(chances[face.headwear_likelihood]))

def searchLandmark(uri):
    client = vision.ImageAnnotatorClient()
    image = vision.types.Image()
    image.source.image_uri = uri

    response = client.landmark_detection(image=image)
    landmarks = response.landmark_annotations
    for landmark in landmarks:
        myFile.write("The landmark is: " + landmark.description)
        


def searchLogos(uri):
    # Instantiates a client
    translate_client = translate.Client()

    # Instantiates a client
    vision_client = vision.ImageAnnotatorClient()

    image = vision.types.Image()
    image.source.image_uri = uri

    response = vision_client.logo_detection(image=image)
    logos = response.logo_annotations
    print('Logos:')

    for logo in logos:
        myFile.write("\n" + logo.description)
        translateStuff(transLang, logo.description)

def searchText(uri):

    # Instantiates a client
    translate_client = translate.Client()

    # Instantiates a client
    vision_client = vision.ImageAnnotatorClient()

    image = vision.types.Image()
    image.source.image_uri = uri

    # Performs text detection on the image file
    response = vision_client.text_detection(image=image)
    texts = response.text_annotations

    print('Text:')
    for text in texts:
        myFile.write("\n" + text.description)
        translateStuff(transLang, text.description)


labelsUrl(userImage)
searchFace(userImage)
searchLandmark(userImage)
searchLogos(userImage)
searchText(userImage)

myFile.close()
myFile2 = open('Twitter_Sayings.txt', 'r', encoding="utf-8")

fileLines = myFile2.readlines()


print(fileLines)

def tweetStuff():
    # for line in fileLines:
    #     api.update_status(line)
        
    api.update_with_media('temp.jpg', fileLines) 

tweetStuff()
myFile2.close()