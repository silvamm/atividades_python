"""
Classe Conta de Investimento: Faça uma classe contaInvestimento que seja semelhante a classe contaBancaria, 
com a diferença de que se adicione um atributo taxaJuros. Forneça um construtor que configure tanto o saldo inicial 
como a taxa de juros. Forneça um método adicioneJuros (sem parâmetro explícito) que adicione juros à conta. 
Escreva um programa que construa uma poupança com um saldo inicial de R$100,0 e uma taxa de juros de 10%. 
Depois aplique o método adicioneJuros() cinco vezes e imprime o saldo resultante. 
"""


class ContaInvestimento:

    def __init__(self, saldo, taxaJuros):
        self.saldo = saldo
        self.taxaJuros = taxaJuros

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo

    @property
    def taxaJuros(self):
        return self._taxaJuros

    @taxaJuros.setter
    def taxaJuros(self, taxaJuros):
        self._taxaJuros = taxaJuros

    def adicioneJuros(self):
        self._saldo += ((self._saldo * self._taxaJuros) / 100)
