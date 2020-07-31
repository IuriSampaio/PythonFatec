## QUICKSORT -> pega um pivo e ordena todo mundo de acordo com esse pivo
# COM O PIVO NO LUGAR CERTO, REPETE-SE O MESMO ESTRE AS LISTAS ADJACENTES

def quickSort(lista , inicio=0 , fim=None):
    if fim is None:
        fim = len(lista)-1
    if inicio < fim:
        pivo = particiona(lista,inicio,fim)
        quickSort(lista,inicio,pivo-1)
        quickSort(lista,pivo+1,fim)
    print(lista)

def particiona(lista,inicio,fim):
    pivo = lista[fim]
    index = inicio
    for j in range(inicio,fim):
        if lista[j]<= pivo:
            lista[j],lista[index] = lista[index],lista[j]
            index+=1
    lista[index],lista[fim] = lista[fim], lista[index]
    #retornando o indicie do pivo no lugar certo para dividr a lista entre duas
    return index

quickSort([9,8,5,4,1,0,3,2,7,1])