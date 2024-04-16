class Cidade:
    def __init__(self, nome, distanciaObjetivo):
        self.nome = nome
        self.distanciaObjetivo = distanciaObjetivo
        self.vizinhos = []

    def adicionarVizinho(self, vizinho, distancia):
        self.vizinhos.append({"cidade": vizinho, "custo": distancia})

def buscaAEstrela(inicio, objetivo):
    abertos = [inicio]  
    fechados = []  
    caminho = {}

   
    def custoTotalEstimado(cidade):
        return cidade.distanciaObjetivo + caminho[cidade.nome]["custo"]

    caminho[inicio.nome] = {"custo": 0, "pai": None}  

    while abertos:
        
        cidadeAtual = min(abertos, key=lambda cidade: custoTotalEstimado(cidade))

        if cidadeAtual == objetivo:
            caminhoFinal = []
            while cidadeAtual:
                caminhoFinal.insert(0, cidadeAtual.nome)
                cidadeAtual = caminho[cidadeAtual.nome]["pai"]
            return caminhoFinal

        
        abertos.remove(cidadeAtual)
        fechados.append(cidadeAtual)

        for vizinho in cidadeAtual.vizinhos:
            if vizinho["cidade"] not in fechados:  
                custoAtualizado = caminho[cidadeAtual.nome]["custo"] + vizinho["custo"]

                
                if vizinho["cidade"] not in abertos or custoAtualizado < caminho[vizinho["cidade"].nome]["custo"]:
                    caminho[vizinho["cidade"].nome] = {"custo": custoAtualizado, "pai": cidadeAtual}  
                    if vizinho["cidade"] not in abertos:
                        abertos.append(vizinho["cidade"])  
    return None


arad = Cidade("Arad", 366)
zerind = Cidade("Zerind", 374)
oradea = Cidade("Oradea", 380)
sibiu = Cidade("Sibiu", 253)
timisoara = Cidade("Timisoara", 329)
lugoj = Cidade("Lugoj", 244)
mehadia = Cidade("Mehadia", 241)
dobreta = Cidade("Dobreta", 242)
craiova = Cidade("Craiova", 160)
rimnicuVilcea = Cidade("Rimnicu Vilcea", 193)
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


resultado = buscaAEstrela(arad, bucharest)

if resultado:
    print("Caminho encontrado:")
    print(resultado)
else:
    print("Caminho não encontrado.")
