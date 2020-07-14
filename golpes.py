class Golpe:
    def __init__(self, id, move, description, type, category, power, accuracy, pp, priority, crit):
        self.id = id
        self.move = move
        self.description = description
        self.type = type
        self.category = category
        self.power = power
        self.accuracy = accuracy
        self.pp = pp
        self.priority = priority
        self.crit = crit

def import_golpe(dataset_ulr):
    file = open(dataset_ulr)
    golpes = {}
    for golpe in file:
        linha = golpe.split('|')
        if not linha[0].isnumeric:
            continue
        try:
            golpe = Golpe(linha[0], linha[1], linha[2], linha[3], linha[4], int(linha[5]), linha[6], int(linha[7]), linha[9], linha[10])
        except ValueError:
            linha[5] = 0
        else:
            linha[5] = int(linha[5])
        golpes[linha[1]] = golpe
    return golpes

# Cabeçalho da tabela moves.csv:
# id|move|description|type|category|power|accuracy|pp|z-effect|priority|crit
