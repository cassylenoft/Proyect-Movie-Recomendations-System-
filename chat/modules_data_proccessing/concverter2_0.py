# this module allows you to proccess data text to make it able to machine learning technichs\

#libreries
import nltk
import re 
from unidecode import unidecode
import numpy as np
import pandas as pd

# imports to avoid messages in code below
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('corpus')
nltk.download('stem')
import nltk.corpus

global tokens_list, no_stopwords, stemms, bows
tokens_list, no_stopwords, stemms, bows = [],[],[],[]

class bower:
    def __init__(self):
        pass
    # def df(self,bow_model,text): #if text is dataframe data format\
    #     self.text = text
    #     self.bow_model = bow_model #selfs
    #     from nltk import word_tokenize #librery for tokens
    #     self.text = (' ').join(self.text)
    #     self.text = self.text.lower() #no caps
    #     self.text = unidecode(self.text) #no accents
    #     patron = re.compile('[^a-zA-Z\s]') #no numbers and marks
    #     tokenized = word_tokenize(self.text)
    #     for row in self.text: 
    #         tokens_list.append([word for word in tokenized if not patron.match(word)])
    #     return tokens_list #list format
    
    def text(self,text):
        self.text = text
        from nltk import word_tokenize #librery for tokens
        self.text = self.text.lower() #no caps
        self.text = unidecode(self.text) #no accents
        patron = re.compile('[^a-zA-Z\s]') #no numbers and marks
        tokenized = word_tokenize(self.text)
        tokens = [word for word in tokenized if not patron.match(word)]
        from nltk.corpus import stopwords
        # stop words en espanol
        stopwords_es = nltk.corpus.stopwords.words('spanish')
        no_stopwords = [word for word in tokens if word not in stopwords_es]
        #lemmetized
        from nltk.stem import SnowballStemmer
        stemmizer = SnowballStemmer('spanish')
        stemmed_text = [stemmizer.stem(word) for word in no_stopwords]
        return tokens,no_stopwords,stemmed_text

    def df(self,toks,stop,lemms,bow,model):
        pass 
        