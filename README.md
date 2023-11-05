# AED_AlgoritmoPesquisa

Neste repositório, encontrarás dois módulos que implementam algoritmos de pesquisa e análise de complexidade. Este trabalho tem como objetivo analisar o desempenho de algoritmos de pesquisa em diferentes tipos de dados, incluindo listas não ordenadas e ordenadas. 

Detalhes do projeto:

**Módulos**
Módulo pesquisa.py

Este módulo contém a implementação de quatro algoritmos de pesquisa:

Pesquisa Sequencial
Pesquisa Sequencial Recursiva
Pesquisa Binária
Pesquisa Binária Recursiva

Módulo complexidade.py
Este módulo fornece funções para analisar o desempenho de algoritmos, medindo o tempo de execução e criar os respectivos gráficos.

Aqui estão as principais funcionalidades do módulo:

Função f_tempo
Esta função calcula o tempo médio de execução de uma determinada função. Ela executa a função várias vezes e calcula o tempo médio e o desvio padrão dos tempos de execução. Os argumentos da função são:

funcao: A função a ser analisada.
entrada: Um input para a função.
n_vezes: O número de vezes que a função deve ser executada.

Função f_boxplot
Esta função gera um gráfico do tipo "boxplot" dos tempos de execução. Ela recebe uma lista de tempos de execução e cria um gráfico visual para analisar a distribuição dos tempos.

Função f_complexidade
Esta função avalia a complexidade de uma função para diferentes inputs. Ela chama a função f_tempo para vários inputs e gera estatísticas, incluindo o tempo médio e o desvio padrão, para cada input.

funcao: A função a ser analisada.
lista_inputs: Uma lista de inputs da função para avaliar o tempo de execução.
n_vezes: O número de vezes que a função deve ser executada para cada input.

Função f_complexidade_boxplot
Esta função gera um gráfico que mostra o tempo médio de execução em função dos inputs. Ela usa os dados gerados pela função f_complexidade para criar um gráfico de linhas que representa o tempo médio de execução em relação aos diferentes inputs.

Este módulo é útil para analisar o desempenho de algoritmos e entender como o tempo de execução varia com diferentes inputs. Pode ser usado para identificar a complexidade temporal de algoritmos e fazer comparações entre eles.


**Função para criar dados**
Geração de Dados
Foram gerados ficheiros contendo números inteiros aleatórios nos seguintes tamanhos: 100, 1 000, 10 000, 100 000 e 1 000 000. Os valores foram gerados aleatoriamente no intervalo de 0 a 1 000 000. Para cada um destes tamanhos, foi criado um ficheiro com os números não ordenados e outro ficheiro com os números ordenados. Isso resultou em um total de 8 ficheiros.

Análise de Desempenho
Para analisar o desempenho dos algoritmos, foi criado um Jupyter Notebook onde cada uma das funções de pesquisa é apresentada, e o número de operações T(n) é calculado. A complexidade temporal de cada algoritmo foi avaliada teoricamente, identificando o Big-O correspondente.

Usando o módulo de complexidade, a complexidade temporal de cada algoritmo de pesquisa foi avaliada para sequências não ordenadas e ordenadas. Três casos foram avaliados: melhor, pior e caso intermédio. O pior caso ocorre quando o número é o último da lista, enquanto o melhor caso é pelo contrário o primeiro elemento, e o caso intermédio um número aleatório que situado no meio da lista. 
