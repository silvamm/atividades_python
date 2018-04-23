#Crie uma classe que modele uma bola:
#Atributos: Cor, circunferência, material
#Métodos: trocaCor e mostraCor

class Bola:
    #Atributos:
    
    #atributos com estruta de encapsulamento '__variavel'
    def __init__(self, cor, circunferencia, material):
        self.__cor = cor
        self.__circunferencia = circunferencia
        self.__material = material
    
    #Métodos:
    
    #Trocar a cor
    def setCor(self, cor):
        self.__cor = cor
    
    #Mostrar a cor
    def getCor(self):
        return self.__cor


#POSSIVEIS MELHORIAS:

class BolaMelhorias:

    def __init__(self, cor, circunferencia, material):
        self.__cor = 0
        self.__circunferencia = 0
        self.__material = 0
        
        #1. - métodos para verifiar a validade da entrada
        self.setCor(cor)
        self.setCircunferencia(circunferencia)
        self.setMaterial(material)

    #1.1 - método para verificar a validade da entrada e fazer modificação no atributo
    def setCor(self, cor):
        if not isinstance(cor, str):
            raise TypeError(f'Cor inválida: {cor}') 
        self.__cor = cor

    #1.2 - método para verificar a validade da entrada e fazer modificação no atributo
    def setCircunferencia(self, circunferencia):
        if not isinstance(circunferencia, float) and (circunferencia <= 0):
            raise ValueError (f'Circuferência inválida: {circunferencia}')
        self.__circunferencia = circunferencia
    
    #1.3 - método para verificar a validade da entrada e fazer modificação no atributo
    def setMaterial(self, material):
        if not isinstance(material, str):
            raise TypeError(f'Material inválido: {material}')
        self.__material = material
    
    #2. Mostrar o resto dos atributos
    
    #2.1 -Mostrar a circunferencia
    def getCircunferencia(self):
        return self.__circunferencia

    #2.2 - Mostrar o material
    def getMaterial(self):
        return self.__material

    #3. Efetuando testes
    if __name__ == '__main__':
        pass




