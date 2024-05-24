#NÚMERO PRIMO

num=int(input("digite um número:"))
tot=0
for i in range(1,num+1):
    if num % i == 0:
       print('\033[33m',i,end='')
       tot+=1
    else:
       print('\033[35m',i,end='')


print(" o número {} foi divisível {} vezes".format(num,tot))
if tot == 2:
   print(" E por isso ele é primo")
else:
   print("E por isso ele não é primo")