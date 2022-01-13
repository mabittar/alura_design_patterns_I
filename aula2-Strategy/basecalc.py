import abc

class BaseCalc(metaclass=abc.ABCMeta):
    """
    classe base para calculo de descontos e impostos
    """

    @abc.abstractclassmethod
    def calcula(self):
        pass