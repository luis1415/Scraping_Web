### Scraping Web

##### Luis Bermudez

- Este codigo esta en python 2.7 los input, que son urls se deben poner entre comillas simples ''.

- Este codigo selecciona todos los `<a href=""></a>` de una pagina.

- El patron que pide el programa es un patron que aparezca en el href de los links de interes.

- El patron de error es un patron que hace que la descarga se cancele.


###### Descarga
> Para descargar los archivos se recorre la lista y se usa wget.download()


en este paso pueden, haber links que tienen un formato distinto y dan errores
hay que quitarlos.

para eso primero recorremos la lista de links y los mostramos en pantalla para
identificar posibles patrones de error.

luego eliminamos los que tengan ese patron de error y luego los descargamos.
