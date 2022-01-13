from impostos import ISS, ICMS


class CalculadorImpostos(object):
    def realiza_calculo(self, orcamento, imposto):
        imposto_calculado = 0
        imposto_calculado = imposto.calcula(orcamento.valor)

        print (imposto_calculado)


if __name__ == '__main__':
    from orcamento import Orcamento

    calculador = CalculadorImpostos()

    orcamento = Orcamento(valor=500)

    calculador.realiza_calculo(orcamento=orcamento, imposto=ISS)
    calculador.realiza_calculo(orcamento=orcamento, imposto=ICMS)