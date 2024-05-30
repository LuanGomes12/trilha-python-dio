# DEPURADOR: função que executa antes da sua função, utiliza-se o "@" antes do nome do depurador
# - Pega um método e transforma em uma propriedade
# - Utiliza a sintaxe de atributo
class Foo:
    def __init__(self, x=None):
        self._x = x

    # Permite retornar o valor
    @property
    def x(self):
        return self._x or 0

    # A sintaxe não é a mesma do método
    # Permite alterar valor
    @x.setter
    def x(self, value):
        self._x += value

    # Permite deletar/trocar o valor
    @x.deleter
    def x(self):
        # del self._x # Para deletar 
        self._x = 0


foo = Foo(10)
print(foo.x)
del foo.x
print(foo.x)
foo.x = 10
print(foo.x)