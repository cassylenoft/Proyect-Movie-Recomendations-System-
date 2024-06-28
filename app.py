from flask import (Flask, request, render_template, make_response, redirect, jsonify)
from chat.english_version import procces_entry
import json

app = Flask(__name__, template_folder='./template',static_folder='./css',)
with open('./data/moives_home.json') as file:
        home=json.load(file)


@app.route('/')
def hello():
    initial_bot_ms = 'write whatever\nyou want to watch'

    return render_template('home.html',initial_bot_ms=initial_bot_ms,home=home)

@app.route('/chat',methods=['GET','POST'])
def get_text():

    texto = request.form.get('texto','')
    category,recomend_df = get_bot_response()
    respuesta = {'categoria': category,
                'movies':recomend_df,
                'imagen_url':"/css/images/alien_poster.jpg"
            }
    return render_template('response_3.html', **respuesta)



@app.route('/view',methods=['GET','POST'])
def view():

    dicc = {}
    info = request.form.get('info')
    for i in home:

        if i['title'] == info:
            for name in ['title','director','release_year','genres_reduction','cast','posters','description']:
                 value = i[name]
                 dicc[name] = value


    return render_template('view_template.html',info=info,dicc=dicc)

@app.route('/view/recommend',methods=['GET','POST'])
def recommend():
    df1= procces_entry.df
    dicc = {}
    title = request.form.get('info')
    title = df1[df1['title'] == title]
    print(title)
    for name in ['title','director','release_year','genres_reduction','cast','description']:
         texto = str(title[name].values)
         texto_sin = quitar_caracteres_especiales(texto)
         dicc[name] = texto_sin
    
    # title = df1[df1['title'] == title]
    # print(f' este el title {title}')


    return render_template('view_recommend.html',dicc=dicc)


def quitar_caracteres_especiales(texto):
    caracteres_a_eliminar = ['[', ']', "'", '"']
    
    # Itera sobre cada caracter a eliminar y reemplázalo con una cadena vacía
    for caracter in caracteres_a_eliminar:
        texto = texto.replace(caracter, '')
    
    return texto



def get_bot_response():
    texto = request.form.get('texto','')
    category = procces_entry.get_prediction(texto)
    recomend_df = procces_entry.show_random_movies(category)
    recomend_df = recomend_df.reset_index(drop=True)


    return category, recomend_df


if __name__ == " __main__":
    app.run(debug=True)
