def beeramid(bonus, price):
    avCan = bonus/price 
    sum = 0
    i = 1
    while(sum <= avCan):
        sum += i * i
        i += 1
    return i - 2, sum


print(beeramid(1500, 2))
