class Calcula_impostos(object):
	def calcula(self,orcamento, imposto):
		return imposto.calcula(orcamento) # Duck typing


if __name__ == "__main__":
	from orcamento import Orcamento
	import impostos as ipt
	print(
			[
				Calcula_impostos().calcula(Orcamento(500), i)
				 for i in ipt.get()
			]
		)
		