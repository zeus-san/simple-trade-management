import os
from datetime import datetime
#pecorrer uma lista na tela com os elementos que aparecm na outra lista
a = {'nome':'zeus','idade':19}
f = [a[x] for x in a]
print('zeus' in a.values())
b = ['nome']
print(f)
for row in b:
    print(a[row])
print(a.pop('nome'),1)
print(a)
c = ''
print(c.isdigit())
a = "  1,22  "
try:
    float(a.replace(',','.'))
    print(1.2)
except:
    print(2)
print(5.2%1==0)
a = "zeus"
print(eval("a"))
print(dir(dict))

a = [1,2,3,4,5]
print(a.index(2))
a=['a','b','c','d','e']
b="".join(a)
print(b)
print(b[:b.index("c")])
print(not '1' in b)

print(os.path.exists('classes.txt'))

data_hora = datetime.now()
print(data_hora.strftime('%H:%M %d/%m'))

a = [x for x in range(1,10)]
b = [x for x in range(10,20)]
print(dir(a))