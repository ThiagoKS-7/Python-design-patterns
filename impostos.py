from calcula_descontos import Calcula_descontos
from abc import ABC, abstractmethod


'''
Patterns do arquivo: 
Chain of responsibility - Cada imposto é um handler; Imposto(ABC) é a interface
Decorators (IPVX);
Template Method - Todos usam a Config de template;
'''

class Imposto(ABC):
	@abstractmethod
	def calcula():
		pass
	
	@abstractmethod
	def jsonify():
		pass

class Conf(Imposto):
	def __init__(self):
		self.calculo = 0
  
	def jsonify(name, imposto, orcamento):
		return {
			"nome": name,
			"resultado": imposto + orcamento.valor - Calcula_descontos().calcula(orcamento),
			"imposto": round(imposto,2),
			"desconto": round(Calcula_descontos().calcula(orcamento),2),
		}

	def eh_mais_q_500(orcamento):
		return orcamento.valor > 500

	def tem_item_valendo_mais_q_100(orcamento):
		for i in orcamento.obter_itens():
			return i.valor > 100

	def calcula(self, orcamento,condicao,min,max):
		if condicao:
			self.calculo = (orcamento.valor * (max/100))
		else:
			self.calculo = (orcamento.valor * (min/100))
		return self.calculo

	def retorna_valor(self, orcamento,nome,condicao,min,max):
		return self.jsonify(nome,Conf.calcula(self,orcamento,condicao,min,max), orcamento)

def IPVX(func):
	def inner(self, orcamento):
		print(Conf.jsonify("IPVX",func(self, orcamento) + 50, orcamento))
	return inner
class ISS(Conf):
	@IPVX
	def get(self, orcamento):
		return orcamento.valor * 0.1
	def calcula(self,orcamento):
		return self.jsonify("ISS",orcamento.valor * 0.1, orcamento)
class ICMS(Conf):
	def calcula(self,orcamento):
		return self.jsonify("ICMS",orcamento.valor * 0.06, orcamento)

class ICPP(Conf):
	def get(self, orcamento):
		return Conf.calcula(self, orcamento, self.eh_mais_q_500(orcamento), 7, 5)
	def calcula(self, orcamento):
		return self.retorna_valor(self, orcamento, "ICPP", self.eh_mais_q_500(orcamento), 7, 5)

class IKCV(Conf): 
	def get(self, orcamento):
		return Conf.calcula(self, orcamento,self.eh_mais_q_500(orcamento) and self.tem_item_valendo_mais_q_100(orcamento) , 10, 6)
	def calcula(self, orcamento):
		return self.retorna_valor(self, orcamento,"IKCV",self.eh_mais_q_500(orcamento) and self.tem_item_valendo_mais_q_100(orcamento) , 10, 6)


def get():
	return [
		ISS,
		ICMS,
		ICPP,
		IKCV,
		IPVX,
	]
 