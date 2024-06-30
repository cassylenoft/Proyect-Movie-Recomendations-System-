import bing_image_downloader
from pathlib import Path
from bing_image_downloader import downloader

def get_images(df):
    titles = df['title'].values.tolist()
    year = df['release_year'].values.tolist()
    type = df['type'].values.tolist()
    bin_searchs = [titles[i] + ' ' + type[i] + ' ' + str(year[i]) + ' poster' for  i in range(0,len(titles))] 
    images_dir = []
    for name in bin_searchs:
        path = Path(f'/css/images/bing_images/{name}')
        if path.is_dir():
            print('el directorio existe no se descargo nada')
            continue
        else:
            print('el directorio no existia se creo uno y se descargo la imagen')
            downloader.download(name,limit=1,
                                adult_filter_off=True, force_replace=False, timeout=60,output_dir='/home/ackerman/Proyect-Movie-Recomendations-System-/css/images/bing_images/')
            images_dir.append(str(path)+'/Image_1.jpg')
    return images_dir