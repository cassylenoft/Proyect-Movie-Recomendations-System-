from flask import (Flask, request, render_template, make_response, redirect, jsonify)
from chat.english_version import procces_entry
import json
import re
from recomendation import get_recomendation
from download_images import get_images


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
    images=get_images(recomend_df)
    respuesta = {'categoria': category,
                'movies':recomend_df,
                'image':images            }
    return render_template('response_3.html', **respuesta)



@app.route('/view',methods=['GET','POST'])
def view():
    df1= procces_entry.df
    dicc = {}
    title = request.form.get('info')
    title = df1[df1['title'] == title]
    
    for name in ['title','director','release_year','genres_reduction','cast','description']:    
        texto = str(title[name].values)
        texto_sin = no_corcher(texto)
        dicc[name] = texto_sin

    dicc2={}
    similars = get_recomendation(title=dicc['title'],show_count=3)
    dicc2 ={'r1': no_corcher(similars[0]['title']),
         'r2': no_corcher(similars[1]['title']),
         'r3': no_corcher(similars[2]['title'])                                   
    }
    return render_template('view_template.html',dicc=dicc,dicc2=dicc2)

@app.route('/view/recommend',methods=['GET','POST'])
def recommend():
    df1= procces_entry.df
    dicc = {}
    title = request.form.get('info')
    title = df1[df1['title'] == title]
   
    for name in ['title','director','release_year','genres_reduction','cast','description']:
        texto = str(title[name].values)
        texto_sin = no_corcher(texto)
        dicc[name] = texto_sin
    dicc2={}
    similars = get_recomendation(title=dicc['title'],show_count=3)
    dicc2 ={'r1': no_corcher(similars[0]['title']),
         'r2': no_corcher(similars[1]['title']),
         'r3': no_corcher(similars[2]['title'])                                   
    }

    
    
    

    return render_template('view_recommend.html',dicc=dicc,dicc2=dicc2)


def no_corcher(texto):
    caracteres_a_eliminar = ['[', ']','"',"'"]
    
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
