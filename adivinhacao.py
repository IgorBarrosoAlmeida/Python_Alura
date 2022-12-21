'''
 * @File adivinhacao.py
 * @Author Igor Barroso Almeida
 * @Brief Jogo de adivinhação criado
 * no curso de introdução ao python da Alura
 * @Date 14/12/2022 
'''

print("-----------------------------------")
print("Bem vindo ao jogo de adivinhação!!")
print("-----------------------------------")

num_secreto = 42
max_tentativas = 3
rodada = 1

for rodada in range(1, max_tentativas+1):
    print(f"Tentativa {rodada} de {max_tentativas}")
    chute = int(input("Digite um número entre 1 e 100: "))

    if(chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue

    acertou = (chute == num_secreto)
    menor   = (chute < num_secreto)
    maior   = (chute > num_secreto)

    if(acertou):
        print("Você acertou :)")
        break
    elif(menor):
        print("Você chutou um numero menor")
    elif(maior):
        print("Você chutou um numero maior")

print("------------FIM DE JOGO------------")