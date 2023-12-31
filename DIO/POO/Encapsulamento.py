"""
O conceito de encapsulamento envolve a proteção do acesso aos atributos e
caractecristicas de determinada classe. Python usa convenção no nome do recurso
para determinar um atributo como público ou privado. Os atributos
públicos (escrito normal) podem ser acessados fora da classe,
os privados (usa-se _ antes do nome) podem ser acessados somente na classe.
Para acessar um atributo de fora da classe, temos de criar um método para
tal devido às questões de segurança. A exemplo, um sistema de caixa 
eletrônico bancário, onde teria as funções de consultar saldo, sacar, 
depositar... um usuário não pode ter acesso direto ao saldo pois pode 
manipular ele, então para isso criamos um método que só tem a função de
acessar o saldo, dessa forma acessamos o saldo não diretamente, mas por 
um método que acessa o atributo/característica da classe desejada.
"""


class Conta:
    def __init__(self, nro_agencia, saldo=0):  # Iniciamos o construtor da classe e definimos os atributos
        self._saldo = saldo  # Definimos os saldo como privado
        self.nro_agencia = nro_agencia  # Definimos o número da agencia como publico

    def depositar(self, valor):  # criamos o método de saque que acrescenta no saldo
        self._saldo += valor

    def sacar(self, valor):  # criamos o método sacar que decrementa no saldo
        self._saldo -= valor

    def mostrar_saldo(self):  # criamos o método de acesso ao saldo, devido atributo privado
        return self._saldo


conta = Conta('001', 100)
# print(conta._saldo) -> segundo a convenção este acesso ao atributo privado está errado
print(conta.mostrar_saldo())
print(conta.nro_agencia)

