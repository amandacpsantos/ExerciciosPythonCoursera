from math import sqrt

a = int(input('a:'))
b = int(input('b:'))
c = int(input('c:'))
delta = (b**2)- 4*a*c
if(delta<0):
    print('esta equação não possui raízes reais')
elif(delta==0):
    print('a raiz desta equação é {}'.format(-b/(2*a)))
else:
    raiz1 = (-b + sqrt(delta))/(2*a)
    raiz2 = (-b - sqrt(delta))/(2*a)
    if(raiz1<raiz2):
        print('as raízes da equação são {} e {}'.format(raiz1, raiz2))
    else:
        print('as raízes da equação são {} e {}'.format(raiz2, raiz1))
