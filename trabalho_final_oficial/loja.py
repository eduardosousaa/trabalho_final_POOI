from taxa import Taxacao

class Loja:
    def __init__(self):
        self._clientes = {}
        self._funcionarios = {}
        self._camisas_nacionais = {}
        self._camisas_inter = {}
        self._taxa_importacao = []
    
    @property
    def clientes(self):
        return self._clientes

    @clientes.setter
    def clientes(self, clientes):
        self._clientes = clientes

    @property
    def funcionarios(self):
        return self._funcionarios

    @funcionarios.setter
    def funcionarios(self, funcionarios):
        self._funcionarios = funcionarios

    @property
    def camisas_nacionais(self):
        return self._camisas_nacionais
    
    @camisas_nacionais.setter
    def camisas_nacionais(self, camisas_nacionais):
        self._camisas_nacionais = camisas_nacionais

    @property
    def camisas_inter(self):
        return self._camisas_inter

    @camisas_inter.setter
    def camisas_inter(self, camisas_inter):
        self._camisas_inter = camisas_inter

    @property
    def taxa_importacao(self):
        return self._taxa_importacao

    @taxa_importacao.setter
    def taxa_importacao(self, taxa_importacao):
        self._taxa_importacao = taxa_importacao

    def calcular_taxacao(self):
        a = SistemaDeTaxacao()
        cont = 0
        for x in self.camisas_inter.values():
            cont += a.taxa(x)
        self.taxa_importacao.append(cont)

    def imprimir_taxacao(self):
        for x in self.taxa_importacao:
            print(f'Taxa de importação: R$ {float(x)}')
            print()

class SistemaDeTaxacao():

    def taxa(self, obj):
        if isinstance(obj, Taxacao):
            return obj.taxar()