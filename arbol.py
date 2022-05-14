#Integrantes: Nicolas Viñolo, Juan Spadaro y Victoria Sosa.

"""
TODO: Aquí escribiremos la definición de nuestra clase Arbol según los requerimietnos del enunciado:
- Ya se cuenta con el Constructor (__init__)
- Operaciones para:
    - conocer la longitud
    - cononcer la latitud
    - conocer la especie
    - conocer el barrio
    - conocer la dirección
    - representación como string (__repr__)
"""

#Clase que representa los arboles
class Arbol:
    
    # Constructor de objetos de tipo Arbol
    def __init__(self,longitud,latitud,id_arbol,altura,especie,barrio,calle,chapa1,chapa2):
        self._longitud = float(longitud)
        self._latitud = float(latitud)
        self._id_arbol = id_arbol
        self._altura = float(altura)
        self._especie = especie 
        self._barrio = barrio
        self._calle = calle
        self._chapa1 = chapa1
        self._chapa2 = chapa2

    # Devuelve la longitud del arbol
    def longitud(self):
        return self._long
    
    # Devuelve la latitud del arbol
    def latitud(self):
        return self._lat
    
    # Método que devuelve la especie del arbol
    def especie(self):
        return self._especie

    # Devuelve el barrio del arbol
    def barrio(self):
        return self._barrio
    
    # Devuelve la direccion del arbol   
    def direccion(self):
        return self._calle + " " + self._chapa1
    
    # Nos permite representar al arbol como un string
    def __repr__(self):
        return "(" + self.especie() +' ' + "@" + self.direccion() + ")"


