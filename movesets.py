class MoveSet:
    def __init__(self, forme):
        self.forme = forme
        self.moveset = []

def import_moveset(dataset_ulr):
    file = open(dataset_ulr)
    # D = {Chave pokemon: Value :{chave lv: value move}}
    movesets = {}
    for moveset in file:
        linha = moveset.split(',')
        if not linha[0].isnumeric:
           continue
        golpes = {}
        for move in linha[3:]:
            golpe = move.split(' , ') # Ex.: L3 - Growl -> golpe[0] = L3 e golpe[1] = Growl, logo golpe[0] = quando aprende e golpe[1] = golpe. eu quero chamar pelo nome do golpe
            if not move.isalnum:
                continue
            golpes[golpe[1]] = golpe[0]
        movesets[linha[2]] = golpes
    return movesets
