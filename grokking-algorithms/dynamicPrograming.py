def print_matriz(matriz):
    for linha in matriz:
        print(linha)

def maior_valor_matriz(matriz):
    maior = 0
    
    for linha in matriz:
        for valor in linha:
            if valor > maior: 
                maior = valor
    
    return maior

def criar_matriz(quantidade_linhas : int, quantidade_colunas : int): 
    matriz = []

    for i in range(quantidade_linhas):
        matriz.append([])
        for j in range(quantidade_colunas):
            matriz[i].append(0)
    
    return matriz

def calcula_maior_substring(matriz, palavra_a, palavra_b):
    
    for i in range(len(palavra_a)):
            
            for j in range(len(palavra_b)):
                if palavra_a[i] == palavra_b[j]:
                    matriz[i][j] = matriz[i-1][j-1] + 1
                else:
                    matriz[i][j] = 0   
    
    return matriz

def calcula_palavra(palavra_a, palavra_b):
    matriz = criar_matriz(len(palavra_a) + 1, len(palavra_b) +1 )
    matriz = calcula_maior_substring(matriz, palavra_a, palavra_b)
    print_matriz(matriz)
    print(maior_valor_matriz(matriz))


calcula_palavra("FISH", "HISH")
