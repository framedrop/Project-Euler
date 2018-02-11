sum = []

for n in range(1000):
    if n % 3 == 0 or n % 5 == 0:
        sum.append(n)

def summa(n):
    summan = 0
    for i in n:
        summan += i
    return summan

print(summa(sum))
