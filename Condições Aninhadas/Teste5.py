#IMC

peso=float(input("digite seu peso:"))
altura=float(input("digite sua altura:"))

IMC=peso/(altura*altura)

if IMC < 18.5:
    print("abaixo do peso")
elif IMC > 18.5 and IMC <=25:
    print("peso ideal")
elif IMC > 25 and IMC <= 30:
    print("sobrepeso")
elif IMC > 30 and IMC <= 40:
    print("obesidade")
else:
    print("obesidade mórbida")