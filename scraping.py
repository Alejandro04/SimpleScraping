import requests
from bs4 import BeautifulSoup

url = 'https://lanacionweb.com/tecnologia/'

# Extraer el HTML de la página
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

listings = soup.find_all('div', {'id': 'tdi_24'})

# Almacenar los datos en una lista
data_list = []
for data in listings:
    title = data.find('h3').text
    description = data.find('div', {'class': 'td-excerpt'}).text
    date = data.find('time').text
    descendants = [descendant.strip() for descendant in data.descendants if isinstance(descendant, str)]
    data_list.append({'descendants': descendants})

# Imprimir los datos almacenados en la lista
for data in data_list:
    for descendant in data['descendants']:
        print(' -', descendant)