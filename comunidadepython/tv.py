#Classe TV: Faça um programa que simule 
# um televisor criando-o como um objeto.
#O usuário deve ser capaz de informar 
#o número do canal e aumentar ou diminuir o volume.
#Certifique-se de que o número do canal e 
#o nível do volume permanecem dentro da faixas válidas.


class TV:

    def __init__ (self, canal, volume=0):
        self.canal = canal
        self.volume = volume

    @property
    def canal(self):
        return self._canal
    @canal.setter
    def canal(self, canal):
        if not (isinstance(canal, int) and (canal <= 1000 and canal >= 0)):
            raise ValueError(f'Canal inválido: {canal} Canal [0..1000]')
        self._canal = canal
    
    @property
    def volume(self):
        return self._volume
    @volume.setter
    def volume(self, volume):
        if not (isinstance(volume, int) and (volume <= 100 and volume >= 0)):
            raise ValueError(f'Volume inválido: {volume} Volume [0..100]')
        self._volume = volume





