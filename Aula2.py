#função que faz a soma 
def soma(a,b):
    c=a+b
    print("A SOMA É:",c)
#função que ve se a soma de duas idades é maior de idade
def emaior1(idadeA,idadeB):
    somaIdades= idadeA+idadeB
    if somaIdades>=18:
        print(somaIdades+5,"esse é o resultado")
    else:
        print(somaIdades-7,"esse é o resultado")
def emaior2(idadeA,idadeB):
    somaIdades= idadeA+idadeB
    if somaIdades>=18:
        print(somaIdades+5,"esse é o resultado")
    else:
        print(somaIdades-7,"esse é o resultado")
#verifica o salario do funcionario apos um mes que recebe aumento
def salariosBunda(salario):
    if salario<=500:
        salarioNovo=salario+(salario*(15/100))
    elif salario<=1000:
        salarioNovo=salario+(salario*(10/100))
    else:
        salarioNovo=salario+(salario*(5/100))
    print("o novo salario será:",salarioNovo)
#funçao que atribui os salarios do funcionario a cada mês com os acresimos nescessarios
def salarios(salario):
    for mes in range(100):
        while salario<=500:
            print("o salario no",mes,"mes será",salario)%"%.2f"
            salario=salario+(salario*(15/100))
        while salario<=1000:
            print("o salario no",mes,"mes será",salario)%"%.2f"
            salario=salario+(salario*(10/100))
        while salario<=1500:
            print("o salario no",mes,"mes será",salario)%"%.2f"
            salario=salario+(salario*(5/100))
#função que calcula o maior peso entre 3 pessos
def maiorPeso(peso1,peso2,peso3):
    if (peso1>peso2):
        if(peso1>peso3):
            maiorPeso=peso1
        else:
            maiorPeso=peso3
    else:
        if(peso2>peso3):
            maiorPeso=peso2
        else:
            maiorPeso=peso3
    print('o maior peso é',maiorPeso)
def maiorOrdenado(a,b,c):
    if (a>b):
        if(a>c):
            if(b>c):
                print(c,b,a)
            else:
                print(b,c,a)
        else:
            print(b,a,c)
    else:
        if(b>c):
            if(c>a):
                print(a,c,b)
            else:
                print(c,a,b)
        else:
            print(a,b,c)
def maior5(a,b,c,d,e):
    if(a>b):
        if(a>c):
            if(a>d):
                if(a>e):
                    maior=a
                    menor=b
                else:
                    maior=e
                    menor=b
            else:
                if(d>e):
                    maior=d
                    if(b>e):
                        menor=e
                    else:
                        menor=b
                else:
                    maior=e
                    if(b>d):
                        menor=d
                    else:
                        menor=b
        else:
            if(c>d):
                if(c>e):
                    maior=c
                else:
                    maior=e
                    if(b>c):
                        menor=c
                    else:
                        if(b>d):
                            menor=d
                        else:
                            menor=b
                    
                    
                






