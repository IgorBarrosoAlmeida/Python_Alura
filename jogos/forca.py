'''
 * @File adivinhacao.py
 * @Author Igor Barroso Almeida
 * @Brief Jogo de forca criado
 * no curso de introdução ao python da Alura
 * @Date 27/12/2022 
'''

def menu(acertos):
    for e in acertos:
        print(e, end=" ")
    print("")

def jogar():
    print("-----------------------------------")
    print("   Bem vindo ao jogo da forca!!   ")
    print("-----------------------------------")

    enforcou = False
    acertou = False

    palavra_chave = "Banana"

    acertos = ["_","_","_","_","_","_"]

    menu(acertos=acertos)
    while((not enforcou) and (not acertou)):

        chute = input("Chute: ").strip() # Tira espaços do começo e final
    
        i = 0
        for letra in palavra_chave:
            if(chute.upper() == letra.upper()):
                acertos[i] = letra
            i += 1
        menu(acertos=acertos)
        

if(__name__ == "__main__"):
    jogar()