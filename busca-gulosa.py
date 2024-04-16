class Cidade:
    def __init__(self, nome, distancia_objetivo):
        self.nome = nome
        self.distancia_objetivo = distancia_objetivo
        self.vizinhos = []

    def adicionar_vizinho(self, vizinho):
        self.vizinhos.append({"cidade": vizinho})


def busca_gulosa(inicio, objetivo):
    atual = inicio
    caminho = [inicio.nome]  

    while atual.nome != objetivo.nome:  
        menor_distancia = float("inf")  
        proxima_cidade = None

        for vizinho in atual.vizinhos:  
            if vizinho["cidade"].distancia_objetivo < menor_distancia:
                menor_distancia = vizinho["cidade"].distancia_objetivo
                proxima_cidade = vizinho["cidade"]

        if proxima_cidade is None:
            return None

        atual = proxima_cidade
        caminho.append(atual.nome)

    return caminho


arad = Cidade("Arad", 366)
zerind = Cidade("Zerind", 374)
oradea = Cidade("Oradea", 380)
sibiu = Cidade("Sibiu", 253)
timisoara = Cidade("Timisoara", 329)
lugoj = Cidade("Lugoj", 244)
mehadia = Cidade("Mehadia", 241)
dobreta = Cidade("Dobreta", 242)
craiova = Cidade("Craiova", 160)
rimnicu_vilcea = Cidade("Rimnicu Vilcea", 193)
fagaras = Cidade("Fagaras", 178)
pitesti = Cidade("Pitesti", 98)
bucharest = Cidade("Bucharest", 0)
giurgiu = Cidade("Giurgiu", 77)
urziceni = Cidade("Urziceni", 80)
hirsova = Cidade("Hirsova", 151)
eforie = Cidade("Eforie", 161)
vaslui = Cidade("Vaslui", 199)
iasi = Cidade("Iasi", 226)
neamt = Cidade("Neamt", 234)


arad.adicionar_vizinho(sibiu)
arad.adicionar_vizinho(timisoara)
arad.adicionar_vizinho(zerind)

zerind.adicionar_vizinho(arad)
zerind.adicionar_vizinho(oradea)

oradea.adicionar_vizinho(zerind)
oradea.adicionar_vizinho(sibiu)

sibiu.adicionar_vizinho(arad)
sibiu.adicionar_vizinho(fagaras)
sibiu.adicionar_vizinho(oradea)
sibiu.adicionar_vizinho(rimnicu_vilcea)

timisoara.adicionar_vizinho(arad)
timisoara.adicionar_vizinho(lugoj)

lugoj.adicionar_vizinho(timisoara)
lugoj.adicionar_vizinho(mehadia)

mehadia.adicionar_vizinho(lugoj)
mehadia.adicionar_vizinho(dobreta)

dobreta.adicionar_vizinho(mehadia)
dobreta.adicionar_vizinho(craiova)

craiova.adicionar_vizinho(dobreta)
craiova.adicionar_vizinho(pitesti)
craiova.adicionar_vizinho(rimnicu_vilcea)

rimnicu_vilcea.adicionar_vizinho(sibiu)
rimnicu_vilcea.adicionar_vizinho(pitesti)
rimnicu_vilcea.adicionar_vizinho(craiova)

fagaras.adicionar_vizinho(sibiu)
fagaras.adicionar_vizinho(bucharest)

pitesti.adicionar_vizinho(rimnicu_vilcea)
pitesti.adicionar_vizinho(craiova)
pitesti.adicionar_vizinho(bucharest)

bucharest.adicionar_vizinho(fagaras)
bucharest.adicionar_vizinho(pitesti)
bucharest.adicionar_vizinho(giurgiu)
bucharest.adicionar_vizinho(urziceni)

giurgiu.adicionar_vizinho(bucharest)

urziceni.adicionar_vizinho(bucharest)
urziceni.adicionar_vizinho(hirsova)
urziceni.adicionar_vizinho(vaslui)

hirsova.adicionar_vizinho(urziceni)
hirsova.adicionar_vizinho(eforie)

eforie.adicionar_vizinho(hirsova)

vaslui.adicionar_vizinho(urziceni)
vaslui.adicionar_vizinho(iasi)

iasi.adicionar_vizinho(vaslui)
iasi.adicionar_vizinho(neamt)

neamt.adicionar_vizinho(iasi)


resultado = busca_gulosa(arad, bucharest)
if resultado is not None:
    print("Caminho encontrado:", " -> ".join(resultado))
else:
    print("Caminho não encontrado!")