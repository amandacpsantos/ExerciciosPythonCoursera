tem = False
num = int(input(':'))
while(num!=0):
    aux = num%10
    num = num // 10
    aux1 = num%10
    if aux == aux1:
        tem = True

if not tem:
    print('não')
else:
    print('sim')
