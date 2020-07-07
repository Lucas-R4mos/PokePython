from pokemons import Pokemon
from pokemons import import_pokemon
from atributos import Atributos
from atributos import import_atributo
from movesets import MoveSet
from movesets import import_moveset
from golpes import Golpe
from golpes import import_golpe

lista_pokemons = import_pokemon('pokemon.csv')
lista_atributos = import_atributo('pokemon.csv')
lista_movesets = import_moveset('movesets.csv')
lista_golpes = import_golpe('moves.csv')

class Loader:
    def __init__(self, forme):
        self.forme = forme
        self.pokemon = lista_pokemons[self.forme]
        self.atributos = lista_atributos[self.forme]
        self.movesets = lista_movesets[self.forme]
#        self.golpes = [] #fazer um algorítimo que escolha 4 golpes em self.moveses.golpes_possiveis
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