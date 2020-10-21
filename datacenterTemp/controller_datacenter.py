import sqlite3
from datetime import datetime

class Datacenter:
	barra = lambda self,n=40,char='$' : print(char*n)

	def menu(self):
		self.barra()
		print("$  1 -> Verificar Qualidade da temperatura do datacenter")
		print("$  2 -> Historico das temperaturas verificadas")
		print("$  99 -> Sair do sistema ")
		self.barra()

	def temperatureItsIdeal( self, temperature ):
		if (not type( temperature ) == 'float' or not type ( temperature ) == 'int' ):
			temperature = float( temperature )

		if ( temperature < 18 ):
			status = "$ Esta muito frio para os computadores $"
		elif ( temperature >= 18 and temperature <= 27 ):
			status = "$ A temperatura está perfeita $"
		else:
			status = "$ Esta muito quente para os computadores $"

		temp = Temperature()
		temp.create(temperature, status)
		return status

	def historicoTemps(self):
		temp = Temperature()
		temp.index()

class Temperature:
	barra = lambda self,n=40,char='$':print(char*n)
	conex = sqlite3.connect('temperature.db')
	cursor = conex.cursor()
	cursor.execute('''
		CREATE TABLE IF NOT EXISTS tbl_temperatures(
			temperature text not null,
			status text not null,
			datetime text not null
		);
	''')


	def create(self, temp , status):
		now = datetime.now().strftime('%d/%m/%Y - %H:%M')
		self.temp = temp
		self.status = status
		self.cursor.execute(f'''
			INSERT INTO tbl_temperatures VALUES
			('{self.temp}','{self.status}','{now}')
		''')
		self.conex.commit()

	def index(self):
		self.cursor.execute('''
			SELECT * FROM tbl_temperatures
		''')
		for i in self.cursor.fetchall():
			self.barra()
			print(f'Temperatura : {i[0]}\nStatus : {i[1]}\nDia e Hora : {i[2]}')
		input("precione enter para continuar...")
		self.conex.commit()
