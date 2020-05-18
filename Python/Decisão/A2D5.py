print("===================Aula 2 == Desafio 5======================")
# Entrada do Salario
salario = float(input("Digite o salario atual:"))

#proscesamento para ver o aumento de acordo com o atual
if salario <= 500:

    salarioNovo = salario + (salario * 0.15)

elif salario <= 1000:

    salarioNovo = salario + (salario * 0.10)

else:

    salarioNovo = salario + (salario * 0.05)

#saida de dados
print("o novo salario sera:",salarioNovo)