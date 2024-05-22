salario = 2000

# Utilizar variáveis "global" não é uma boa técnica, pois torna o debug muito complexo
def salario_bonus(bonus, lista):
    global salario

    lista_aux = lista.copy()
    lista_aux.append(2)
    print(f"lista auxi = {lista_aux}")

    salario += bonus
    return salario

lista = [1]

salario_com_bonus = salario_bonus(500, lista)  # 2500
print(salario_com_bonus)
print(lista)