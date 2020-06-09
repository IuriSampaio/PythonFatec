# as variaveis seguintes são globais 
#podem ser usadas de qulaquer lugar do programa
min = 10
max = 100
def existe(min,max):
    while True:
        #a variavel existe é uma variavel local
        #só pode ser chamada dentro da função
        existe = int(input("digite o valor:"))
        if existe>=min and existe<=max:
            return print(f'o valor {existe} esta entre {min} e {max}')
        else:
            return print(f'o valor {existe} NÃO esta entre {min} e {max}')

existe(min,max)
# DEFINIÇÃO DE PARAMETROS DEFAULTS EM UMA FUNÇÃO
# se não colocar nada os padroes ja estão declarados
def barra(n=40, caractere='$'):
    print (caractere*n)
barra()