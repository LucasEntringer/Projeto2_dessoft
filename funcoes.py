def define_posicoes (linha, coluna, orientacao, tamanho):
    res = []
    if orientacao == "vertical":
        for i in range(tamanho):
            res.append([linha+i, coluna])
    elif orientacao == "horizontal":
        for i in range(tamanho):
            res.append([linha, coluna + i])
    return res
