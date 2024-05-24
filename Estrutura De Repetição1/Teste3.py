#PALINDROMO

frase=input("digite uma frase:")
palavras=frase.split()
junto=''.join(palavras)
inverso=''
for letra in range(len(junto)-1,-1,-1): #i == letra
    inverso+=junto[letra]
if inverso == junto:
    print("temos um palindromo")
else: 
    print("a frase não é palindromo")