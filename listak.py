#                     0         1         2         3         4
nevek:list[str] = ['Zsuzsa', 'Renáta', 'Emese', 'Bianka', 'Zsófia']

print(nevek)
print(nevek[3])
nevek[1] = 'János'
print(nevek)

nevek.append('Ferenc')
print(nevek)
print(nevek[5])

hossz:int = len(nevek)
print(f'lista elemeinek száma: {hossz}')

print('nevek végigjárása lista elemei szerint:')
for nev in nevek:
    print(f'\t- {nev}')


print('nevek végigjárása lista indexei szerint:')
for i in range(len(nevek)):
    print(f'\t- a nevek {i}. indexű eleme: {nevek[i]}')

nevek.insert(2, 'Béla')
print(nevek)

nevek.pop()
print(nevek)

nevek.pop(1)
print(nevek)

# OoR Exc.:
# nevek.pop(102)

nevek.remove('Béla')
print(nevek)

nevek.reverse()
print(nevek)

nevek.extend(['Abigél', 'alma'])
print(nevek)

nevek.sort()
print(nevek)

# value error
# nevek.remove('babzsákfotel')