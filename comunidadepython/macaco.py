#Classe Macaco
#Desenvolva uma classe Macaco
#Atributos:Nome, estômago
#Métodos: Comer, verBucho e digerir
#Faça um programa ou teste interativamente, criando pelo menos dois macacos, a
#Alimentando-os com pelo menos 3 alimentos diferentes e verificando 
#o conteúdo do estomago a cada refeição. 
#Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal? 


class Macaco:

    def __init__ (self, nome, estomago=[]):
        self.nome = nome
        self.estomago = estomago

    @property
    def estomago(self):
        return self._estomago
    @estomago.setter
    def estomago(self, estomago):
        self._estomago = estomago
    @estomago.deleter
    def estomago(self):
        self._estomago = []
    
    def comer(self, alimento):
        self._estomago.append(alimento)

# teste = Macaco('a')
# teste2 = Macaco('b')
# print(teste.estomago)
# teste.comer(teste2.nome)
# print(teste.estomago)
# del teste.estomago
# print(teste.estomago)

print('#'*5+' Criando MACACOS! '+'#'*5)
nomeMacaco = 'Jonathan' #str(input('Digite o nome do seu primeiro MACACO!: '))
print(f'Muito bem! Agora você tem um macaquinho chamado {nomeMacaco}!')
macaco1 = Macaco(nomeMacaco)
print(f'Que tal alimenta-lo?')
print(f'Primeiro, vamos fazer {nomeMacaco} comer três diferentes alimentos.')
for i in range(1,4):
    #falta trabalhar mais excecões
    alimento = input(f'Digite o {i}º alimento: ')
    alimento = alimento.capitalize()
    while alimento in macaco1.estomago:
        alimento = input(f'Ele já comeu isto! Coloque algo diferente: ')
        alimento = alimento.capitalize()    
    macaco1.comer(alimento)
    print(f'O estômago de {nomeMacaco} tem {macaco1.estomago}')
print(f'{nomeMacaco} está com a barriga cheia! Deixa ele descansar para digerir os alimentos!')
descansar = False
while descansar == False:
    #trabalhar mais exceções
    resposta = input('Certo? [S/N]: ')
    resposta = resposta.upper()
    if resposta == 'S':
         descansar = True
    else:
        print('Tenha dó do macaquinho! Ele esta de barriga cheia! Deixa ele descansar agora?')
del macaco1.estomago
print('Eita que o maquinho descansou foi muito, viu? Agora ta feliz da vida!')
print(f'Digeriu todo o alimento e a barriga dele agora tem {macaco1.estomago}')






