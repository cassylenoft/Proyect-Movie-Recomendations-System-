import pickle, joblib, gzip
import pandas as pd


with open('chat/english_version/objects/vectorizer.pkl','rb') as file:
    vectorizer = pickle.load(file)

modelo_prediction = joblib.load('chat/english_version/models/english_model.joblib')
encoder = pickle.load(open('chat/english_version/objects/encoder.pkl','rb'))
with gzip.open('recomendation_model/pickle_objects_saved/comprimed_df.pkl','rb') as f:
    df = pickle.load(f)


def get_similarity():
    data = pd.read_json('recomendation_model/data/proccesed_data/df_to_similarity')
    from sklearn.feature_extraction.text import CountVectorizer
    cv = CountVectorizer(max_features=7942 , stop_words='english')
    vector = cv.fit_transform(data['tags'].values.astype('U'))
    from sklearn.metrics.pairwise import cosine_similarity
    similarity  = cosine_similarity(vector)
    return similarity

similarity = get_similarity()
