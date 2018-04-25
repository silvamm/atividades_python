# Classe Pessoa: Crie uma classe que modele uma pessoa: 
# Atributos: nome, idade, peso e altura 
# Métodos: Envelhecer, engordar, emagrecer, crescer. 
# Obs: Por padrão, a cada ano que nossa pessoa envelhece, 
# sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm. 

class Pessoa:
    
    #Atributos
    def __init__ (self, nome, idade, peso, altura):  
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    
    #Propriedades
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nome):
        if not isinstance(nome, str):
            raise ValueError(f'Nome inválido {nome}')
        self._nome = nome
    
    @property
    def idade(self):
        return self._idade
    @idade.setter
    def idade(self, idade):
        if not (isinstance(idade, int) and (idade > 0)):
            raise ValueError(f'Idade inválida {idade}')
        self._idade = idade
    
    @property
    def peso(self):
        return self._peso
    @peso.setter
    def peso(self, peso):
        if not (isinstance(peso, float) and (peso > 0)):
            raise ValueError (f'Peso inválido {peso}')
        self._peso = peso
    
    @property
    def altura(self):
        return self._altura
    @altura.setter
    def altura(self, altura):
        if not( (isinstance(altura, float) and (altura > 0))):
            raise ValueError (f'Altura inválida {altura}')
        self._altura = altura
    
    #Métodos
    def envelhecer(self, maisanos):
        for i in range(maisanos):
            if self._idade < 21:
                self._idade += 1
                self.altura += 0.05
            else:
                self._idade += 1
    
    def engordar(self, maispeso):
        self._peso += maispeso
    
    def emagrecer(self, menospeso):
        self.peso -= menospeso
    
    def crescer(self, maisaltura):
        self.altura += maisaltura



