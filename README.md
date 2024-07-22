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
<a href="https://github.com/Jossellu/Proyect-Movie-Recomendations-System-/blob/main/chat/notebooks/creating_statmens_for_model.ipynb">
Backend </a> <br>
 <a href="https://github.com/Jossellu/Proyect-Movie-Recomendations-System-/blob/main/chat/notebooks/Model1.ipynb">
Descargador de imágenes para los posters</a> <br>  


<samp>
  <h2>
    Demos
  </h2>
</samp>
<img source="Proyect-Movie-Recomendations-System-/demos/gift-chat.gif"> </img>

![Chat-demo](/Proyect-Movie-Recomendations-System-/demos/gift-chat.gif) <br>
![Home-demo](/Proyect-Movie-Recomendations-System-/demos/gift-demo-home.gif) <br>
![View-demo](/Proyect-Movie-Recomendations-System-/demos/gift-demo-view.gif) <br>
![Credits-demo](Proyect-Movie-Recomendations-System-/demos/gift-credits.gif)
<samp>
  <h2>
    Detalles de proyecto
  </h2>
</samp>
    <p>
        
La pagina inicial (/) es un chat con el que puedes interactuar pues se trata de un modelo de ML de clasificación de texto. este modelo puede identificar palabras usadas para saludar, despedirse, dar las gracias, pedir información o función, pedir ver algo para ver. 

la pagina principal (/home) por defecto te muestra películas con su título, imagen y año de salida. Las imágenes en esta pagina son las únicas incluidas en el repositorio, para cualquier otra miniatura son descargadas con el modulo *bing_image_downloader* LINK, se hace uso de este modulo para no tener que descargar manualmente para el proyecto estas imágenes y  aligerar el peso del repositorio.
Para cada película mostrada en esta página, puedes hacer click en la miniatura para redirigirte a otra pagina (/view) y ver mas información de la peli entre ella titulo, año de salida, géneros, cast, director etc. esta otra pagina también incluye un sistema de recomendación basada en la similitud de sus features, desarrollada con *CosineSimilarity* que calcula el coseno del angulo entre los vectores- 
    </p>