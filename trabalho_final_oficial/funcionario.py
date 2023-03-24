from pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, cpf, data_nascimento, salario):
        super().__init__(nome, cpf, data_nascimento)
        self._salario = salario

    #Get e Set
    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, salario):
        self._salario = salario

    