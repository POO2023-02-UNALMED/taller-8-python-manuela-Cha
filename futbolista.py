from deportista import Deportista
from persona import Persona

class Futbolista(Persona, Deportista):
    listaFutbolistas = []
    
    def __init__(self, nombre:str, edad:int, altura:str, sexo:str, anosPracticando:int,golesMarcados:int, tarjetasRojas:int, piernaHabil:str):
        Persona.__init__(self,nombre,edad,altura,sexo)
        Deportista.__init__(self,anosPracticando)
        self._golesMarcados = golesMarcados
        self._tarjetasRojas = tarjetasRojas
        self._piernaHabil = piernaHabil
        
        Futbolista.listaFutbolistas.append(self)
        
    def getGolesMarcados(self):
        return self._golesMarcados
    def setGolesMarcados(self, goles):
        self._golesMarcados = goles
    
    def getTarjetasRojas(self):
        return self._tarjetasRojas
    def setTarjetasRojas(self, tarjetas):
        self._tarjetasRojas = tarjetas
    
    def getPiernaHabil(self):
        return self._piernaHabil
    def setPiernaHabil(self, pierna):
        self._piernaHabil = pierna
        
    def __str__(self):
        return f"Mi nombre es {super().getNombre()} soy profesional en el deporte {super().getDeporte()} Tengo {super().getEdad()} años de edad y llevo {super().getAñosPracticando()} años en el deporte"
