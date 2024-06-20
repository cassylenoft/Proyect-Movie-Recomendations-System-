import pandas as pd
import pickle
import colorama
from colorama import Fore, Back, init
import random

with open('./pickle_objects_saved/df.pkl','rb') as f:
    df = pickle.load(f)

with open('./pickle_objects_saved/similarity.pkl','rb') as f:
    similarity = pickle.load(f)

def run():
    instr = Fore.YELLOW
    system = Fore.CYAN
    random_color = random.choice([Fore.GREEN,Fore.LIGHTMAGENTA_EX,Fore.MAGENTA,Fore.LIGHTBLUE_EX])
    init(autoreset=True)
    print(instr+'Welcome to system R\n Please pick a category to give random recomendations then choose one you like') 
    categories = ['short','long','old','recent','local','foregin','action',
       'anime', 'classic', 'comedy', 'documental', 'drama', 'family',
       'fantasy', 'foregin', 'lgbt', 'music', 'religion', 'romance', 'show',
       'sports', 'suspense']
    print(system+f'avaliable categories: {categories}')
    category = input(instr+'please write your option :')
    print(instr+f'for {category} here you go these randoms titles')
    print(system+str(get_random_movie(category=category)))
    movie_selected = input(instr+'please type title of the movie you rather: ')
    
    movies_recomended = get_recomendation(title=movie_selected, show_count=3)
    print(random_color+str(movies_recomended.iloc[0]))
    print(random_color+str(movies_recomended.iloc[1]))
    print(random_color+str(movies_recomended.iloc[2]))



def index_from_title(title:str): 
    return df[df['title'] == title].index[0]

def title_from_index(list_movies_indexes:list):
    for i in list_movies_indexes:
        print(df.iloc[i,0:10])

def get_recomendation(title:str, show_count:int):
    index = index_from_title(title)
    idx_similarity = sorted(list(enumerate(similarity[index])),reverse=True,key=lambda idx:idx[1])[1:show_count+1] #gets major similarity for a title and its idx in dataframe
    movies_indexes = [elem[0] for elem in idx_similarity]
    title_from_index(movies_indexes)

def get_random_movie(category: str):
    if category in ['old','recent']:
        if category == 'old':
            random_movies = df[df[category] == 1].sample(n=3)
            return pd.DataFrame(random_movies[['title','type','cast','genres_reduction','description']])
        else:
            random_movies = df[df[category] == 0].sample(n=3)
            return pd.DataFrame(random_movies[['title','type','cast','genres_reduction','description']])

    elif category in ['short','long']:
        if category == 'short':
            random_movies = df[df[category] == 1].sample(n=3)
            return pd.DataFrame(random_movies[['title','type','cast','genres_reduction','description']])
        else:
            random_movies = df[df[category] == 0].sample(n=3)
            return pd.DataFrame(random_movies[['title','type','cast','genres_reduction','description']])

    elif category in ['local','foregin']:
        if category == 'foregin':
            random_movies = df[df[category] == 1].sample(n=3)
            return pd.DataFrame(random_movies[['title','type','cast','genres_reduction','description']])
        else:
            random_movies = df[df[category] == 0].sample(n=3)
            return pd.DataFrame(random_movies[['title','type','cast','genres_reduction','description']])

    elif category in  ['action',
       'anime', 'classic', 'comedy', 'documental', 'drama', 'family',
       'fantasy', 'foregin', 'lgbt', 'music', 'religion', 'romance', 'show',
       'sports', 'suspense', 'short', 'movie']:
        for name in ['action',
       'anime', 'classic', 'comedy', 'documental', 'drama', 'family',
       'fantasy', 'foregin', 'lgbt', 'music', 'religion', 'romance', 'show',
       'sports', 'suspense', 'short', 'movie']:
            if category == name:
                random_movies = df[df[category] == 1].sample(n=3)
        return pd.DataFrame(random_movies[['title','type','cast','genres_reduction','description']])
    else:
        print('sorry category not avaliable')

if __name__ == "__main__":
    run()