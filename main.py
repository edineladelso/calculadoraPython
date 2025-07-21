from calc import Calcular

def main():
    print("\t\t========================================================================================")
    print("\t\t==                              EIS A SUA CALCULADORA                                 ==")
    print("\t\t========================================================================================")
    print("\t\t==                                                                                    ==")
    print("\t\t==                             REGRAS:                                                ==")
    print("\t\t==  >>     Para encerrar a calculadora Digite: AC ou P                                ==")
    print("\t\t==  >>     Insira os Valores de forma normal ex: 1+2                                  ==")
    print("\t\t==                                                                                    ==")
    print("\t\t========================================================================================")
    print("\t\t==                                                                                    ==")

    while True:
        
        r = input("\t\t==\t\t: ")
        if r.lower() == "ac" or r.lower() == "p":
            return
        else:
            calc = Calcular(r)
            print(f"\t\t==\t\t\t\t\t\t{calc}")

if __name__ == "__main__".strip():
    main()