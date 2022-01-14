from impostos import ISS, ICMS
from orcamento import Item

class CalculadorImpostos(object):
    def realiza_calculo(self, orcamento, imposto):
        imposto_calculado = 0
        imposto_calculado = imposto.calcula(orcamento.valor)

        print (imposto_calculado)


if __name__ == '__main__':
    from orcamento import Orcamento

    calculador = CalculadorImpostos()
    orcamento = Orcamento()

    orcamento.adiciona_item(Item(nome='Item 1', valor=100))

    calculador.realiza_calculo(orcamento=orcamento, imposto=ISS)
    calculador.realiza_calculo(orcamento=orcamento, imposto=ICMS)