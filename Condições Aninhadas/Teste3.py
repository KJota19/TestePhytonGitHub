#APROVAÇÃO/REPROVAÇÃO

nota1=int(input("digite sua nota1 : "))
nota2=int(input("digite sua nota2 :"))

media=(nota1+nota2) /2

if media < 50:
    print("reprovado")
elif media >50 and media <= 69:
    print("recuperação")
elif media >=70:
    print("aprovado")