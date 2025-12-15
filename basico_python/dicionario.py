pessoa = {'nome': 'Guilherme', 'idade': 28}
pessoa = dict(nome = 'Guilherme', idade = 28)

pessoa['telefone'] = '3333-1234'

print(pessoa)

print('-' * 15)
print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['telefone'])

print('-' * 15)
pessoa['nome'] = 'Maria'
pessoa['idade'] = 18
pessoa['telefone'] = '9988-1781'

print(pessoa)

#aninhado

print('-' * 15)
contatos = {
    'mail1@gmail.com': {'nome':'sr1', 'tel': 'sr1t'},
    'mail2@gmail.com': {'nome':'sr2', 'tel': 'sr2t'},
    'mail3@gmail.com': {'nome':'sr3', 'tel': 'sr3t'},
    'mail4@gmail.com': {'nome':'sr4', 'tel': 'sr4t'},
}

print(contatos['mail1@gmail.com']['tel'])

print('-' * 15)

for chave in contatos:
    print(chave, contatos[chave])

print('-' * 15)

for chave, valor in contatos.items():
    print(chave,valor)