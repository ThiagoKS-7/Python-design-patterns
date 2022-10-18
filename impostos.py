class ISS(object):
	def calcula(orcamento):
		return jsonify("ISS",orcamento.valor * 0.1)

class ICMS(object):
	def calcula(orcamento):
		return jsonify("ICMS",orcamento.valor * 0.06)


def jsonify(name, value):
	return {
		"name": name,
		"value": value
	}

def get():
	return [
		ISS,
		ICMS
	]