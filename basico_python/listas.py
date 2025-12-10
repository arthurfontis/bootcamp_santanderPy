frutas = ['laranja', 'maca' , 'uva']
letras = list('python')
numeros = list(range(10))
carro = ['ferrari', 'f8', 420000, 2020, 2900, 'São Paulo', True]

print(frutas)
print(letras)
print(numeros)
print(carro)

print('-' * 15)

print(frutas[0])

matriz = [
    [1,'a',2],
    ['b',3,4],
    [6,5,'c']
]

print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])

print('-' * 15)

print(letras[2:])
print(letras[:2])
print(letras[1:3])
print(letras[0:3:2])
print(letras[::])
print(letras[::-1])

print('-' * 15)

for indice, i in enumerate(frutas):
    print(indice, i)


print('-' * 15)

pares = []
for i in numeros:
    if i % 2 == 0:
        pares.append(i)

print(pares)

# OU 
# pares = [i for i in numeros if i % 2 == 0]

print('-' * 15)

quadrado = []
for j in numeros:
    quadrado.append(j ** 2)

print(quadrado)