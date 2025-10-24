def define_posicoes (linha, coluna, orientação, tamanho):
    res = []
    if orientação == 'vertical':
        for i in range(tamanho):
            casa = [linha + i, coluna]
            res.append(casa)
    else:
        for i in range(tamanho):
            casa = [linha, coluna + i]
            res.append(casa)
    return res
