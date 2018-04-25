#Classe Conta Corrente: Crie uma classe pra implementar uma conta corrente.
#Atributos: Número de conta, nome do correntista e saldo.
#Métodos: Alterar o nome, depósito e saque.
#No construtor saldo é opcional, com o valor default zero
#e os demais atributos são obrigatórios.

class ContaCorrente:

    def __init__(self, numeroConta, nomeCorrentista, saldo=0):
        self.numeroConta = numeroConta
        self.nomeCorrentista = nomeCorrentista
        self.saldo = saldo
        
    @property
    def nomeCorrentista(self):
        return self._nomeCorrentista
    @nomeCorrentista.setter
    def nomeCorrentista(self, nome):
        if not isinstance(nome, str):
            raise ValueError(f'Nome inválido: {nome}') 
        self._nomeCorrentista = nome
    
    def deposito(self, valor):
        if not (isinstance(valor, int) and (valor > 0)):
            raise ValueError(f'Valor inválido: {valor}')    
        self.saldo += valor 
        
    def saque(self, valor):
        if not isinstance(valor, int):
            raise ValueError(f'Valor inválido: {valor}')
        if not (self.saldo >= valor):
            print(f'Você não pode sacar {valor}')
            print(f'Seu saldo é de {self.saldo}')
        else:
            self.saldo -= valor       

