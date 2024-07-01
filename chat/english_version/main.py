import colorama
from colorama import Fore, Back, init
init(autoreset=True)

from procces_entry import get_prediction, show_random_movies

def run():
    while True:
        bot = Fore.CYAN
        user = Fore.GREEN
        system = Fore.RED
        
        
        entry = input(user+f'you ->: ')

        if entry.lower == 'exit':
            break
        else:
            category = get_prediction(entry)
            print(bot+'okay showing stuff for you choice: {}'.format(category))
            randoms = show_random_movies(category=category)
            print(system+str(randoms))
            

        
if __name__ == "__main__":
    print(Fore.CYAN+'Welcome im chatbot!')
    print(Fore.RED+'exit -> write exit')
    run()