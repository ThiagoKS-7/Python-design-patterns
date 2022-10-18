from calcula_descontos import Calcula_descontos

class ISS(object):
	def calcula(orcamento):
		return jsonify("ISS",orcamento.valor * 0.1, orcamento)

class ICMS(object):
	def calcula(orcamento):
		return jsonify("ICMS",orcamento.valor * 0.06, orcamento)


def jsonify(name, imposto, orcamento):
	return {
		"name": name,
		"value": imposto + orcamento.valor - Calcula_descontos().calcula(orcamento),
		"imposto": round(imposto,2),
		"desconto": round(Calcula_descontos().calcula(orcamento),2),
	}

def get():
	return [
		ISS,
		ICMS
	]