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

class Player:
    def __init__(self, nome):
        self.nome = nome
        self.pokemon = lista_pokemons[self.nome]
        self.atributos = lista_atributos[self.nome]
        self.movesets = lista_movesets[self.nome]
        self.golpes = [] #fazer um algorítimo que escolha 4 golpes em self.moveses.golpes_possiveis
        self.golpe_usado = []
        
def import_player(dataset_ulr):
    file = open(dataset_ulr)
    pokemon_player = {}
    for poke in file:
        linha = poke.split(',')
        if not linha[0].isnumeric:
           continue
        poke = Player(linha[3]) 
        pokemon_player[linha[3]] = poke
    return pokemon_player
