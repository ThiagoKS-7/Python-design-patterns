import types
from datetime import date

'''
Template method: criar esqueleto que muda em pequenos detalhes
Factory method: Bom pra usar junto com o template, fazendo uma única classe mãe chamar o mesmo método de várias classes 
Chain of responsibility: Parecido com factories, mas a principal vantagem é que dá pra mexer na ordem de execução
Decorator: decorar métodos ao invés de chamar muitos ifs
State: gerencia status
Observers: gerencia chamadas de vários métodos em um processo em comum (junta bem com duck typing)
Builder: Bom pra simplificar complexidade de um código, "aumentando o nível" da implementanção, (quase como uma factory, com a
principal diferença que a factory  só chama classes duck typed's e o builder cria properties em comum pra elas)


#TODO: implementar um exemplo de Chain of Responsibility a parte -> https://refactoring.guru/design-patterns/chain-of-responsibility/python/example 
'''

'''
Patterns do arquivo: 
Chain of responsibility - Calcula_impostos equivale ao client code;
'''

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
	from observador import gerenciaNf
 
	total=0
	itens = [
			Calcula_impostos().calcula(Orcamento(), i)
			for i in ipt.get()
		]
	for j in itens:
		if not isinstance(j, types.FunctionType):
			print(j)
			total += j['resultado']
	(
    Criador_de_nota_fiscal()
	.com_razao_social("FHSA Limitada")
	.com_cnpj("92347526000160")
	.com_itens(itens)
	.com_total(total)
	.que_notifica(['Admin', 'O5 Council', 'Financeiro', 'Setor 202', 'Teste', 'Zézinho'])
 	.com_observers([gerenciaNf])
	).__str__()
	(
		Criador_de_nota_fiscal()
	.com_razao_social("FHSA Limitada")
	.com_cnpj("92347526000160")
 	.com_itens(itens)
	.com_total(total)
	.com_template(2)
 	.que_notifica([ 'Setor financeiro', 'Setor 504', 'Adalberto'])
	.com_observers([gerenciaNf])
	).__str__() 		

