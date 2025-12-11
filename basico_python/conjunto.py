print(set([1,2,3,1,3,4]))
print(set('abacaxi'))
print(set(('palio', 'gol', 'celta', 'palio')))

linguagens = {'python', 'java','python'}
print(linguagens)

print('-' * 15)

numeros = {1,2,3,2}
numeros = list(numeros)
print(numeros[0])

print('-' * 15)

conjA = {1,2}
conjB = {3,4}

print(conjA.union(conjB))

conjuntoA = {1,2,3}
conjuntoB = {2,3,4}

print(conjuntoA.intersection(conjuntoB))

print(conjuntoA.difference(conjuntoB))
print(conjuntoB.difference(conjuntoA))
print(conjuntoB.symmetric_difference(conjuntoA))

conja = {1,2,3}
conjb = {4,1,2,5,6,3}

print(conja.issubset(conjb))
print(conjb.issubset(conja))


print('-' * 15)

conjunto_a = {1,2,3,4,5}
conjunto_b = {6,7,8,9}
conjunto_c = {1,0}

print(conjunto_a.isdisjoint(conjunto_b))
print(conjunto_a.isdisjoint(conjunto_c))


print('-' * 15)

sorteio = {1,23}

sorteio.add(25)
sorteio.add(42)
sorteio.add(25)

print(sorteio)

sorteio.clear()
print(sorteio)


numero = {1,23,4,2,6,2,7,4,88,53,726,24,42}

print(numero)

numero.discard(1)
print(numero)
numero.discard(4)
print(numero)
numero.pop()
print(numero)
numero.remove(7)
print(numero)

print(len(numero))

print(6 in numero)
print(2 in numero)