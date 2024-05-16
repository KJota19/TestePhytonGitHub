#Manipulação De Frase

frase=input("escreva uma frase:")

fraseQTD=frase.count("a")
print("A letra 'A' aparece {} vezes na frase.".format(fraseQTD))
frasePVZ=frase.find("a")
print("A primeira letra 'A' apareceu na posição {}".format(frasePVZ))
fraseUVZ=frase.rfind("a")
print("A ultima letra 'A' apareceu na posição {}".format(fraseUVZ))