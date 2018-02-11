lista = []

for x in range(100, 1000):
    for y in range(100, 1000):
        summa = str(x*y)
        if summa == summa[::-1]:
            lista.append(summa)

lista = [int(n) for n in lista]
lista.sort()
print(lista)
