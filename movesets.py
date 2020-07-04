class MoveSet:
    def __init__(self, forme):
        self.forme = forme
        self.moveset = []

def import_moveset(dataset_ulr):
    file = open(dataset_ulr)
    movesets = {}
    for moveset in file:
        linha = moveset.split(',')
        if not linha[0].isnumeric:
           continue
        moveset = MoveSet(linha[2])
        movesets[linha[2]] = moveset
        for move in linha[3:]:
            if move == '':
                continue
            moveset.moveset.append(move)
    return movesets