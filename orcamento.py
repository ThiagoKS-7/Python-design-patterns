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
            orcamento.adiciona_desconto_extra(orcamento.valor * 0.02)
    def aprova(self):
        pass
    def reprova(self):
        pass
    def finaliza(self):
        raise Exception("Orçamentos finalizados não receberam desconto extra")
            

class Aprovado(Desconto_extra):
    def aplica_desconto_extra(self, orcamento):
            orcamento.adiciona_desconto_extra(orcamento.valor * 0.05)
    def aprova(self):
        raise Exception("Orçamentos finalizados não receberam desconto extra")
    def reprova(self):
        raise Exception("Orçamentos finalizados não receberam desconto extra")
    def finaliza(self):
        pass

class Reprovado(Desconto_extra):
    def aplica_desconto_extra(self,orcamento):
        raise Exception("Orçamentos reprovados não receberam desconto extra")
    def aprova(self):
        raise Exception("Orçamentos finalizados não receberam desconto extra")
    def reprova(self):
        raise Exception("Orçamentos finalizados não receberam desconto extra")
    def finaliza(self):
        pass
    
class Finalizado(Desconto_extra):
    def aplica_desconto_extra(self,orcamento):
        raise Exception("Orçamentos finalizados não receberam desconto extra")
    def aprova(self):
        raise Exception("Orçamentos finalizados não receberam desconto extra")
    def reprova(self):
        raise Exception("Orçamentos finalizados não receberam desconto extra")
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
    orcamento.estado_atual = Aprovado()
    orcamento.aplica_desconto_extra()
    print(orcamento.valor)