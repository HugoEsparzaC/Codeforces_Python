lista = []
a = input()
for i in range(0, len(a), 2):
    lista.append(a[i])
lista.sort()
print(*lista, sep="+", end="\n")