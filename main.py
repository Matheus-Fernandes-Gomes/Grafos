import os
import timeit
import funcoes_de_matrizes
import funcoes_de_listas
import numpy as np
#verifica e entra no arquivo do grafo
verificador = False
arquivo = ''
while not verificador:
    arquivo = input('\n Informe o nome do arquivo: ')
    verificador = os.path.exists(arquivo)
    if not verificador:
        espera = input("\nArquivo não encontrado!\n Verifique o nome do arquivo e tente novamente!")
print('\n Arquivo encontrado!\n')
arquivo = open(arquivo, 'r')

#seleção de lista ou matriz para o grafo.
print('\tEscolha a representação do grafo desejado:\nSendo:')
cond=True
while (cond):
    selecao = input('\t1 para lista de adjacencias. \n\t2 para matriz de adjacencias: ')
    selecao = int(selecao)
    if ((selecao==1)or(selecao==2)):
        cond=False
    else:
        print('\n selecao invalida!')


if selecao == 1:
    #Lista de adjacencias
    print('\n\nLista de adjacencias:')
    #Medindo o tempo de execução
    tempoinicio = timeit.default_timer()
    #chamando a função de listas
    retorno = funcoes_de_listas.GrafoLista(arquivo)
    tempofinal = timeit.default_timer()
    #limitando impressão do grafo em 12 vertices
    if retorno.vertices < 12:
        for item in retorno.grafo:
            print('\t', item)
    else:
        print('\n Grafo muito grande para ser impresso')
else:
    #Matriz de adjacencias
    print('\n\nMatriz de adjacencias:')
    #Medindo o tempo de execução
    tempoinicio = timeit.default_timer()
    #chamando a função de matrizes
    retorno = funcoes_de_matrizes.GrafoMatriz(arquivo)
    tempofinal = timeit.default_timer()
    #limitando impressão do grafo em 12 vertices
    if retorno.vertices < 12:
        for item in retorno.grafo:
            print('\t', item)
    else:
        print('\n Grafo muito grande para ser impresso')


#C vertice de maior e menor grau, o grau medio dos vertices e a distribuicão empirica do grau dos vertices

print('Maior grau:', retorno.maior_grau[1], '- vertice:', retorno.maior_grau[0])
print('Menor grau:', retorno.menor_grau[1], '- vertice:', retorno.menor_grau[0])
print('\nGrau Medio:', retorno.grau_medio)
print('Frequencia relativa:')

for (grau, freq) in retorno.frequencia:
    print('\tGrau', grau, ': ', freq)
    
#E Componentes Conexas
print('Componentes conexas: ', retorno.componentes_conexas)

for item in retorno.num_conexa:
    print('-', item, 'vertices')
print('-Tempo de execução:',  tempofinal - tempoinicio)
input()

print('Numero de vertices:', retorno.vertices)
print('Numero de arestas:', retorno.arestas)
