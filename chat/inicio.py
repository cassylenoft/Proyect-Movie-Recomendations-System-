
#runs thechatbot
# import analize_input
# import get_response 
# import give_response
from colorama import Fore, init, Back

init(autoreset=True)
print(Fore.CYAN+'***Hola soy chatbot escribe aqui debajo: ')
print(Fore.RED+Back.WHITE+'NOTA: si deseas salir del chat escribe salir o exit')
def run():
    while True:
        global texto_input
        texto_input = input(Fore.YELLOW+Back.BLACK+'you ->: ')
        if (texto_input.lower() == 'salir') or (texto_input.lower() == 'exit'):
            break
        #print(texto_input)
        print(Fore.CYAN+Back.BLACK+'bot ->: [respuesta del bot]')
        # analize_input()
        # give_response()
if __name__ == "__main__":
    run()