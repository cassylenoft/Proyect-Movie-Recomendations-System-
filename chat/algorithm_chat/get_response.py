




def give_response(predictions_list):
    rcm,b,c = 0, 0, 0
    print(predictions_list)
    predict_basic, predict_rcm, predict_rcm_82acc, rcnn_predict, rcnn2_predict = predictions_list[0],predictions_list[1],predictions_list[2],predictions_list[3],predictions_list[4]
    print(f' las predicc las recibio:')
    print(predict_basic, predict_rcm, predict_rcm_82acc, rcnn_predict,rcnn2_predict,sep='\n')
    if (predict_rcm == 0) or (rcnn_predict == 0):  
        rcm = 0     
        print('prediccion: critica')
    elif (rcnn2_predict == 1) or (rcnn_predict == 1):
        rcm = 1    
        print('prediccion: pop')
    elif (rcnn2_predict == 2 ) or (rcnn_predict == 2):
        rcm = 3    
        print('prediccion: recientes')
    elif (rcnn2_predict == 3) or (rcnn_predict == 3):
        rcm = 4    
        print('prediccion: culto')
    elif (rcnn2_predict == 4) or (rcnn_predict == 4):
        rcm = 5   
        print('prediccion: genero')
    elif(rcnn2_predict == 5) or (rcnn_predict == 5):
        rcm = 6   
        print('prediccion: owner')
    elif (rcnn2_predict == 6) or (rcnn_predict == 6):
        rcm = 7
        print('prediccion: similitud')
    # else: 
    #     print('No match for rcm')

    if predict_basic == 0:
        b,c = 0, 1
        print('prediccion de basic: saludo')
    elif predict_basic == 1:
        print('prediccion de basic: presentacion')
        b,c = 1, 1 
    elif predict_basic == 2:
        b,c = 2,1
        print('prediccion de basic: informacion')
    elif predict_basic == 3:
        b,c = 3,1
        print('prediccion de basic: recomendacion')
    else: 
        print('No match for any')
        return 1, 0, 0
    return c, b, rcm

if __name__ == "__main__":
    predictions_list = input('ingresar lista')
    give_response(predictions_list)
