import types


class Calcula_impostos(object):
	def calcula(self,orcamento, imposto):
		from impostos import Conf, ISS
		orcamento.set_item(
			[
			Item('Item A', 1900.0),
			Item('Item B', 150.0),
			Item('Item C', 800.0)
			]
		)
		if not isinstance(imposto, types.FunctionType):
			return imposto.calcula(Conf, orcamento) # Duck typing
		else:
			return imposto(ISS.get(Conf, orcamento))


if __name__ == "__main__":
	from orcamento import Orcamento, Item
	import impostos as ipt
	for j in [
			Calcula_impostos().calcula(Orcamento(), i)
			for i in ipt.get()
		]:
		if not isinstance(j, types.FunctionType):
			print(j)
		