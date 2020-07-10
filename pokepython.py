from loader import Loader
from loader import import_loader
from loader import escolher_level
from loader import escolher_golpes

loader = import_loader('pokemon.csv')

confirma = False
while not confirma:
    try:
        player1 = loader[input('Player 1: Escolha um Pokémon: ')]
    except KeyError:
        print('Opção Inválida.')
    else:
        confirma = True
escolher_level(player1)
escolher_golpes(player1)

confirma = False
while not confirma:
    try:
        player2 = loader[input('Player 2: Escolha um Pokémon: ')]
    except KeyError:
        print('Opção Inválida.')
    else:
        confirma = True
escolher_level(player2)
escolher_golpes(player2)
players = [player1, player2]

print('{} L{} vs {} L{}'.format(player1.forme, player1.level, player2.forme, player2.level))
players = [player1, player2]
print('')

player1.atributos.hp = int(player1.atributos.hp)
player2.atributos.hp = int(player2.atributos.hp)
while not player1.atributos.hp <= 0 or player2.atributos.hp <= 0:
    for player in players:
        print('{} ({}/{}): HP: {}'.format(player.forme, player.pokemon.type1, player.pokemon.type2, player.atributos.hp)) 
        print('Golpes:')
        golpes = (player.golpe1, player.golpe2, player.golpe3, player.golpe4)
        for golpe in golpes:
            print('{} ({}): PP: {} Power: {} Accuracy: {}'.format(golpe.move, golpe.type, golpe.pp, golpe.power, golpe.accuracy))
        player.golpe_usado = input('Escolha um golpe: ')  
        print('')
    
    print('{} usou {}.'.format(player1.forme, player1.golpe_usado))
    print('{} usou {}.'.format(player2.forme, player2.golpe_usado))
    print('')


# Dano = (((((2 * level) / 5) + 2) * poder * (ataque / defesa) / 50) + 2) * Modificador
