class Golpes:
    def __init__(self, nome, tipo, pp, poder, precisao, prioridade, efeito):
        self.nome = nome
        self.tipo = str(tipo)
        self.pp = int(pp)
        self.poder = int(poder)
        self.precisao = int(precisao)
        self.efeito = efeito

Tackle = Golpes('Tackle', ['Normal'], 35, 35, 95, 0, [''])
Tail_Whip = Golpes('Tail_Whip', ['Normal'], 30, 0, 100, 0, ['Reduz a defesa do alvo'])
Scratch = Golpes('Scratch', ['Normal'], 35, 40, 100, 0, [''])
Growl = Golpes('Growl', ['Normal'], 40, 0, 100, 0, ['Reduz o ataque do alvo']) 

class Pokemon:
    def __init__(self, nome, tipo, level, vida, ataque, defesa, especial, velocidade, set_golpes, golpe_usado = None):
        self.nome = nome
        self.tipo = tipo
        self.level = level
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.especial = especial
        self.velocidade = velocidade
        self.set_golpes = set_golpes

bulbasaur = Pokemon('Bulbasaur', ['Grama', 'Veneno'], 5, 45, 49, 49, 65, 45, [Tackle, Growl])
charmander = Pokemon('Charmander', ['Fogo'], 5, 39, 52, 43, 50, 65, [Scratch, Growl])
squirtle = Pokemon('Squirtle', ['Água'], 5, 44, 48, 65, 50, 43, [Tackle, Tail_Whip])

def prioridade_ataque(p1, p2):
    primeiro = []
    segundo = []
    if p1.velocidade > p2.velocidade:
        primeiro == p1
        segundo == p2
    if p2.velocidade > p1.velocidade:
        primeiro == p2
        segundo == p1


p1 = input('Player 1: Escolha um pokémon, \'bulbasaur\', \'charmander\' ou \'squirtle\': ')
if p1 == 'bulbasaur':
    p1 = bulbasaur
if p1 == 'squirtle':
    p1 = squirtle
if p1 == 'charmander':
    p1 = charmander
p2 = input('Player 2: Escolha um pokémon, \'bulbasaur\', \'charmander\' ou \'squirtle\': ')
if p2 == 'bulbasaur':
    p2 = bulbasaur
if p2 == 'squirtle':
    p2 = squirtle
if p2 == 'charmander':
    p2 = charmander

print('')
print(p1.nome,'vs', p2.nome)
players = [p1, p2]
print('')

while not p1.vida <= 0 or p2.vida <= 0:

    for p in players:
        print('{}: HP: {}'.format(p.nome, round((p.vida),0)))
        print('Golpes:')
        for g in p.set_golpes:
            print('{}: Tipo {}, PP {}, Poder {}, Precisão {}'.format(g.nome, g.tipo, g.pp, g.poder, g.precisao))
        p.golpe_usado = input('Escolha o golpe: ')
        if p.golpe_usado == 'scratch':
            p.golpe_usado = Scratch
        if p.golpe_usado == 'tackle':
            p.golpe_usado = Tackle
        if p.golpe_usado == 'growl':
            p.golpe_usado = Growl
        if p.golpe_usado == 'tail_whip':
            p.golpe_usado = Tail_Whip
        print('')

    danop1 = (((((2 * p1.level) / 5) + 2) * p1.golpe_usado.poder * (p1.ataque / p2.defesa) / 50) + 2)
    danop2 = (((((2 * p2.level) / 5) + 2) * p2.golpe_usado.poder * (p2.ataque / p1.defesa) / 50) + 2)

    p1.golpe_usado.pp = p1.golpe_usado.pp - 1
    p2.golpe_usado.pp = p2.golpe_usado.pp - 1

    p1.vida = p1.vida - danop2
    p2.vida = p2.vida - danop1 

    print('{} usou {}. Causou {} de dano.'.format(p1.nome, p1.golpe_usado.nome, danop1))
    print('{} usou {}. Causou {} de dano.'.format(p2.nome, p2.golpe_usado.nome, danop2))
    print('')


# Dano = (((((2 * level) / 5) + 2) * poder * (ataque / defesa) / 50) + 2) * Modificador
