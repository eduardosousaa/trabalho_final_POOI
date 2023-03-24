import abc
import datetime

class Camisas(abc.ABC):
    def __init__(self, id, time, preco = 0, quantidade = 0, tamanho = '', pais = ''):
        self._id = id
        self._time = time
        self._preco = preco
        self._quantidade = quantidade
        self._tamanho = tamanho
        self._pais = pais

    #Método abstrato
    @abc.abstractmethod
    def comprar(self, quantidade, cpf):
        pass

    #Getters e Setters
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id 

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, time):
        self._time = time 

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, preco):
        self.preco = preco

    @property
    def quantidade(self):
        return self._quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        self._quantidade = quantidade

    @property
    def tamanho(self):
        return self._tamanho

    @tamanho.setter
    def tamanho(self, tamanho):
        self._tamanho = tamanho

    @property
    def pais(self):
        return self._pais

    @pais.setter
    def pais(self, pais):
        self._pais = pais


class Historico():
    def __init__(self):
        self._compra = []
    
    @property
    def compra(self):
        return self._compra
    
    def add_compra(self, t):
        self.compra.append(t)

    def imprime(self):
        for t in self.compra:
            print(t)

    