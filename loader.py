# Estes imports irão alimentar a classe Loader
from pokemons import Pokemon
from pokemons import import_pokemon
from atributos import Atributos
from atributos import import_atributo
from movesets import MoveSet
from movesets import import_moveset

lista_pokemons = import_pokemon('pokemon.csv')
lista_atributos = import_atributo('pokemon.csv')
lista_movesets = import_moveset('movesets.csv')

# A classe Loader surgiu pela necessidade de relacionar os diversos dados de cada Pokémon, de forma que apenas com o 'forme' do Pokémon estes dados são relacionados. Além disto, esta classe também carregará as variáveis de batalha para o Pokémon (Level e golpes).
class Loader:
    def __init__(self, forme):
        self.forme = forme
        self.pokemon = lista_pokemons[self.forme]
        self.atributos = lista_atributos[self.forme]
        self.movesets = lista_movesets[self.forme]
        self.level = []
        self.golpe1 = []
        self.golpe2 = []
        self.golpe3 = []
        self.golpe4 = []
        self.golpe_usado = []

# Este import servirá para alimentar a classe Loader.
def import_loader(dataset_ulr):
    file = open(dataset_ulr)
    loader = {}
    for poke in file:
        linha = poke.split(',')
        if not linha[0].isnumeric:
           continue
        poke = Loader(linha[3]) 
        loader[linha[3]] = poke
    return loader

# Esta função irá fazer todo a escolha de Pokémon para o usuário.
def escolher_pokemon(player):
    from loader import Loader
    from loader import import_loader

    loader = import_loader('pokemon.csv')

    # Escolha do Pokémon
    confirma = False
    while not confirma:
        try:
            poke = loader[input('{}: Escolha um Pokémon: '.format(player))]
        except KeyError:
            print('Opção inválida.')
        else:
            confirma = True
    
    # Escolha do Level
    confirma = False
    while not confirma:
        try:
            poke.level = int(input('{} lvl: '.format(poke.forme)))
        except ValueError:
            print('Valor inválido.')
        else:
            confirma = True
    
    # Escolha dos Golpes
    from golpes import Golpe
    from golpes import import_golpe
    from loader import aprende_level
    from loader import aprende_start
    from loader import filtra_level
    # lista_golpes = import_golpe('moves.csv')

    print('Golpes possíveis para {}'.format(poke.forme))
    for key in poke.movesets.golpes_possiveis:
        if aprende_start(poke.movesets.golpes_possiveis[key]):
            print(key + ' : ' + poke.movesets.golpes_possiveis[key])
        if aprende_level(poke.movesets.golpes_possiveis[key]):
            level_golpe = filtra_level(poke.movesets.golpes_possiveis[key])
            if level_golpe <= poke.level:
                print(key + ' : ' + poke.movesets.golpes_possiveis[key])
    
    player = poke
    return player

# Daqui pra baixo são filtros de expressões regulares.
def aprende_level(golpe):
    import re
    
    check = re.findall(r'\AL', golpe)
    return check
def aprende_start(golpe):
    import re
    
    check = re.findall(r'\AStart', golpe)
    return check
def filtra_level(valor):
    import re
    
    sub = int(re.sub('L', '', valor))
    return sub
