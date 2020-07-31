# BUBBLE SORT => VAI MANDANDO O MAIOR FINAL
# COMPARA O ELEMENTO COM O PROXIMO ELEMTO DA LISTA SE FOR MAIOR, VAI MANDANDO PRO PROXIMO E COMPARANDO
def bubbleSort(lista):
    print("Lista entregue:",lista)
    n = len(lista)
    for j in range(n-1):
        for i in range(n-1):
            if lista[i] > lista[i+1]:
                ##### OS DOIS TIPOS DE ATRIBUIÇÃO SEGUINTES TEM O MESMO RESULTADO
                #### A TROCA DOS ELEMENTOS ENTRE A POSIÇÃO [i] E [i+1]
                ## SÓ EM PYTHON
                lista[i], lista[i+1] = lista[i+1], lista[i]
                ## EM TODAS AS LINGUAGEM
                # aux = lista[i]
                # lista[i] = lista[i+1]
                # lista[i+i] = aux
    print("Lista ordenada por bubble sort:",lista)

bubbleSort([4,2,1,2,3,4,5,8,6,9,76,4,3,2,3,4,63,2])