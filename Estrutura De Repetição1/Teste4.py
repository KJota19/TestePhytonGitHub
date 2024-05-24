#PESO

maior=0
menor=0
for i in range(1,6):
    peso=int(input("digite o peso:"))
    if peso >= maior:
        maior=peso
    else:
        menor=peso
print("o maior peso foi {}".format(maior))
print("o menor peso foi {}".format(menor))