'''
M10L-ex01. Crie uma classe Person, contendo os atributos encapsulados, com seus respectivos 
seletores (getters) e modificadores (setters), e ainda o construtor padrão. Atributos: 
nome, endereço, CPF, RG e telefone. 
'''

class Pessoa:
    def __init__(self, nome, endereço, cpf, rg, telefone):
        if not self.verify_nome(nome):
            raise Exception("NOME INVÁLIDO\n")
        else:
            self.__name = nome

        '''if not self.verify_endereço(endereço):
            raise Exception("ENDEREÇO INVÁLIDO\n")
        else:'''
        self.__endereço = endereço

        if not self.verify_cpf(cpf):
            raise Exception("CPF INVÁLIDO\n")
        else:
            self.__cpf = cpf

        if not self.verify_rg(rg):
            raise Exception("RG INVÁLIDO\n")
        else:
            self.__rg = rg

        if not self.verify_telefone(telefone):
            raise Exception("TELEFONE INVÁLIDO\n")
        else:
            self.__telefone = telefone

    def get_name(self):
        return self.__name

    def set_name(self, nome):
        self.__nome = nome

    def get_endereço(self):
        return self.__endereço

    def set_endereço(self, endereço):
        self.__endereço = endereço

    def get_cpf(self):
        return self.__cpf

    def set_cpf(self, cpf):
        self.__cpf = cpf

    def get_rg(self):
        return self.__rg

    def set_rg(self, rg):
        self.__rg = rg

    def get_telefone(self):
        return self.__telefone

    def set_telefone(self, telefone):
        self.__telefone = telefone

    def formatar_cpf(self):
        return f"{self.__cpf[:3]}.{self.__cpf[3:6]}.{self.__cpf[6:9]}-{self.__cpf[9:11]}"

    def formatar_rg(self):
        return f"{self.__rg[:2]}.{self.__rg[2:5]}.{self.__rg[5:8]}-{self.__rg[8:9]}"

    def formatar_telefone(self):
        return f"({self.__telefone[:2]}) {self.__telefone[2:7]}-{self.__telefone[7:11]}"

    @staticmethod
    def verify_nome(nome):
        if len(nome) >= 3 and nome.replace(" ", "").isalpha():
            return True
        return False

    @staticmethod
    def verify_endereço(endereço):
        pass

    @staticmethod
    def verify_cpf(cpf):
        if len(cpf) == 11:
            return True
        return False

    @staticmethod
    def verify_rg(rg):
        if len(rg) == 9:
            return True
        return False
    
    @staticmethod
    def verify_telefone(telefone):
        if len(telefone) == 11:
            return True
        return False

'''
M10L-ex02. Considere, como subclasse da classe Person, a classe Supplier, para representar um 
fornecedor. Considere que cada instância da classe Supplier tem, para além dos
atributos que caracterizam a classe Person, os atributos valueCredit (correspondente 
ao crédito máximo atribuído ao fornecedor) e valueDebt (montante da dívida para com 
o fornecedor). Implemente na classe Supplier, para além dos usuais métodos 
seletores e modificadores, um método getBalance() que devolve a diferença entre os 
valores dos atributos valueCredit e valueDebt. Depois de implementada a classe 
Supplier, altere o main para que você possa verificar o funcionamento dos métodos 
implementados na classe Supplier e os herdados da classe Person. 
'''

class Supplier(Pessoa):
    def __init__(self, nome, endereço, cpf, rg, telefone, valueCredit, valueDebt):
        super().__init__(nome, endereço, cpf, rg, telefone)
        self.__valueCredit = valueCredit
        self.__valueDebt = valueDebt

    def get_valueCredit(self):
        return self.__valueCredit

    def set_valueCredit(self, valueCredit):
        self.__valueCredit = valueCredit

    def get_valueDebt(self):
        return self.__valueDebt

    def set_valueDebt(self, valueDebt):
        self.__valueDebt = valueDebt

    def getBalance(self):
        return self.__valueCredit - self.__valueDebt
