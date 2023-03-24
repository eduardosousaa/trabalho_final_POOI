from camisas import Camisas, Historico
import datetime

class Nacionais(Camisas):
    def __init__(self, id, time, preco=0, quantidade=0, tamanho='', pais=''):
        super().__init__(id, time, preco, quantidade, tamanho, pais)
        self.historico_compras = Historico()

    def comprar(self, quantidade, cpf):
        data = datetime.datetime.now()
        '''A variável data pega o momento exato da compra da camisa e armazena no histórico.'''
        if quantidade > 0 and quantidade <= self.quantidade:
            self.quantidade -= quantidade
            self.historico_compras.add_compra(f'Data da compra: {data}\nCPF do cliente: {cpf}\nQuantidade de camisas compradas: {quantidade}\nTotal do pedido: R$ {quantidade * self.preco}\n')
            return True, ('Sucesso na compra :)')
        else:
            self.historico_compras.add_compra('Ops, algo deu errado! ')
            return False, ('Erro na compra :( ')
        
    def listar_camisas(self):
        print('-' * 30)
        print(f'Id: {self.id}')
        print(f'Time: {self.time}')
        print(f'País: {self.pais}')
        print(f'Preco: {self.preco}')
        print(f'Quantidade: {int(self.quantidade)}')
        print(f'Tamanho: {self.tamanho}')
        print('-' * 30)
        print()