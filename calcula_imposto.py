class Calcula_impostos(object):
	def calcula(self,orcamento, imposto):
		from impostos import Conf
		orcamento.set_item(
			[
			Item('Item A', 100.0),
			Item('Item B', 50.0),
			Item('Item C', 400.0)
			]
		)
		return imposto.calcula(Conf, orcamento) # Duck typing


if __name__ == "__main__":
	from orcamento import Orcamento, Item
	import impostos as ipt
	for j in [
			Calcula_impostos().calcula(Orcamento(), i)
			for i in ipt.get()
		]:
		print(j)
		