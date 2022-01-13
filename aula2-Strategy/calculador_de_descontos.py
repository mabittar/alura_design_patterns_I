from curses.ascii import isdigit
from decimal import Decimal
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

    print(orcamento.valor)

    desconto_calculado = CalculadoraDescontos.calcula(orcamento)

    print(f"Desconto calculado: {desconto_calculado}")