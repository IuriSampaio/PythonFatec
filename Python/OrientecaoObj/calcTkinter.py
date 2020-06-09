from tkinter import *
from tkinter import messagebox






calculadora = Tk()
calculadora.title("Calculadora")
calculadora["bg"] = "black"
calculadora.geometry("305x500+100+200")

resultado = Label(calculadora,text="resultado",width="22",height="2",font=("monospace","15"))
resultado.place(x=30,y=10)
resultado["bg"]="white"






# #### ### BOTÕES ### #### #
# Button(calculadora,width="2",height="4",text="0",command= ,font=("monospace","15")).place(x=5,y=80)
# Button(calculadora,width="2",height="4",text="1",command= ,font=("monospace","15")).place(x=35,y=80)
# Button(calculadora,width="2",height="4",text="2",command= ,font=("monospace","15")).place(x=65,y=80)
# Button(calculadora,width="2",height="4",text="4",command= ,font=("monospace","15")).place(x=125,y=80)
# Button(calculadora,width="2",height="4",text="5",command= ,font=("monospace","15")).place(x=155,y=80)
# Button(calculadora,width="2",height="4",text="3",command= ,font=("monospace","15")).place(x=95,y=80)
# Button(calculadora,width="2",height="4",text="6",command= ,font=("monospace","15")).place(x=185,y=80)
# Button(calculadora,width="2",height="4",text="7",command= ,font=("monospace","15")).place(x=215,y=80)
# Button(calculadora,width="2",height="4",text="8",command= ,font=("monospace","15")).place(x=245,y=80)
# Button(calculadora,width="2",height="4",text="9",command= ,font=("monospace","15")).place(x=275,y=80)




calculadora.mainloop()