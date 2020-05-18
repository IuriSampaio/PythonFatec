print("\n\t\t\t====Aula 4 Exercicio 10====")
primos = 2
# enquanto $primos for menor que 1000(laco que repete os numeros do 2 ao 999)
while primos < 1000:
    # criando parametro para realizar a divisao de cada numero que passar por $primos.
    parametro = 2
    # variavel booleana para ver se o numero que passa por $primos e dividido em algum momento.
    eDividido = False
    # enquanto o $parametro for menor que $primos (pois nao se divide por 0)...
    while parametro < primos:
        # se o resto da divisão $primos/$parametros for igual a 0...
        if primos % parametro == 0:
            # ...Siginifica que o valor em $primos nao e primo pois foi dividido por um valor maior que 1 e menor que ele mesmo.
            eDividido = True
            # sendo ele primo ou nao, soma-se 1 a $parametro para continuar o teste de divisao dos numeros.
            parametro += 1
        else:
            parametro += 1
    # se nao $eDividido...
    if not eDividido:
        # ...mostrar na tela pois são valores primos.
                # aqui temos uma gambiarra para colocar um ponto final no ultimo numero primo, nao uma virgula
        if parametro == 997:
            print('', primos, end='.')
        else:
            print('', primos, end=',')
    # se e(true) $eDividido...
    else:
        # ...nao sera um numero primo
        # $eDividido prescisa ser retornada ao DEFAULT pois ira realizar teste com...
        eDividido = False
    # ... o proximo numero de $primos para voltar a condicao do while
    primos += 1
