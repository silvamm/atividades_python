"""
Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades: 
A. Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível no tanque. 
B. O consumo é especificado no construtor e o nível de combustível inicial é 0. 
C. Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância, reduzindo o nível de combustível no tanque de gasolina.
D. Forneça um método obterGasolina( ), que retorna o nível atual de combustível. 
E. Forneça um método adicionarGasolina( ), para abastecer o tanque.

F. meuFusca = Carro(15);	# 15 quilômetros por litro de combustivel.

Exemplo de uso: 
meuFusca.andar(100);	# anda 100 quilômetros.
meuFusca.obterGasolina()	# Imprime o combustível
meuFusca.adicionarGasolina(20); # abastece com 20 litros de combustível somar com o que resta no tanque.
"""

class Carro:

    def __init__(self, consumo):
        self.consumo = consumo
        self.combustivel = 0
    
    @property
    def consumo(self):
        return self._consumo

    @consumo.setter
    def consumo(self, consumo):
        self._consumo = consumo
    
    @property
    def combustivel(self):
        return self._combustivel

    @combustivel.setter
    def combustivel(self, combustivel):
        self._combustivel = combustivel

    def andar(self, quilometros):
        consumoLitros = quilometros / self._consumo
        if (consumoLitros > self._combustivel):
            faltaLitros = consumoLitros - self._combustivel
            quilometrosPercorridos = self._combustivel * self._consumo
            self._combustivel -= (consumoLitros - faltaLitros)
            return print(f'A gasolina acabou! Você andou {quilometrosPercorridos:.1f}km dos {quilometros}km desejados. Abasteça mais {faltaLitros:.1f}L para chegar ao destino.')
        self._combustivel -= consumoLitros
    
    def adicionarGasolina(self, gasolina):
        self._combustivel += gasolina


