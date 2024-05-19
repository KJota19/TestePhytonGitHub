#MULTA

KMh=int(input("Digite a velocidade do carro: "))

if KMh > 80:
    print("Você foi multado !")
    multa=(KMh - 80) * 7
    print("Você terá que pagar R${}".format(multa))