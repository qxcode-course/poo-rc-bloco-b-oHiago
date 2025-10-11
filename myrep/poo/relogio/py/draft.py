class Relogio:
    def __init__ (self):
        self.__hora = 0
        self.__minuto = 0
        self.__segundo = 0

    def getHora(self) -> int:
        return self.__hora
    
    def getMinuto(self) -> int:
        return self.__minuto
    
    def getSegundo(self) -> int:
        return self.__segundo

    def setHora(self, hora: int) -> bool:
        hora = int(hora)
        if 0 <= hora <= 23:
            self.__hora = hora
        else:
            print("fail: hora invalida")

    def setMinuto(self, minuto: int) -> bool:
        minuto = int(minuto)
        if 0 <= minuto <= 59:
            self.__minuto = minuto
        else:
            print("fail: minuto invalido")

    def setSegundo(self, segundo: int) -> bool:
        segundo = int(segundo)
        if 0 <= segundo <= 59:
            self.__segundo = segundo
        else:
            print("fail: segundo invalido")

    def next(self):
        self.__segundo +=1
        if self.__segundo == 60:
            self.__segundo = 0
            self.__minuto += 1
            if self.__minuto == 60:
                self.__minuto = 0
                self.__hora += 1
                if self.__hora == 24:
                    self.__hora = 0 

    def __str__(self) -> str:
        return f"{self.__hora:02}:{self.__minuto:02}:{self.__segundo:02}"

def main():
    relogio = Relogio()

    while True:
        
        line = input()
        print("$"+line)
        args = line.split()

        if args[0] == "end":
            break

        elif args[0] == "init":
            hora = int(args[1])
            minuto = int(args[2])
            segundo = int(args[3])

            if not (0 <= hora < 24):
                print("fail: hora invalida")
                hora = 0
            if not (0 <= minuto < 60):
                print("fail: minuto invalido")
                minuto = 0

            if not (0 <= segundo < 60):
                print("fail: segundo invalido")
                segundo = 0

            relogio.setHora(hora)
            relogio.setMinuto(minuto)
            relogio.setSegundo(segundo)

        elif args[0] == "set":
            hora = args[1]
            minuto = args[2]
            segundo = args[3]
            relogio.setHora(hora)
            relogio.setMinuto(minuto)
            relogio.setSegundo(segundo)
        elif args[0] == "show":
            print(relogio)
        elif args[0] == "next":
            relogio.next()
        else:
            print("fail: comando não encontrado")
main()        

