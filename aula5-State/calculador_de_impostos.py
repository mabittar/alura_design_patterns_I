from impostos import ICMS, ICPP, IKCV, ISS
from orcamento import Item


class CalculadorImpostos(object):
    def realiza_calculo(self, orcamento, imposto):
        imposto_calculado = 0
        if imposto in (ISS, ICMS):
            imposto_calculado = imposto.calcula(orcamento)
        elif imposto in (ICPP, IKCV):
            imposto_calculado = imposto().calcula(orcamento)

        print (imposto_calculado)


if __name__ == '__main__':
    from orcamento import Orcamento

    calculador = CalculadorImpostos()
    orcamento = Orcamento()

    orcamento.adiciona_item(Item(nome='Item 1', valor=100))

    print("Calcula ISS E ICMS")
    calculador.realiza_calculo(orcamento=orcamento, imposto=ISS())
    calculador.realiza_calculo(orcamento=orcamento, imposto=ICMS())
    calculador.realiza_calculo(orcamento=orcamento, imposto=ICMS(ISS()))

    print("Calcula ICPP E IKCV")
    calculador.realiza_calculo(orcamento=orcamento, imposto=ICPP)
    calculador.realiza_calculo(orcamento=orcamento, imposto=IKCV)
