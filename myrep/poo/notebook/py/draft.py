class Bateria:
    def __init__(self, capacidade):
        self.__capacidade: int = capacidade 
        self.__carga: int = capacidade 

class Carregador: 
    def __init__(self, potencia):
        self.__potencia: int = potencia

class Notebook:
    def __init__(self):
        self.__ligado: bool = False 
        self.__bateria: Bateria | None = None
        self.__carregador: Carregador | None = None

    def 

        
