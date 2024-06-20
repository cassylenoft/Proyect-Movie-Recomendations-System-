from modules_data_proccessing.text_2_bow_stopsTrue import generate_bowler, text_to_matrix
#Proyect-Movie-Recomendations-System
import pandas as pd
import numpy as np
import joblib #cargar modelos de sklearn
import tensorflow as tf





def collect_predictions(texto):

    #basic model
    basic_dff = pd.read_csv('/home/ackerman/Proyect-Movie-Recomendations-System-/chat/data/proccesed_data/chat_texts.csv')
    basic_bowler = generate_bowler(basic_dff['text'])
    basic_model = joblib.load('/home/ackerman/Proyect-Movie-Recomendations-System-/chat/models/basic_model_upgraded.joblib')

    # recomendation clasificator model
    rcm_dff = pd.read_json('/home/ackerman/Proyect-Movie-Recomendations-System-/chat/data/proccesed_data/recomend_clasification.json')
    rcm_bowler = generate_bowler(rcm_dff['text'])
    rcm_model_1 = joblib.load('/home/ackerman/Proyect-Movie-Recomendations-System-/chat/models/recomendation_clasificator.joblib')
    rcm_model_82acc =joblib.load('/home/ackerman/Proyect-Movie-Recomendations-System-/chat/models/recomendation_82acc') 
    rcm_model_nn = tf.keras.models.load_model('/home/ackerman/Proyect-Movie-Recomendations-System-/chat/models/modelo_deep.h5')
    recm_model_nn2 =  tf.keras.models.load_model('/home/ackerman/Proyect-Movie-Recomendations-System-/chat/models/modelo_deep_98acc.h5')
    #codify text input
    text_coded_basic = text_to_matrix(bow_model=basic_bowler,text=texto)
    text_coded_rcm = text_to_matrix(bow_model=rcm_bowler,text=texto)

    #getting predictions
    predict_basic = basic_model.predict(text_coded_basic.reshape(1,366))
    prediction_probs = basic_model.predict_proba(text_coded_basic.reshape(1,366))

    predict_rcm_1 = rcm_model_1.predict(text_coded_rcm.reshape(1,512))
    predict_probs1 = rcm_model_1.predict_proba(text_coded_rcm.reshape(1,512))
    
    predict_rcm_82acc = rcm_model_82acc.predict(text_coded_rcm.reshape(1,512))
    predict_probs2 = rcm_model_82acc.predict_proba(text_coded_rcm.reshape(1,512))
    
    predict_rcm_nn = rcm_model_nn.predict(text_coded_rcm.reshape(1,1,512))
    predict_rcm_nn = np.squeeze(predict_rcm_nn)
    #predict_probs3 = rcm_model_nn.predict(text_coded_rcm.reshape(1,1,512))

    predict_rcm_nn2 = rcm_model_nn.predict(text_coded_rcm.reshape(1,1,512))
    predict_rcm_nn2 = np.squeeze(predict_rcm_nn2)
    #predict_probs4 = rcm_model_nn.predict(text_coded_rcm.reshape(1,1,512))
    
    # #basic
    # print(f'prediccion de basic mode: {predict_basic}') 
    # print(f'saludo: {round(prediction_probs[0][0]*100,2)}%, presentacion: {round(prediction_probs[0][1]*100,2)}%, informacion: {round(prediction_probs[0][2]*100,2)}%, recomendacion: {round(prediction_probs[0][3]*100,2)}%')
    
    # #rcm
    # print(f'prediccion de rcm 1: {predict_rcm_1}')
    # print(f'critica: {round(predict_probs1[0][0]*100,2)}%, pop: {round(predict_probs1[0][1]*100,2)}%, recientes: {round(predict_probs1[0][2]*100,2)}%, culto: {round(predict_probs1[0][3]*100,2)}%, genero: {round(predict_probs1[0][4]*100,2)}%, owner: {round(predict_probs1[0][5]*100,2)}%, similitud: {round(predict_probs1[0][6]*100,2)}%')

    # print(f'prediccion de rcm 84 acc: {predict_rcm_82acc}')
    # print(f'critica: {round(predict_probs2[0][0]*100,2)}%, pop: {round(predict_probs2[0][1]*100,2)}%, recientes: {round(predict_probs2[0][2]*100,2)}%, culto: {round(predict_probs2[0][3]*100,2)}%, genero: {round(predict_probs2[0][4]*100,2)}%, owner: {round(predict_probs2[0][5]*100,2)}%, similitud: {round(predict_probs2[0][6]*100,2)}%')

    # print(f'prediccion de rcm nn: {np.max(predict_rcm_nn)}')
    # print(f'critica: {round(predict_rcm_nn[0][0][0]*100,2)}%, pop: {round(predict_rcm_nn[0][0][1]*100,2)}%, recientes: {round(predict_rcm_nn[0][0][2]*100,2)}%, culto: {round(predict_rcm_nn[0][0][3]*100,2)}%, genero: {round(predict_rcm_nn[0][0][4]*100,2)}%, owner: {round(predict_rcm_nn[0][0][5]*100,2)}%, similitud: {round(predict_rcm_nn[0][0][6]*100,2)}%')


    return list((predict_basic, predict_rcm_1, predict_rcm_82acc, np.argmax(predict_rcm_nn),np.argmax(predict_rcm_nn2)))
    # if predict_basic + predict_rcm_82acc == 0:
    #         print('prediccion: critica')
    # elif predict_basic + predict_rcm_82acc == 1:
    #     print('prediccion: pop')
    # elif predict_basic + predict_rcm_82acc == 2:
    #     print('prediccion: recientes')
    # elif predict_basic + predict_rcm_82acc == 3:
    #     print('prediccion: culto')
    # elif predict_basic + predict_rcm_82acc == 4:
    #     print('prediccion: genero')
    # elif predict_basic + predict_rcm_82acc == 5:
    #     print('prediccion: owner')
    # elif predict_basic + predict_rcm_82acc == 6:
    #     print('prediccion: similitud')
    # else: 
    #     print('No match for rcm')

    # if predict_basic == 0:
    #     print('prediccion de basic: saludo')
    # elif predict_basic == 1:
    #     print('prediccion de basic: presentacion')
    # elif predict_basic == 2:
    #     print('prediccion de basic: informacion')
    # elif predict_basic == 3:
    #     print('prediccion de basic: recomendacion')
    # else: 
    #     print('No match for basic')

if __name__ == "__main__":
    texto = input('ingresa un texto: ')
    collect_predictions(texto)