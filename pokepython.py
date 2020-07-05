from player import Player
from player import import_player

lista_player = import_player('pokemon.csv')

player1 = lista_player[input('Player 1: Escolha um pokémon: ')]
player1.pokemon.level = input('{} lvl: '.format(player1.pokemon.forme))
print('')

player2 = lista_player[input('Player 2: Escolha um pokémon: ')]
player2.pokemon.level = input('{} lvl: '.format(player2.pokemon.forme))
print('')

print('{} lvl {} vs {} lvl {}'.format(player1.pokemon.forme, player1.pokemon.level, player2.pokemon.forme, player2.pokemon.level))
players = [player1, player2]
print('')

player1.atributos.hp = int(player1.atributos.hp)
player2.atributos.hp = int(player2.atributos.hp)
while not player1.atributos.hp <= 0 or player2.atributos.hp <= 0:
    for player in players:
        print('{} ({}/{}): HP: {}'.format(player.pokemon.forme, player.pokemon.type1, player.pokemon.type2, player.atributos.hp)) 
        print('Golpes:')
        player.golpe_usado = input('Escolha um golpe: ')  
        print('')
    
    print('{} usou {}.'.format(player1.pokemon.forme, player1.golpe_usado))
    print('{} usou {}.'.format(player2.pokemon.forme, player2.golpe_usado))
    print('')


# Dano = (((((2 * level) / 5) + 2) * poder * (ataque / defesa) / 50) + 2) * Modificador