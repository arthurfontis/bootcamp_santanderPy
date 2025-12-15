contatos = {
    'mail1@gmail.com': {'nome':'sr1', 'tel': 'sr1t'},
    'mail2@gmail.com': {'nome':'sr2', 'tel': 'sr2t'},
    'mail3@gmail.com': {'nome':'sr3', 'tel': 'sr3t'},
    'mail4@gmail.com': {'nome':'sr4', 'tel': 'sr4t'},
}
copia = contatos.copy()
contatos.clear()

print(contatos)

print('-' * 15)


copia['mail1@gmail.com'] = {'nome': 'Gui'}
print(copia)

print('-' * 15)
dict1 = dict.fromkeys(['nome', 'telefone'])
dict2 = dict.fromkeys(['nome', 'telefone'], 'vazio')

print(dict1)
print(dict2)

print('-' * 15)

print(copia.get("chave"))
print(copia.get("chave", {}))
print(copia.get("mail1@gmail.com", {}))

print('-' * 15)

print(copia.items())
print('-' * 15)
print(copia.keys())
print(len(copia.keys()))

print('-' * 15)

print(copia.pop('mail1@gmail.com'))
print(copia.pop('mail1@gmail.com', {}))

print('-' * 15)

copia.popitem() #tirou o 4
print(copia)

print('-' * 15)

copia.setdefault('nome', 'Arthur')
print(copia)
copia.setdefault('idade1', 28)
print(copia)


print('-' * 15)
contato = {
    'mail1@gmail.com': {'nome': 'Guilherme', 'telefone': '3333-2221'}
}


contato.update({'mail1@gmail.com': {'nome': 'Gui'}})
print(contato)
contato.update({'mail2@gmail.com': {'nome': 'fontis', 'idade': 21}})
print(contato)

print('-' * 15)
mail = {
    'mail1@gmail.com': {'nome':'sr1', 'tel': 'sr1t'},
    'mail2@gmail.com': {'nome':'sr2', 'tel': 'sr2t'},
    'mail3@gmail.com': {'nome':'sr3', 'tel': 'sr3t'},
    'mail4@gmail.com': {'nome':'sr4'},
}

print(mail.values())

print('-' * 15)

result = 'mail1@gmail.com' in mail
print(result)
result = 'mail6@gmail.com' in mail
print(result)

print('-' * 15)

print('tel' in mail['mail2@gmail.com'])
print('tel' in mail['mail4@gmail.com'])


del mail['mail2@gmail.com']['tel']
del mail['mail3@gmail.com']

print(mail)