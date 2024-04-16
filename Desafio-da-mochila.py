class Objeto:
    def __init__(self, nome, peso, valor):
        self.nome = nome
        self.peso = peso
        self.valor = valor
        self.razao = valor / peso

def preencher_mochila(objetos, capacidade_maxima):
    # Ordena os objetos por valor/peso em ordem decrescente
    objetos.sort(key=lambda x: x.razao, reverse=True)

    mochila = []
    peso_atual = 0
    valor_total = 0

    for obj in objetos:
        if peso_atual + obj.peso <= capacidade_maxima:
            mochila.append(obj)
            peso_atual += obj.peso
            valor_total += obj.valor

        if peso_atual == capacidade_maxima:
            break

    return mochila, peso_atual, valor_total

# Exemplos de uso
objetos = [
    Objeto('Estojo', 3, 80),
    Objeto('Caderno', 8, 100),
    Objeto('Garrafinha', 4, 60),
    Objeto('Casaco', 7, 120),
    Objeto('Computador', 35, 200)
]

capacidade_maxima = 20

print("Capacidade máxima da mochila:", capacidade_maxima)
mochila_selecionada, peso_total, valor_total = preencher_mochila(objetos, capacidade_maxima)
print("Objetos selecionados na mochila:")
for obj in mochila_selecionada:
    print(f"- {obj.nome}: Peso - {obj.peso}, Valor - {obj.valor}")
print("Peso total na mochila:", peso_total)
print("Valor total na mochila:", valor_total)
