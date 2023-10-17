class Deportista:
    def __init__(self, anosPracticando:int,deporte= "Futbol"):
        self._deporte = deporte
        self._añosPracticando = anosPracticando
        
    def getDeporte(self):
        return self._deporte
    
    def setDeporte(self, deporte):
        self._deporte = deporte
    
    def getAñosPracticando(self):
        return self._añosPracticando
    
    def setAñosPracticando(self, años):
        self._añosPracticando = años
