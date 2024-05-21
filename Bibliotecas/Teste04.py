#BIBLIOTECA RANDOM

import random

lista=[1,2,3]
resposta1=2+2
resposta2=2*9
resposta3=6*5
num=random.choice(lista)
if num == 1:
    print("quanto é 2 + 2 ?")
    resposta=int(input())
    if resposta == resposta1:
        print("você acertou !")
    else:
        print("você errou !, a resposta correta é {}".format(resposta1))
elif num == 2:
    print("quanto é 2 x 9 ?")
    resposta=int(input())
    if resposta == resposta2:
        print("você acertou !")
    else:
        print("você errou !, a resposta correta é {}".format(resposta2))
elif num == 3:
    print("quanto é 6 x 5 ?")
    resposta=input()
    if resposta == resposta3:
        print("você acertou !")
    else:
        print("você errou ! a resposta correta é {}".format(resposta3))