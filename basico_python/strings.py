curso = 'pYtHon'

print(curso.upper())
print(curso.lower())
print(curso.title())

print('-' * 15)

curso = "    Python "

print(curso.strip() + '.')
print(curso.lstrip() + '.')
print(curso.rstrip() + '.')

print('-' * 15)

curso = 'python'
print(curso.center(10,'#'))
print('.'.join(curso))

print('-' * 15)

nome = 'Fontis'
idade = 19
profissao = 'Programador'
linguagem = 'python'

print('Olá, me chamo {}. Tenho {} anos de idade, trabalho como {} e estou no curso de {}'.format(nome, idade, profissao, linguagem))
print('Olá, me chamo {3}. Tenho {2} anos de idade, trabalho como {1} e estou no curso de {0}'. format(linguagem, profissao, idade, nome))

print('-' * 15)

pi = 3.14159
print(f"valor de pi {pi:.2f}")
print(f"valor de pi {pi:10.2f}")

#fatiamentos

print('-' * 15)

nome = 'Arthur Carvalho Fontinele'

print(nome[0])
print(nome[:6])
print(nome[7:])
print(nome[7:15])
print(nome[7:15:2])
print(nome[:])
print(nome[:: -1])

#multiplas linhas

print('-' * 15)
nome = 'fontis'

mensagem = f"""
Olá meu nome é {nome}
Eu estou aprendendo python
"""

print(mensagem)

print('-' * 15)
nome = 'fontis'

mensagem = f'''
   Olá meu nome é {nome},
Eu estou aprendendo python.
    essa mensagem tem diferentes recuos
'''

print(mensagem)