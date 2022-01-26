from curses.ascii import isdigit
from decimal import Decimal
from os import stat
from descontos import DescontoPorItens, DescontoPorTotal

class CalculadoraDescontos:
    @classmethod
    def calcula(cls, orcamento) -> Decimal:
        desconto = DescontoPorItens.calcula(orcamento)
        if desconto == 0:
            desconto = DescontoPorTotal.calcula(orcamento)
        return Decimal(desconto).quantize(Decimal("1.00"))

if __name__ == '__main__':
    from orcamento import Orcamento, Item

    orcamento = Orcamento()
    orcamento.adiciona_item(Item(nome='Item 1', valor=100))
    orcamento.adiciona_item(Item(nome='Item 2', valor=50))
    orcamento.adiciona_item(Item(nome='Item 2', valor=50))
    orcamento.adiciona_item(Item(nome='Item 2', valor=50))
    orcamento.adiciona_item(Item(nome='Item 2', valor=50))
    orcamento.adiciona_item(Item(nome='Item 2', valor=50))
    orcamento.adiciona_item(Item(nome='Item 2', valor=50))
    orcamento.adiciona_item(Item(nome='Item 2', valor=50))
    orcamento.adiciona_item(Item(nome='Item 2', valor=50))
    orcamento.adiciona_item(Item(nome='Item 2', valor=50))
    orcamento.adiciona_item(Item(nome='Item 2', valor=50))
    orcamento.adiciona_item(Item(nome='Item 2', valor=50))
    orcamento.adiciona_item(Item(nome='Item 2', valor=50))
    orcamento.adiciona_item(Item(nome='Item 2', valor=50))
    orcamento.adiciona_item(Item(nome='Item 3', valor=100))

    print(f"Orçamento inicial: {orcamento.valor}")
    print(f"Aplicando descontos")

    desconto_calculado = CalculadoraDescontos.calcula(orcamento)

    print(f"Desconto calculado: {desconto_calculado}")
    print(f"Desconto extra: {orcamento.desconto_extra}")
    print(f"Orçamento total: {orcamento.valor}, status: {orcamento.status}")
    print(f"Orçamento aprovado!!!!")
    orcamento.aplica_desconto_extra(status="aprovado")
    print(f"Desconto extra: {orcamento.desconto_extra}")
    print(f"Orçamento total: {orcamento.valor}, status: {orcamento.status}")
    print(f"Orçamento finalizado!!!!")
    orcamento.aplica_desconto_extra(status="finalizado")
