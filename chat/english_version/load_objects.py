import pickle, joblib, gzip

with open('/home/ackerman/Proyect-Movie-Recomendations-System-/chat/english_version/objects/vectorizer.pkl','rb') as file:
    vectorizer = pickle.load(file)
#vectorizer= pickle.load(open('../objects/vectorizer.pkl','rb'))
modelo_prediction = joblib.load('/home/ackerman/Proyect-Movie-Recomendations-System-/chat/english_version/models/english_model.joblib')
encoder = pickle.load(open('/home/ackerman/Proyect-Movie-Recomendations-System-/chat/english_version/objects/encoder.pkl','rb'))
with gzip.open('/home/ackerman/Proyect-Movie-Recomendations-System-/recomendation_model/pickle_objects_saved/comprimed_df.pkl','rb') as f:
    df = pickle.load(f)
#df = pickle.load(open('/home/ackerman/Proyect-Movie-Recomendations-System-/recomendation_model/pickle_objects_saved/comprimed_df.pkl','rb'))
with gzip.open('/home/ackerman/Proyect-Movie-Recomendations-System-/recomendation_model/pickle_objects_saved/comprimed_similarity.pkl','rb') as f:
    symilarity = pickle.load(f)
#symilarity = pickle.load(open('/home/ackerman/Proyect-Movie-Recomendations-System-/recomendation_model/pickle_objects_saved/comprimed_similarity.pkl','rb'))

