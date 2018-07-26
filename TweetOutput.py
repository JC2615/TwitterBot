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


userImage = input("Enter an image url: ")
userTranslateLanguage = input("Enter a number that corresponds to the language you'd like the output to be translated to - [1] Spanish, [2] Japanese, [3] Arabic, [4] Russian, [5] German, [6] English: ")


if userTranslateLanguage == "1":
    userTranslateLanguage = "es-US"
elif userTranslateLanguage == "2":
    userTranslateLanguage = "ja-JP"
elif userTranslateLanguage == "3":
    userTranslateLanguage = "ar-AE"
elif userTranslateLanguage == "4":
    userTranslateLanguage = "ru-RU"
elif userTranslateLanguage == "5":
    userTranslateLanguage = "de-DE"

transLang = userTranslateLanguage[0:2]

response = requests.get(userImage)
img = Image.open(BytesIO(response.content))
img.save("temp.jpg", "JPEG")
myFile = open('Twitter_Sayings.txt', 'w', encoding="utf-8")

def translateStuff(targetLanguage, text):
    global userTranslateLanguage
    translate_client = translate.Client()
    translation = translate_client.translate(text, target_language = targetLanguage)
    translatedText = translation["translatedText"]
    myFile.write(" (Translation: " + translatedText + ")")

def labelsUrl(uri):
    """Detects labels in the file located in Google Cloud Storage or on the
    Web."""
    counter = 0
    client = vision.ImageAnnotatorClient()
    image = types.Image()
    image.source.image_uri = uri

    response = client.label_detection(image=image)
    labels = response.label_annotations
    print('Labels:')

    for label in labels:
        myFile.write("\n" + label.description)
        translateStuff(transLang, label.description)
        counter += 1
        if counter == 3:
            break

def searchFace(uri):
    client = vision.ImageAnnotatorClient()
    image = vision.types.Image()
    image.source.image_uri = uri

    response = client.face_detection(image=image)
    faces = response.face_annotations

    # Names of likelihood from google.cloud.vision.enums
    chances = ('UNKNOWN', 'VERY UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY LIKELY')
    print('Faces:')

    for face in faces:
        myFile.write("\n" + 'anger: {}'.format(chances[face.anger_likelihood]))

        myFile.write("\n" + 'joy: {}'.format(chances[face.joy_likelihood]))

        myFile.write("\n" + 'sorrow: {}'.format(chances[face.sorrow_likelihood]))
        break

def searchLandmark(uri):
    client = vision.ImageAnnotatorClient()
    image = vision.types.Image()
    image.source.image_uri = uri

    response = client.landmark_detection(image=image)
    landmarks = response.landmark_annotations
    for landmark in landmarks:
        myFile.write("\nThe landmark is: " + landmark.description)
        break
        
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
        break

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
        break
        

def runProgram(runLabel = "1", runFace = "0", runLandmark = "0", runLogos = "0", runText = "0"):
    if runLabel == "1":
        labelsUrl(userImage)
    
    if runFace == "1":
        searchFace(userImage)
    
    if runLandmark == "1":
        searchLandmark(userImage)
    
    if runLogos == "1":
        searchLogos(userImage)
    
    if runText == "1":
        searchText(userImage)


runProgram(runLabel="0", runLandmark="0", runLogos="0", runText="0", runFace="0")

myFile.close()
myFile2 = open('Twitter_Sayings.txt', 'r', encoding="utf-8")

newline = "\n"
fileLines = myFile2.readlines()
newLines = []
for line in fileLines:
    print(line)
    line1 = line.replace("\n", "")
    if line1 != "":
        newLines.append(line1)

print(newLines)
def tweetStuff(newLines):
    api.update_with_media('temp.jpg', newLines) 

tweetStuff(newLines)
myFile2.close()