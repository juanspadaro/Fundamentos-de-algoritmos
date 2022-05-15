#Integrantes: Nicolas Viñolo, Juan Spadaro y Victoria Sosa.

#Clase que representa los arboles
class Arbol:
    
    # Constructor de objetos de tipo Arbol
    def __init__(self,longitud,latitud,id_arbol,altura,especie,barrio,calle,chapa1):
        self._longitud = float(longitud)
        self._latitud = float(latitud)
        self._id_arbol = int(id_arbol)
        self._altura = int(altura)
        self._especie = especie 
        self._barrio = barrio
        self._calle = calle
        self._chapa1 = chapa1

    # Método que devuelve la longitud del arbol
    def longitud(self):
        return self._longitud
    
    # Método que devuelve la latitud del arbol
    def latitud(self):
        return self._latitud
    
    # Método que devuelve la altura del arbol
    def altura(self):
        return self._altura
    
    # Método que devuelve la especie del arbol
    def especie(self):
        return self._especie

    # Método que devuelve el barrio del arbol
    def barrio(self):
        return self._barrio
    
    # Método que devuelve la dirección del arbol   
    def direccion(self):
        return self._calle + " " + self._chapa1
    
    # Nos permite representar al arbol como un string
    def __repr__(self):
        return "(" + self.especie() + "@" + self.direccion() + ")"

