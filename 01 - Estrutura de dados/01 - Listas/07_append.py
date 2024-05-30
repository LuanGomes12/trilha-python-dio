usuarios = []
usuarios2 = []

# usuarios.append({"nome": "Luan"})
# usuarios.append({"data_nascimento": "13"})
# usuarios.append({"cpf": "123456"})
# usuarios.append({"endereço": "Rua a"})

usuarios2.append({"nome": "Luan", "data_nascimento": "13", "cpf": "123456", "endereco": "Rua a"})
# usuarios2.append({"nome": "Lua", "data_nascimento": "13", "cpf": "123456", "endereco": "Rua a"})

# lista.append(1)
# lista.append("Python")
# lista.append([40, 30, 20])

# print(usuarios)  # [1, "Python", [40, 30, 20]]
#print(usuarios2)


for usuario in usuarios2:
    if usuario["cpf"] == "123456":
        print(usuario)
    else:
        print("não")
