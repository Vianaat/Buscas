from queue import PriorityQueue

class Cidade:
    def __init__(self, nome):
        self.nome = nome
        self.vizinhos = []

    def adicionarVizinho(self, vizinho, distancia):
        self.vizinhos.append({"cidade": vizinho, "custo": distancia})

def buscaDeCustoUniforme(origem, objetivo):
    borda = PriorityQueue() 
    borda.put((0, origem)) 
    visitados = set()

    while not borda.empty():
        custo, cidade = borda.get() 
        if cidade == objetivo:
            return custo

        if cidade not in visitados:
            visitados.add(cidade)
            for vizinho in cidade.vizinhos:
                custo_vizinho = custo + vizinho["custo"]
                borda.put((custo_vizinho, vizinho["cidade"]))

    return None

arad = Cidade("Arad")
zerind = Cidade("Zerind")
oradea = Cidade("Oradea")
sibiu = Cidade("Sibiu")
timisoara = Cidade("Timisoara")
lugoj = Cidade("Lugoj")
mehadia = Cidade("Mehadia")
dobreta = Cidade("Dobreta")
craiova = Cidade("Craiova")
rimnicuVilcea = Cidade("Rimnicu Vilcea")
fagaras = Cidade("Fagaras")
pitesti = Cidade("Pitesti")
bucharest = Cidade("Bucharest")
giurgiu = Cidade("Giurgiu")
urziceni = Cidade("Urziceni")
hirsova = Cidade("Hirsova")
eforie = Cidade("Eforie")
vaslui = Cidade("Vaslui")
iasi = Cidade("Iasi")
neamt = Cidade("Neamt")

arad.adicionarVizinho(sibiu, 140)
arad.adicionarVizinho(timisoara, 118)
arad.adicionarVizinho(zerind, 75)

zerind.adicionarVizinho(arad, 75)
zerind.adicionarVizinho(oradea, 71)

oradea.adicionarVizinho(zerind, 71)
oradea.adicionarVizinho(sibiu, 151)

sibiu.adicionarVizinho(arad, 140)
sibiu.adicionarVizinho(fagaras, 99)
sibiu.adicionarVizinho(oradea, 151)
sibiu.adicionarVizinho(rimnicuVilcea, 80)

timisoara.adicionarVizinho(arad, 118)
timisoara.adicionarVizinho(lugoj, 111)

lugoj.adicionarVizinho(timisoara, 111)
lugoj.adicionarVizinho(mehadia, 70)

mehadia.adicionarVizinho(lugoj, 70)
mehadia.adicionarVizinho(dobreta, 75)

dobreta.adicionarVizinho(mehadia, 75)
dobreta.adicionarVizinho(craiova, 120)

craiova.adicionarVizinho(dobreta, 120)
craiova.adicionarVizinho(pitesti, 138)
craiova.adicionarVizinho(rimnicuVilcea, 146)

rimnicuVilcea.adicionarVizinho(sibiu, 80)
rimnicuVilcea.adicionarVizinho(pitesti, 97)
rimnicuVilcea.adicionarVizinho(craiova, 146)

fagaras.adicionarVizinho(sibiu, 99)
fagaras.adicionarVizinho(bucharest, 211)

pitesti.adicionarVizinho(rimnicuVilcea, 97)
pitesti.adicionarVizinho(craiova, 138)
pitesti.adicionarVizinho(bucharest, 101)

bucharest.adicionarVizinho(fagaras, 211)
bucharest.adicionarVizinho(pitesti, 101)
bucharest.adicionarVizinho(giurgiu, 90)
bucharest.adicionarVizinho(urziceni, 85)

giurgiu.adicionarVizinho(bucharest, 90)

urziceni.adicionarVizinho(bucharest, 85)
urziceni.adicionarVizinho(hirsova, 98)
urziceni.adicionarVizinho(vaslui, 142)

hirsova.adicionarVizinho(urziceni, 98)
hirsova.adicionarVizinho(eforie, 86)

eforie.adicionarVizinho(hirsova, 86)

vaslui.adicionarVizinho(urziceni, 142)
vaslui.adicionarVizinho(iasi, 92)

iasi.adicionarVizinho(vaslui, 92)
iasi.adicionarVizinho(neamt, 87)

neamt.adicionarVizinho(iasi, 87)


resultado = buscaDeCustoUniforme(sibiu, bucharest)

if resultado is not None:
    print("Menor custo:", resultado)
else:
    print("Não foi possível encontrar um caminho.")
