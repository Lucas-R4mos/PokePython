from pokemons import Pokemon
from pokemons import import_pokemon
from atributos import Atributos
from atributos import import_atributo
from movesets import MoveSet
from movesets import import_moveset
from golpes import import_golpe

lista_pokemons = import_pokemon('pokemon.csv')
lista_atributos = import_atributo('pokemon.csv')
lista_movesets = import_moveset('movesets.csv')
lista_golpes = import_golpe('moves.csv')

class Loader:
    def __init__(self, forme):
        self.forme = forme
        self.pokemon = lista_pokemons[self.forme]
        self.atributos = lista_atributos[self.forme]
        self.movesets = lista_movesets[self.forme]
        self.level = []
        self.golpes_liberados = []
        self.golpe1 = []
        self.golpe2 = []
        self.golpe3 = []
        self.golpe4 = []
        self.golpe_usado = []

def aprende_level(golpe):
    import re
    
    check = re.findall(r'\AL', golpe)
    return check
def aprende_start(golpe):
    import re
    
    check = re.findall(r'\AStart', golpe)
    return check
def filtra_level(valor):
    import re
    
    sub = int(re.sub('L', '', valor))
    return sub

def import_loader(dataset_ulr):
    file = open(dataset_ulr)
    loader = {}
    for poke in file:
        linha = poke.split(',')
        if not linha[0].isnumeric:
           continue
        poke = Loader(linha[3]) 
        loader[linha[3]] = poke
    return loader

def escolher_level(player):
    confirma = False
    while not confirma:
        try:
            player.level = int(input('{} lvl: '.format(player.forme)))
            if player.level < 1 or player.level > 100:
                raise ValueError
        except ValueError:
            print('Valor inválido.')
        else:
            confirma = True
    print('')
def escolher_golpes(player):
    print('Golpes possíveis para {}'.format(player.forme))
    
    for key in player.movesets.golpes_possiveis:
        if aprende_start(player.movesets.golpes_possiveis[key]):
            player.golpes_liberados.append(key)
        if aprende_level(player.movesets.golpes_possiveis[key]):
            level_golpe = filtra_level(player.movesets.golpes_possiveis[key])
            if level_golpe <= player.level:
                player.golpes_liberados.append(key)
    
    for golpe in player.golpes_liberados:
        try:
            print('{} ({}) -> Power: {}, Accuracy: {}'.format(lista_golpes[golpe].move, lista_golpes[golpe].type, str(lista_golpes[golpe].power), lista_golpes[golpe].accuracy))
        except KeyError:
            continue

    print('')
    print('Escolha 4 entre os golpes listados: ')

    confirma1 = False
    while not confirma1:
        try:
            player.golpe1 = lista_golpes[input('Golpe 1: ')]
            if not player.golpe1.move in player.golpes_liberados:
                raise KeyError
        except KeyError:
            print('Opção Inválida.')
        else:
            confirma1 = True

    confirma2 = False
    while not confirma2:
        try:
            player.golpe2 = lista_golpes[input('Golpe 2: ')]
            if not player.golpe2.move in player.golpes_liberados:
                raise KeyError
            if player.golpe2 == player.golpe1:
                raise KeyError
        except KeyError:
            print('Opção Inválida.')
        else:
            confirma2 = True

    confirma3 = False
    while not confirma3:
        try:
            player.golpe3 = lista_golpes[input('Golpe 3: ')]
            if not player.golpe3.move in player.golpes_liberados:
                raise KeyError
            if player.golpe3 == player.golpe2 or player.golpe3 == player.golpe1:
                raise KeyError
        except KeyError:
            print('Opção Inválida.')
        else:
            confirma3 = True

    confirma4 = False
    while not confirma4:
        try:
            player.golpe4 = lista_golpes[input('Golpe 4: ')]
            if not player.golpe4.move in player.golpes_liberados:
                raise KeyError
            if player.golpe4 == player.golpe3 or player.golpe4 == player.golpe2 or player.golpe4 == player.golpe1:
                raise KeyError
        except KeyError:
            print('Opção Inválida.')
        else:
            confirma4 = True
    
    print('')

    return player
