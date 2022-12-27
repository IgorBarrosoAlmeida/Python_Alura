'''
 * @File adivinhacao.py
 * @Author Igor Barroso Almeida
 * @Brief arquivo que permite escolher o 
 * jogo a ser executado
 * @Date 27/12/2022 
'''

# Importações
import forca
import adivinhacao

print("(1) Adivinhação (2) Forca")
escolha = int(input("Escolha um jogo para jogar: "))

if(escolha == 1):
    adivinhacao.jogar()
elif(escolha == 2):
    forca.jogar()