# __métodos__
soma = lambda a,b:print(a,"+",b,"=",a+b)
menos = lambda a,b:print(a,"-",b,"=",a-b)
vezes = lambda a,b:print(a,"x",b,"=",a*b)
dividi = lambda a,b: print(a,"/",b,"=",a/b) if (not b==0) else print("O limite tende ao infinito, a divisão inteira não existe")
potencia = lambda a,b: print(a,"^",b,"=",a**b)
def logaritimo(b:float):
    a = b
    i = 1.0
    while (i < a):
        if (10**i == b):
            print(i)
            break
        else :
            i += 1
            continue
raiz = lambda a,b: print("raiz",a,"de",b,"=",b**(1/a))
eqDe2grau = lambda a,b,c: print( "X1 =",-b+((b**2)-4*a*c)**1/2/2*a ,"\nX2 =", -b-((b**2)-4*a*c)**1/2/2*a)
def fatorial(a):
    i=1
    fat=1
    while i<=a:
        fat = fat*i
        i += 1
    print(fat)

# __main__
while True:
    print("Qual operação vc deseja ?")
    res = int(input("\n soma -> 1 \n subtração -> 2 \n multiplicação -> 3 \n divisão -> 4 \n potencia -> 5 \n logaritimo -> 6 \n Equação de 2° -> 7 \n Fatorial -> 8 \n raiz -> 9 \n"))
    if res == 1:
        a = float(input("digite o primeiro numero\t"))
        b = float(input("digite o segundo numero\t"))
        soma(a,b)
    elif res == 2:
        a = float(input("digite o primeiro numero\t"))
        b = float(input("digite o segundo numero\t"))
        menos(a,b)
    elif res == 3:
        a = float(input("digite o primeiro numero\t"))
        b = float(input("digite o segundo numero\t"))
        vezes(a,b)
    elif res == 4 :
        a = float(input("digite o primeiro numero\t"))
        b = float(input("digite o segundo numero\t"))
        dividi(a,b)
    elif res == 5 :
        a = float(input("digite o primeiro numero\t"))
        b = float(input("digite o segundo numero\t"))
        potencia(a,b)
    elif res == 6:
        a = float(input("digite o primeiro numero\t"))
        logaritimo(a)
    elif res == 7:
        a = float(input("digite o primeiro numero\t"))
        b = float(input("digite o segundo numero\t"))
        c = float(input("digite o segundo numero\t"))
        eqDe2grau(a,b,c)
    elif res == 8:
        a = float(input("digite o primeiro numero\t"))
        fatorial(a)
    elif res == 9:
        a = float(input("digite o primeiro numero\t"))
        b = float(input("digite o segundo numero\t"))
        raiz(a,b)
    else: 
        print("essa opção não foi cadastrada")
    continuar = input("Deseja Continuar S/n :")
    if continuar == 'n':
        break
    else:
        continue
