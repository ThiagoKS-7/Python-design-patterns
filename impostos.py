from calcula_descontos import Calcula_descontos
from abc import ABCMeta, abstractmethod

class Conf(object):
	__metaclass__ = ABCMeta

	def __init__(self):
		self.calculo = 0
  
	def jsonify(name, imposto, orcamento):
		return {
			"nome": name,
			"valor": imposto + orcamento.valor - Calcula_descontos().calcula(orcamento),
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

class ISS(Conf):
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
	]