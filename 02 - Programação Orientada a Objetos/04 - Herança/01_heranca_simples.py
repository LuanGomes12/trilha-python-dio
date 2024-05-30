# também chamada de herança única
# A classe filha extende apenas de uma classe pai

# Classe pai
class Veiculo:
    # Características/ atributos em comum
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    # Comportamentos/ métodos em comum
    def ligar_motor(self):
        print("Ligando o motor")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

# Motocicleta extende a classe Veiculo, ou seja, é filha da classe Veiculo
# Classe filha
class Motocicleta(Veiculo):
    pass

# Classe filha
class Carro(Veiculo):
    pass

# Classe filha
class Caminhao(Veiculo):
    # Caso seja adicionada uma nova funcionalidade, deve resgatar os atributos da classe pai
    def __init__(self, cor, placa, numero_rodas, carregado):
        # Python permite sobrescrever uma implementação!!! Para manter utiliza-se "super( )", herdar as características da classe pai
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")


moto = Motocicleta("preta", "abc-1234", 2)
carro = Carro("branco", "xde-0098", 4)
caminhao = Caminhao("roxo", "gfd-8712", 8, True)

print(moto)
print(carro)
print(caminhao)

caminhao.esta_carregado()
