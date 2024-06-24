import streamlit as st

# Definición de estilos con Streamlit
st.markdown(
    """
    <style>
        body {
            background-color: #141414;
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
            color: #ffffff;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
            padding: 20px;
            overflow: hidden;
        }

        h1 {
            font-size: 2.5em;
            margin-bottom: 20px;
            text-align: center;
        }

        .recommendation-box {
            background-color: #2c2c2c;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            width: 80%;
            max-width: 400px;
            margin-top: 20px;
        }

        input[type="text"] {
            width: 100%;
            padding: 10px;
            margin-bottom: 10px;
            border: none;
            border-radius: 5px;
            font-size: 1em;
        }

        button {
            background-color: #e50914;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 1em;
            width: 100%;
        }

        button:hover {
            background-color: #f40612;
        }

        .result {
            margin-top: 20px;
            font-size: 1.2em;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Título de la aplicación
st.title('Recomendador de Películas')

# Caja de recomendación
st.markdown('<div class="recommendation-box">', unsafe_allow_html=True)

# Campo de entrada de texto
pregunta = st.text_input('¿Qué tipo de película te gustaría ver?', '')

# Botón para obtener recomendación
if st.button('Obtener Recomendación'):
    resultado = f'Recomendación para "{pregunta}": \n **Inception**'
else:
    resultado = ''

# Mostrar el resultado
st.markdown(f'<div class="result">{resultado}</div>', unsafe_allow_html=True)

# Cierre de la caja de recomendación
st.markdown('</div>', unsafe_allow_html=True)