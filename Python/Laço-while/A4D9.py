print('\n\t\t======Aula 4 exercicio 9======\n')
# Definindo variaveis como os primeiros numeros do fibonacci
a = 0
b = 1
numeroTermos = 15
# Mostrando-os
print('\t  ', a, end='-')
print(b, end='-')
contadorTermo = 2
while True:
    # se o $contadorTermo chegar ao 15 vai sair do laco
    if contadorTermo == numeroTermos:
        break
    # Repetir ate o $contadorTermo ser 15:
    # O proximo valor sempre vai ser a soma dos dois anteriores
    c = a + b
    # dando o valor da variavel seguinte a anterior
    a = b
    b = c
    # se for o ultimo termo vai ser mostrado de um jeito diferente
    if contadorTermo == numeroTermos - 1:
        print('%d\n' % c, end='')
    else:
        print(c, end='-')
    # Adicionando mais um ao $contadorTermo
    contadorTermo += 1
