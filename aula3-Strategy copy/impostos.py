from decimal import Decimal

from basecalc import BaseCalc


class ISS(BaseCalc):
    """
    classe para calculo do ISS
    """

    @staticmethod
    def calcula(valor: Decimal) -> Decimal:
        return Decimal(valor) * Decimal(0.1)


class ICMS(BaseCalc):
    """
    classe para calculo do ICMS
    """

    @staticmethod
    def calcula(valor: Decimal) -> Decimal:
        return Decimal(valor) * Decimal(0.06)
