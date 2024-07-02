import pandas as pd
import pickle, gzip
with gzip.open('/home/ackerman/Proyect-Movie-Recomendations-System-/recomendation_model/pickle_objects_saved/comprimed_df.pkl','rb') as f:
    df = pickle.load(f)
# df = pickle.load(open('/home/ackerman/Proyect-Movie-Recomendations-System-/recomendation_model/pickle_objects_saved/comprimed_df.pkl','rb'))
with gzip.open('/home/ackerman/Proyect-Movie-Recomendations-System-/recomendation_model/pickle_objects_saved/comprimed_similarity.pkl','rb') as f:
    symilarity = pickle.load(f)
#symilarity = pickle.load(open('/home/ackerman/Proyect-Movie-Recomendations-System-/recomendation_model/pickle_objects_saved/comprimed_similarity.pkl','rb'))
def index_from_title(title:str): 
    return df[df['title'] == title].index[0]

def title_from_index(list_movies_indexes:list):
    titles_df = pd.DataFrame()
    for i in list_movies_indexes:
        titles_df = pd.concat([titles_df, pd.Series(df.iloc[i,0:10])],axis=1,ignore_index=True)
    return titles_df

def get_recomendation(title:str, show_count:int):
    index = index_from_title(title)
    idx_similarity = sorted(list(enumerate(symilarity[index])),reverse=True,key=lambda idx:idx[1])[1:show_count+1] #gets major similarity for a title and its idx in dataframe
    movies_indexes = [elem[0] for elem in idx_similarity]
    df = title_from_index(movies_indexes)
    return df






