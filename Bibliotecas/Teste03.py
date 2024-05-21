#BIBLIOTECA RANDOM

import random

frase=input("digite um frase:")
juntar=frase.strip()
lista_frase=list(juntar)
random.shuffle(lista_frase)
frase_embaralhada=''.join(lista_frase)
print("Frase embaralhada: {}".format(frase_embaralhada))