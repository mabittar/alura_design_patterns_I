from abc import ABCMeta, abstractclassmethod
from ast import Or
from decimal import Decimal
from typing import Optional, Union
from orcamento import Orcamento


class BaseCalc(metaclass=ABCMeta):
    """
    classe base para calculo de descontos e impostos
    """

    def __init__(self, outra_base=None):
        self.__outra_base = outra_base

    def calculo_da_outra_base(self, orcamento: Orcamento) -> Decimal:
        if self.__outra_base is None:
            return Decimal(0)
        else:
            return self.__outra_base(orcamento)


    @abstractclassmethod
    def calcula(self, orcamento: Orcamento):
        pass


class TemplateImpostosCondicionais(BaseCalc):
    __metaclass__ = ABCMeta

    def calcula(self, orcamento) -> Decimal:
        if self.deve_usar_maxima_tax(orcamento):
            return self.maxima_tax(orcamento) + self.calculo_da_outra_base(
                orcamento)
        else:
            return self.minima_tax(orcamento) + self.calculo_da_outra_base(
                orcamento)

    @abstractclassmethod
    def deve_usar_maxima_tax(self, orcamento: Decimal):
        pass

    @abstractclassmethod
    def maxima_tax(self, orcamento: Decimal):
        pass

    @abstractclassmethod
    def minima_tax(self, orcamento: Decimal):
        pass