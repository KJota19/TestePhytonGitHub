#NOME MANIPULADO

1.
nome=input("Digite seu nome completo:")

maiusculo=nome.upper()
print("o nome com todas as letras maiúsculas : {}".format(maiusculo))
minusculo=nome.lower()
print("o nome com todas a letras minúsculas: {}".format(minusculo))
qletrasespa=nome.strip()
qletrasespa=len(qletrasespa)
print("a quantidade de letras sem considerar os espaços: {}".format(qletrasespa))
qtprimeiroN=nome.split()
qtprimeiroN=len(qtprimeiroN[0])
print("a quantidade de letras no primeiro nome: {}".format(qtprimeiroN))