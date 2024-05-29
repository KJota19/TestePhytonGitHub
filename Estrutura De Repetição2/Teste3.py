#JOGO DA ADIVINHAÇÃO

import random
from random import randint
computador = randint(0,10)
numero=0

while numero != computador:
    numero=int(input("digite um número entre 0 e 10: "))
    if numero == computador:
     print("parabéns você acertou !")
     break
    else:
        numero=int(input("digite um número entre 0 e 10: "))