from datetime import date
from abc import ABCMeta, abstractmethod

class Nota_fiscal_Um(object):
    __metaclass__ = ABCMeta
    
    def __init__(self, razao_social, cnpj, total, data_de_emissao, detalhes):
        self.__razao_social = razao_social
        self.__cnpj = cnpj
        self.__data_de_emissao = data_de_emissao
        if(len(detalhes) > 20):
            raise NameError('Detalhes da nota não pode ter mais do que 20 caracteres')
        self.__detalhes = detalhes
        self.__total = total

    def __str__(self):
        return f"   NOTA FISCAL 1 - 2022      \n"

class Nota_fiscal_Dois(object):
    __metaclass__ = ABCMeta
    
    def __init__(self, razao_social, cnpj, total, data_de_emissao, detalhes):
        self.__razao_social = razao_social
        self.__cnpj = cnpj
        self.__data_de_emissao = data_de_emissao
        if(len(detalhes) > 20):
            raise NameError('Detalhes da nota não pode ter mais do que 20 caracteres')
        self.__detalhes = detalhes
        self.__total = total

    def __str__(self):
        return f"    NOTA FISCAL 2 - 2022      \n"
        


class Criador_de_nota_fiscal(object):
    def __init__(self):
        self.__razao_social = None
        self.__cnpj = None
        self.__data_de_emissao = date.today()
        self.__itens = None
        self.__detalhes = ""
        self.__template = 1
            
    def com_razao_social(self,razao_social):
        self.__razao_social = razao_social
        return self
        
    def com_cnpj(self,cnpj):
        self.__cnpj = cnpj
        return self
        
    def com_data_de_emissao(self,data_de_emissao):
        self.__data_de_emissao = data_de_emissao
        return self
        
    def com_detalhes(self,detalhes):
        self.__detalhes = detalhes
        return self
    
    def com_itens(self,itens):
        self.__itens = itens
        return self
        
    def com_total(self,total):
        self.__total = total
        return self
    
    def com__template(self, template):
        self.__template = template
        return self
    
    def checaTemplateNf(self):
        if self.__template == 1:
            return Nota_fiscal_Um(self.__razao_social,self.__cnpj, self.__total,self.__data_de_emissao, self.__detalhes).__str__()
        return Nota_fiscal_Dois(self.__razao_social,self.__cnpj, self.__total,self.__data_de_emissao, self.__detalhes).__str__()
    
    def mostraItens(self):
        teste = ''
        for i in self.__itens:
           teste = i['nome'] + teste
        return teste
            
    def __str__(self):
        return  (
            f"=================================\n"+
            self.checaTemplateNf() +
            f"Razão Social: {self.__razao_social}\n"+
            f"CNPJ: {self.__cnpj}\n"+
            f"Detalhes: {self.__detalhes if self.__detalhes != '' else '-'}\n"+
            f"    ITENS      \n" 
            f"Total: R$ {self.__total}\n"+
            f"Emissão: {self.__data_de_emissao}\n"
            f"=================================\n")
    
    def constroi(self):
        if self.__razao_social == None:
            raise Exception("Razão social é obrigatória")        
        elif self.__cnpj == None:
            raise Exception("CNPJ é obrigatório")   
        elif self.__itens == None:
            raise Exception("Itens são obrigatórios")   
        
        return self.__str__() 
        
