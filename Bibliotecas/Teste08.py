#BIBLIOTECA MATH

import math

cateto_adjacente=float(input("digite o valor do cateto adjacente: "))
cateto_oposto=float(input("digite o valor do cateto oposto: "))
hipotenusa=math.hypot(cateto_adjacente,cateto_oposto)
print("a hipotenusa de um triângulo retângulo é : {}".format(hipotenusa))