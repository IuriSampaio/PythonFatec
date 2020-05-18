#verificar se é ou não um ano bisexto
ano = int(input("coloca ai um ano pra ver se é bisexto ou não \n"))
if(ano%4)==0:
    if(ano%100)==0:
        if(ano%400==0):
            print("{0} é um ano bisexto".format(ano))
        else:
            print("{0} não é um ano bisexto".format(ano))
    else:
        print("{0} é um ano bisexto".format(ano))
else:
    print("{0} não é um ano bisexto".format(ano))
        
