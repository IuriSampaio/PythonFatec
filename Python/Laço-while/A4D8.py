salario = int(input("Digite o salario inicial:"))
mes = 1
jurus = salario / 99
while mes <= 12:
    print('jurus no',mes,'R$',int(jurus))
    salario = salario + jurus
    print('Salario no mes', mes, 'sera R$', int(salario), ',00')
    jurus += 1
    mes += 1
    desejaAporte = input('Deseja fazer um aporte? S/n')
    if desejaAporte == 'n':
        aporte = 0
    else:
        aporte = float(input('Digite o valor do Aporte:'))
        salario += aporte
