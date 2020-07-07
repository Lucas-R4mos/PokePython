class MoveSet:
    def __init__(self, forme, golpes_possiveis):
        self.forme = forme
        self.golpes_possiveis = golpes_possiveis

def isvazio(campo):
    if campo == '':
        return True
    else:
        return False

def import_moveset(dataset_ulr):
    from movesets import isvazio
    file = open(dataset_ulr)
    movesets = {}
    for poke in file:
        linha = poke.split(',')
        if not linha[0].isnumeric:
           continue
        golpes = []
        for golpe in linha[3:]:
            if isvazio(golpe):
                continue
            linha_golpe = golpe.split(' - ')
            golpes.append(
                {
                    'move' : linha_golpe[-1],
                    'aprende' : linha_golpe[0]
                }
            )
        moveset = MoveSet(linha[2], golpes)
        movesets[linha[2]] = moveset
    return movesets