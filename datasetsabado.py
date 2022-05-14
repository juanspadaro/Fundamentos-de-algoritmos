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
            linea = linea.replace('"', "")
            linea = linea.replace(", ", " ")
            # Separamos cada uno de los campos en variables
            campos = linea.split(",")
            longitud = campos[0]
            latitud = campos[1]
            id_arbol = campos[2]
            altura = campos[3]
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
        self._filename = arboles
        
    #Método que devuelve cantidad de árboles   
    def tamano(self):
       return "La cantidad de arboles es: " + str(len(self._filename)) + "."
   
    #Método que devuelve el conjunto de especies de los árboles
    def especies(self):
        # Creamos un set para evitar duplicados
        especies = set()
        # Para cada arbol, agregamos su especie a la lista
        for arbol in self._filename:
            especies.add(arbol._especie)
        return especies
    
    #Método que devuelve el conjunto de barrios de los árboles
    def barrios(self):
        #Creamos un set para evitar duplicados
        barrios = set()
        # Para cada árbol, agregamos el barrio a la lista
        for arbol in self._filename:
            barrios.add(arbol._barrio)
        return barrios
    
    #Método que devuelve los árboles de la especie indicada
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
        
    def exportar_por_especie_y_altura(self, especie,alt_min, alt_max):
        lista_de_arboles = []
        for arbol in self._filename:
            if arbol._especie == especie and arbol._altura >= alt_min and arbol._altura <= alt_max:        
                lista_de_arboles.append(arbol)
        return lista_de_arboles

      
   
    
 
    
 #   def cantidad_por_especie(self):
        # Creamos el diccionario
        #Creamos las claves
   #     key_list=list(self.especies().split(','))
    #    values_list= list((self.arboles_de_la_especie(key_list).split(',')))
        # for key in key_list:
        #     values_list.append(len(self.arboles_de_la_especie(key).split(',')))            
    
    #    dicc_especies= dict(zip(key_list, values_list))
        
    #    return dicc_especies    
            
    
    ## y así con el resto de los métodos a implementar, o cualquier
    ## función auxiliar que se necesite definir.
    

d = DataSetArboreo('C:/AAMIM/Fundamentos de Algoritmos/TP2/arbolado-publico-lineal-2011.csv')
#print(d.tamano())
#print(d.especies())
#print(d.barrios())
#print(d.arboles_de_la_especie('Salix humboldtiana'))
j = d.arbol_mas_cercano('Citrus aurantium', -34.55472, -58.44583)
k = d.exportar_por_especie_y_altura("Fraxinus pennsylvanica", 5,100000)