class MoveSet:
    def __init__(self, forme):
        self.forme = forme
        self.golpes_possiveis = []

def import_moveset(dataset_ulr):
    file = open(dataset_ulr)
    # movesets = {Chave pokemon: Value :{chave lv: value move}}
    movesets = {}
    for moveset in file:
        linha = moveset.split(',')
        if not linha[0].isnumeric:
           continue
        moveset = MoveSet(linha[2]) #aqui eu tô dizendo que moveset é um objeto da classe MoveSet e que a forme dele é a linha[2]
        golpes = {}
        for move in linha[3:]:
            golpe = move.split(' , ') # Ex.: L3 - Growl -> golpe[0] = L3 e golpe[1] = Growl, logo golpe[0] = quando aprende e golpe[1] = golpe. eu quero chamar pelo nome do golpe
            movetitle = move.title()
            if not movetitle.istitle: #eu tenho L3 - Growl, que já é title, porém para o caso de ORAS - Algumgolpe, a função title acusa False. então eu começo criando a função movetitle pra já deixar o texto escrito em title e só filtrar as colunas vazias.
                continue
            golpes[golpe[1]] = golpe[0]
        moveset.golpes_possiveis = golpes
    return movesets
