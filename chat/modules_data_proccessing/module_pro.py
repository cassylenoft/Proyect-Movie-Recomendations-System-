#this module converts texto into matrixes for machine learning pourposses 

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

def limpia_texto(text):
   text = text.lower()
   text = unidecode(text)
   m= re.sub(r'[^a-zA-Z\s]', '', text)
   return m

def get_tokens(text):
    tokens_list = []
    from nltk import word_tokenize
    if type(text) == type(tokens_list):
        #print('entraste al if de df')
        for row in(text):
            texto_limpio = limpia_texto(row)
            token = word_tokenize(texto_limpio)
            tokens_list.append(token)
    else:
        texto_limpio = limpia_texto(text)
        token = word_tokenize(texto_limpio)
        return token
        
    return tokens_list

def nostops(text,df):
    stopswords_used = None
    nostops_list = []
    
    from nltk.corpus import stopwords
    spanis_stopswords = nltk.corpus.stopwords.words('spanish')
    if df == True:
        for row in text:
            nostops_list_for_row = []
            row_limpio = get_tokens(row)
            for word in row_limpio:
                if word not in spanis_stopswords:
                    nostops_list_for_row.append(word)
            nostops_list.append(nostops_list_for_row)
        #setattr(nostops_list,'stops',str(spanis_stopswords))
        return nostops_list            
    else:
        text_token = get_tokens(text)
        no_stops = []
        for word in text_token:
                if word not in spanis_stopswords:
                    no_stops.append(word)
        #setattr(no_stops,'stop',str(spanis_stopswords))
        return no_stops

        
def lematize(text,df):
    lemms_list = []
    from nltk.stem import SnowballStemmer
    stemmizer = SnowballStemmer('spanish')
    if df == True:
        row_limpio = nostops(text,df=True)
        for row in row_limpio:
            lemms_list_for_row = []
            for word in row:
                lemms_list_for_row.append(stemmizer.stem(word))
            lemms_list.append(lemms_list_for_row)
        return lemms_list
    else:
        leems = []
        text_nostops = nostops(text,df=False)
        for word in text_nostops:
            leems.append(stemmizer.stem(word))
        return leems

def generate_model(full_data,df):
    if df == True:
        data = (' ').join(full_data)
        data = limpia_texto(data)
    else:
        data = limpia_texto(full_data)

    from sklearn.feature_extraction.text import CountVectorizer
    bower = CountVectorizer()
    lem_data = lematize(data,df=False)
    lem_data = set(lem_data)
    bower.fit(lem_data)
    return bower 

def bow_text(text,bow_model,df):
    if df == True:
        text_coded_list = []
        lemms = lematize(text,df=True)
        for lemm in lemms:
            matrix = bow_model.transform(lemm)
            matrix = matrix.toarray()
            text_coded_list .append(matrix)
        result = []
        for code in text_coded_list:
            sum_text = np.zeros((code.shape[1:]))
            for idx in range(0,len(code)):
                sum_text = sum_text + code[idx]
            result.append(sum_text)
        return result
    else:
        lemm = lematize(text,df=False)
        text_coded = bow_model.transform(lemm)  
        text_coded = text_coded.toarray()
        sum_text = np.zeros((text_coded[0].shape))
        for idx in range(0,len(text_coded)):
            sum_text = sum_text + text_coded[idx]
        return sum_text

def generate_df(text,bow_model):
    tokens_list = []
    from nltk import word_tokenize
    for row in(text):
        texto_limpio = limpia_texto(row)
        token = word_tokenize(texto_limpio)
        tokens_list.append(token)
    stops = nostops(tokens_list,df=True)
    lemms = lematize(text,df=True)
    matrices = bow_text(text,bow_model,df=True)
    #print(len(tokens_list),len(stops),len(lemms),len(matrices))
    return pd.DataFrame({'raw_data':text,
                        'tokens':tokens_list,
                         'no stops words':stops,
                         'lematization':lemms,
                         'text coded':matrices})