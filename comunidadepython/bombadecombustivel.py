"""
Classe Bomba de Combustível: Faça um programa completo utilizando 
classes e métodos que: a. Possua uma classe chamada BombaCombustível, com 
no mínimo esses: 
Atributos: i. tipoCombustivel. ii. valorLitro iii. quantidadeCombustivel 
B. Possua no mínimo esses métodos: 
i. abastecerPorValor( ) – método onde é informado o valor a ser abastecido 
e mostra a quantidade de litros que foi colocada no veículo 
ii. abastecerPorLitro( ) – método onde é informado a quantidade em litros 
de combustível e mostra o valor a ser pago pelo cliente. 
iii. alterarValor( ) – altera o valor do litro do combustível. 
iv. alterarCombustivel( ) – altera o tipo do combustível. 
v. alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.
"""


class BombaCombustivel:
    
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    @property
    def tipoCombustivel(self):
        return self._tipoCombustivel

    @tipoCombustivel.setter
    def tipoCombustivel(self, combustivel):
        self._tipoCombustivel = combustivel

    @property
    def valorLitro(self):
        return self._valorLitro

    @valorLitro.setter
    def valorLitro(self, valorLitro):
        self._valorLitro = valorLitro
    
    @property
    def quantidadeCombustivel(self):
        return self._quantidadeCombustivel
    
    @quantidadeCombustivel.setter
    def quantidadeCombustivel(self, quantidadeCombustivel):
        self._quantidadeCombustivel = quantidadeCombustivel
    
    def menosCombustivel(self, quantidadeCombustivel):
        self._quantidadeCombustivel -= quantidadeCombustivel
    
    def abastecerPorValor(self, valor):
        quantidadeCombustivel = valor / self.valorLitro
        if not (quantidadeCombustivel < self._quantidadeCombustivel):
            return print(f'Valor indisponível. Abasteça R${self._quantidadeCombustivel * self._valorLitro:.2f} ou menos.')
        self.menosCombustivel(quantidadeCombustivel)
        return print(f'Abasteceu {quantidadeCombustivel:.2f}L')
    
    def abastecerPorLitro(self, litro):
        quantidadeAPagar = self.valorLitro * litro
        if not (litro <= self._quantidadeCombustivel):
            return print(f'Valor indisponível. Abasteça {self._quantidadeCombustivel:.2f}L ou menos')
        self.menosCombustivel(litro)
        return print(f'Valor a pagar R${quantidadeAPagar:.2f}')

        

    