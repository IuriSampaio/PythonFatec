# def kauan(nome, qualidade):
#     print (nome,"osvaldo",qualidade)
# qualidade = input("digite uma coisa xingando: \n")
# nome = input("digite seu nome \n ")
# kauan("iuri",qualidade)
######################################################
# função que pede dois valores e soma eles enquanto o usuario quiser
def somando( ):
    continua = True
    while continua:
        a = int(input("digite um numero:"))
        b = int(input("digite um numero:"))
        print(a,"+",b,"=",a+b)
        res = input("deseja Continuar?")
        if res == 'n':
            continua = False
        else:
            continue

##############as duas tem o mesmo resultado#################

# funçao de soma sem usar lambda
def somar(a,b):
    print(a,"+",b,"=",a+b)
#somar(9,5)

# usando lambda
# a = int(input("digite um numero:"))
# b = int(input("digite um numero:"))
soma = lambda a,b:print(a,"+",b,"=",a+b)
#soma(9,5)

# funçao que subtrai sem usar lambda
def subtrair(a,b):
    print(a,"-",b,"=",a-b)
#subtrair(9,5)
# usando lambda
menos = lambda a,b:print(a,"-",b,"=",a-b)
#menos(9,5)

# funçao que subtrai sem usar lambda
def multiplica(a,b):
    print(a,"x",b,"=",a*b)
#multiplica(9,5)
# usando lambda
vezes = lambda a,b:print(a,"x",b,"=",a*b)
#vezes(9,5)

# funçao que subtrai sem usar lambda
def dividir(a,b):
    if b == 0:
        print("O limite tende ao infinito, a divisão inteira não existe")
    else:
        print(a,"/",b,"=",a/b)
#dividir(9,5)
# usando lambda
dividi = lambda a,b: print(a,"/",b,"=",a/b) if (not b==0) else print("O limite tende ao infinito, a divisão inteira não existe")
#dividi(9,5)

## ver se é par ou impar
def ehPar(n):
    return n%2 == 0 
def parImpar(n):
    if ehPar(n):
        return 'par'
    else:
        return 'impar'

## pesquisando um valor na lista
def pesquisaValor(lista, valorPesquisado):
    for posicao, valoresLista in enumerate(lista):
        if valoresLista == valorPesquisado:
            return print("na",posicao,"posição temos",valoresLista)
       
    return print('não existe na lista')

lista =[2,5,8,3,7,1,9]
pesquisaValor(lista,9)