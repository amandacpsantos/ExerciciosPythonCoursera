def é_hipotenusa(cat1, cat2, h):
    if (h**2) == (cat1**2) + (cat2**2):
        return True


def soma_hipotenusas(hip):
    cat1 = 1
    cat2 = 1
    hipTem=1
    ultHip = 0
    soma = 0
    while hipTem <= hip:
        while cat1 < hipTem:
            while cat2 < cat1:
                #print(cat1, cat2, hipTem)
                if é_hipotenusa(cat1,cat2,hipTem) and ultHip != hipTem:
                    #if ultHip != hipTem:
                    soma += hipTem
                    ultHip = hipTem
                    #print('achou', soma, hipTem, cat1, cat2)
                cat2 += 1
            cat2 = 1
            cat1 += 1
        cat1 = 1
        hipTem += 1
    return soma


num = int(input(':'))
if num > 0:
    print(soma_hipotenusas(num))