from abc import ABC, abstractmethod, abstractproperty


class ControleRemoto(ABC):
    # Não tem um corpo e todas as classes filhas devem instanciar
    # Não é possível instanciar uma classe abstrata
    # Contratos: ligar e desligar
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractproperty
    def marca(self):
        pass


class ControleTV(ControleRemoto):
    # Implementação necessária do método ligar
    def ligar(self):
        print("Ligando a TV...")
        print("Ligada!")

    # Implementação necessária do método desligar
    def desligar(self):
        print("Desligando a TV...")
        print("Desligada!")

    @property
    def marca(self):
        return "Philco"


class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o Ar Condicionado...")
        print("Ligado!")

    def desligar(self):
        print("Desligando o Ar Condicionado...")
        print("Desligado!")

    @property
    def marca(self):
        return "LG"


controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)


controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)

# Na herança o método pode ser implmentado ou não na classe filha, já com a classe abstratra é
# necessário implementar todos os métodos
