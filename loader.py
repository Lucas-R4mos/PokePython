from pokemons import Pokemon
from pokemons import import_pokemon
from atributos import Atributos
from atributos import import_atributo
from movesets import MoveSet
from movesets import import_moveset

lista_pokemons = import_pokemon('pokemon.csv')
lista_atributos = import_atributo('pokemon.csv')
lista_movesets = import_moveset('movesets.csv')

class Loader:
    def __init__(self, forme):
        self.forme = forme
        self.pokemon = lista_pokemons[self.forme]
        self.atributos = lista_atributos[self.forme]
        self.movesets = lista_movesets[self.forme]
        self.golpe1 = []
        self.golpe2 = []
        self.golpe3 = []
        self.golpe4 = []
        self.golpe_usado = []
        
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

def aprende_level(golpe):
    import re
    
    check = re.findall('\AL', golpe)
    return check

def aprende_start(golpe):
    import re
    
    check = re.findall('\AStart', golpe)
    return check

def filtra_level(valor):
    import re
    
    sub = int(re.sub('L', '', valor))
    return sub

def escolher_golpes(player):
    from golpes import Golpe
    from golpes import import_golpe
    
    lista_golpes = import_golpe('moves.csv')

    print('Golpes possíveis para {}'.format(player.forme))
    for key in player.movesets.golpes_possiveis:
        if aprende_start(player.movesets.golpes_possiveis[key]):
            print(key + ' : ' + player.movesets.golpes_possiveis[key])
        if aprende_level(player.movesets.golpes_possiveis[key]):
            level_golpe = filtra_level(player.movesets.golpes_possiveis[key])
            if level_golpe <= player.pokemon.level:
                print(key + ' : ' + player.movesets.golpes_possiveis[key])
    return
