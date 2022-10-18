class Desconto_mais_q_cinco_itens(object):
	def calcula(orcamento):
		if orcamento.total_itens > 5:
			return orcamento.valor * 0.1
		else:
			return 0

class Desconto_mais_q_quinhentos_reais(object):
	def calcula(orcamento):
		if orcamento.valor > 500:
			return orcamento.valor * 0.07
		return 0

def get():
	return [
		Desconto_mais_q_cinco_itens,
		Desconto_mais_q_quinhentos_reais
	]