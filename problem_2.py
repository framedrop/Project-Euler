a, b = 0, 1
sekvens = []

while b < 4000000:
    sekvens.append(b)
    a, b = b, a + b

def even(n):
    summan = 0
    for i in n:
        if i % 2 == 0:
            summan += i
    return summan

print(even(sekvens))
