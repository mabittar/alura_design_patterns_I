from decimal import Decimal
from basecalc import BaseCalc
from orcamento import Orcamento


class DescontoPorItens(BaseCalc):

    @classmethod
    def calcula(cls, orcamento: Orcamento):
        print("verificando desconto por itens")

        if orcamento.total_itens >= 5:
            return orcamento.valor * Decimal(0.1)
        else:
            return 0


class DescontoPorTotal(BaseCalc):

    @classmethod
    def calcula(cls, orcamento):
        print("verificando desconto por total")

        valor = orcamento.valor
        if valor >= 500:
            return valor * Decimal(0.07)
        else:
            return 0