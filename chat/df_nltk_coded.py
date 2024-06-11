#this module converts a dataframe with nltk pourposses

from text2bow import *
import numpy as np
import pandas as pd

df = pd.read_excel('data/raw_data/excel chat.xlsx')
#print(df['informacion'].shape)
#text = (' ').join(df['informacion'])
#print(text)
#generate_tokens().get_tokens(text,show=True)




def step1(df_text_series):
    global tokens_list
    tokens_list = []
    for row in df_text_series:
        tokens_list.append(generate_tokens().get_tokens(row,df=True))
    #return tokens_list


#tokens_df = step1(df['saludos']) 


def step2():
    global no_stopwords_list
    no_stopwords_list = []
    for row in tokens_list:
        no_stopwords_list.append(del_stopwords().no_stopwords(row))
    return no_stopwords_list

def step3():
    global stemmed_list
    stemmed_list = []
    for row in no_stopwords_list:
        stemmed_list.append(lematization().lematize(row))
    return stemmed_list
# 
# print(len(no_stopwords_list),len(stemmed_list),sep='\n**************')


from sklearn.feature_extraction.text import CountVectorizer

def df_by_step(bow_model,df_text_series):
    step1(df_text_series)
    step2()
    step3()
    #to_fit = full_data_stemm().stem(df_text_series,df_token=df_token)
    #bow_model.fit(to_fit)
    global codigo
    codigos = []
    for row in stemmed_list:
        codigo = bow_model.transform(row)
        codigo = codigo.toarray()
        codigos.append(codigo)
    dict_to_df = {'tokens': tokens_list,
              'no stopwords':no_stopwords_list,
              'lematization':stemmed_list,
              'text coded': codigos
                } 
    return pd.DataFrame(dict_to_df)

# model_bow = CountVectorizer()
# to_fit = full_data_stemm().stem(text_from_tokens=df['saludos'],df_token=False)
# model_bow.fit(to_fit)
# df_by_step(bow_model=model_bow,df_text_series=df['saludos'])





