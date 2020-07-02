#aqui são definidos os pokémons com suas características. cada self.algumacoisa define uma característica
class Pokemon:
    def __init__(self, id, species, forme, type1, type2, hp, attack, defense, spattack, spdefense, speed, sex = None, level = None):
        self.id = id
        self.species = species
        self.forme = forme
        self.type1 = type1
        self.type2 = type2
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.spattack = spattack
        self.spdefense = spdefense
        self.speed = speed
        self.movimentos = []

#aqui eu estou dizendo pro programa ler um arquivo com o dataset e atribuir cada coluna a uma característica anteriormente definida na classe Pokemon.
def import_pokemon(dataset_ulr):
    file = open(dataset_ulr)
    pokemons = {}
    for poke in file:
        coluna = poke.split(',')
        if not coluna[0].isnumeric:
           continue
        poke = Pokemon(coluna[0], coluna[2], coluna[3], coluna[4], coluna[5], coluna[9], coluna[10], coluna[11], coluna[12], coluna[13], coluna[14]) 
        pokemons[coluna[3]] = poke
    return pokemons

#rodando a função anterior
lista_pokemons = import_pokemon('pokemon.csv')


# Para a batalha: escolher dois pokémons, um para cada jogador.
# Pensar em uma forma de o programa jogar com o segundo poké (IA, talvez?).
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