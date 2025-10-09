class Camisa:
    def __init__(self, tamanho: str):
        self.__tamanho = ""

    def getTamanho(self) -> str:
        return self.__tamanho

    def setTamanho(self, valor: str) -> bool:
        if not (valor == "PP" or valor == "P" or valor == "M" or valor == "G" or valor == "GG" or valor == "XG"):
            print("valor invalido, tente PP, P, M, G, GG ou XG")
            return False
        self.__tamanho = valor
        return True

camisa = Camisa()

while camisa.getTamanho() == "":
        print("digite seu tamanho de roupa:")
        tamanho = input()
        if camisa.setTamanho(tamanho):
            break

        print("parabens, voce comprou uma roupa tamanho", camisa.getTamanho())