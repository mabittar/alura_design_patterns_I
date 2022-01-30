from decimal import Decimal
from orcamento import Orcamento
from basecalc import BaseCalc, TemplateImpostosCondicionais


class ISS(BaseCalc):
    """
    classe para calculo do ISS
    """

    def calcula(self, orcamento: Orcamento) -> Decimal:
        return orcamento.valor * Decimal(0.1) + self.calculo_da_outra_base(orcamento)


class ICMS(BaseCalc):
    """
    classe para calculo do ICMS
    """

    def calcula (self, orcamento: Orcamento) -> Decimal:
        return orcamento.valor * Decimal(0.06) + self.calculo_da_outra_base(
            orcamento)


class ICPP(TemplateImpostosCondicionais):

    def deve_usar_maxima_tax(self, orcamento: Orcamento) -> bool:
        return orcamento.valor >= Decimal(500)

    def maxima_tax(self, orcamento):
        return orcamento.valor * Decimal(0.07)

    def minima_tax(self, orcamento):
        return orcamento.valor * Decimal(0.05)


class IKCV(TemplateImpostosCondicionais):

    def deve_usar_maxima_tax(self, orcamento: Orcamento) -> bool:
        return (orcamento.valor > Decimal(500)
                and self.__tem_item_maior_que_100(orcamento))

    def maxima_tax(self, orcamento):
        return orcamento.valor * Decimal(0.1)

    def minima_tax(self, orcamento):
        return orcamento.valor * Decimal(0.06)

    def __tem_item_maior_que_100(self, orcamento: Orcamento):
        return any(x.valor() for x in orcamento.obter_itens())
