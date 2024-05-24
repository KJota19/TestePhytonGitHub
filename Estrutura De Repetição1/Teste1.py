#DÉCIMO TERMO P.A

pt=int(input("primeiro termo:"))
r=int(input("razão:"))
an=pt+(10-1)*r
print("o décimo termo da P.A é {}".format(an))
for i in range(pt,an+r,r):
    print('{}'.format(i),end='->')