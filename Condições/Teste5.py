#PREÇO VIAGEM

km=int(input("Digite a distância da viagem em KM:"))

if km <= 200:
    preco1=0.50 * km
    print("a viagem de {} KM custará R${}".format(km,preco1))
else:
    preco2=0.45 * km
    print("a viagem de {} KM custará R${}".format(km,preco2))