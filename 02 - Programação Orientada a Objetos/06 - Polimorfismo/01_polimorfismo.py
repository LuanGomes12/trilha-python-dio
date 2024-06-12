class Passaro:
    def voar(self):
        print("Voando...")


class Pardal(Passaro):
    def voar(self):
        print("Pardal pode voar")


class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar")


# NOTE: exemplo ruim do uso de herança para "ganhar" o método voar
class Aviao(Passaro):
    def voar(self):
        print("Avião está decolando...")


# Conceito de polimorfismo está aqui
# O objeto se comporta de maneiras diferentes, mas usa o mesmo método, independente do objeto
def plano_voo(obj):
    obj.voar()


plano_voo(Pardal())
plano_voo(Avestruz())
plano_voo(Aviao())
