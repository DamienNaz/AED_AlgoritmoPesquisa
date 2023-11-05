import time
import statistics
import matplotlib.pyplot as plt
import random

def f_tempo(funcao, entrada, n_vezes, *args):
    """
    Calcula o tempo médio e desvio padrão de execução de uma função.

    Args:
        funcao: A função a ser analisada.
        entrada: Um input para a função.
        n_vezes: O número de vezes que a função deve ser executada.

    Returns:
        tempos_execucao: Uma lista dos tempos de execução individuais.
        tempo_medio: O tempo médio de execução.
        desvio_padrao: O desvio padrão do tempo de execução.
    """
    tempos_execucao = []
    for _ in range(n_vezes):
        start_time = time.time()
        funcao(entrada, *args)
        end_time = time.time()
        tempos_execucao.append(end_time - start_time)

    tempo_medio = statistics.mean(tempos_execucao)
    desvio_padrao = statistics.stdev(tempos_execucao)

    return tempos_execucao, tempo_medio, desvio_padrao


def f_boxplot(tempos_execucao):
    """
    Desenha um boxplot dos tempos de execução.

    Args:
        tempos_execucao: Uma lista de tempos de execução.
    """
    plt.boxplot(tempos_execucao)
    plt.show()

def f_complexidade(funcao, lista_inputs, n_vezes):
    """
    Avalia a complexidade de uma função para diferentes inputs.

    Args:
        funcao: A função a ser analisada.
        lista_inputs: Lista de inputs da função para avaliar o tempo de execução.
        n_vezes: O número de vezes que a função deve ser executada para cada input.

    Returns:
        dic_stats: Um dicionário com médias e desvios padrão para cada input.
        dic_tempos: Um dicionário com listas de tempos para cada input.
    """
    dic_stats = {}
    dic_tempos = {}

    for entrada in lista_inputs:
        tempos_execucao, tempo_medio, desvio_padrao = f_tempo(funcao, entrada, n_vezes)
        dic_stats[entrada] = (tempo_medio, desvio_padrao)
        dic_tempos[entrada] = tempos_execucao

    return dic_stats, dic_tempos

def f_complexidade_boxplot(dic_tempos):
    """
    Gera um gráfico de tempo médio de execução em função dos inputs.

    Args:
        dic_tempos: Um dicionário com listas de tempos de execução para diferentes inputs.
    """
    medias = [statistics.mean(dic_tempos[entrada]) for entrada in dic_tempos]
    inputs = list(dic_tempos.keys())

    plt.plot(inputs, medias, marker='o')
    plt.xlabel('Entradas')
    plt.ylabel('Tempo Médio de Execução')
    plt.show()
