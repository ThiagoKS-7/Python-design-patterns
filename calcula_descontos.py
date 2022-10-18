class Calcula_descontos(object):
	def calcula(self, orcamento):
		import descontos as dct
		desconto = 0
		for i in dct.get():
			res = i.calcula(orcamento) if desconto == 0 else 0
		return res