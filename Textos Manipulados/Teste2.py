#MANIPULAÇÃO DE NÚMEROS

numero=int(input("digite um número de 0 até 9999:"))

#n=str(numero)
u=numero//1%10
d=numero//10%10
c=numero//100%10
m=numero//1000%10
print("analisando o número {}".format(numero))
#print('unidade: {}'.format(n[3]))
print('unidade: {}'.format(u))
#print('dezena: {}'.format(n[2]))
print('dezena: {}'.format(d))
#print('centena: {}'.format(n[1]))
print('centena: {}'.format(c))
#print('milhar: {}'.format(n[0]))
print('milhar: {}'.format(m))