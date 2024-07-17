import bing_image_downloader
from pathlib import Path
from bing_image_downloader import downloader
import re 
import os

def get_images(df):
    titles = df['title'].values.tolist()
    titles_clean=[]
    for name in titles:
        title_clean = only_letters_numbers(name)
        titles_clean.append(title_clean)
    
    year = df['release_year'].values.tolist()
    type = df['type'].values.tolist()
    bin_searchs = [titles_clean[i] + ' ' + type[i] + ' ' + str(year[i]) + ' poster' for  i in range(0,len(titles_clean))] 
    images_dir = []
    for name in bin_searchs:
        path = f'/css/images/bing_images/{name}'
        if os.path.exists(path):
            extension = image_extension(directory=str(path)[1:])
            images_dir.append(str(path)+f'/Image_1{extension}')
        else:
            downloader.download(name,limit=1,adult_filter_off=True, force_replace=False, timeout=60,
                            output_dir='css/images/bing_images/')
            extension = image_extension(directory=str(path)[1:])
            images_dir.append(str(path)+f'/Image_1{extension}')
        
    return images_dir

def only_letters_numbers(texto):
    # keep just text and numbers
    texto_limpio = re.sub(r'[^a-zA-Z0-9]', ' ', texto)
    return texto_limpio

def image_extension(directory):
  contenido = os.listdir(directory)
  for idx, l  in enumerate(contenido[0]):
    if l == '.':
      extension = contenido[0][idx:]
  return extension

print(os.listdir('css/images/bing_images/House of Cards TV Show 2018 poster'))