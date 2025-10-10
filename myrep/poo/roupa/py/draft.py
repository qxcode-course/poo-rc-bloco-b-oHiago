class Camisa:
    def __init__(self): 
        self.__tamanho = ""   

    def getTamanho(self) -> str:
        return self.__tamanho

    def setTamanho(self, valor: str) -> bool:
        if valor not in ["PP", "P", "M", "G", "GG", "XG"]:
            print("fail: Valor inválido, tente PP, P, M, G, GG ou XG")
            return False
        self.__tamanho = valor
        return True

def main():
    camisa = Camisa()
    
    while True:

        line = input()
        print("$"+line)
        args = line.split()

        if args[0] == "end":
            break
        elif args[0] == "size":
            valor = args[1]
            camisa.setTamanho(valor)
        elif args[0] == "show":
            print("size: (",camisa.getTamanho(),")",sep="") 
        else:
            print("fail: comando não encontrado")

main()

