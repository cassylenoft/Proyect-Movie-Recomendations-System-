<h1> Titulo de proyecto: Proyect-Movie-Recomendations-System- </h1>
This is a Data Science Project that includes a movie recomendation model, a chatbot and a web page
Uses a machine learning movie to recommend a movie from a local database <br> <br> 
Este proyecto incluye una web realizada con Flask, chatbot y un sistema de recomendación, en ella que puedes explorar información de películas. la información de las películas pertenece a un <a href="https://www.kaggle.com/datasets/shivamb/netflix-shows">dataset</a> con mas de 7000 títulos.
<br></br>

<samp>
  <h2>
    Tecnologías usadas
  </h2>
</samp>

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) ![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white) ![Flask](	https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white) ![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white) ![Anaconda](https://img.shields.io/badge/Anaconda-%2344A833.svg?style=for-the-badge&logo=anaconda&logoColor=white)





<samp>
  <h2>
    Técnicas
  </h2>
</samp>
<h4> Ciencia de datos </h4> 
    
<a href="https://github.com/Jossellu/Proyect-Movie-Recomendations-System-/blob/main/recomendation_model/notebooks/EDA_1.ipynb">
Análisis exploratorio de datos </a> <br>   
<a href="https://github.com/Jossellu/Proyect-Movie-Recomendations-System-/blob/main/recomendation_model/notebooks/proccesing_data_2.ipynb">
Procesamiento de datos </a> <br>    
<a href="https://github.com/Jossellu/Proyect-Movie-Recomendations-System-/blob/main/recomendation_model/notebooks/generating_recom_sys_3.ipynb">
Sistema de recomendación de películas </a>    
   

<h4> Machine Learning </h4>

<a href="https://github.com/Jossellu/Proyect-Movie-Recomendations-System-/blob/main/chat/notebooks/Model1.ipynb">
Clasificación de texto (chatbot) </a> <br>  
<a href="https://github.com/Jossellu/Proyect-Movie-Recomendations-System-/blob/main/chat/notebooks/creating_statmens_for_model.ipynb">
Clasificación de texto (géneros de películas) </a> 

<h4> Desarrollo Web </h4>
<a href="https://github.com/Jossellu/Proyect-Movie-Recomendations-System-/blob/main/app.py">
Backend </a> <br>
 <a href="https://pypi.org/project/bing-image-downloader/">
Descargador de imágenes para los posters</a>  

  <h2>
    Detalles de proyecto
  </h2>
</samp>
    <p>
        
La página inicial _/_ es un chat con el que puedes interactuar,se trata de un modelo de ML de clasificación de texto. Este modelo puede identificar palabras usadas para saludar, despedirse, dar las gracias, pedir información o algo para ver. 

![Chat-demo](https://github.com/Jossellu/Proyect-Movie-Recomendations-System-/blob/main/demos/gift-chat.gif?raw=true) <br>

La página principal _/home_ por defecto te muestra películas con su título, imagen y año de salida. Las imágenes en esta pagina son las únicas incluidas en el repositorio _archivos locales_, para cualquier otra miniatura, las imágenes son descargadas con el módulo <a href="https://pypi.org/project/bing-image-downloader/">*bing_image_downloader*</a>, se hace uso de este módulo para no tener que descargar manualmente para el proyecto estas imágenes y  aligerar el peso del repositorio. <br>

![Home-demo](https://github.com/Jossellu/Proyect-Movie-Recomendations-System-/blob/main/demos/gift-demo-home.gif) <br>

Para cada película mostrada en esta página, puedes hacer click y redirigirte a otra pagina _/view_ en esta puedes ver mas información de la película, entre ella título, año de salida, géneros, cast, director. Ésta otra página también incluye un sistema de recomendación basada en la similitud de sus _features_ (género,cast,descripción), desarrollada con _CosineSimilarity_ que calcula el coseno del ángulo entre los vectores.

![View-demo](https://github.com/Jossellu/Proyect-Movie-Recomendations-System-/blob/main/demos/gift-demo-view.gif) <br>

Puedes ingresar palabras claves para filtrar las películas mostradas por su género, éste también es un modelo ML de clasificación de texto. 

![Credits-demo](https://github.com/Jossellu/Proyect-Movie-Recomendations-System-/blob/main/demos/gift-credits.gif) <br>

    
  </p>

<samp>
  <h2>
    Créditos
  </h2>
  <p>
    Colaboradores: <br>
    <a href="https://www.linkedin.com/in/carlosm1698" > Carlos Ángel Mayorga López </a> <br>
    <a href="https://www.linkedin.com/in/josé-luis-lópez-rodriguez-aa9a16181/" > José Luis López Rodriguez
  </a>

  </p>
</samp>

