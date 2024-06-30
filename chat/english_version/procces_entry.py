from .load_objects import vectorizer, modelo_prediction, encoder, df #note if you want to run this script mainly please delete dot rigth before .load_objects, then put it back for running web 
#[['title','type','cast','genres_reduction','description']]
import re

def get_prediction(text):
    matrix = vectorizer.transform([text]).toarray()
    prediction = modelo_prediction.predict(matrix.reshape(1,-1))
    prediction_encoded = encoder.inverse_transform(prediction)
    category = prediction_encoded
    category = only_letters(str(category))
    
    return category

def show_random_movies(category):
    if category in ['old','recent']:
        if category == 'old':
            random_movies = df[df[category] == 1].sample(n=9)
            return random_movies
        else:
            random_movies = df[df['old'] == 0].sample(n=9)
            return random_movies

    elif category in ['short','long']:
        if category == 'short':
            random_movies = df[df[category] == 1].sample(n=9)
            return random_movies
        else:
            random_movies = df[df['short'] == 0].sample(n=9)
            return random_movies

    elif category in ['local','foregin']:
        if category == 'foregin':
            random_movies = df[df[category] == 1].sample(n=9)
            return random_movies
        else:
            random_movies = df[df['foregin'] == 0].sample(n=9)
            return random_movies

    elif category in  ['action',
       'anime', 'classic', 'comedy', 'documental', 'drama', 'family',
       'fantasy', 'foregin', 'lgbt', 'music', 'religion', 'romance', 'show',
       'sports', 'suspense', 'short', 'movie']:
        for name in ['action',
       'anime', 'classic', 'comedy', 'documental', 'drama', 'family',
       'fantasy', 'foregin', 'lgbt', 'music', 'religion', 'romance', 'show',
       'sports', 'suspense', 'short', 'movie']:
            if category == name:
                random_movies = df[df[category] == 1].sample(n=9)
        return random_movies
    else:
        print('sorry category not avaliable')

def only_letters(input_string):
    # Patrón regex para encontrar solo letras (mayúsculas y minúsculas)
    patron = re.compile(r'[^a-zA-Z]+')
    
    # Aplicar el patrón para limpiar el string
    resultado = patron.sub('', input_string)
    return resultado

if __name__ == "__main__":
    texto = input('ingresa un texto: ')
    category = get_prediction(texto)
    print(type(category))
    print('here youve some to watch for your category: {}'.format(category))
    df_random = show_random_movies(category=category)
    print(df_random)
    
