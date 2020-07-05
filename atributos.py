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
    for atributo in file:
        coluna = atributo.split(',')
        if not coluna[0].isnumeric:
           continue
        atributo = Atributos(coluna[3], coluna[9], coluna[10], coluna[11], coluna[12], coluna[13], coluna[14]) 
        atributos[coluna[3]] = atributo
    return atributos