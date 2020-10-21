from controller_datacenter import Datacenter

dt= Datacenter()

while (True):
	dt.menu()
	res = input("Digite oque vc quer fazer : ")

	if ( res == '1' ):
		temperature = input("digite a temperatura no seu datacenter: ")
		quality = dt.temperatureItsIdeal(temperature)
		print(quality)
	elif (res == '2' ):
		dt.historicoTemps()
	else:
		break

	r = input("Deseja Continuar : S/n ")
	if ( r == 'n' ):
		break
	else:
		continue
