class Estudante:
    # Atributos de classe, vem logo após a criação da classe, são compartilhados entre os objetos, são únicas
    escola = "DIO"

    def __init__(self, nome, matricula):
        # Atributos de instância, são diferentes para cada objeto (cada objeto tem uma cópia)
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"


def mostrar_valores(*objs):
    for obj in objs:
        print(obj)


aluno_1 = Estudante("Guilherme", 1)
aluno_2 = Estudante("Giovanna", 2)
mostrar_valores(aluno_1, aluno_2)

# Se alterar a variável de classe, altera todas as variáveis da classe "Estudante"
Estudante.escola = "Python"
#aluno_1.escola = "PHP" # Altera a escola do aluno_1, embora seja uma variável de classe, ela funciona aqui como instância
# já que passo o objeto e não a classe
aluno_3 = Estudante("Chappie", 3)
mostrar_valores(aluno_1, aluno_2, aluno_3)
