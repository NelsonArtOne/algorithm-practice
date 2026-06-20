estados_abranger = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

arr = [1, 2, 2, 3, 3, 3]

arr = set(arr)

print(arr)

estacoes = {}
estacoes["kum"] = set(["id", "nv", "ut"])
estacoes["kdois"] = set(["wa", "id", "mt"])
estacoes["ktres"] = set(["or", "nv", "ca"])
estacoes["kquatro"] = set(["nv", "ut"])
estacoes["kcinco"] = set(["ca", "az"])

estacoes_final = set()


def calcula_melhores_estações(estados_abranger : set):
    while estados_abranger:
        melhor_estacao = None
        estados_cobertos = set()

        for estacao, estado_por_estacao in estacoes.items():
            cobertos = estados_abranger & estado_por_estacao

            if len(cobertos) > len(estados_cobertos):
                melhor_estacao = estacao
                estados_cobertos = cobertos

        estados_abranger -= estados_cobertos
        estacoes_final.add(melhor_estacao)

calcula_melhores_estações(estados_abranger)
print(estacoes_final)



frutas = set(["abacate", "tomate", "banana"])
vegetais = set(["beterraba", "cenoura", "tomate"])
print(frutas | vegetais)
print(frutas & vegetais)
print(frutas - vegetais)
print(vegetais - frutas)

