from flask import (Flask, request, render_template, make_response, redirect)
from chat.english_version import procces_entry
#from procces_entry import get_prediction, show_random_movies
app = Flask(__name__, template_folder='./template')

@app.route('/')
def hello():
    return render_template('chatgpt.html')

@app.route('/chat',methods=['GET','POST'])
def get_text():
    # user_ip = request.cookies.get('user_ip')
    # return render_template('chat.html',user_ip = user_ip)
    texto = request.form.get('texto','')
    respuesta = get_bot_response()
    return render_template('response.html', respuesta=respuesta)
    #return 'el texto ingresado es: {}; la respuesta del bote es {}'.format(texto,respuesta)

def get_bot_response():
    texto = request.form.get('texto','')
    category = procces_entry.get_prediction(texto)
    procces_entry.show_random_movies(category)
    return category 

    
# def index():
#     return render_template('chat.html', resultado="")

# @app.route('/procesar', methods=['POST'])
# def procesar():
#     texto_ingresado = request.form['texto']
#     # Aquí puedes agregar la lógica para obtener un comentario del bot según el texto ingresado
#     comentario_bot = obtener_comentario_bot(texto_ingresado)  # Define esta función según tu necesidad
#     resultado = f"Texto ingresado: {texto_ingresado}. {comentario_bot}"
#     return render_template('chat.html', resultado=resultado)

# def obtener_comentario_bot(texto):
#     # Esta función puede ser modificada según la lógica que quieras implementar
#     # Aquí se puede simular un comentario del bot basado en el texto ingresado
#     return "Aquí obtendrás un comentario del bot basado en el texto ingresado."

if __name__ == " __main__":
    app.run(debug=True)
