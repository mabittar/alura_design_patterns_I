from decimal import Decimal

class Orcamento(object):

    def __init__(self):
        self.status_dict = {
            "em_aprovação": 0.02,
            "aprovado": 0.05,
            "reprovado": 0,
            "finalizado": 0
        }

        self.__itens = []
        self.status = "em_aprovação"
        self.desconto_extra = Decimal(0.02).quantize(Decimal("1.00"))
        self.total = Decimal(0)

    def aplica_desconto_extra(self, status: str):
        desconto = self.status_dict.get(status, "em_aprovação")
        if self.status in ("reprovado", "finalizado"):
            raise Exception(f"Nào pode haver alteração de status para orçamento finalizado ou reprovado")
        if desconto is None:
            raise Exception(f"Status ainda não definido ou inválido: {status}")
        else:
            self.status = status
            desconto = self.valor * Decimal(desconto).quantize(Decimal("1.00"))
            self.desconto_extra = desconto

    @property
    def valor(self) -> Decimal:
        total = Decimal(0)
        for item in self.__itens:
            total += Decimal(item.valor)
        total = total - self.desconto_extra
        self.total = total.quantize(Decimal("1.00"))
        return self.total

    def obter_itens(self):
        return tuple(self.__itens)

    @property
    def total_itens(self):
        return len(self.__itens)

    def adiciona_item(self, item):
        self.__itens.append(item)


class Item(object):

    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    @property
    def nome(self):
        return self.__nome
