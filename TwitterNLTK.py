import nltk, random
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import tweepy
from time import sleep
from nltk.tokenize import RegexpTokenizer


global corpus


consumer_key = YOUR_KEY
consumer_secret = YOUR_SECRET
access_token = YOUR_TOKEN
access_token_secret = YOUR_SECRET

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


langModel = {
    
}


with open("C:\\Users\\jfhaw\\OneDrive\\Desktop\\vision-cssi\\whitefang.txt", "r") as f:
    global corpus
    text = f.read()
    tokenizer = RegexpTokenizer(r'\w+')
    corpus = tokenizer.tokenize(text)
    # print(corpus)
    # print("TOKENIZE")
def updateLangModel(firstWord, secondWord, model = langModel):
    if firstWord not in model:
        model[firstWord] = []
    val = model[firstWord]
    val.append(secondWord)
    #print(langModel)

for i in range(len(corpus)-1):
    current_word = corpus[i]
    next_word = corpus[i+1]
    updateLangModel(current_word, next_word)
    
#print(langModel)

for words in range(10):
    key = random.choice(list(langModel))
    val = random.choice(langModel[key])
    val2 = random.choice(langModel[val])
    val3 = random.choice(langModel[val2])
    val4 = random.choice(langModel[val3])
    val5 = random.choice(langModel[val4])
    val6 = random.choice(langModel[val5])
    val7 = random.choice(langModel[val6])
    val8 = random.choice(langModel[val7])
    val9 = random.choice(langModel[val8])
    api.update_status(key + " " + val + " " + val2 + " " + val3 + " " + val4 + " " + val5 + " " + val6 + " " + val7 + " " + val8 + " " + val9)
