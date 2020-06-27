#de NOMEPROGRAMA importar CLASSEDESEJADA
from televisao import televisao
#instanciado a classe televisão
tv1 = televisao('LG','42',60,2010,ligada=True)
#mostrando um atributo passado no momento da instanciação da classe
print(tv1.canal)
#chamando função que muda canal
tv1.mudaCanal(40)
print(tv1.canal)

tv1.timeOfLife()

tv1.turnOnOff()
tv1.turnOnOff()

tv1.descTv()