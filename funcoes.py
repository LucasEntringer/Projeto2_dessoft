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

def posiciona_frota (frota):
    res = [[0] * 10 for _ in range(10)]
    for nome, lista in frota.items():
        for navio in lista:
            for posicao in navio:
                y,x = posicao
                res[y][x] = 1
    return  res

def afundados (frota, tabuleiro):
    res = 0
    for nome, lista in frota.items():
        for navio in lista:
            afunda = True
            for posicao in navio:
                y,x = posicao
                if tabuleiro[y][x] != 'X':
                    afunda = False
                    break
            if afunda == True:
                res += 1
    return res

def posicao_valida (frota, linha, coluna, orientacao, tamanho):
    novo = define_posicoes(linha, coluna, orientacao, tamanho)
    for posicao in novo:
        y,x = posicao
        if x >= 10 or y >= 10 or x< 0 or y < 0:
            return False
    for nome, lista in frota.items():
        for navio in lista:
            for pos in navio:
                if pos in novo:
                    return False
    return True

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto