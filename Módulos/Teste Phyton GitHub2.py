#Cateto oposto e cateto adjacente

import math

catetoOP=int(input("digite o cateto oposto:"))
catetoAD=int(input("digite o cateto adjacente:"))

triret=math.hypot(catetoAD,catetoOP)

print(triret)