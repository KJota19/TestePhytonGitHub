#OPERAÇÕES NÚMERICAS

print("menu de operações númericas:")
print("1. somar")
print("2. multiplicar")
print("3. maior")
print("4. novos números")
print("5. sair do programa")

opção=''
resultado=0
while True:
    valor1=int(input("digite o primeiro valor:"))
    valor2=int(input("digite o segundo valor:"))
    if valor1 == 0 and valor2 == 0:
        break
    else:     
        opção=int(input("escolha a opção que deseja de 1 a 5: "))
        
        if opção == 1:
            resultado=valor1+valor2
            print("a soma dos valores {} + {} = {} ".format(valor1,valor2,resultado))
        elif opção == 2:
            resultado=valor1*valor2
            print("a multiplicação de {} x {} = {}".format(valor1,valor2,resultado))
        elif opção == 3:
            if  valor1 > valor2:
                resultado=valor1
            else: 
                resultado = valor2
            print("o maior valor entre {} e {} é {}".format(valor1,valor2,resultado))
    
        elif opção == 4 or opção == 5:
            break