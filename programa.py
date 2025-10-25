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

for navio, tam in tamanho.items():
    colocados = 0
    print(f'Insira as informações referentes ao navio {navio} que possui tamanho {tam}')
    while colocados < quantidade[navio]:
        while True:
            linha = int(input("Linha (0-9): "))
            if linha < 0 or linha > 9:
                print("Entrada inválida. Digite apenas números inteiros não-negativos.")
                continue
            break
        while True:
            coluna = int(input("Coluna (0-9): "))
            if coluna < 0 or coluna > 9:
                print("Valor fora do intervalo [0-9]. Tente novamente.")
                continue
            break
        orientacao = 'vertical'
        if navio != 'submarino':
            while True:
                d = input("Digite 1 para vertical ou 2 para horizontal: ").strip()
                if d == '1':
                    orientacao = 'vertical'
                    break
                elif d == '2':
                    orientacao = 'horizontal'
                    break
                else:
                    print("Entrada inválida. Digite 1 ou 2.")
        else:
            orientacao = 'vertical'

        if posicao_valida(frota, linha, coluna, orientacao, tam):
            frota = preenche_frota(frota, navio, linha, coluna, orientacao, tam)
            colocados += 1
        else:
            print("Esta posição não é válida. Tente novamente.")
print(frota)
