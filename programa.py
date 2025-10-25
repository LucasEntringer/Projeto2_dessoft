from funcoes import define_posicoes, preenche_frota, faz_jogada, posiciona_frota, afundados, posicao_valida, monta_tabuleiros
import random

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
    while colocados < quantidade[navio]:
        while True:
            print(f'Insira as informações referentes ao navio {navio} que possui tamanho {tam}')
            linha = int(input("Linha (0-9): "))
            if linha < 0 or linha > 9:
                print("Esta posição não está válida!")
                continue
            break
        while True:
            coluna = int(input("Coluna (0-9): "))
            if coluna < 0 or coluna > 9:
                print("Esta posição não está válida!")
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
                    print("Esta posição não está válida!")
        else:
            orientacao = 'vertical'

        if posicao_valida(frota, linha, coluna, orientacao, tam):
            frota = preenche_frota(frota, navio, linha, coluna, orientacao, tam)
            colocados += 1
        else:
            print("Esta posição não está válida!")

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}
tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro_jogador = posiciona_frota(frota)
print (monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))
while True:
    linha = int(input('Jogador, qual linha deseja atacar? '))
    while linha < 0 or linha > 9:
        print('Linha inválida!')
        linha = int(input('Jogador, qual linha deseja atacar? '))
    coluna = int(input('Jogador, qual coluna deseja atacar? '))
    while coluna < 0 or coluna > 9:
        print('Coluna inválida!')
        coluna = int(input('Jogador, qual coluna deseja atacar? '))
    if tabuleiro_oponente[linha][coluna] == '-' or tabuleiro_oponente[linha][coluna] == 'X':
        print(f'A posição linha {linha} e coluna {coluna} já foi informada anteriormente!')
        continue
    else:
        tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha, coluna)
    if afundados(frota_oponente, tabuleiro_oponente) == 10:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        break
    else:
        tentativas = 0
        while True: 
            linha_o = random.randint(0, 9)
            coluna_o = random.randint(0, 9)
            tentativas += 1
            if tentativas > 200:
                print('O oponente não encontrou posições válidas para poder atacar')
                break
            if tabuleiro_jogador[linha_o][coluna_o] == '-' or tabuleiro_jogador[linha_o][coluna_o] == 'X':
                continue
            tabuleiro_jogador = faz_jogada(tabuleiro_jogador, linha_o, coluna_o)
            print(f"Seu oponente está atacando na linha {linha_o} e coluna {coluna_o}")
            break

    if afundados(frota, tabuleiro_jogador) == 10:
        print("Xi! O oponente derrubou toda a sua frota =(")
        break
    
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))