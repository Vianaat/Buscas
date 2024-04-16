class Cidade:
    def __init__(self, nome):
        self.nome = nome
        self.vizinhos = []

    def adicionarVizinho(self, vizinho):
        self.vizinhos.append({"cidade": vizinho})


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


arad.adicionarVizinho(sibiu)
arad.adicionarVizinho(timisoara)
arad.adicionarVizinho(zerind)

zerind.adicionarVizinho(arad)
zerind.adicionarVizinho(oradea)

oradea.adicionarVizinho(zerind)
oradea.adicionarVizinho(sibiu)

sibiu.adicionarVizinho(arad)
sibiu.adicionarVizinho(fagaras)
sibiu.adicionarVizinho(oradea)
sibiu.adicionarVizinho(rimnicuVilcea)

timisoara.adicionarVizinho(arad)
timisoara.adicionarVizinho(lugoj)

lugoj.adicionarVizinho(timisoara)
lugoj.adicionarVizinho(mehadia)

mehadia.adicionarVizinho(lugoj)
mehadia.adicionarVizinho(dobreta)

dobreta.adicionarVizinho(mehadia)
dobreta.adicionarVizinho(craiova)

craiova.adicionarVizinho(dobreta)
craiova.adicionarVizinho(pitesti)
craiova.adicionarVizinho(rimnicuVilcea)

rimnicuVilcea.adicionarVizinho(sibiu)
rimnicuVilcea.adicionarVizinho(pitesti)
rimnicuVilcea.adicionarVizinho(craiova)

fagaras.adicionarVizinho(sibiu)
fagaras.adicionarVizinho(bucharest)

pitesti.adicionarVizinho(rimnicuVilcea)
pitesti.adicionarVizinho(craiova)
pitesti.adicionarVizinho(bucharest)

bucharest.adicionarVizinho(fagaras)
bucharest.adicionarVizinho(pitesti)
bucharest.adicionarVizinho(giurgiu)
bucharest.adicionarVizinho(urziceni)

giurgiu.adicionarVizinho(bucharest)

urziceni.adicionarVizinho(bucharest)
urziceni.adicionarVizinho(hirsova)
urziceni.adicionarVizinho(vaslui)

hirsova.adicionarVizinho(urziceni)
hirsova.adicionarVizinho(eforie)

eforie.adicionarVizinho(hirsova)

vaslui.adicionarVizinho(urziceni)
vaslui.adicionarVizinho(iasi)

iasi.adicionarVizinho(vaslui)
iasi.adicionarVizinho(neamt)

neamt.adicionarVizinho(iasi)


def buscaEmProfundidadeLimitada(inicio, objetivo, limiteProfundidade):
    pilha = [] 
    visitados = set() 

    pilha.append({"no": inicio, "profundidade": 0}) 
    visitados.add(inicio) 

    while pilha:
        no_atual = pilha.pop() 

        no = no_atual["no"]
        profundidade = no_atual["profundidade"]

        print(f"Visitando a cidade: {no.nome}")

        if no.nome == objetivo.nome:
            print(f"Encontrou o objetivo: {no.nome}")
            return True

        if profundidade >= limiteProfundidade:
            continue

        for vizinho in reversed(no.vizinhos):
            if vizinho["cidade"] not in visitados: 
                pilha.append({"no": vizinho["cidade"], "profundidade": profundidade + 1})
                visitados.add(vizinho["cidade"]) 

    return False


def buscaProfundidadeIterativa(inicio, objetivo):
    limiteProfundidade = 0 

    while True:
        print(f"Tentando com limite de profundidade: {limiteProfundidade}")

        encontrado = buscaEmProfundidadeLimitada(inicio, objetivo, limiteProfundidade)

        if encontrado:
            print(f"Objetivo encontrado com limite de profundidade {limiteProfundidade}")
            return True
        else:
            print(f"Objetivo não encontrado com limite de profundidade {limiteProfundidade}")
            limiteProfundidade += 1


resultado = buscaProfundidadeIterativa(arad, bucharest)

if resultado:
    print("Caminho encontrado!")
else:
    print("Caminho não encontrado!")
