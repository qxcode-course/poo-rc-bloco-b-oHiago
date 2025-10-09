class Camisa:
    def __init__(self, tamanho: str):
        self.__tamanho: int = ""

    def getTamanho(self) -> str:
        return self.__tamanho

    def setTamanho(self, valor: str):
        if not (valor == "PP" or valor == "P" or valor == "M" or valor == "G" or valor == "GG" or valor == "XG"):
            print("valor invalido, tente PP, P, M, G, GG ou XG")
        self.__tamanho = valor

    camisa = Camisa()

    while roupa.getTamanho() == "":
        print("digite seu tamanho de roupa:")
        tamanho = input()
        if roupa.setTamanho(tamanho):
            break
        print("parabens, voce comprou uma roupa tamanho", roupa.getTamanho())