import time


# Define nosso decorator
def calcula_duracao(funcao):

    def wrapper(*args):
        # Calcula o tempo de execução
        tempo_inicial = time.time()
        funcao(*args)
        tempo_final = time.time()

        # Formata a mensagem que será mostrada na tela
        print("[{funcao}] Tempo total de execução: {tempo_total}".format(
            funcao=funcao.__name__,
            tempo_total=str(tempo_final - tempo_inicial)))

    return wrapper


@calcula_duracao
def executa(end: int):
    for n in range(0, end):
        if end <= 100:
            pass
        else:
            print("end deve ser menor que 100!!!")

if __name__ == '__main__':
    executa(20)