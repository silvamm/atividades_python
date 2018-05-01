'''
Classe Quadrado: Crie uma classe que modele um quadrado:
Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área.
'''

class Quadrado:
    # Atributos:
    # atributos com estrutura de encapsulamento '__variavel'
    def __init__ (self, lado):
        self._lado = lado

    #Métodos
    #Mudar valor do lado
    def setLado(self, lado):
        self._lado = lado

    #Retornar o valor do lado
    def getLado(self):
        return self._lado
    
    #Calculando a Área
    def getArea(self):
        return self._lado ** 2


#POSSIVEIS MELHORIAS:

class QuadradoMelhorias:

    def __init__(self,lado):
        self.lado = lado
    
    @property
    def lado(self):
        return self._lado
    @lado.setter
    def lado(self, lado):
        if not isinstance(lado, float) and (lado > 0):
            raise ValueError (f'Lado inválido: {lado}')
        self._lado = lado 
    
    @property
    def area(self):
        return self._lado ** 2



       
    

    