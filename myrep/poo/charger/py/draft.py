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
        
class Carregador: 
    def __init__(self, potencia):
        self.__potencia: int = potencia
    def get_potencia(self):
        return self.__potencia

class Notebook:
    def __init__(self):
        self.__ligado: bool = False 
        self.__bateria: Bateria | None = None
        self.__carregador: Carregador | None = None
        self.status: str

    def get_bateria (self):
        return self.__bateria

    def get_carregador (self):
        return self.__carregador

    def set_bateria (self, bateria: Bateria):
        self.__bateria = bateria

    def set_carregador (self, carregador: Carregador):
        self.__carregador = carregador

    def temCarregador(self):
        if self.__carregador == None:
            print("fail:sem carregador")
            return

    def turn_on(self):
        if self.__ligado == False:
            print("fail: não foi possível ligar")

    def use(self):
        if self.__ligado == False:
            print("fail: desligado")   

    def __str__(self):
        status: str = ""
        if self.__ligado ==  True:
            status = "ligado"
        else:
            status = "desligado"

        if self.__carregador == None:
            return f"Notebook: {status}"
        else: 
            return f"Notebook: {status}, Bateria {self.__carregador}"

        
def main():
    notebook = Notebook()

    while True:

        line = input()
        print("$" + line)
        args:list[str] = line.split(" ")

        if args[0] == "end":
            break
        if args[0] == "show":
            print(notebook)
        if args[0] == "turn_on":
            notebook.turn_on()
        if args[0] == "use":
            notebook.use()

main()        
