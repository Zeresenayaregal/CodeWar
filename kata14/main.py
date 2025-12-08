def beeramid(bonus, price):
    avCan = bonus/price 
    sum = 0
    i = 1
    while(sum <= avCan):
        sum += i * i
        i += i
    return i - 1


print()
