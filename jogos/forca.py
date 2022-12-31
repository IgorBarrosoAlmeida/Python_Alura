'''
 * @File adivinhacao.py
 * @Author Igor Barroso Almeida
 * @Brief Jogo de forca criado
 * no curso de introdução ao python da Alura
 * @Date 30/12/2022 
'''

# importações 
import random

# Função principal do jogo da forca
def jogar():

    bem_vindo()

    # Começando o jogo
    palavra_secreta = gera_palavra_aleatoria()
    acertos = ["_" for letra in palavra_secreta]
    enforcou = False
    acertou = False
    erros = 0

    menu(acertos)
    while((not enforcou) and (not acertou)):
        chute = input("Chute: ").strip() # Tira espaços do começo e final
    
        if(chute.upper() in palavra_secreta.upper()):
            inclui_letras_acertadas(chute, palavra_secreta, acertos)
        else:
            erros += 1
            desenha_forca(erros)
        menu(acertos)
        
        enforcou = (erros == 7)
        acertou = ("_" not in acertos)
    
    mensagem_final(acertou, palavra_secreta)

# ----------------Funções----------------

# Imprime mensagem de bem vindo
def bem_vindo():
    print("-----------------------------------")
    print("   Bem vindo ao jogo da forca!!   ")
    print("-----------------------------------")

# Função que apartir do arquivo contendo palavras retorna uma palavra aleatoria
def gera_palavra_aleatoria(nome_arquivo="jogos\palavras.txt", primeira_linha=0):
    # Abre o arquivo que comtem as palavras
    file = open(nome_arquivo, "r")
    palavras = []

    for linha in file:
        linha = linha.strip()
        palavras.append(linha)
    file.close()

    # Escolha aleatoria de uma palavra
    index = random.randint(primeira_linha, len(palavras) -1)
    return palavras[index]

# Função que dado um chute e uma palavra chave inclui os acertos em uma lista de letras também dada
def inclui_letras_acertadas(chute, palavra_chave, acertos):
    i = 0
    for letra in palavra_chave:
        if(chute.upper() == letra.upper()):
            acertos[i] = letra
        i += 1

# Imprime menu com as letras acertadas e espaços que faltam
def menu(acertos):
    for e in acertos:
        print(e, end=" ")
    print("")

# Imprime se o usuario ganhou ou perdeu
def mensagem_final(acertou, palavra_secreta):
    if(acertou):    
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
    else:
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

# Imprime a forca com base nos erros
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
    print()

if(__name__ == "__main__"):
    jogar()