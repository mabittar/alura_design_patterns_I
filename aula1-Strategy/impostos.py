import abc
from decimal import Decimal


class BaseImpostos(metaclass=abc.ABCMeta):
    """
    classe base para impostos
    """
    @abc.abstractclassmethod
    def calcula(self):
        pass


class ISS(BaseImpostos):
    """
    classe para calculo do ISS
    """
    def calcula(valor: float) -> Decimal:
        return Decimal(valor * 0.1)


class ICMS(BaseImpostos):
    """
    classe para calculo do ICMS
    """
    def calcula(valor: float) -> Decimal:
        return Decimal(valor * 0.06)
