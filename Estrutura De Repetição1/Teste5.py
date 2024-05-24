#DADOS


maior_idadeHomem=0
qntsMulheresM20=0
soma=0
for i in range(1,4):
    nome=input("nome:")
    sexo=input("homem ou mulher:")
    idade=int(input("idade:"))
    soma=soma+idade
    if idade > maior_idadeHomem and sexo == "homem":
     maior_idadeHomem=idade 
    if sexo == "mulher" and idade < 20:
     qntsMulheresM20=+1

media=soma/4

print("a media de idade é {}".format(media))
print("o homem mais velho é {}".format(maior_idadeHomem))
print("a quantidade de mulheres com menos de 20 anos é {}".format(qntsMulheresM20))