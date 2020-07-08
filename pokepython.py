from loader import Loader
from loader import import_loader
from loader import escolher_golpes

loader = import_loader('pokemon.csv')

player1 = loader[input('Player 1: Escolha um pokémon: ')]
player1.pokemon.level = int(input('{} lvl: '.format(player1.pokemon.forme)))
print('')
escolher_golpes(player1)
print('')


player2 = loader[input('Player 2: Escolha um pokémon: ')]
player2.pokemon.level = int(input('{} lvl: '.format(player2.pokemon.forme)))
print('')
escolher_golpes(player2)
print('')

print('{} lvl {} vs {} lvl {}'.format(player1.pokemon.forme, player1.pokemon.level, player2.pokemon.forme, player2.pokemon.level))
players = [player1, player2]
print('')

player1.atributos.hp = int(player1.atributos.hp)
player2.atributos.hp = int(player2.atributos.hp)
while player1.atributos.hp <= 0 or player2.atributos.hp <= 0:
    for player in players:
        print('{} ({}/{}): HP: {}'.format(player.pokemon.forme, player.pokemon.type1, player.pokemon.type2, player.atributos.hp)) 
        print('Golpes:')
        for golpe in player.movesets.golpes_possiveis:
            print(golpe)
        player.golpe_usado = input('Escolha um golpe: ')  
        print('')
    
    print('{} usou {}.'.format(player1.pokemon.forme, player1.golpe_usado))
    print('{} usou {}.'.format(player2.pokemon.forme, player2.golpe_usado))
    print('')


# Dano = (((((2 * level) / 5) + 2) * poder * (ataque / defesa) / 50) + 2) * Modificador
