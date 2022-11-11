from abc import ABCMeta, abstractmethod

class Desconto_extra(object):
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def aplica_desconto_extra(self,orcamento):
        pass
    
    @abstractmethod
    def aprova(self):
        pass
    @abstractmethod
    def reprova(self):
        pass
    @abstractmethod
    def finaliza(self):
        pass
            
class Em_aprovacao(Desconto_extra):
    def aplica_desconto_extra(self, orcamento):
        self.aprova(orcamento)
    def aprova(self,orcamento):
        orcamento.estado_atual = Aprovado()
        orcamento.estado_atual.aplica_desconto_extra(orcamento)
    def reprova(self):
        orcamento.estado_atual = Reprovado()
    def finaliza(self):
        raise Exception("Orçamentos em aprovação não podem ser finalizados")
            

class Aprovado(Desconto_extra):
    def aplica_desconto_extra(self, orcamento):
        orcamento.adiciona_desconto_extra(orcamento.valor * 0.05)
        self.finaliza()
    def aprova(self):
        raise Exception("Orçamento já aprovado")
    def reprova(self):
        raise Exception("Orçamentos aprovados não podem ser reprovados")
    def finaliza(self):
        orcamento.estado_atual = Finalizado()
        print(orcamento.estado_atual.get(orcamento))

class Reprovado(Desconto_extra):
    def aplica_desconto_extra(self,orcamento):
        raise Exception("Orçamentos reprovados não recebem desconto extra")
    def aprova(self):
        raise Exception("Orçamentos reprovados não podem ser aprovados")
    def reprova(self):
        raise Exception("Orçamento já reprovado")
    def finaliza(self):
        orcamento.estado_atual = Finalizado()
    
class Finalizado(Desconto_extra):
    def aplica_desconto_extra(self,orcamento):
        raise Exception("Orçamentos finalizados não receberam desconto extra")
    def get(self,orcamento):
        return  {"valor":orcamento.valor, "estado":orcamento.estado_atual}
    def aprova(self):
        raise Exception("Orçamentos finalizados não podem ser aprovados")
    def reprova(self):
        raise Exception("Orçamentos finalizados não podem ser aprovados")
    def finaliza(self):
        raise Exception("Orçamentos finalizados não receberam desconto extra")
    
class Orcamento(object):


    def __init__(self,estado_atual=Em_aprovacao()):
        self.__itens = []
        self.estado_atual = estado_atual
        self.__desconto_extra = 0

    def aplica_desconto_extra(self):
        self.estado_atual.aplica_desconto_extra(self)
        
    def adiciona_desconto_extra(self, desconto):
        self.__desconto_extra += desconto
    
    # quando a propriedade for acessada, ela soma cada item retornando o valor do orçamento
    @property
    def valor(self):
        total = 0.0
        for item in self.__itens:
            total+= item.valor
        return total - self.__desconto_extra

    # retornamos uma tupla, já que não faz sentido alterar os itens de um orçamento
    def obter_itens(self):

        return tuple(self.__itens)

    @property
    def total_itens(self):
        return len(self.__itens)

    def adiciona_item(self, item):
        self.__itens.append(item)

    def set_item(self,value):
        self.__itens = value
        return Orcamento()

# um item criado não pode ser alterado, suas propriedades são somente leitura
class Item(object):

    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    @property
    def nome(self):
        return self.__nome
    

if __name__ == '__main__':
    orcamento = Orcamento()

    orcamento.set_item(
			[
			Item('Item A', 1900.0),
			Item('Item B', 150.0),
			Item('Item C', 800.0)
			]
		)
    orcamento.aplica_desconto_extra()    