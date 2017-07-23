lar = int(input(':'))
alt = int(input(':'))
temp = lar
while alt > 0:
    lar = temp
    while lar > 0:
        print('#', end='')
        lar -= 1

    print()
    alt -=1
