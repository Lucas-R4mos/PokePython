class Pokemon:
    def __init__(self, id, species, forme, type1, type2, sex = None, level = None):
        self.id = id
        self.species = species
        self.forme = forme
        self.type1 = type1
        self.type2 = type2
        self.moveset = []
        self.golpes = []
        self.golpe_usado = []

def import_pokemon(dataset_ulr):
    file = open(dataset_ulr)
    pokemons = {}
    for poke in file:
        linha = poke.split(',')
        if not linha[0].isnumeric:
           continue
        poke = Pokemon(linha[0], linha[2], linha[3], linha[4], linha[5]) 
        pokemons[linha[3]] = poke
    return pokemons