def n_primos(num):
    #primo = 0
    quant = 0

    for i in range(1, num+1):
        check = 1
        div = 0

        while check <= i:
            if i % check == 0:
                div += 1
            check += 1
        #checa se é primo
        if div == 2:
            quant +=1

    return quant

num = int(input(':'))
if num >= 2:
    print(n_primos(num))
