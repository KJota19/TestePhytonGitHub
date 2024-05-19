#CONVERSÃO

numero=int(input("digite um número:"))

print("1.Binário")
print("2.Octal")
print("3.Hexadecimal")
choice=int(input("escolha 1 ou 2 ou 3 :"))

if choice == 1:
    binario=bin(numero)
    print("o número ", numero, "convertido para binário:", binario[2:])
elif choice == 2:
    octal= oct(numero)
    print("o número ", numero, "convertido para octal: ", octal[2:])
elif choice == 3:
    hexadecimal=hex(numero)
    print("o número ", numero, "convertido para hexadeicmal: ",hexadecimal[2:])