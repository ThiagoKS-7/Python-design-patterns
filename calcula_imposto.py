import types
from datetime import date

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
	from criador_de_nota_fiscal import Criador_de_nota_fiscal
	total=0
	itens = [
			Calcula_impostos().calcula(Orcamento(), i)
			for i in ipt.get()
		]
	for j in itens:
		if not isinstance(j, types.FunctionType):
			print(j)
			total += j['resultado']
	nf1 = (
     Criador_de_nota_fiscal()
	.com_razao_social("FHSA Limitada")
	.com_cnpj("012345678901234")
	.com_itens(itens)
	.com_total(total)
	) 
	print(nf1)	
	nf2 = (
		Criador_de_nota_fiscal()
	.com_razao_social("FHSA Limitada")
	.com_cnpj("012345678901234")
 	.com_itens(itens)
	.com_total(total)
	.com__template(2)
	) 
	print(nf2)		

