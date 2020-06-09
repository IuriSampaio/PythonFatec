nomes = ['iuri','carla','iuri','maria','carlos','ana','clara','python ']
print(nomes[3:6])
 # vai mostrar do terceiro até o 5 nome
print(nomes[:6])
 # vai mostrar do primeiro até o 5 item
print(nomes[::-1])
 # vai mostrar a lista inteira ao contrario

# NOMEDALISTA [ VALORDEINICIO : VALORFINAL : VALORDOSALTO ]
# VALORDEINICIO (default) = 0
# VALORFINAL (DEFAULT) = ultimo valor da lista

# tudo que pode ser feito com uma lista(para mostrar) tbm pode ser feito com uma string
nome = "iuri doido maluco"
print(nome[12::-1])

# adicionar um valor na lista
nomes.append('braga')
print(nomes[6::])#mostrando a partir do sexto elemento

# exclui o elemento especificado
print(nomes.pop(2))
# retona a posição do array que contem esse valor
print(nomes.index('iuri'))

#### dicionario

dicionario = {"oi" : "comprimenro comum",
              "tchau":"dar um adeus",
              "iuri":list('iuri sampaio')
              }

print(dicionario)

## tupla == lista mas é imutavel
tupla = ('i','r','a','c','v','a')
print(tupla.__len__())
print(tupla.index('a'))
print(tupla.count('a')) # verifica o numero de vezes que o elemenro aparece

iuri = list('iuri')
print(iuri.index('i'))

importa = {'nome': 'iuri',
           'idade': 17,
           'formação': 'TI',
           'salario': 2000}
# pegando o valor contido na chave nome
print(importa.get('nome'))
# remove o item do dicionario 
print(importa.pop('idade'))
# descreve os itens do dicionario 
print(importa.items())
# adiciona um item no final do dicionario 
importa.__setitem__('alguma','coisa')
print(importa)
# enumerando os itens de uma lista usando for
#print('===============laço com for e lista===================')
#for n, nomes in enumerate(nomes):
#    print(n, nomes)
print('=================laço com while e lista====================')
i = 1 
while i <= nomes.__len__() :
    print(i,"-", nomes[i-1])
    i += 1 
print("====================laço com for e dicionario=====================")
for i in dicionario.keys():
    print(i,":",dicionario.get(i))


