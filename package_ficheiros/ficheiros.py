import random
def gerar_arquivo_aleatorio(nome_arquivo, num_registros):
    """
    Gera um arquivo com números aleatórios.

    Args:
        nome_arquivo (str): O nome do arquivo a ser criado.
        num_registros (int): O número de registros a serem gerados e escritos no arquivo.
    """
    with open(nome_arquivo, 'w') as arquivo:
        for _ in range(num_registros):
            num = random.randint(0, 1000000)
            arquivo.write(str(num) + '\n')

def ordenar_arquivo(arquivo_entrada, arquivo_saida):
    """
    Lê um arquivo de entrada, ordena os números e escreve o resultado no arquivo de saída.

    Args:
        arquivo_entrada (str): O nome do arquivo de entrada com números desordenados.
        arquivo_saida (str): O nome do arquivo onde os números ordenados serão gravados.
    """
    with open(arquivo_entrada, 'r') as arquivo_entrada:
        numeros = [int(linha) for linha in arquivo_entrada]
        numeros.sort()
    with open(arquivo_saida, 'w') as arquivo_saida:
        for num in numeros:
            arquivo_saida.write(str(num) + '\n')

tamanhos_arquivos = [100, 1000, 10000, 100000]
for tamanho in tamanhos_arquivos:
    arquivo_aleatorio = f'aleatorio_{tamanho}.txt'
    arquivo_ordenado = f'ordenado_{tamanho}.txt'
    gerar_arquivo_aleatorio(arquivo_aleatorio, tamanho)
    ordenar_arquivo(arquivo_aleatorio, arquivo_ordenado)

    print(f'Arquivos criados para {tamanho} números.')
print('Concluído.')
