class Persona:
    def __init__(self, nombre:str, edad:int, altura:str, sexo:boolean):
        self._nombre = nombre
        self._edad = edad
        self._altura = altura
        self._sexo = sexo
        
    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nom):
        self._nombre = nom
    
    def getEdad(self):
        return self._edad
    
    def setEdad(self, edad):
        self._edad = edad
    
    def getAltura(self):
        return self._altura
    
    def setAltura(self, altura):
        self._altura = altura
    
    def getSexo(self):
        return self._sexo
    
    def setSexo(self, sexo):
        self._sexo = sexo
  
