import numpy as np
import math
import collections
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
#inicializando maior e menor valor 
cont=0
aux=0
ultimo=-1
maior=-1

cont2=0
aux2=0
ultimo2=-1
menor=-1

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
  #maior e menor grau
  #c=(collections.Counter(info[0]))
  if info[0]==ultimo:
    cont+=1
    aux+=1
  else:
    if cont>=aux:
      maior=info[0]
      aux+=1
  ultimo=info[0]
  cont=0
  #menor grau
  if info[0]==ultimo2:
    cont2+=1
    aux2+=1
  else:
    if cont2<aux2:
      menor=info[0]
      aux2=1
  ultimo2=info[0]
  cont2=0
#busca
i=0
for i in range(int(info[0])):
  print(info[i])

  
print("Maior grau: ",aux,"- vertice: ",maior)   
print("Menor grau: ",aux2,"- vertice: ",menor)

  
 
print("Lista de adjacencias:")
for i in range(nVertices):
  print(lista[i])

print("Matriz de adjacencias: \n",matriz)



#print("Lista de adjacencias: \n",lista)


file.close()