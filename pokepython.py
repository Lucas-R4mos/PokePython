# passar essas imports todos pro arquivo Player e criar a classe Player com elas inseridas. Class Player vai servir para integrar as diversas informações do pokémon para o usuário.

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
    def __init__(self):
        self.pokemon = lista_pokemons[self]
        self.atributo = lista_atributos[self]
        self.movesets = lista_movesets[self]
        self.golpes = []

pokemon1 = Player(input('Player 1: Escolha um pokémon: '))
pokemon1.level = input('{} lvl: '.format(pokemon1.Pokemon.forme))
print('')

pokemon2 = Player(input('Player 2: Escolha um pokémon: '))
pokemon2.level = input('{} lvl: '.format(pokemon2.forme))
print('')

print('{} lvl {} vs {} lvl {}'.format(pokemon1.forme, pokemon1.level, pokemon2.forme, pokemon2.level))
players = [pokemon1, pokemon2]
print('')

atributos1.hp = int(atributos1.hp)
atributos2.hp = int(atributos2.hp)
while not atributos1.hp <= 0 or atributos2.hp <= 0:
    for pokemon in players:
        if pokemon == pokemon1:
            atributos = atributos1
            moveset = moveset1
        if pokemon == pokemon2:
            atributos = atributos2
            moveset = moveset2
        print('{}: HP: {}'.format(pokemon.forme, atributos.hp)) 
        print('Golpes:')
        pokemon.golpe_usado = input('Escolha um golpe: ')  
        print('')


# Dano = (((((2 * level) / 5) + 2) * poder * (ataque / defesa) / 50) + 2) * Modificador