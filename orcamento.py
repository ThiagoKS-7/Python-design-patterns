class Orcamento(object):
	def __init__(self, valor):
		self.__valor = valor # dado "privado"

	@property	# encapsulamento
	def valor(self):
		return self.__valor
