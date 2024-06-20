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

#generate tokens from text
class generate_tokens:
    def __init__(self) -> None:
        pass

    def info(self):
        print('this function gets tokens fron any text data')
        print('function tokens -> get tokens, deleted marks and numeric data; args -> raw_data : its a string data in a list')
        print('function show_tokens -> show tokens generated')

    def get_tokens(self,raw_data,show=False,df=True):

        from nltk import word_tokenize
        self.raw_data = raw_data
        if df == False:
            self.raw_data = (' ').join(raw_data) #convert dataframe column to string
        raw_text = self.raw_data.lower() #lowers
        raw_text = unidecode(raw_text) #no accents
        tokenized = word_tokenize(raw_text)
        patron = re.compile('[^a-zA-Z\s]') #no numbers and marks
        global permited #will use permited for class df_clean and df_by_step
        permited = [word for word in tokenized if not patron.match(word)]
        if show == True:
            print('tokens generated: \n',permited)
        return permited

#delete stopwords from text    
class del_stopwords:
    def __init__(self) -> None:
        pass
    def show_stopwords(self):
        from nltk.corpus import stopwords
        # stop words en espanol
        stopwords_es = nltk.corpus.stopwords.words('spanish')
        return print(stopwords_es)
    
    def no_stopwords(self,tokened_text,show=False):
        self.tokened_text = tokened_text
        stopwords_es = nltk.corpus.stopwords.words('spanish')
        global no_stopwords
        no_stopwords = [word for word in tokened_text if word not in stopwords_es]
        if show == True:
            print('no stopwords generated: \n',no_stopwords)
        return no_stopwords
    

class lematization:
    def __init__(self) -> None:
        pass
    def lematize(self,tokens_no_stopwords,show=False):
        from nltk.stem import SnowballStemmer
        self.tokens_no_stopwords = tokens_no_stopwords
        stemmizer = SnowballStemmer('spanish')
        global stemmed_text
        stemmed_text = [stemmizer.stem(word) for word in self.tokens_no_stopwords]
        if show == True:
            print('stemmed text: \n',stemmed_text)
        return stemmed_text


class full_data_stemm:
    #all process together
    def __init__(self):
       pass
    def stem(self,text_from_tokens,df_token,show=False):
        self.text_from_tokens = text_from_tokens
        self.df_token = df_token
        generate_tokens().get_tokens(df=self.df_token,raw_data=self.text_from_tokens)
        del_stopwords().no_stopwords(permited)
        lematization().lematize(no_stopwords)
        if show == True:
            print('full data ready to transform')
            
        return stemmed_text


class bower:
    def __init__(self) -> None:
        pass

    def bow_transform(self,model,text_from_tokens,df_token,show=False):
        self.text_from_tokens = text_from_tokens
        self.df_token = df_token
        self.model = model
        generate_tokens().get_tokens(df=self.df_token,raw_data=self.text_from_tokens)
        del_stopwords().no_stopwords(permited)
        lematization().lematize(no_stopwords)
        codin = model.transform(stemmed_text)
        codin = codin.toarray()
        if show == True:
            print('codin generated: ',codin)
        return codin