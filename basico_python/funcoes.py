def somar(a,b):
    return a + b
def subtrair(a,b):
    return a - b

def exibir_resultado(a,b,funcao):
    resultado = funcao(a,b)
    print(f'O resultado da operação é = {resultado}')

exibir_resultado(10,10, somar)
exibir_resultado(10,10, subtrair)

salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

print(salario_bonus(500))