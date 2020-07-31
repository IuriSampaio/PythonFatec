# MERGE SORT -> SEPARA EM LISTAS MENORES PARA ENTÃO ORDENALAS NO MOMENTO DE JUNÇÃO DELAS
## ex: [4,7,8,2] -> [4,7] [8,2] -> [4] [7] [8] [2] -> [4,7] [2,8] -> [2,4,7,8]
def mergeSort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)

    if (fim - inicio > 1):
        meio = (fim + inicio) // 2
        mergeSort(lista, inicio, meio)
        mergeSort(lista, meio, fim)
        merge(lista, inicio, meio, fim)

    print(lista)



def merge(lista, inicio, meio, fim):
    inicioPmeio = lista[inicio:meio]
    meioPfim = lista[meio:fim]
    maiorInicioPmeio, maiorMeioPfim = 0, 0
    for k in range(inicio, fim):

        if maiorInicioPmeio >= len(inicioPmeio):
            lista[k] = meioPfim[maiorMeioPfim]
            maiorMeioPfim += 1
        elif maiorMeioPfim >= len(meioPfim):
            lista[k] = inicioPmeio[maiorInicioPmeio]
            maiorInicioPmeio += 1

        elif inicioPmeio[maiorInicioPmeio] < meioPfim[maiorMeioPfim]:
            lista[k] = inicioPmeio[maiorInicioPmeio]
            maiorInicioPmeio += 1
        else:
            lista[k] = meioPfim[maiorMeioPfim]
            maiorMeioPfim += 1


lista = [4, 3, 5, 3, 2, 1, 3, 4, 6, 5, 4, 3, 2, 3, 4, 5, 3, 2, 2]

mergeSort(lista)
