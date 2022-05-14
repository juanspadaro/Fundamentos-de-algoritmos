from arbol import Arbol

#Implementamos la clase DataSetArboreo
class DataSetArboreo:
    #Constructor de objetos de la clase
    def __init__(self, filename):
        
        # Creamos la lista de árboles y leemos el archivo
        arboles = []
        archivo_csv = open(filename, encoding='UTF-8')

        # Salteamos la primera linea que tiene el encabezado 
        archivo_csv.readline()

        # Recorremos el resto de las lineas
        for linea in archivo_csv:
            #Eliminamos las comillas y la coma que separa el nombre de las calles (y no los campos)
            linea = linea.replace('"', "") #si el valor trae una comilla, reemplazarlo por un campo vacío.
            linea = linea.replace(", ", " ") #si el valor trae una coma, reemplazarlo por un espacio.
            # Separamos cada uno de los campos en variables
            campos = linea.split(",")
            longitud = campos[0]
            latitud = campos[1]
            id_arbol = campos[3]
            altura = campos[4]
            especie = campos[10]
            barrio = campos[15]
            calle = campos[17]
            chapa1 = campos[18]
            chapa2 = campos[19]
           
            # Creamos el nuevo arbol y le brindamaos sus atributos
            arbol_nuevo = Arbol(
                longitud, latitud, id_arbol, altura, especie, barrio, calle, chapa1, chapa2)

            # Agregamos el arbol a la lista de árboles
            arboles.append(arbol_nuevo)

        # Cerramos el archivo
        archivo_csv.close()
        self._filename = arboles # no debería ir un return arboles???
        
        
    #Método que devuelve cantidad de árboles del dataset d
    def tamano(self):
       return "La cantidad de arboles es: " + str(len(self._filename)) + "."
   
    #Método que devuelve el conjunto de especies de los árboles del dataset d
    def especies(self):
        # Creamos un set para evitar duplicados (por eso no se utiliza listas)
        especies = set()
        # Para cada arbol, agregamos su especie al set
        for arbol in self._filename:
            especies.add(arbol._especie)
        return especies # notar que tendremos las especies como categorías únicas (es decir, no se repiten)
    
    #Método que devuelve el conjunto de barrios de los árboles del dataset d
    def barrios(self):
        #Creamos un set para evitar duplicados
        barrios = set()
        # Para cada árbol, agregamos el barrio a la lista
        for arbol in self._filename:
            barrios.add(arbol._barrio)
        return barrios # notar que tendremos el mismo comportamiento que el mencionado para especies
    
    #Método que devuelve los árboles del dataset d para la especie indicada
    def arboles_de_la_especie(self, especie):
        #Creamos la lista 
        especie_filtrada=[]
        # N (cantidad de árboles) iteraciones
        for arbol in self._filename:
            #Si la especie de cada arbol es igual a la especie indicada, se agrega a la lista
            if arbol._especie == especie:
                especie_filtrada.append(arbol)
        return especie_filtrada
      #Mejorar la representacion    
    
    #Método que devuelve un diccionario que indica la cantidad de ejemplares
    #de cada especie existente en el dataset d, pero incluyendo solamente a 
    #las especies que tienen como mínimo la cantidad de ejemplares indicado
    def cantidad_por_especie(self):
    # Creamos el diccionario y las claves
        key_list=list(self.especies().split(','))
        values_list= list((self.arboles_de_la_especie(key_list).split(',')))
        for key in key_list:
            values_list.append(len(self.arboles_de_la_especie(key).split(',')))
            dicc_especies= dict(zip(key_list, values_list))
        return dicc_especies    
       
    #Método que devuelve el arbol mas cercano
    def arbol_mas_cercano(self, especie, lat, lng):
        if especie in self.especies():
            distancia_minima= None
            arbol_distancia_minima = []
        for arbol in self._filename:
            if arbol._especie == especie:
                arbol_distance = ((lat-arbol._latitud)**2+ (lng-arbol._longitud)**2)** (1/2)
                if distancia_minima == None:
                    distancia_minima = arbol_distance
                    arbol_distancia_minima = arbol
                if arbol_distance < distancia_minima:
                     distancia_minima = arbol_distance
                     arbol_distancia_minima = arbol
        return arbol_distancia_minima
    #mejorar la sintaxis seguro hay cosas al pedo    
    
    #Método que genera un archivo con nombre filename que incluye el listado 
    #de los árboles del dataset d de la especie indicada cuya altura es mayor
    #o igual a alt_min y menor o igual a alt_maxdevuelve el arbol mas cercano    
    def exportar_por_especie_y_altura(self, especie, alt_min, alt_max):
        lista_de_arboles = []
        for arbol in self._filename:
            if  arbol._altura >= alt_min and arbol._altura <= alt_max:
                lista_de_arboles.append(arbol)
        return lista_de_arboles.sort(key=(arbol._altura))
     

    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Cargamos el archivo y vamos realizando algunos print a modo de observar los resultados
d = DataSetArboreo('arbolado-publico-lineal-2011.csv')

#Veamos la cantidad de arboles
print(d.tamano())

#Veamos todos los nombres de las especies que hay
print(d.especies())
#Veamos la cantidad total de especies que hay
print('En total hay', len(d.especies()), 'especies', end ='.')

#Veamos todos los nombres de los barrios que hay
print(d.barrios())
#Veamos la cantidad total de barrios que hay
print('En total hay', len(d.barrios()), 'barrios', end ='.')

#Veamos los árboles del dataset d para la especie Salix humboldtiana
print(d.arboles_de_la_especie('Salix humboldtiana'))

#Veamos la cantidad por especie mayores a los ejemplares que solicitamos
print(d.cantidad_por_especie(20000))

#Veamos el árbol de la especie indicada que está más cercano al punto 
# hlat, lngi en el dataset d, usando la distancia euclidiana:
print(d.arbol_mas_cercano('Citrus aurantium', -34.55472, -58.44583))

#Veamos lo que obtenemos con la función creada previamente para una determinada especie
print(d.exportar_por_especie_y_altura("Fraxinus pennsylvanica", 5,100000))

