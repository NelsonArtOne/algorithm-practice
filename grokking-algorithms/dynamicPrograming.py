def print_matriz(matriz):
    mat = []
    for lin in range(len(matriz)):
        linha = []

        for col in range(len(matriz[lin])):
            linha.append(matriz[lin][col])
        mat.append(linha)

    for i in range(len(mat)):
        print(mat[i])

def maior_valor_linha(matriz):
    linha = []
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            linha.append(matriz[i][j])
    
    print(max(linha))

def calcula_palavra(palavra1, palavra2):
    matriz = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
    
    for i in range(len(palavra1)):
        
        for j in range(len(palavra2)):
            if palavra1[i] == palavra2[j]:
                matriz[i][j] = matriz[i-1][j-1] + 1
            else:
                matriz[i][j] = 0
       

    print_matriz(matriz)
    maior_valor_linha(matriz)


calcula_palavra("FISH", "HISH")


