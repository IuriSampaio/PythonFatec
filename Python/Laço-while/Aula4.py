def enquantoVDD(s):
    # O continue volta daqui
    while True:
        v = int(input('digite um valor para ser somado, ou 0 para sair\t'))
        if v == 0:
            break  # para o laco
        elif 200 <= v <= 300:  # poderia ser (v<=200 and v<=300)
            continue  # vai pro while
        s = s + v
    print(s)
    print('fim do loop')


#enquantoVDD(0)  # --> chamada da funcao sobre o while true usando break e continue


def enquantoEncadeado(s):
    while s <= 10:
        n = 0
        print("======Tabuada do %d========" % (s))
        while n <= 10:
            # print("%d"%(VariavelDecimal))
            # print("%s"%(variavelString))
            # print("%i"%(variavelInteira))
            print("%d * %d = %d" % (s, n, s * n))
            n += 1
        s += 1


enquantoEncadeado(0)
