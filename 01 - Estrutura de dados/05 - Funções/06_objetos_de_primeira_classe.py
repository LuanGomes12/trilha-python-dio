def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação é {resultado}")

# Passa apenas o nome da função sem os parênteses, passagem por referência
exibir_resultado(10, 10, somar)  # O resultado da operação 10 + 10 = 20
exibir_resultado(10, 10, subtrair)  # O resultado da operação 10 - 10 = 0

# Outra alternativa
op = somar
print(op(1, 23))