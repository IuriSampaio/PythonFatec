## INSERTION SORT -> ORDENA A LISTA POR MEIO DA CRIAÇÃO DE UM LISTA MENOR COM DOIS VALORES DA LISTA ORIGINAL
## QUNADO ESSES SÃO ORDENADOS, ADICIONASE MAIS UM ELEMENTO A LISTA, E ORDENASE COM OS JÁ EXISTENTES SEGUINDO
## ASSIM ATÉ ORDENAR TUDO
def insertionSort(lista):
    print("lista entregue:",lista)
    n = len(lista)
    for i in range(1,n):
        chave = lista[i]
        j = i - 1
        while j>=0 and lista[j] > chave:
            lista[j+1]= lista[j]
            j-=1
        lista[j+1] = chave
    print("Lista ordenada com insertionSort:",lista)



insertionSort([4.3,4,56,67,8,7,4,2,6,8,5,3,2,1,0,5,'k'])