'''
Autor:Rodnei Carvalho - python-brasil
colaborador: Edson J. Silva- python-brasil

Jogo da forca V.01
20/06/18
    - adicionado listas chutes.
    - adicionado print de chutes e qtd de chutes e chutes restantes.
    - adicionado tratamento de erro na entrada.
    - adicionado Placar.
    - adicionado contadores de acertos e erros
'''

from random import randrange

chutes= []       #lista pra guardar os chutes

def boas_vindas(palavra_secreta):
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")
    print()                                     #espaço apenas para melhorar a leitura
    print("A palavra secreta tem %i letras!"%len(palavra_secreta))
    print()                                     #espaço apenas para melhorar a leitura

def gerador_de_nomes():
    arquivo = open("nomes.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()

    return palavra_secreta


def caracteres_letras_acertadas(palavra):
    return ["_" for letra in palavra]


def chute_jogador():
    global chutes
    while True:
        try:
            chute = input("\nDigite a letra: ")
            if chute.isalpha():
                chute = chute.strip().upper()
                if chute.upper() not in chutes:
                    chutes.append(chute)  #
                    break
                else:
                    print("Você já deu este chute, Tente novamente!")
                    print("Seus chutes: %s\n" % chutes)
            else:
                print("Entrada inválida!\nPor favor digite somente letra \"a-z ou A-Z\"")
            
        except AttributeError:
            print("Entrada inválida!\nPor favor, digite somente letra \"A-Z\"")
    return chute


def chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    acerto = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
        index += 1

def imprime_mensagem_vencedor():

    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_mensagem_perdedor(palavra_secreta):

    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    
def placar_erros(chutes,erros):
    print("Você já errou  %i/%i tentativas." %(erros, 7))
    print("Seus chutes: %s\n" % chutes)

def placar_acertos(acertos,palavra_secreta):
    print("Você acertou %i/%i letras."%(acertos,(len(palavra_secreta))))
    print("Seus chutes: %s\n" % chutes)

def jogar():
    palavra_secreta = gerador_de_nomes()
    boas_vindas(palavra_secreta)
    letras_acertadas = caracteres_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0
    acertos = 0

    print(letras_acertadas)

    while not enforcou and not acertou:

        chute = chute_jogador()

        if chute in palavra_secreta:
            chute_correto(chute, letras_acertadas, palavra_secreta)
            acertos += 1
            placar_acertos(acertos, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)
            placar_erros(chutes, erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)


    if (acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)



if (__name__ == "__main__"):
    jogar()
