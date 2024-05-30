class Cachorro:
    # Construtor, é sempre executado primeiro
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe...")
        # Atributos
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    # Destrutor, é executado no final
    def __del__(self):
        print("Removendo a instância da classe.")

    def falar(self):
        print("auau")


def criar_cachorro():
    c = Cachorro("Zeus", "Branco e preto", False)
    print(c.nome)

# Instância
c = Cachorro("Chappie", "amarelo")
c.falar()

print("Ola mundo")

# Forçar o destrutor a executar antes de terminar a execução do código
del c

print("Ola mundo")
print("Ola mundo")
print("Ola mundo")

# criar_cachorro()
