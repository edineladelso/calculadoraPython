def Adicionar(a, b):
    return a+b

def Subtrair(a, b):
    return a-b

def Multiplicar(a, b):
    return a*b

def Dividir(a, b):
    return a/b

def Elevar(a, b):
    return a**b

def Raiz(a, b):
    return a**(1/b)

def em(n):                          # em = expressao matematica == RECEBER exprecao matematica para realizar o calculo
    sv = ""
    l = []
    for i in n:
        if i.isnumeric():
            continue
        else:
            sv = i
            l = n.split(sv)
            l.append(sv)
    return l

def re(s):                          #   re = remover epaços vasios  == CRIANDO string sem espacos vasios                        
    st = str(s)
    sl = ""
    for i in st:
        if i != " ":
            sl += i
    return sl
 
def Calcular(s):
    formatada = re(s)
    expressao = em(formatada)

    a, b, o = expressao
    if a.isnumeric() and b.isnumeric():
        a = int(a)
        b = int(b)

        if o == "+": 
            return Adicionar(a, b)

        elif o == "-":
            return Subtrair(a, b)

        elif o == "/":
            return Dividir(a, b)

        elif o == "*":
            return Multiplicar(a, b)

        elif o == "^":
            return Elevar(a, b)

        elif o == "r":
            return Raiz(a, b)
    
    else:
        raise TypeError(f"'{a}' e '{b}' não são numeros")