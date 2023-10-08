import requests
from bs4 import BeautifulSoup
import re
import urllib.request
url = "https://datos.cdmx.gob.mx/tl/dataset/certificados-de-defuncion-sedesa"

csv_link = BeautifulSoup(requests.get(url).text, 'html.parser').find('a', href=re.compile(r'\.csv$')).get('href')

urllib.request.urlretrieve(csv_link, "Defunciones-Covid.csv")

#Juan Manuel Martínez Ramírez
#1897962
