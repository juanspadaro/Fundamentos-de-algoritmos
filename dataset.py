#Integrantes: Nicolas Viñolo, Juan Spadaro y Victoria Sosa.

from arbol import Arbol

#------Función auxiliar---------
#La siguiente función nos permitirá calcular la distancia euclidiana posteriormente
def distancia_euclidiana(x1, x2, y1, y2): 
        x1 = float(x1)
        x2 = float(x2)
        y1 = float(y1)
        y2 = float(y2)
        distancia_euclidiana = ((x1 - x2)**2 + (y1 - y2)**2)**(1/2)
        return distancia_euclidiana
#-------------------------------

#Implementamos la clase DataSetArboreo
class DataSetArboreo:
    #Constructor de objetos de la clase
    def __init__(self, filename):
        
        # Creamos la lista árboles y abrimos el archivo
        arboles = []
        archivo_csv = open(filename, encoding='UTF-8')

        # Salteamos la primera linea que tiene el encabezado 
        archivo_csv.readline()

        # Recorremos el resto de las lineas
        # N (cantidad de árboles) iteraciones leyendo cada una de las líneas
        for linea in archivo_csv:
            #Eliminamos las comillas y la coma que separa el nombre de las calles (y no los campos)
            linea = linea.replace('"', "") #si el valor trae una comilla, reemplazarlo por un campo vacío.
            linea = linea.replace(", ", " ") #si el valor trae una coma con un espacio, reemplazarlo solo por un espacio.
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
                   
            # Creamos el nuevo arbol y le brindamos sus atributos
            arbol_nuevo = Arbol(
                longitud, latitud, id_arbol, altura, especie, barrio, calle, chapa1)

            # Agregamos el arbol a la lista de árboles
            arboles.append(arbol_nuevo)

        # Cerramos el archivo
        archivo_csv.close()
        # Guardamos el dataset
        self._dataset = arboles
        
        
    #Método que devuelve cantidad de árboles   
    def tamano(self):
       return len(self._dataset)
   
    
    #Método que devuelve el conjunto de especies de los árboles
    def especies(self):
       # Creamos un conjunto para evitar duplicados (por eso no se utiliza listas)
        especies = set()
       # Para cada arbol, agrega su especie al conjunto solo si esta no se encuentra
        for arbol in self._dataset:
            especies.add(arbol.especie())
        #Devuelve el conjunto de especies
        return especies
    
    
    #Método que devuelve el conjunto de barrios de los árboles
    def barrios(self):
        #Creamos un conjunto para evitar duplicados
        barrios = set()
        # Para cada árbol, agregamos el barrio al conjunto
        for arbol in self._dataset:
            barrios.add(arbol.barrio())
        #Devuelve el conjunto de barrios
        return barrios

 
    #Método que devuelve los árboles de la especie indicada
    def arboles_de_la_especie(self, especie):
        #Creamos una lista vacía
        arboles_especie = []
        # Realizamos N iteracciones para recorrer todos los árboles
        for arbol in self._dataset:
            #Si la especie del arbol es igual a la especie indicada, se agrega a la lista
            if arbol.especie() == especie:
                arboles_especie.append(arbol)
        #Devuelve los árboles filtrados
        return arboles_especie 
    
    
    #Método que devuelve un diccionario que indica la cantidad de ejemplares
    #para aquellas especies que tienen como mínimo la cantidad indicada
    def cantidad_por_especie(self, minimo):
        #Creamos un diccionario
        diccionario = dict()
        # Realizamos N iteracciones para recorrer todos los árboles
        for arbol in self._dataset:
            #Calculamos la cantidad de arboles de la especie
            cantidad_de_la_especie = len(self.arboles_de_la_especie(arbol.especie()))
            #Si la cantidad de árboles de cierta especie supera o iguala al minimo indicado,
            #se agrega al diccionario la llave especie junto con su valor asociado cantidad
            if cantidad_de_la_especie >= minimo:
                diccionario[arbol.especie()] = cantidad_de_la_especie
        #Devuelve el diccionario 
        return diccionario
    
    
    #Método que devuelve el arbol mas cercano
    def arbol_mas_cercano(self, especie, lat, lng):
        #Creamos una variable y una lista vacias
        distancia_minima= None
        arbol_distancia_minima = []
        # Realizamos N iteracciones para recorrer todos los árboles
        for arbol in self._dataset:
            #Si la especie del arbol es igual a la indicada
            if arbol.especie() == especie:
                #Calculamos la distancia euclideana entre el arbol y la latitud y longitud indicada
                arbol_distancia = distancia_euclidiana(lat, arbol.latitud(), lng, arbol.longitud())
                #Asignamos la distancia del primer arbol de la especie a la variable distancia_minima y guardamos el arbol
                if distancia_minima == None:
                    distancia_minima = arbol_distancia
                    arbol_distancia_minima = arbol
                #Si la distancia del arbol es menor a la distancia minima, guardamos el arbol y la nueva distancia minima
                if arbol_distancia < distancia_minima:
                     distancia_minima = arbol_distancia
                     arbol_distancia_minima = arbol
        #Devuelve el arbol con menor distancia             
        return arbol_distancia_minima

   
    #Método que genera un txt con los arboles de cierta especie dentro de cierta altura     
    def exportar_por_especie_y_altura(self, filename, especie, alt_min, alt_max):
        #Creamos una lista vacía
        lista_de_arboles = []
        # Realizamos N iteracciones para recorrer todos los árboles
        for arbol in self._dataset:
            #Si la especie es la indicada y el árbol cumple con los requisitos de altura, agregamos el árbol a la lista
            if arbol.especie() == especie and arbol.altura() >= alt_min and arbol.altura() <= alt_max:
               lista_de_arboles.append(arbol)
        #Ordenamos la lista en forma ascendente según la altura
        lista_de_arboles.sort(key=lambda arbol: arbol.altura())
        #Generamos el txt               
        txt= open(filename, "w+")
        for arbol in lista_de_arboles:
           linea = str(arbol.altura()) +";"+ arbol.__repr__()  + "\n"
           txt.write(linea ) 
        txt.close()

