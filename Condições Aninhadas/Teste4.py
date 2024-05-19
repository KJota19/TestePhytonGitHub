#LADOS DE UM TRIÂNGULO

lado1=int(input("digite o lado 1 :"))
lado2=int(input("digite o lado 2 :"))
lado3=int(input("digite o lado 3 :"))

if lado1== lado2 and lado1 == lado3 and lado2 == lado3 and lado2 ==lado1 and lado3==lado1 and lado3 == lado2:
    print("Equilátero")
elif lado1== lado2 or lado1 == lado3 or lado2 == lado3 or lado2 == lado1 or lado3 == lado1 or lado3 == lado2:
    print("isóceles")
elif lado1!= lado2 and lado1 != lado3 and lado2!= lado3 and lado2 != lado1 and lado3!= lado1 and lado3 != lado2:
    print("escaleno")
