div = 0
i=1
num = int(input(':'))
while(i<=num):
    if(num%i==0):
        div += 1
    i += 1
if(div == 2):
    print('primo')
else:
    print('não primo')

