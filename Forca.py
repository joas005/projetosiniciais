import os
import time
import random
import getpass
os.system('cls' if os.name == 'nt' else 'clear')

# Modo 1 -
def modoPC():
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n\033[32mVocê escolheu Modo Palavras Escolhidas!\033[0m')
    print(
        '''\nComo funciona:\nVocê terá \033[32m6 chances\033[0m para advinhar as letras de uma palavra escolhida aleatóriamente do nosso banco de dados!\nPara terminar o jogo continue chutando letras até a palavra estar completa!.''')
    print()
    input('Clique enter para começar! ')
    palavra = escolherPalavra()
    começandoJogo(palavra, 6)

# Modo 2 -
def modoPVP():
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n\033[34mVocê escolheu Modo Clássico!\033[0m')
    print(
        '''\nComo funciona:\nVocê terá \033[32m6 chances\033[0m para advinhar as letras de uma palavra escolhida por outro jogador!\nPara terminar o jogo continue chutando letras até a palavra estar completa!.\n\nNeste modo o seu adversário pode colocar acentos, caso ele coloque para vencer o jogo você deverá inserir a letra \033[32mCOM ACENTO\033[0m para vencer!''')
    print()
    print('\033[31mATENÇÃO! A palavra ficará invisível enquanto você digita porém ela está sendo computada!\033[0m')
    palavra = getpass.getpass(
        '\033[34mPeça para outro jogador inserir uma palavra aqui >\033[0m ').lower()
    validandoPalavraEscolhida(palavra)
    modoPVP()  # Rechamando o modo por que o ínicio do jogo é feito dentro da validação da palavra

# Modo 3 -
def modoHard():
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n\033[31mVocê escolheu Modo Hardcore!\033[0m')
    print(
        '''\nComo funciona:\nVocê terá \033[31m6 chances\033[0m para advinhar as letras de uma palavra escolhida aleatóriamente do nosso banco de dados de pavras difíceis!\nPara terminar o jogo continue chutando letras até a palavra estar completa!.''')
    print()
    input('\033[31mClique enter para começar!\033[0m ')
    palavra = escolherPalavraDificil()
    começandoJogo(palavra, 6)

# Funçoes --
def escolherPalavra():
    BancoDePalavras = ['amarelo', 'amiga', 'amor', 'ave', 'limonada', 'meia', 'noite', 'ovo', 'bolo', 'branco', 'cama', 'caneca',
                       'celular', 'janela', 'clube', 'copo', 'doce', 'elefante', 'escola', 'estojo', 'faca', 'foto', 'garfo', 'geleia', 'girafa', 'passarinho', 'peixe', 'pijama', 'rato', 'umbigo', 'desalmado', 'eloquente', 'esfirra', 'esquerdo', 'caminho'
                       ]
    palavra = random.choice(BancoDePalavras)
    return palavra

def escolherPalavraDificil():
    BancoDePalavrasDificeis = ['almofariz', 'prurido', 'quadriciclo', 'quinquilharia', 'reciclar', 'reflorescer', 'reivindicar', 'rescindir', 'retrógrado', 'retrovisor', 'ritmo', 'seborreia', 'sensatez', 'serelepe', 'serpentina', 'simulacro', 'travesseiro',
                               'trilogia', 'universidade', 'vangloriar', 'vaporizador', 'ventilador', 'ziguezague', 'ziquizira', 'zumbido', 'invertebrado', 'iogurte', 'irascível', 'lantejoula', 'licenciado', 'losango', 'madrasta', 'manteigueira', 'marimbondo', 'mesclar']
    palavra = random.choice(BancoDePalavrasDificeis)
    return palavra

# Validando a palavra inserida no modo 2 - 
def validandoPalavraEscolhida(palavra): 
    if len(str(palavra.strip())) > 2:
        começandoJogo(palavra, 6)
    else:
        print('\n\033[31mPalavra inválida!\033[0m\nA palavra escolhida não pode conter conter \033[31m pelo menos de 3 letras!\033[0m\n\nTente novamente.')
    time.sleep(2)

def começandoJogo(palavra, vidas):
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')
    vidas = vidas
    print('\033[35mQue começe o jogo!\nAqui está sua palavra:\033[0m')
    for letra in palavra:
        print('\033[35m_', end='', sep='')
    print(f'\nPalavra de - {len(palavra)} letras')
    achandoLetras(vidas, palavra)
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')

def achandoLetras(vidas, palavra):
    letrasChutadas = []
    while True:
        chute = input('\033[0m\nChute algo: ').lower()
        chute = chute[0]
        if chute in letrasChutadas:
            print(
                f'\nVocê já chutou a letra \033[31m{chute[0]}\033[0m antes!\nChute outras letras.')
            continue

        letrasChutadas.append(chute)

        if chute in palavra:
            print('\n\033[32mVocê achou uma letra!!\033[0m')
            print(
                f'A letra \033[32m{chute.upper()}\033[0m se encontra na palavra!')
        else:
            print('\n\033[31mVocê errou!!\033[0m')
            print(
                f'A letra \033[31m{chute}\033[0m não se encontra na palavra.')
            vidas -= 1

        imprimindoaPalava(letrasChutadas, palavra, vidas)

        if vidas < 1:
            print('\nSuas vidas acabaram!')
            perdeuJogo(palavra)
            break

        continue

def imprimindoaPalava(letrasChutadas, palavra, vidas):
    desenhoVidas(vidas)
    time.sleep(2)

    encontrouaPalavra = True # Checa se algum _ foi imprimido, se não foi o jogador ganhou
    for letra in palavra:
        if letra in letrasChutadas:
            print(f'\033[35m{letra}', end='', sep='')
        else:
            print('\033[35m_', end='', sep='')
            encontrouaPalavra = False

    print(f'\nPalavra de - {len(palavra)} letras')
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')

    if encontrouaPalavra == True:
        ganhouJogo(palavra, vidas)

def desenhoVidas(vidas):
    HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
    time.sleep(1.5)
    print(f'\nAinda te restam - \033[31m{vidas}\033[0m vida(s).')
    match(vidas):
        case 1: print(HANGMANPICS[5], '\n\n')
        case 0: print(HANGMANPICS[6], '\n\n')
        case 2: print(HANGMANPICS[4], '\n\n')
        case 3: print(HANGMANPICS[3], '\n\n')
        case 4: print(HANGMANPICS[2], '\n\n')
        case 5: print(HANGMANPICS[1], '\n\n')
        case 6: print(HANGMANPICS[0], '\n\n')
    time.sleep(2)

def perdeuJogo(palavra):
    print(
        f'\033[31mVocê perdeu o jogo!\033[0m😥\nInfelizmente você não encontrou a palavra \033[35m{palavra}\033[0m, antes de acabar com as suas vidas.\n')
    jogarDenovo()

def ganhouJogo(palavra, vidas):
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n\033[32mPARABÉNS VOCÊ ACERTOU A PALAVRA!!! 🎉🎉')
    print(
        f'\nSua palavra era: {palavra}!\033[0m\nVocê conseguiu adivinhar e ainda tinha \033[31m{vidas} vida(s) sobrando!\033[0m')
    jogarDenovo()

def jogarDenovo():
    denovo = input('\nGostaria de jogar denovo?? ').lower()
    if denovo != 'sim':
        print(
            '''\n\033[35mObrigado por jogar!\n---\033[0m\n\nVolte sempre 😁😁\n✌️''')
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        exit()
    time.sleep(1.5)
    os.system('cls' if os.name == 'nt' else 'clear')
    main()

# Código principal --
def main():
    print('''\033[35mBem vindos ao jogo da forca!\n------\033[0m''')
    print()

    while True:
        modo = int(input(
            '''Escolha o modo que você deseja jogar: \n\033[32m[1] Palavras escolhidas pela gente (Recomendado para jogadores solo).\n\033[34m[2] Modo clássico (Recomendado para 2 jogadores).\n\033[31m[3] Modo hard!\n\033[0mEm que modo você deseja jogar? '''))
        match(modo):
            case 1: modoPC()
            case 2: modoPVP()
            case 3: modoHard()
            case _:
                print(
                    '\033[31mVocê escolheu uma opcão inválida!\nTente novamente.\033[0m')
                continue

        jogarDenovo()

main()
