from datetime import datetime
from nota_fiscal import NotaFiscal
from nota_fiscal import Item
from observadores import imprime, envia_email, salva_banco

class CriadorNotaFiscal:
    def __init__(self):
        self.__razao_social = None
        self.__cnpj = None
        self.__data_de_emissao = None
        self.__itens = None
        self.__detalhes = None


        # chamando os métodos
        self.__envia_por_email(self)
        self.__salva_no_banco(self)
        self.__imprime(self)

    def __envia_por_email(self, nota_fiscal):
        print ('enviando nota por e-mail...')

    def __salva_no_banco(self, nota_fiscal):
        print ('salvando no banco...')

    def __imprime(self, nota_fiscal):
        print ('imprimindo ...')


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
                detalhes=self.__detalhes,
                observadores=[imprime, envia_email, salva_banco]
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