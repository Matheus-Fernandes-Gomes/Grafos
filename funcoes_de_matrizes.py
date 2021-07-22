class GrafoMatriz:
    # Inicializador
    def __init__(self, arquivo):
        # Classe com todos os atributos e metodos do grafo na representação matriz de adjacencias
        (self.vertices, self.arestas, self.grafo) = self.cria_adjacencia(arquivo)
        (self.maior_grau, self.menor_grau, self.grau_medio, self.frequencia) = self.definir_graus()
        #busca no vertices 0
        self.busca_em_largura(0)
        self.busca_de_profundidade(0)
        (self.componentes_conexas, self.num_conexa) = self.conexidade()

    def cria_adjacencia(self, arquivo):
        # cria matriz de adjacencias
        header = arquivo.readline()
        info = header.split(' ')
        vertices = int(info[0])
        arestas = int(info[1])
        matriz = [[0 for _ in range(vertices)] for _ in range(vertices)]

        for header in arquivo:
            info = header.split(' ')
            origem = int(info[0])
            destino = int(info[1])
            peso = int(info[2])
            matriz[origem][destino] = peso
            matriz[destino][origem] = peso
        return (vertices, arestas, matriz)

    def definir_graus(self):
        # #C vertice de maior e menor grau, o grau medio dos vertices e a distribuicão empirica do grau dos vertices
       
        maior = [0, 0]
        menor = [0, 1000000]
        soma = 0
        distribuicao = [0 for _ in range(self.vertices)]
        frequencia = []
        arquivo4 = open("distribuicao.txt", 'w')
        for i in range(self.vertices):
            aux = 0
            for j in range(self.vertices):
                if self.grafo[i][j] != 0:
                    aux = aux + 1
            distribuicao[aux] = distribuicao[aux] + 1
            if maior[1] < aux:
                maior[0] = i
                maior[1] = aux
            elif menor[1] > aux:
                menor[0] = i
                menor[1] = aux
            soma = soma + aux
        for i in range(self.vertices):
            if distribuicao[i] != 0:
                frequencia.append((i, distribuicao[i]))
                st = str(i) + ':' + str(100 * distribuicao[i] / self.vertices) + '\n'
                arquivo4.write(st)
        arquivo4.close()
        media = float(soma)/float(self.vertices)
        return (maior, menor, media, frequencia)

    def busca_em_largura(self, s):
        # cria um arquivo com arestas percorridas por largura

        arquivo2 = open('nivel_largura.txt', 'w')
        desc = [0 for _ in range(len(self.grafo))]
        Q = [s]
        R = [s]
        desc[s] = 1
        ordem = [-1 for _ in range(len(self.grafo))]
        ordem[s] = 0
        while len(Q) != 0:
            u = Q.pop(0)
            for v in range(len(self.grafo[u])):
                if self.grafo[u][v] != 0 and desc[v] == 0:
                    Q.append(v)
                    R.append(v)
                    desc[v] = 1
                    if ordem[v] == -1:
                        ordem[v] = ordem[u] + 1
        for i in range(len(ordem)):
            if ordem[i] != -1:
                saidas = str(i) + ':' + str(ordem[i]) + '\n'
                arquivo2.write(saidas)
        arquivo2.close()

    def busca_de_profundidade(self, s):
        # cria um arquivo com arestas percorridas por profundidade

        arquivo3 = open('nivel_profundidade.txt', 'w')
        desc = [0 for _ in range(len(self.grafo))]
        S = [s]
        R = [s]
        desc[s] = 1
        ordem = [-1 for _ in range(len(self.grafo))]
        ordem[s] = 0
        while len(S) != 0:
            u = S[-1]
            desempilhar = True
            for v in range(len(self.grafo[u])):
                if self.grafo[u][v] != 0 and desc[v] == 0:
                    desempilhar = False
                    S.append(v)
                    R.append(v)
                    desc[v] = 1
                    if ordem[v] == -1:
                        ordem[v] = ordem[u] + 1
                    break
            if desempilhar:
                S.pop()
        for i in range(len(ordem)):
            if ordem[i] != -1:
                saidas = str(i) + ':' + str(ordem[i]) + '\n'
                arquivo3.write(saidas)
        arquivo3.close()

    def busca_largura(self, comp, s):
        # busca em largura 
        desc = [0 for _ in range(self.vertices)]
        Q = [s]
        R = [s]
        desc[s] = 1
        comp[s] = 0
        while len(Q) != 0:
            u = Q.pop(0)
            for v in range(self.vertices):
                if self.grafo[u][v] != 0 and desc[v] == 0:
                    Q.append(v)
                    R.append(v)
                    desc[v] = 1
                    comp[v] = 0
        return R

    def conexidade(self):
        # numero de componentes conexas no grafo, e vertices na componentes
        componente = [1 for _ in range(self.vertices)]
        t = []
        k = 0
        for i in range(len(self.grafo)):
            bit = 0
            if componente[i] != 0:
                busca = self.busca_largura(componente, i)
                t.append(len(busca))
                k = k + 1
            for j in range(self.vertices):
                if componente[j] == 0:
                    bit = bit + 1
                if bit == self.vertices:
                    return (k, t)
