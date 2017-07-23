soma = 0
num = int(input(':'))
while(num!=0):
    aux = num%10
    soma = soma + aux
    num = num//10
print(soma)
