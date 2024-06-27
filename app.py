from flask import (Flask, request, render_template, make_response, redirect)
from chat.english_version import procces_entry
import json
#from procces_entry import get_prediction, show_random_movies
app = Flask(__name__, template_folder='./template',static_folder='./css',)
with open('./data/moives_home.json') as file:
        home=json.load(file)


@app.route('/')
def hello():
    initial_bot_ms = 'write whatever\nyou want to watch'
    
    return render_template('home.html',initial_bot_ms=initial_bot_ms,home=home)

@app.route('/chat',methods=['GET','POST'])
def get_text():
    # user_ip = request.cookies.get('user_ip')
    # return render_template('chat.html',user_ip = user_ip)
    texto = request.form.get('texto','')
    category,f1 = get_bot_response()
    respuesta = {'categoria': category,
                'movie1':f1,
                'imagen_url':"/css/images/alien_poster.jpg"
            }
    return render_template('response_3.html', **respuesta)
    #return 'el texto ingresado es: {}; la respuesta del bote es {}'.format(texto,respuesta)


@app.route('/view')
def show():
     return 

def get_bot_response():
    texto = request.form.get('texto','')
    category = procces_entry.get_prediction(texto)
    f1 = procces_entry.show_random_movies(category)

    return category, f1


if __name__ == " __main__":
    app.run(debug=True)
