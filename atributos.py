class Atributos:
    def __init__(self, forme, hp, attack, defense, spattack, spdefense, speed):
        self.forme = forme
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.spattack = spattack
        self.spdefense = spdefense
        self.speed = speed

def import_atributo(dataset_ulr):
    file = open(dataset_ulr)
    atributos = {}
    for linha in file:
        coluna = linha.split(',')
        if not coluna[0].isnumeric:
           continue
        atributo = Atributos(coluna[3], int(coluna[9]), int(coluna[10]), int(coluna[11]), int(coluna[12]), int(coluna[13]), int(coluna[14]))
        atributos[coluna[3]] = atributo
    return atributos

lista = import_atributo('pokemon.csv')