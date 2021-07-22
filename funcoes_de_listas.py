class GrafoLista:
    # Classe com todos os atributos do grafo na representação lista de adjacencias
    def __init__(self, arquivo):
        (self.vertices, self.arestas, self.grafo) = self.cria_lista(arquivo)
        (self.maior_grau, self.menor_grau, self.grau_medio, self.frequencia) = self.definir_graus()
        #busca no vertice 0
        self.busca_em_largura2(0)
        self.busca_de_profundidade2(0)
        (self.componentes_conexas, self.num_conexa) = self.conexidade()

    def cria_lista(self, arquivo):
        # Cria lista de adjacencias"
        header = arquivo.readline()
        info = header.split(' ')
        vertices = int(info[0])
        arestas = int(info[1])
        lista = []
        for i in range(vertices):
            lista.append([])
        for header in arquivo:
            info = header.split(' ')
            origem = int(info[0])
            destino = int(info[1])
            peso = int(info[2])
            lista[origem].append((destino, peso))
            lista[destino].append((origem, peso))
        return (vertices, arestas, lista)

    def definir_graus(self):
        #C vertice de maior e menor grau, o grau medio dos vertices e a distribuicão empirica do grau dos vertices
        maior = [0, 0]
        menor = [0, 1000000]
        soma = 0
        cont = [0 for _ in range(self.vertices)]
        frequencia = []
        arquivo4 = open("cont.txt", 'w')
        for i in range(self.vertices):
            cont[len(self.grafo[i])] = cont[len(self.grafo[i])] + 1
            if maior[1] < len(self.grafo[i]):
                maior[0] = i
                maior[1] = len(self.grafo[i])
            elif menor[1] > len(self.grafo[i]):
                menor[0] = i
                menor[1] = len(self.grafo[i])
            soma = soma + len(self.grafo[i])
        for i in range(self.vertices):
            if cont[i] != 0:
                frequencia.append((i, cont[i] / self.vertices))
                st = str(i) + ':' + str(100 * cont[i] / self.vertices) + '\n'
                arquivo4.write(st)
        arquivo4.close()
        media = float(soma) / float(self.vertices)
        return (maior, menor, media, frequencia)

    def busca_em_largura2(self, s):
        # cria um arquivo com arestas percorridas por largura
        arquivo2 = open('largura.txt', 'w')
        desc = [0 for _ in range(self.vertices)]
        Q = [s]
        R = [s]
        desc[s] = 1
        ordem = [-1 for _ in range(self.vertices)]
        ordem[s] = 0
        while len(Q) != 0:
            u = Q.pop(0)
            for (v, a) in self.grafo[u]:
                if desc[v] == 0:
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

    def busca_de_profundidade2(self, s):
        # cria um arquivo com arestas percorridas por profundidade
        arquivo3 = open('profundidade.txt', 'w')
        desc = [0 for _ in range(self.vertices)]
        S = [s]
        R = [s]
        desc[s] = 1
        ordem = [-1 for _ in range(self.vertices)]
        ordem[s] = 0
        while len(S) != 0:
            u = S[-1]
            desempilhar = True
            for (v, a) in self.grafo[u]:
                if desc[v] == 0:
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
        # busca em largura para lista
        desc = [0 for _ in range(self.vertices)]
        Q = [s]
        R = [s]
        desc[s] = 1
        comp[s] = 0
        while len(Q) != 0:
            u = Q.pop(0)
            for (v, a) in self.grafo[u]:
                if desc[v] == 0:
                    Q.append(v)
                    R.append(v)
                    desc[v] = 1
                    comp[v] = 0
        return R

    def conexidade(self):
        # Numero de componentes conexas no grafo, e vertices na componentes
        componente = [1 for _ in range(self.vertices)]
        t = []
        k = 0
        for i in range(self.vertices):
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
