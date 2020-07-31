# SELECTION SORT -> VAI DEIXANDO O MENOR ELEMENTO NO COMEÇO E FAZ ISSO COM O RESTO DA LISTA
# SEMPRE DEIXA O MENOR NO COMEÇO E PARTE PRO RESTO DA LISTA, FAZENDO O MESMO, ATÉ ORDENA-LA
def selectionSort(lista):
    print("Lista entregue:",lista)
    n = len(lista)

    for j in range (n-1):
        minimo_index = j

        for i in range(j , n):
            if lista[i] < lista[minimo_index]:
                minimo_index = i

        if lista[j] > lista[minimo_index]:

            aux = lista[j]
            lista[j] = lista[minimo_index]
            lista[minimo_index] = aux
        #print(lista)
    print("Lista ordenada por meio do selection sort: ",lista)

lista = [3,9,4,5,6,3,4.1,2,2,1]
selectionSort(lista)
