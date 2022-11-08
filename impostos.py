from calcula_descontos import Calcula_descontos
class Conf(object):
	def __init__(self):
		self.calculo = 0;
  
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

	def checa_valor(orcamento,nome,condicao, val1,val2):
		if condicao:
			Conf.calculo = orcamento.valor * val1
		else:
			Conf.calculo = orcamento.valor * val2
		return Conf.jsonify(nome,Conf.calculo, orcamento)

class ISS(object):
	def calcula(orcamento):
		return Conf.jsonify("ISS",orcamento.valor * 0.1, orcamento)

class ICMS(object):
	def calcula(orcamento):
		return Conf.jsonify("ICMS",orcamento.valor * 0.06, orcamento)

class ICPP(object):
	def calcula(orcamento):
		return Conf.checa_valor(orcamento, "ICPP", Conf.eh_mais_q_500(orcamento), 0.07, 0.05)

class IKCV(object):
	def calcula(orcamento):
		return Conf.checa_valor(orcamento, "ICPP", Conf.eh_mais_q_500(orcamento) and Conf.tem_item_valendo_mais_q_100(orcamento), 0.07, 0.05)


def get():
	return [
		ISS,
		ICMS,
		ICPP,
		IKCV,
	]