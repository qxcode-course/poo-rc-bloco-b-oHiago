class Bateria:
    def __init__(self, capacidade):
        self.__capacidade: int = capacidade 
        self.__carga: int = capacidade 
    def get_carga(self):
        return self.__carga
    def get_capacidade(self):
        return self.__capacidade
    def set_carga(self, valor: int):
        self.__carga = valor
    def set_capacidade(self, max:int):
        self.__capacidade = max
    def __str__(self):
        



class Carregador: 
    def __init__(self, potencia):
        self.__potencia: int = potencia

class Notebook:
    def __init__(self):
        self.__ligado: bool = False 
        self.__bateria: Bateria | None = None
        self.__carregador: Carregador | None = None

    def 

        
