from funcoes import define_posicoes, preenche_frota, faz_jogada, posiciona_frota, afundados, posicao_valida

frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}     

tamanho = {
    "porta-aviões":4,
    "navio-tanque":3,
    "contratorpedeiro":2,
    "submarino": 1,
}

quantidade = {
    "porta-aviões": 1,
    "navio-tanque": 2,
    "contratorpedeiro": 3,
    "submarino": 4,
}

for navio, valor in tamanho.items():
    for i in range(quantidade[navio]):
        print(f'Insira as informações referentes ao navio {navio} que possui tamanho {valor}')
        linha = int(input('Linha: '))
        coluna = int(input('Coluna: '))
        orientacao = 'vertical'
        if navio != 'submarino':
            direcao = int(input('Digite 1 para vertical ou 2 para horizontal: '))
            if direcao == 2:
                orientacao = 'horizontal'
        if posicao_valida(frota, linha, coluna, orientacao, tamanho) == True:
            frota = preenche_frota(frota, navio, linha, coluna, orientacao, tamanho)
        else: print('Esta posição não é válida')