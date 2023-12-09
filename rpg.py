# O ssegundo jogo saiu \o/
# 
# Esse deu muuuuuuito mais trabalho, é tanta variável que eu me embananei em alguns momentos.
# 
# Características:
# - O jogador possui 3 habilidades com carga que se recarregam a cada x números de turno.
# - O jogador possui uma habilidade que causa dano de sangramento por 3 turnos.
# - O jogador possui uma habilidade que aumenta a defesa em 10 por 3 turnos.
# - O oponente possui uma habilidade que atordoa o jogador por 3 turnos.
# - Fiz formatação de cores pra melhorar a visualização.
# - Quem joga games com frequência já deve ter ouvido falar no tal balanceamento, oh trem chato de fazer, em um joguinho simples já foi difícil, imagina em jogos gigantescos, então pode acontecer de estar fácil ou roubado pro computador, não consegui balancear com consistência.
# - Joguem em tela cheia senão bagunça tudo, e se bagunçar por favor me avisem porque eu não sei como ele vai se comportar em telas menores.

from time import sleep
from random import randint

turno = 0
cargaespadada = 5
cargaescudo = 1
cargaestocar = 2
defesaplayer = 0
hpplayer = hpmonstro = 200
contsangramento = contescudo = contstun = contcd = stacksangramento = 0
danomonstro = 27
danoplayer = 25
danoestocada = 0
nonstun = True
cdstun = escudo = False

while True:
    turno += 1
    print(f'\033[1;36m{f"TURNO {turno}"::^117}\033[m')
    sleep(1)
    if turno % 5 == 0:
        if cargaespadada < 5:
            cargaespadada += 1
        if cargaestocar < 2:
            cargaestocar += 1
    if turno % 7 == 0:
        if cargaescudo < 1:
            cargaescudo += 1

    if nonstun:
        while True:
            print('Ações: ')
            if cargaespadada > 0:
                print(f'\033[1;32m{"[1] Espadada":<23}\033[m', end='')
            else:
                print(f'\033[1;31m{"[Recarga] Espadada":<23}\033[m', end='')
            if cargaescudo > 0 and escudo == False:
                print(f'\033[1;32m{"[2] Brandir Escudo":<40}\033[m', end='')
            else:
                print(f'\033[1;31m{"[Recarga] Brandir Escudo":<40}\033[m', end='')
            if cargaestocar > 0:
                print(f'\033[1;32m{"[3] Estocar"}\033[m')
            else:
                print(f'\033[1;31m{"[Recarga] Estocar"}\033[m')

            print(f'{f"Causa {danoplayer} de dano":<23}', end='')
            print(f'{"Recebe +10 de defesa por 3 turnos":<40}', end='')
            print(f'{"Causa 3 danos entre 4 a 12 e sangramento por 3 turnos"}')

            print(f'Carga: {cargaespadada:<16}', end='')
            print(f'Carga: {cargaescudo:<33}', end='')
            print(f'Carga: {cargaestocar}')

            escolha = str(input('Escolha a ação: '))
            if escolha == '1' and cargaespadada == 0:
                print(' ')
                print('\033[1;31mHabilidade em recarga, tente novamente!\033[m')
            elif escolha == '2' and cargaescudo == 0:
                print('\033[1;31mHabilidade em recarga, tente novamente!\033[m')
                print(' ')
            elif escolha == '2' and escudo:
                print('\033[1;31mHabilidade já ativa, tente novamente!\033[m')
                print(' ')
            elif escolha == '3' and cargaestocar == 0:
                print(' ')
                print('\033[1;31mHabilidade em recarga, tente novamente!\033[m')
            elif escolha == '1' or escolha == '2' or escolha == '3':
                break
            elif escolha != '1' or escolha != '2' or escolha != '3':
                print(' ')
                print('\033[1;31mOpção inválida, tente novamente!\033[m')

        if escolha == '1':
            hpmonstro -= danoplayer
            cargaespadada -= 1
            print('\033[1;34m-\033[m' * 117)
            print(f'Você causa \033[1;31m{danoplayer}\033[m de dano!')
            if hpmonstro > 0:
                print(f'HP do inimigo: \033[1;32m{hpmonstro}\033[m')
            else:
                print(f'HP do inimigo: \033[1;32m0\033[m')
            print('\033[1;34m-\033[m' * 117)
            sleep(1)

        elif escolha == '2':
            cargaescudo -= 1
            contescudo = 3
            defesaplayer += 10
            print('\033[1;34m-\033[m' * 117)
            print(f'Sua defesa sobe para \033[1;34m{defesaplayer}!')
            print('\033[1;34m-\033[m' * 117)
            escudo = True
            sleep(1)

        if escolha == '3':
            stacksangramento += 1
            cargaestocar -= 1
            if contsangramento == 0:
                contsangramento = 3
            print('\033[1;34m-\033[m' * 117)
            for c in range(1, 4):
                if hpmonstro > 0:
                    danoestocada = randint(4, 12)
                    hpmonstro -= danoestocada
                print(f'{c}° dano causa \033[1;31m{danoestocada}\033[m!')
                sleep(0.7)
            if hpmonstro > 0:
                print(f'HP do inimigo: \033[1;32m{hpmonstro}\033[m')
            else:
                print(f'HP do inimigo: \033[1;32m0\033[m')
            print('\033[1;34m-\033[m' * 117)

    if contescudo > 0:
        contescudo -= 1
    elif contescudo == 0:
        defesaplayer = 0
        escudo = False

    if contsangramento > 0:
        if hpmonstro > 0:
            hpmonstro -= 5 * stacksangramento
            contsangramento -= 1
            print('\033[1;35m-\033[m' * 117)
            print('O inimigo recebe dano por \033[1;31msangramento\033[m!')
            if hpmonstro > 0:
                print(f'HP do inimigo: \033[1;32m{hpmonstro}\033[m')
            else:
                print(f'HP do inimigo: \033[1;32m0\033[m')
            print('\033[1;35m-\033[m' * 117)
        sleep(1)
    elif contsangramento == 0:
        stacksangramento = 0

    if hpmonstro <= 0:
        print('\033[1;34mParabéns, você venceu!\033[m')
        break

    if not cdstun:
        escolhamonstro = randint(1, 2)
    else:
        escolhamonstro = randint(1, 1)

    if escolhamonstro == 1:
        danomonstro -= defesaplayer
        hpplayer -= danomonstro
        print('\033[1;31m-\033[m' * 117)
        print(f'O inimigo te causa \033[1;31m{danomonstro}\033[m de dano!')
        if hpplayer > 0:
            print(f'Seu HP: \033[1;32m{hpplayer}\033[m')
        else:
            print(f'Seu HP: \033[1;32m0\033[m')
        print('\033[1;31m-\033[m' * 117)
        sleep(1)
        danomonstro = 27

    if escolhamonstro == 2:
        nonstun = False
        cdstun = True
        contcd = 5
        print('\033[1;31m-\033[m' * 117)
        print('O inimigo te atordoa por 2 turno!')
        print('\033[1;31m-\033[m' * 117)
        sleep(1)
        contstun = 2
    if contcd > 0:
        contcd -= 1
    elif contcd == 0:
        cdstun = False

    if contstun == 0:
        nonstun = True
    elif contstun <= 2:
        contstun -= 1

    if hpplayer <= 0:
        print('\033[1;31mO inimigo te derrotou!\033[m')
        break