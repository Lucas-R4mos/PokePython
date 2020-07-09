print('Esta versão contém erro após a escolha dos Pokémons.')

from loader import escolher_pokemon

player1 = 'Player 1'
player2 = 'Player 2'
players = [player1, player2]
for player in players:
    escolher_pokemon(player)
    print('')

# Com as exceções de escolha prontas, o próximo passo é fazer a relação dos novos dados com os códigos a seguir, que estão no formato dos dados antigos.
print('{} lvl {} vs {} lvl {}'.format(player1.forme, player1.level, player2.forme, player2.level))
players = [player1, player2]
print('')

player1.atributos.hp = int(player1.atributos.hp)
player2.atributos.hp = int(player2.atributos.hp)
while player1.atributos.hp <= 0 or player2.atributos.hp <= 0:
    for player in players:
        print('{} ({}/{}): HP: {}'.format(player.forme, player.pokemon.type1, player.pokemon.type2, player.atributos.hp)) 
        print('Golpes:')
        for golpe in player.movesets.golpes_possiveis:
            print(golpe)
        player.golpe_usado = input('Escolha um golpe: ')  
        print('')
    
    print('{} usou {}.'.format(player1.forme, player1.golpe_usado))
    print('{} usou {}.'.format(player2.forme, player2.golpe_usado))
    print('')


# Dano = (((((2 * level) / 5) + 2) * poder * (ataque / defesa) / 50) + 2) * Modificador
