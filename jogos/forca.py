'''
 * @File adivinhacao.py
 * @Author Igor Barroso Almeida
 * @Brief Jogo de forca criado
 * no curso de introdução ao python da Alura
 * @Date 30/12/2022 
'''

def menu(acertos):
    for e in acertos:
        print(e, end=" ")
    print("")

def jogar():
    print("-----------------------------------")
    print("   Bem vindo ao jogo da forca!!   ")
    print("-----------------------------------")

    # Leitura de arquivo
    file = open("jogos\palavras.txt", "r")
    palavras = []

    for linha in file:
        linha = linha.strip()
        palavras.append(linha)
    file.close()

    # Escolha aleatoria de uma palavra
    import random

    index = random.randint(0, len(palavras) -1)
    palavra_chave = palavras[index]

    # Começando o jogo
    acertos = ["_" for letra in palavra_chave]
    enforcou = False
    acertou = False
    erros = 0

    menu(acertos=acertos)
    while((not enforcou) and (not acertou)):

        chute = input("Chute: ").strip() # Tira espaços do começo e final
    
        if(chute.upper() in palavra_chave.upper()):
            i = 0
            for letra in palavra_chave:
                if(chute.upper() == letra.upper()):
                    acertos[i] = letra
                i += 1
        else:
            erros += 1
            print(f"Você errou faltam {6-erros} erro(s)")
        menu(acertos=acertos)
        
        enforcou = (erros == 6)
        acertou = ("_" not in acertos)
    
    if(acertou):
        print("Parabens você acertou!!")
    else:
        print("Game over, o personagem enforcou.")

if(__name__ == "__main__"):
    jogar()