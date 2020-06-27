from datetime import datetime
class televisao:
    anoAtual = int(datetime.strftime(datetime.now(), '%Y'))
    def __init__(self , marca , polegadas , canal , anoLancamento, ligada=False):
        self.marca = marca 
        self.polegadas = polegadas
        self.canal = canal
        self.anoLancamento = anoLancamento
        self.ligada = ligada
    def mudaCanal(self, qtdMudanca):
        if self.ligada:
            self.qtdMudanca = qtdMudanca
            if self.canal+self.qtdMudanca <= 60:
                if self.canal> -self.qtdMudanca:
                    canalNew = self.canal + self.qtdMudanca
                    print(f'mudando do canal {self.canal} para o canal {canalNew}')
                    self.canal = canalNew
                    return
                else:
                    lastChannel = 60 + self.canal
                    canalNew = lastChannel + self.qtdMudanca
                    print(f'mudando do canal {self.canal} para o canal {canalNew}')
                    self.canal = canalNew
                    return
            else:
                firstChannel = 2
                canalNew = firstChannel+self.qtdMudanca
                print(f'mudando do canal {self.canal} para o canal {canalNew}')
                self.canal = canalNew
                return
        else:
            print(f'a televisão está desligada')
            return
    def timeOfLife(self):
        ageTV = self.anoAtual - self.anoLancamento 
        print(f'a TV existe a {ageTV}')
        return
    def turnOnOff(self):
        if not self.ligada:
            self.ligada = True
            print(f'ligando a tv {self.marca} de {self.polegadas}')
        else:
            self.ligada = False
            print(f'desligando a tv {self.marca} de {self.polegadas}')
    def descTv(self):
        print(f'marca da TV : {self.marca}\ntamanho em polegadas: {self.polegadas}\nCanal Atual: {self.canal}\nTempo de existencia: {self.anoAtual - self.anoLancamento}')
        return
#fazer o fluxograma e o programma de uma urna eletronica 