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
        print(lista_golpes[golpe].move + ' (' + lista_golpes[golpe].type + ') -> Power: '+ lista_golpes[golpe].power + '/ Accuracy: ' + lista_golpes[golpe].accuracy)

    print('')
    print('Escolha entre os golpes listados: ')

    confirmatry1 = False
    while not confirmatry1:
        try:
            confirma1 = False
            while not confirma1:
                player.golpe1 = lista_golpes[input('Golpe 1: ')]
                if player.golpe1.move in player.golpes_liberados:
                    confirma1 = True
                else:
                    print('Opção inválida.')
        except KeyError:
            print('Opção Inválida.')
        else:
            confirmatry1 = True

    confirmatry2 = False
    while not confirmatry2:
        try:
            confirma2 = False
            while not confirma2:
                player.golpe2 = lista_golpes[input('Golpe 2: ')]
                if player.golpe2.move in player.golpes_liberados:
                    confirma2 = True
                else:
                    print('Opção inválida.')
        except KeyError:
            print('Opção Inválida.')
        else:
            confirmatry2 = True

    confirmatry3 = False
    while not confirmatry3:
        try:
            confirma3 = False
            while not confirma3:
                player.golpe3 = lista_golpes[input('Golpe 3: ')]
                if player.golpe3.move in player.golpes_liberados:
                    confirma3 = True
                else:
                    print('Opção inválida.')
        except KeyError:
            print('Opção Inválida.')    
        else:
            confirmatry3 = True

    confirmatry4 = False
    while not confirmatry4:
        try:
            confirma4 = False
            while not confirma4:
                player.golpe4 = lista_golpes[input('Golpe 4: ')]
                if player.golpe4.move in player.golpes_liberados:
                    confirma4 = True
                else:
                    print('Opção inválida.')
        except KeyError:
            print('Opção Inválida.')
        else:
            confirmatry4 = True

    return player
