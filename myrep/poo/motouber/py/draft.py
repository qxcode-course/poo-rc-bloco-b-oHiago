class Pessoa:
    def __init__(self, nome: str, dinheiro: int):
        self.__nome = nome
        self.__dinheiro = dinheiro

    def __str__(self):
        return f"{self.__nome}:{self.__dinheiro}"
    
    def getNome(self):
        return self.__nome

    def getDinheiro(self):
        return self.__dinheiro
    
    def pagar(self, valor: int):
        if valor > self.__dinheiro:
            valorPago = self.__dinheiro
            self.__dinheiro = 0
            return valorPago
        elif valor <= self.__dinheiro:
            self.__dinheiro -= valor
            return valor
    
    def receber(self, valor:int):
        self.__dinheiro += valor

class Moto:
    def __init__(self):
        self.__custo =  0 
        self.__motorista =  None
        self.__passageiro =  None
    
    def __str__(self):
        return f"Cost: {self.__custo}, Driver: {self.__motorista}, Passenger: {self.__passageiro}"
     
    def setMotorista(self, motorista: Pessoa):
        self.__motorista = motorista
    
    def setPassageiro(self, passageiro: Pessoa):
        self.__passageiro = passageiro

    def drive(self, distancia: int):
            self.__custo += distancia
    
    def leavePass(self):
        passageiro = self.__passageiro
        motorista = self.__motorista
        custo = self.__custo
        if passageiro.getDinheiro() < custo:
            print("fail: Passenger does not have enough money")
        passageiro.pagar(custo)
        motorista.receber(custo)
        print(f"{passageiro.getNome()}:{(passageiro.getDinheiro())} left")
        self.__custo = 0
        self.__passageiro = None


def main():
    moto = Moto()

    while True:
        line = input()
        print("$" + line)
        args = line.split()
        command = args[0]

        if command == "end":
            break

        elif command == "show":
            print(moto)

        elif command ==  "setDriver":
            nome = args[1]
            dinheiro = int(args[2])
            motorista = Pessoa(nome, dinheiro)
            moto.setMotorista(motorista)

        elif command == "setPass":
            nome = args[1]
            dinheiro = int(args[2])
            passageiro = Pessoa(nome, dinheiro)
            moto.setPassageiro(passageiro)

        elif command == "drive":
            distancia = int(args[1])
            moto.drive(distancia)

        elif command == "leavePass":
            moto.leavePass()

main()
