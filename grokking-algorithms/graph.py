grafo = {}
grafo["voce"] = ["alice", "bob", "claire"]
grafo["alice"] = ["peggy"]
grafo["bob"] = ["anuj", "peggy"]
grafo["claire"] = ["thom", "jonny"]
grafo["anuj"] = []
grafo["jonny"] = []
grafo["peggy"] = []
grafo["thom"] = []

fila_pesquisa = list()
fila_pesquisa += grafo["voce"]

def pessoa_e_vendedor(nome):
    return nome == 'jonny'

def busca_fila(fila_pesquisa):
    verificadas = []
    while fila_pesquisa:
        pessoa = fila_pesquisa.pop(0)
        
        if not pessoa in verificadas:
            print(pessoa)
            if pessoa_e_vendedor(pessoa):
                print (pessoa + " é um vendedor")
                return True
                
            else: 
                fila_pesquisa += grafo[pessoa]
                verificadas.append(pessoa)

    return False

busca_fila(fila_pesquisa)

grafo = {} 
grafo["inicio"] = {}
grafo["inicio"]["a"] = 6
grafo["inicio"]["b"] = 2

print (grafo["inicio"].keys())

grafo["a"] = {}
grafo["a"]["fim"] = 1

grafo["b"] = {}
grafo["b"]["a"] = 3
grafo["b"]["fim"] = 5

grafo["fim"] = {}


infinito = float("inf")
custos = {}
custos["a"] = 6
custos["b"] = 2
custos["fim"] = infinito

pais = {}
pais["a"] = "inicio"
pais["b"] = "inicio"
pais["fim"] = None

processados = []

def find_low_node_cost(custos): 
    custo_mais_baixo = float("inf")
    nodo_custo_mais_baixo = None

    for nodo in custos:
        custo = custos[nodo]
        
        if custo < custo_mais_baixo and nodo not in processados:
            custo_mais_baixo = custo
            nodo_custo_mais_baixo = nodo

    return nodo_custo_mais_baixo

nodo = find_low_node_cost(custos)

while nodo is not None:
    custo = custos[nodo]
    vizinhos = grafo[nodo]

    for n in vizinhos.keys():
        novo_custo = custo + vizinhos[n]

        if custos[n] > novo_custo:
            custos[n] = novo_custo
            pais[n] = nodo
    
    processados.append(nodo)
    nodo = find_low_node_cost(custos)

print(custos, pais)