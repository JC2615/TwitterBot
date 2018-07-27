import nltk, random
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import tweepy
from time import sleep
from nltk.tokenize import RegexpTokenizer


global corpus


consumer_key = 'djqF9ATn9TabaAGqJ6v4NvO40'
consumer_secret = 'lzVGLc2b7pkrerCVtol9kbepGWec4JH97opY1DkRK6W6H5d8de'
access_token = '1022124674623463424-0oIYTbhS0rGC2j7jmQqdg2n7Nsy5U9'
access_token_secret = 'yEPSAcJkzJsKMVnhpfm2eqPTo54MoZyTJlm4SwZgUG067'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


langModel = {
    
}

#opens a text file and then tokenizes the entire text, this excludes punctuation
with open("C:\\Users\\jfhaw\\OneDrive\\Desktop\\vision-cssi\\whitefang.txt", "r", encoding ='utf-8') as f:
    global corpus
    text = f.read()
    tokenizer = RegexpTokenizer(r'\w+')
    corpus = tokenizer.tokenize(text)
    
#method to update the dictionary langModel that consists of the words found in the text file specified earlier
def updateLangModel(firstWord, secondWord, model = langModel):
    if firstWord not in model:
        model[firstWord] = []
    val = model[firstWord]
    val.append(secondWord)
    

#updates the dictionary with text in the text file
for i in range(len(corpus)-1):
    current_word = corpus[i]
    next_word = corpus[i+1]
    updateLangModel(current_word, next_word)
    
def generateSent(model = langModel):
    output = ""
    word = random.choice(list(langModel))
    output += word
    output += " "
    for i in range(10):
        nextWord = random.choice(langModel[word])
        output += nextWord
        output += " "
        word = nextWord
    return output

#builds the sentence
for words in range(10):
    key = random.choice(list(langModel))
    api.update_status(generateSent())
