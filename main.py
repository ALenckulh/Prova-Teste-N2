from PROVA_TESTES_2024.testes.stat_funcs import StatsN2

stat = StatsN2()

if __name__ == "__main__":
    lista = [6, 7, 8, 9, 10]
    numeros_unimodal = lista
    numeros_multimodal = lista
    numeros_amodal = lista
    pesos = [0.5,0.1,0.1,0.1,0.1]

    mmodal = stat.multimodal(lista=numeros_multimodal)
    print(f" Distribuição multimodal {mmodal}")
    umodal = stat.unimodal(lista=numeros_unimodal)
    print(f" Distribuição unimodal {umodal}")
    amodal = stat.amodal(lista=numeros_amodal)
    print(f" Distribuição amodal {amodal}")

    media = stat.media(lista=numeros_amodal)
    print(f" Media {media}")

    media_ponderada = stat.media_ponderada(lista=numeros_amodal, pesos=pesos)
    print(f" Media ponderada {media_ponderada}")

    mediana = stat.mediana(lista=numeros_multimodal)
    print(f" Mediana {mediana}")

    variancia = stat.variancia(lista=numeros_multimodal)
    print(f" Variancia {variancia}")

    desvio = stat.dpadrao(var=variancia)
    print(f" Desvio Padrão {desvio}")

    skew = stat.skew(lista=numeros_multimodal)
    print(f" Distribuição: {skew}")