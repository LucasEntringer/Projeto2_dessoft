def define_posicoes (linha, coluna, orientacao, tamanho):
    res = []
    if orientacao == "vertical":
        for i in range(tamanho):
            res.append([linha+i, coluna])
    elif orientacao == "horizontal":
        for i in range(tamanho):
            res.append([linha, coluna + i])
    return res

def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    res = frota
    if nome_navio in frota:
        res[nome_navio].append(define_posicoes(linha, coluna, orientacao, tamanho))
    else:
       res [nome_navio] = [define_posicoes(linha, coluna, orientacao, tamanho)]
    return res

def faz_jogada(tabuleiro, linha, coluna):
    pos = tabuleiro[linha][coluna]
    if pos == 1:
        pos = 'X'
    elif pos == 0:
        pos = '-'
    tabuleiro[linha][coluna] = pos
    return tabuleiro
