from datetime import datetime
# criação de uma classe 
class Pessoa:
    # definindo variavel global que pega o ano atual
    anoAtual = int(datetime.strftime(datetime.now(), '%Y'))
    # criando um método
    # self refere-se ao molde que instanciou a clase --> ex.falar() == falar(ex)
    # def falar(self):
    #     print("pessoa está falando")

    # o método __init__ é o principal quando se trata de programação 
    # orientada a objeto, pois esse é o método que está incorporado na 
    # clase quando á intancia na variavel local. 
    def __init__(self , nome , idade , comendo=False , falando = False):
        # isso vai fazer com que o molde atribua os valores colocando-os 
        # entre os parenteses no momento em que a função é instanciada
        # guardando as variaveis para poder usar em qualquer parte do prog  
        # Assim que faz p trabalhar com os valores passados pelo instanciador
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
    
    # métodos  
    def comer(self,alimento):
        if self.comendo:
            print(f'espera pq o otário do {self.nome} já está comendo {alimento}')
            return
        else:
            print(f'um tal de {self.nome} esta comendo {alimento}')
            self.comendo = True
    
    def ParaDeComer(self):
        if not self.comendo:
            print(f'{self.nome} Não está comendo')
            return
        else:
            print(f'{self.nome} dá um tempo, na molral')
            self.comendo = False
    
    def falar(self,assunto):
        self.assunto = assunto
        if self.comendo:
            print(f'falar comendo é foda ein {self.nome}')
            return
        elif self.falando:
            print(f'ta querendo falar demais {self.nome}')
            return
        else:
            print(f'{self.nome} está falando de {self.assunto}')
            self.falando = True

    def ParaDeFalar(self):
        if self.falando:
            print(f'{self.nome} esta parando de falar')
            self.falando = False
        else:
            print(f'ta querendo demais, {self.nome} nem ta falando')

    def AnoNascimento(self):
        print(self.anoAtual - self.idade)