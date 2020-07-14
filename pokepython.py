from loader import Loader
from loader import import_loader
from loader import escolher_level
from loader import escolher_golpes
from loader import import_golpe

loader = import_loader('pokemon.csv')
lista_golpes = import_golpe('moves.csv')

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
        confirma = False
        while not confirma:
            try:
                player.golpe_usado = input('Escolha um golpe: ')
                for golpe in golpes:
                    if player.golpe_usado == golpe.move:
                        player.golpe_usado = golpe                 
            except KeyError:
                print('Opção inválida.')
            else:
                confirma = True

        print('')
    
    # Cálculos para dano em combate.
    if player1.golpe_usado.category == 'Physical':
        danop1 = (((((2 * player1.level) / 5) + 2) * player1.golpe_usado.power * (player1.atributos.attack / player2.atributos.defense) / 50) + 2)
    if player1.golpe_usado.category == 'Special':
        danop1 = (((((2 * player1.level) / 5) + 2) * player1.golpe_usado.power * (player1.atributos.spattack / player2.atributos.spdefense) / 50) + 2)
    if player1.golpe_usado.category == 'Status':
        danop1 = 0

    if player2.golpe_usado.category == 'Physical':
        danop2 = (((((2 * player2.level) / 5) + 2) * player2.golpe_usado.power * (player2.atributos.attack / player1.atributos.defense) / 50) + 2)
    if player2.golpe_usado.category == 'Special':
        danop2 = (((((2 * player2.level) / 5) + 2) * player2.golpe_usado.power * (player2.atributos.spattack / player1.atributos.spdefense) / 50) + 2)
    if player1.golpe_usado.category == 'Status':
        danop2 = 0

    print('{} usou {}. Causou {} de dano.'.format(player1.forme, player1.golpe_usado.move, round((danop1),0)))
    print('{} usou {}. Causou {} de dano.'.format(player2.forme, player2.golpe_usado.move, round((danop2),0)))
    print('')

    player1.atributos.hp = player1.atributos.hp - danop2
    player2.atributos.hp = player2.atributos.hp - danop1


# Dano = (((((2 * level) / 5) + 2) * poder * (ataque / defesa) / 50) + 2) * Modificador
