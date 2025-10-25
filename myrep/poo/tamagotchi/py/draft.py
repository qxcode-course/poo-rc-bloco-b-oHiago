class Pessoa:
    def __init__(self, nome: str):
        self.__nome = nome
    
    def get_nome(self):
        self.__nome = value
    
    def set_nome(self, value: str):
        self.__nome == value
    
    def __str__(self):
        return self.__nome

class Moto:
    def __init__(self):
        self.cliente: Pessoa | None = None 
    
    def inserir(self, cliente: Pessoa) -> bool:
        if self.cliente != None:
            print("moto ocupada")
            return False 
        self.cliente = cliente 
        return True

    def remover(self) -> Pessoa | None:
        if self.cliente == None:
            print("moto vazia")
            return None
        aux: Pessoa = self.cliente 
        self.cliente = None
        return aux

    def __str__(self):
        return f"moto:{self.cliente}"