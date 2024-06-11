from unidecode import unidecode
import re
import nltk
from nltk import word_tokenize
nltk.download('punkt') #para tokenizar
from nltk.stem import SnowballStemmer #para lematizar

def only_text(text):
    no_acentos=unidecode(text)
    minusculas = no_acentos.lower()
    return re.sub(r'[^a-zA-Z\s]', '', minusculas)

def tokenize(text):
    return word_tokenize(text)

def lematize(text):
    stemmer = SnowballStemmer('spanish')
    return stemmer.stem(text)

def stemizar(tokens): #only for data frame
    stemmer = SnowballStemmer('spanish')
    stemms = []
    for token in tokens:
        stemms.append(stemmer.stem(token))
    return stemms

def generate_bowler(text):
    full_data = (' ').join(text.tolist())
    clean_text = only_text(full_data)
    tokens = tokenize(clean_text)
    lemms = stemizar(tokens)
    from sklearn.feature_extraction.text import CountVectorizer
    model = CountVectorizer()
    model.fit(lemms)
    setattr(model,'show_full_data',clean_text)
    return model



def generate_df(bowler_model,text):
    import pandas as pd
    import numpy as np
    df = pd.DataFrame()



    df['original text'] = text
    df['text_clean'] = df.apply(lambda x: (only_text(x['original text'])),axis=1)
    df['tokens'] = df.apply(lambda x: (word_tokenize(x['text_clean'])),axis=1)
    df['lemms'] = df.apply(lambda x: (stemizar(x['tokens'])),axis=1)

    matrices_list = []
    for lem in df['lemms']:
        matrices = bowler_model.transform(lem).toarray()
        no_matrices = len(matrices)
        shape_matrix = matrices[0].shape
        sum_matrices = np.zeros(shape_matrix)
        for matrix in matrices:
            sum_matrices = sum_matrices + matrix
        matrices_list.append(sum_matrices)
    
    df['matrices'] = matrices_list

    return df