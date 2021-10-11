X=int(input('Введите число X'))
Y=int(input('Введите число Y'))
a=range(X,Y+1)
c=0
for X in a:
  if X%5==0:
   c=X+c
print(c) 
