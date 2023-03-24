from pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome, cpf, data_nascimento, profissao):
        super().__init__(nome, cpf, data_nascimento)
        self._profissao = profissao
    
    #Get e Set
    @property
    def profissao(self):
        return self._profissao

    @profissao.setter
    def profissao(self, profissao):
        self._profissao = profissao
    
    def listar_clientes(self):
        print()
        print('-' * 40)
        print('CLIENTE')
        print(f'Nome: {self.nome}')
        print(f'CPF: {self.cpf}')
        print(f'Data de nascimento: {self.data_nascimento}')
        print(f'Profissão: {self.profissao}')
        print('-' * 40)

    def listar_clientes2(self):
        print()
        print('-' * 40)
        print('CLIENTE')
        print(f'Nome: {self.nome}')
        print(f'CPF: {self.cpf}')
        print('-' * 40)