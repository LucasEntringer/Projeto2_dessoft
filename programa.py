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
    # for i in range(quantidade[navio]):
    i = 1
    while i <= quantidade[navio]:
        j = 0
        while j == 0:
            print(f'Insira as informações referentes ao navio {navio} que possui tamanho {valor}')
            linha = int(input('Linha: '))
            coluna = int(input('Coluna: '))
            orientacao = 'vertical'
            tam = tamanho[navio]
            if navio != 'submarino':
                direcao = int(input('Digite 1 para vertical ou 2 para horizontal: '))
                if direcao == 2:
                    orientacao = 'horizontal'
                elif direcao != 2 and direcao != 1:
                    print('Esta posição não é válida')
                    break
            if posicao_valida(frota, linha, coluna, orientacao, tam) == True:
                frota = preenche_frota(frota, navio, linha, coluna, orientacao, tam)
                j = 1
                break
            else: print('Esta posição não é válida')
print(frota)
