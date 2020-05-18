#importando biblioteca tkinter
from tkinter import *
from tkinter import font
#importando modulo que exibe spans de mensagem
from tkinter import messagebox
#importando biblkioteca para tabalhat com funções com o partial(função , argumento)
from functools import partial

#criando janela a partir da função Tk()
janela = Tk()

#titulo da janela
janela.title("salve capão")

#colocando uma cor na janela
janela["bg"]= "green"
# janela["background"]= "color"

#definindo uma localização e um tamanho
janela.geometry("500x300+450+200")
#.geometry("largura X altura + marginLeft + marginTop")

#coclocando um texto
lb = Label(janela,text="salve cuzaum$!")
#definindo o lugar que vai ficar o salve
lb.grid(row=30,column=10)#.place(x=30,y=70)
#cor de fundo da area de texto
lb["bg"]="gray"
#muda a cor do texto
lb["fg"]="pink"
#função que será chamada ao clicar no botão
def clicou(bt):
     lb["text"]=" Agora Fudeu Mané!"
     lb["bg"]="red"
     bt["bg"]="red"
     bt1["bg"]="red"
     janela["bg"]="pink"
     messagebox.showerror("fudeu","desliga essa merda porra")
def pegaTexto():
    #pegando o conteudo do  Entry e colocando no label
    lb["text"]= ed.get()
    lb["foreground"]="yellow"
    lb["bg"]="green"
    bt1["bg"]="green"
    bt2["bg"]= "green"
    janela["bg"]="green"
    #messagebox.showinfo("acertou","agora foi8 em")
#colocando botão
bt1 = Button(janela, width="20",text="mostra na tela", command=pegaTexto)# assim uma funçao serve para um botão
bt1.grid(row=40 , column=10)#.pack(side=LEFT)
##   .pack() -->propriedade para a organização dos componentes
#           side= LEFT  || side=RIGTH || side=TOP || side=BOTTOM
#           anchor = CENTER || N (norte)|| W (leste)|| S(sul) || E(oeste)|| variações : NW,NE,SW,SE
#           fill = X(ocupar toda a horizontal) || Y(ocupar toda verttical)
#           expand= 1(ocupa  o espaço disponivel)
##   .grid(row=000 , column=000)-->propriedade que coloca o conteudo organizado entre linhas e colunas
#           sticky=  CENTER || N (norte)|| W (leste)|| S(sul) || E(oeste)|| variações : NW,NE,SW,SE
#           rowspan= numero de linhas a serem cobertas (deve ser indicado um sticky com a direção percorrida ex sticky=N+S (+ == ATÉ))
#           colspan= numero de colunas a serem cobertas (deve ser indicado um sticky com a direção percorrida ex sticky=W+E)
#cococando outro botão
bt2 = Button(janela, width="10",text="NÃO CLIQUE")#, command=clicou)
bt2.grid(row=60,column=10)



#--forma de trabalhar com varios notões que podem receber a mesma função
#bt1["command"]= partial(clicou,bt1)
bt2["command"]=partial(clicou,bt2)
#colocando uma caixa de texto
ed = Entry(janela)
ed.grid(row=35,column=10)


###fazendo uma calculadora besta do lado
insira= Label(janela,background="green",text="insira os valores aqui:")
insira.place(x=320,y=0)

n1 = Entry(janela, width= 10)
n1.place(x=300,y=20)

n2 = Entry(janela, width= 10)
n2.place(x=390,y=20)

def soma():
    if (str(n1.get()).isnumeric() and str(n2.get()).isnumeric() ):
        resultado["text"]=int(n1.get())+int(n2.get())
    else:
        resultado["text"]="ERRO"
        
soma=Button(janela,width=20, bg="black",foreground="white",text="soma",command=soma)    
soma.place(x=300,y=60)

def menos():
    if (str(n1.get()).isnumeric() and str(n2.get()).isnumeric() ):
        resultado["text"]=int(n1.get())-int(n2.get())
    else:
        resultado["text"]="ERRO"        

menos=Button(janela,width=20, text="subtrair",command=menos)    
menos.place(x=300,y=90)

def vezes():
    if (str(n1.get()).isnumeric() and str(n2.get()).isnumeric() ):
        resultado["text"]=int(n1.get())*int(n2.get())
    else:
        resultado["text"]="ERRO"
        
vezes=Button(janela,width=20, bg="black",fg="white",text="multiplicar",command=vezes)    
vezes.place(x=300,y=120)

def dividi():
    if (str(n1.get()).isnumeric() and str(n2.get()).isnumeric() ):
        if( str(n2.get()) == "0"):
            resultado["text"]="NÃO DA"
        else:
            resultado["text"]=int(n1.get())/int(n2.get())
    else:
        resultado["text"]="ERRO"
        
divide=Button(janela,width=20,text="dividir",command=dividi)    
divide.place(x=300,y=150)

resultado= Label(janela,bg="pink",width=20,height=5,fg="white", text="resultado")
resultado.place(x=300,y=200)

janela.mainloop()



