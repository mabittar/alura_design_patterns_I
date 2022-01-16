from abc import ABCMeta, abstractclassmethod

class BaseCalc(metaclass=ABCMeta):
    """
    classe base para calculo de descontos e impostos
    """

    @abstractclassmethod
    def calcula(self):
        pass


class TemplateImpostosCondicionais(object):
    __metaclass__ = ABCMeta

    def calcula(self, orcamento):
        if self.deve_usar_maxima_tax(orcamento):
            return self.maxima_tax(orcamento)
        else:
            return self.minima_tax(orcamento)

    @abstractclassmethod
    def deve_usar_maxima_tax(self, orcamento):
        pass

    @abstractclassmethod
    def maxima_tax(self, orcamento):
        pass

    @abstractclassmethod
    def minima_tax(self, orcamento):
        pass