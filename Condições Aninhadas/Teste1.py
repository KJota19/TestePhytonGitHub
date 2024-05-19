#EMPRESTIMO

valor=float(input("Digite o valor da casa :"))
salario=float(input("Digite o salário do comprador :"))
Qanos=int(input("Digite quantos anos vai ser pago :"))

Psalario=salario*(30/100)
prestacao=valor/(Qanos*12)
print("para pagar uma casa de R${:.2f} em {} anos ".format(valor, Qanos),end='')
print("a prestação será de R${:.2f}".format(prestacao))
if prestacao >= Psalario:
    print("empréstimo negado")
else:
    print("empréstimo aceito!")
    print("o valor da prestação mensal será de: ", Psalario )