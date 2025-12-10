lista = []

lista.append(1)
lista.append('PYTHON')
lista.append([3,65,1])

print(lista)
l2 = lista.copy()

lista.clear()

print(lista)
print(l2)

print('-' * 15)

cores = ['vermelho', 'azul', 'verde', 'azul']


print(cores.count('vermelho'))
print(cores.count('azul'))
print(cores.count('verde'))

print('-' * 15)

linguagens = ['python', 'js', 'c']

print(linguagens)
linguagens.extend(['java', 'csharp'])
print(linguagens)

print('-' * 15)

print(linguagens.index('java'))
print(linguagens.index('python'))

print('-' * 15)

linguagens.pop()
linguagens.pop()
print(linguagens)
linguagens.pop()

print(linguagens)


print('-' * 15)
linguagens = ['python', 'js', 'c']

linguagens.remove('c')
print(linguagens)

print('-' * 15)
linguagens = ['python', 'js', 'c']
linguagens.reverse()

print(linguagens)

print('-' * 15)
linguagens = ['python', 'js', 'c']
linguagens.sort()
print(linguagens)

linguagens.sort(reverse=True)
print(linguagens)

print('-' * 15)

linguagens.sort(key=lambda x:len(x))
print(linguagens)
linguagens.sort(key=lambda x:len(x), reverse=True)
print(linguagens)