class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Recebe um primeiro argumento, mas aponta para a classe (cls) e não para a instância (self)
    # Utilizado para criar um método de fábrica
    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return cls(nome, idade)

    # Não pode acessar ou modificar o estado
    # Utilizado para criar uma função utilitária
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18


p = Pessoa.criar_de_data_nascimento(1994, 3, 21, "Guilherme")
print(p.nome, p.idade)

print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(8))
