# CONVENÇÃO
# Privado: começa com underline (_nome)
# Publico: começa sem underline (nome) 
class Conta:
    def __init__(self, nro_agencia, saldo=0):
        self._saldo = saldo
        self.nro_agencia = nro_agencia

    def depositar(self, valor):
        # ...
        self._saldo += valor

    def sacar(self, valor):
        # ...
        self._saldo -= valor

    def mostrar_saldo(self):
        # ...
        return self._saldo

# JAMAIS FAZER ISSO
conta = Conta("0001", 100)
print(conta._saldo)

conta._saldo += 1000
print(conta._saldo, "\n")

# FAZER ASSIM
conta = Conta("0001", 100)
conta.depositar(100)
print(conta.nro_agencia)
print(conta.mostrar_saldo()) # Para acessar um atributo privado, utiliza-se um método