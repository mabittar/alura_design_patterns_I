from datetime import datetime
from nota_fiscal import NotaFiscal
from nota_fiscal import Item


class CriadorNotaFiscal:
    def __init__(self):
        self.__razao_social = None
        self.__cnpj = None
        self.__data_de_emissao = None
        self.__itens = None
        self.__detalhes = None

    def razao_social(self, razao_social):
        self.__razao_social  = razao_social
        return self

    def cnpj(self, cnpj):
        self.__cnpj = cnpj
        return self

    def data__de_emissao(self, data__de_emissao):
        self.__data_de_emissao = data__de_emissao
        return self

    def com_itens(self, items):
        self.__itens = items
        return self

    def com_detalhes(self, detalhes):
        self.__detalhes = detalhes
        return self

    def construtor(self):
        if self.__cnpj is None:
            self.__cnpj = '987654321/0001'
        if self.__razao_social is None:
            self.__razao_social = 'Minha empresa teste'
        if self.__data_de_emissao is None:
            self.__data_de_emissao = datetime.today()
        if self.__detalhes is None:
            self.__detalhes = ""
        if self.__itens is None:
            raise Exception('Nota fiscal não pode ser emitida sem itens')


        nota_fiscal = (
            NotaFiscal(
                razao_social=self.__razao_social,
                cnpj=self.__cnpj,
                data_de_emissao=self.__data_de_emissao,
                itens=self.__itens,
                detalhes=self.__detalhes
            )
            )
        return nota_fiscal


if __name__ == '__main__':

    itens = [
        Item(descricao='ITEM A', valor=100),
        Item(descricao='ITEM B', valor=200)
    ]

    # usando nosso Builder.
    nota_fiscal = (
        CriadorNotaFiscal()
        .razao_social('FHSA Limitada')
        .cnpj('012345678901234')
        .com_itens(itens)
        .construtor()
        )

    print (nota_fiscal.razao_social)
    print (nota_fiscal.cnpj)
    print (nota_fiscal.detalhes)