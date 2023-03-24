import abc

#Classe abstrata
class Taxacao(abc.ABC):
    
    #Método abstrato
    @abc.abstractmethod
    def taxar(self):
        pass