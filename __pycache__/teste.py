from random import randint

a = [['g',12,13],['a',12,13],['f',12,13],['d',12,13]]
item_unico = []

for row in a:
    item_unico.append(row[0])

item_unico.sort()

novalista = []

while item_unico:
    print(item_unico)
    for row3 in a:
        if item_unico[0] == row3[0]:
            novalista.append(row3)
            item_unico.pop(0)
            break
print(novalista)
