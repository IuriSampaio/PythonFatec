######### ESCREVENDO EM UM ARQUIVO ##########
#usa-se o a => append, pois o w => white apaga tudo antes de escrever 
openFile = open('users.txt','a')
listaDeNomes=[]
continua=True

while continua:
    nome=input('Digite um nome')
    listaDeNomes.append(nome)
    res=input("deseja adicionar mais um nome? S/n")
    if res == 'n':
        for i in listaDeNomes:
            if i==listaDeNomes[0] :
                openFile.write(i)
            else:
                openFile.write(f'\n{i}')
        continua=False
        break
    else:
        continue
# ABRINDO ARQUIVO NO MODO r => read
nomeR = open('users.txt','r')
#lendo todas as linhas d
nemas= nomeR.readlines
print(nemas)
#### acresentando os numeros de 1 á 100 no arquivo numbers.txt
nums = open('numbers.txt','a')
for n in range(101):
    nums.write(f'{n}\n')

## lendo os numeros em numbers.txt
numsR=open('numbers.txt','r')
k=numsR.readlines()
print(k)
