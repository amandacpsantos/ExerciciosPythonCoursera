lar = int(input(':'))
alt = int(input(':'))
temp = lar
temp2 = alt
while alt > 0:
    lar = temp
    while lar > 0:
        if alt == 1 or alt == temp2:
            print('#', end='')
        elif lar == temp or lar == 1:
            print('#', end='')
        else:
            print(' ',end='')
        lar -= 1

    print()
    alt -=1
