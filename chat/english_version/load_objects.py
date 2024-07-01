import pickle, joblib

with open('/home/ackerman/Proyect-Movie-Recomendations-System-/chat/english_version/objects/vectorizer.pkl','rb') as file:
    vectorizer = pickle.load(file)
#vectorizer= pickle.load(open('../objects/vectorizer.pkl','rb'))
modelo_prediction = joblib.load('/home/ackerman/Proyect-Movie-Recomendations-System-/chat/english_version/models/english_model.joblib')
encoder = pickle.load(open('/home/ackerman/Proyect-Movie-Recomendations-System-/chat/english_version/objects/encoder.pkl','rb'))
df = pickle.load(open('/home/ackerman/Proyect-Movie-Recomendations-System-/recomendation_model/pickle_objects_saved/comprimed_df.pkl','rb'))
symilarity = pickle.load(open('/home/ackerman/Proyect-Movie-Recomendations-System-/recomendation_model/pickle_objects_saved/comprimed_similarity.pkl','rb'))

