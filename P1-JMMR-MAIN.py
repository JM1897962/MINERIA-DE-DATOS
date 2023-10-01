import requests  # Realiza las solicitudes en HTTP
from bs4 import BeautifulSoup  # Analiza el contenido del HTML
import re  # Trabaja con expresiones regulares
import urllib.request  # Descargar los datos
url = "https://datos.cdmx.gob.mx/tl/dataset/certificados-de-defuncion-sedesa"


#        |Analiza la cosa|PeticionGet|                                  |Busca que termine en .csv| |Obtiene el link wiiii
csv_link = BeautifulSoup(requests.get(url).text, 'html.parser').find('a', href=re.compile(r'\.csv$')).get('href')

# La descarga+-
urllib.request.urlretrieve(csv_link, "Defunciones-Covid.csv")

#Juan Manuel Martínez Ramírez
#1897962
