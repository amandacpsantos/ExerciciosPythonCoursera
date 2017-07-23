from math import sqrt

x1=int(input('x do ponto1:'))
y1=int(input('y do ponto1:'))
x2=int(input('x do ponto2:'))
y2=int(input('y do ponto2:'))
d = sqrt( ((x2-x1)**2) + ((y2-y1)**2) )
if(d>=10):
    print('longe')
else:
    print('perto')

