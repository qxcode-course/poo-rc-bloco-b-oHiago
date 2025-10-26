class Pessoa:
    def __init__ (self, nome: str, age: int):
        self.__nome = nome
        self.__age = age
    def get_nome(self):
        return self.__nome
    def get_age(self):
        return self.__age
    def set_nome(self, value: str):
        self.__nome = value
    def set_age(self, idade:int):
        self.__age = idade
    def __str__(self):
        return f"{self.get_nome()}:{self.get_age()}"

class Moto:
    def __init__(self, potencia = 1):
        self.cliente: Pessoa | None = None
        self.potencia = potencia
        self.time = 0

    def inserir(self, cliente: Pessoa) -> bool:
        if self.cliente != None:
            print ("fail: busy motorcycle")
            return False
        self.cliente = cliente
        return True 

    def remover(self) -> Pessoa | None:
        if self.cliente == None:
            print("fail: empty motorcycle")
            return None
        aux: Pessoa = self.cliente 
        self.cliente = None
        return aux 
    def buyTime(self, time: int):
        self.time += time 

    def drive(self, time: int):
        if self.time == 0:
            print("fail: buy time first")
            return 
        if self.cliente == None:
            print("fail: empty motorcycle")
            return
        if self.cliente.get_age() > 10:
            print("fail: too old to drive")
            return
        if time <= self.time:
            self.time -= time
            return
        if time >= self.time:
            print (f"fail: time finished after {self.time} minutes")
            self.time = 0
            return


        
    def honk(self):
        print("P"+"e" * self.potencia+"m")

    def __str__(self):
        return f"power:{self.potencia}, time:{self.time}, person:({self.cliente if self.cliente != None else "empty"})"

def main():
    moto = Moto()

    while True:
        line = input()
        print ("$" + line)
        args:list[str] = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "show":
            print (moto)
        elif args[0] == "init":
            moto = Moto(int(args[1]))
        elif args[0] == "enter":
            nome = str(args[1])
            age = int(args[2])
            pessoa = Pessoa(nome,age)
            moto.inserir(pessoa)
        elif args[0] == "leave":
            pessoa = moto.remover()
            if pessoa:
                print(pessoa)
        elif args[0] == "buy":
            moto.buyTime(int(args[1]))
        elif args[0] == "drive":
            moto.drive(int(args[1]))
        elif args[0] == "honk":
            moto.honk()

main() 
