import random

sorteio=[0,1,2,3,4,5]
numero_sorteio=random.choice(sorteio)

num=int(input("Escolha um número de 0  até 5: "))

if num == numero_sorteio:
    print("Você Venceu !")
else:
    print("Você perdeu!")