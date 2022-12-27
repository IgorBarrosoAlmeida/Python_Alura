'''
 * @File adivinhacao.py
 * @Author Igor Barroso Almeida
 * @Brief Jogo de adivinhação criado
 * no curso de introdução ao python da Alura
 * @Date 14/12/2022 
'''

def jogar():
    # Importações
    import random

    print("-----------------------------------")
    print("Bem vindo ao jogo de adivinhação!!")
    print("-----------------------------------")

    num_secreto = random.randint(1, 100)
    pontos = 1000

    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Escolha o nivel que você quer jogar: "))

    if(nivel == 1):
        max_tentativas = 20
    elif(nivel == 2):
        max_tentativas = 10
    else:
        max_tentativas = 5

    for rodada in range(1, max_tentativas+1):
        print(f"Tentativa {rodada} de {max_tentativas}")
        chute = int(input("Digite um número entre 1 e 100: "))

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = (chute == num_secreto)
        menor   = (chute < num_secreto)

        if(acertou):
            print(f"Você acertou, ganhou {pontos} pontos")
            break
        else:
            if(rodada == max_tentativas):
                print(f"Game over, o número secreto era {num_secreto}")
            elif(menor):
                print("Você chutou um numero menor")
            else:
                print("Você chutou um numero maior")

        pontos_perdidos = abs(num_secreto - chute)
        pontos = pontos - pontos_perdidos

    print("------------FIM DE JOGO------------")

if(__name__ == "__main__"):
    jogar()