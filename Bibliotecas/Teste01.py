#BIBLIOTECA RANDOM

import random

num=random.randrange(1,10)
while True:
 adv=int(input("digite um número entre 1 e 10: "))
 if adv == num:
  print("acertou !")
  break
 else:
  print("errou !")