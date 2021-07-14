import numpy as np
import math
# Caso arquivo não exita ele é criado, somente leitura utilizar a (fazer try catch)
nome=input("Informe o nome é o formato do arquivo: ")
file = open(nome,'r')

#lendo a primeira linha
header = file.readline()
info = header.replace("\n", "").split(" ")
#salvando nvertices e narestas
nVertices = int(info[0])
nArestas = int(info[1])
#criando matriz de zeros
matriz = np.zeros((nVertices,nVertices))
#criando lista de zeros
lista=[[] for _ in range(nVertices)]


for line in (file):
  # recuperando dados do arquivo (origem, destino e peso)
  info = line.split(" ")
  origem = int(info[0])
  destino = int(info[1])
  peso = int(info[2])
  # criar matriz de adjacencias
  matriz[origem][destino] = peso
  matriz[destino][origem] = peso
  # criando lisa de adjacencias
  lista[origem].append((destino,peso))
  lista[destino].append((origem,peso))
 
print("Lista de adjacencias:")
for i in range(nVertices):
  print(lista[i])

print("Matriz de adjacencias: \n",matriz)



#print("Lista de adjacencias: \n",lista)


file.close()