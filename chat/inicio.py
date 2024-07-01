import sys

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

from colorama import Fore, init, Back


  
textos, predicciones_list =  [], []
init(autoreset=True)
print(Fore.CYAN+'***Hola soy chatbot escriebe aqui debajo: ')
print(Fore.RED+Back.WHITE+'NOTA: si deseas salir del chat escribe salir o exit')
def run():
    control = 0
    caux = 0
    while True:
        #print(control,caux)
        texto_input = input(Fore.YELLOW+Back.BLACK+'you ->: ')
        if texto_input.lower() in ['exit','salir']:
            break
        if control > 2:
            print(Fore.CYAN+Back.BLACK+'bot ->: [ey recuerdas que mis funciones son: recomendarte algo para ver, no puedo ayudarte con nada mas]')
            control = 0
            continue
            
        if caux == 0:
            control = 0
            
            
       
        from algorithm_chat.prediction_from_models import collect_predictions
        predictions = collect_predictions(texto=texto_input)

        textos.append(texto_input.lower())
        predicciones_list.append(predictions[1])
        

        from algorithm_chat.get_response import give_response
        caux, basic, rcm = give_response(predictions_list=predictions)
        if basic == 0:
            #saludar
            print(Fore.CYAN+Back.BLACK+'bot ->: [Saludos]')
            
        elif basic == 1:
            #presentar
            print(Fore.CYAN+Back.BLACK+'bot ->: [mucho gusto mi nombre es bot]')
            
        elif basic == 2:
            #informar
            print(Fore.CYAN+Back.BLACK+'bot ->: [Saludos, mis funciones son recomendarte peliculas escribe que te gustaria ver]')
            
        elif basic == 3:
            #analizar comentario
            #infomar que tipo de recomendaciones puedo dar
            print(Fore.CYAN+Back.BLACK+'bot ->: [claro puedo hacerte recomendaciones por genero o lo que quieras solo comenta que buscas]')
           


if __name__ == "__main__":
    run()
    import pandas as pd 
    dicc = {'text': textos,
        'predicciones model1' : predicciones_list}
    print(pd.DataFrame(dicc))

