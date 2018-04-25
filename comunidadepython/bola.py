#Crie uma classe que modele uma bola:
#Atributos: Cor, circunferência, material
#Métodos: trocaCor e mostraCor


class Bola:
    #Atributos:
    #atributos com estrutura de encapsulamento '__variavel'
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
    
    #Métodos:
    #Trocar a cor
    def setCor(self, cor):
        self._cor = cor
    
    #Mostrar a cor
    def getCor(self):
        return self._cor


#POSSIVEIS MELHORIAS:

class BolaMelhorias:

    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    @property
    def cor(self):
        return self._cor
    @cor.setter
    def cor(self, cor):
        if not isinstance(cor, str):
            raise TypeError(f'Cor inválida: {cor}') 
        self._cor = cor

    @property
    def circunferencia(self):
        return self._circunferencia
    @circunferencia.setter
    def circunferencia(self, circunferencia):
        if not isinstance(circunferencia, float) and (circunferencia <= 0):
            raise ValueError (f'Circuferência inválida: {circunferencia}')
        self._circunferencia = circunferencia
    
    @property
    def material(self):
        return self._material
    @material.setter
    def material(self, material):
        if not isinstance(material, str):
            raise TypeError(f'Material inválido: {material}')
        self._material = material
    