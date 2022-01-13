from decimal import Decimal
from basecalc import BaseCalc

class ISS(BaseCalc):
    """
    classe para calculo do ISS
    """
    def calcula(valor: float) -> Decimal:
        return Decimal(valor * 0.1)


class ICMS(BaseCalc):
    """
    classe para calculo do ICMS
    """
    def calcula(valor: float) -> Decimal:
        return Decimal(valor * 0.06)
