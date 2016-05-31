from bs4 import BeautifulSoup
import requests
import wget

url = input('Ingrese la url: ')
page = requests.get(url)

patron_link = raw_input('Ingrese el patron que tienen los links de interes: ')

bs = BeautifulSoup(page.content, "lxml")
a = bs.find_all("a")

data = []
links = []
for link in a:
    data.append(link.get('href'))

for link in data:
    if patron_link in str(link):
        print link
        links.append(link)

'''
Para descargar los archivos se recorre la lista y se usa wget.download()
------------------------------------------------------------------------

en este paso pueden, haber links que tienen un formato distinto y dan errores
hay que quitarlos.

para eso primero recorremos la lista de links y los mostramos en pantalla para
identificar posibles patrones de error.

luego eliminamos los que tengan ese patron de error y luego los descargamos.
'''

patron_error = raw_input('Ingrese el patron de error en los links: ')
links_buenos = []
for link in links:
    if patron_error not in link:
        links_buenos.append(link)

url_base = input('Ingrese la url base: ')
for link in links_buenos:
    if 'xls' in link:
        wget.download(url_base + link , out='')