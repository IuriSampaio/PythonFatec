#importando a classe criada com nome pessoa
from pessoa import Pessoa

#p1=Pessoa()
#p2=pessoa()
# duas variaveis instanciadas pela mesma função
# são guardadas em lugares diferentes de memoria
#print("sim") if p1==p2 else print("não") # ternario

# colocando os atributos especificados no método __init__   
# instanciando as clases
p1 = Pessoa('iuri',18)
p2 = Pessoa('clara',8)
# método que faz o atributo comendo vire False(0)
p1.ParaDeComer()
# chamando o método comer da classe pessoa e passando o atributo comida
p1.comer('merda')
p2.falar('politica')
p2.ParaDeFalar()
p2.falar('merda')
p1.AnoNascimento()