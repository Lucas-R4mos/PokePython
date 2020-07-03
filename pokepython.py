from pokemons import Pokemon
from pokemons import import_pokemon
from golpes import Golpe
from golpes import import_golpe

lista_pokemons = import_pokemon('pokemon.csv')
lista_golpes = import_golpe('moves.csv')

p1 = lista_pokemons[input('Player 1: Escolha um pokémon: ')]
p1.level = input('{} lvl: '.format(p1.forme))
print('')
p2 = lista_pokemons[input('Player 2: Escolha um pokémon: ')]
p2.level = input('{} lvl: '.format(p2.forme))
print('')
print('{} lvl {} vs {} lvl {}'.format(p1.forme, p1.level, p2.forme, p2.level))
players = [p1, p2]
print('')

# Como a batalha não oferece o uso de itens, por enquanto, mostrar para o jogador o nome, a vida e os golpes do poké.
# Mostrar os golpes em forma de lista, um em cada linha após o nome do poké. Uma linha após pedir 
#def batalha(p1.hp, p2.hp):
#    while (condição de um dos poké morrer para finalizar a batalha)
#        for p in players: #aqui ele vai sempre perguntar primeiro pro p1 depois pro p2
#            print('{} {}: HP: {}'.format(p.nome, p.tipo, p.vida)) 
#            print('Golpes:')   #aqui eu substituo pela função de escolher golpe
   

# Dano = (((((2 * level) / 5) + 2) * poder * (ataque / defesa) / 50) + 2) * Modificador