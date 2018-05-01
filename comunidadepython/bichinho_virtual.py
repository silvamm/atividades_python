'''
Classe Bichinho Virtual: Crie uma classe que modele um Tamagushi.
Atributos: Nome, Fome, Saúde e Idade.
Métodos: Alterar nome, fome, saúde, idade.
Retornar nome, fome, saúde, idade.
Método Humor: Combinação entre Fome e saúde.
'''


class Tamagushi:


    def __init__(self, nome, fome=0, saude=100, idade=0):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nome):
        if not isinstance(nome, str):
            raise ValueError(f'Nome inválido {nome}')
        self._nome = nome
    
    @property
    def fome(self):
        return self._fome
    @fome.setter
    def fome(self, fome):
        if not (fome <=100 and fome >=0):
            raise ValueError(f'Fome inválida {fome}')
        self._fome = fome

    @property
    def saude(self):
        return self._saude
    @saude.setter
    def saude(self, saude):
        if not (saude <=100 and saude >= 0):
            raise ValueError(f'Saúde inválida {saude}')
        self._saude = saude
    
    @property
    def idade(self):
        return self._idade
    @idade.setter
    def idade(self, idade):
        if not (idade >= 0):
            raise ValueError(f'Idade inválida {idade}')
        self._idade = idade

    def humor(self):
        return self._saude - self._fome

