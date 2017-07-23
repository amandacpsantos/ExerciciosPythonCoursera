def maior_primo(num):
    primo = 0

    for i in range(1, num+1):
        check = 1
        div = 0

        while check <= i:
            if i % check == 0:
                div += 1
            check += 1

        if div == 2:
            primo = i

    return primo

num = int(input(':'))
if num >= 2:
    print(maior_primo(num))

