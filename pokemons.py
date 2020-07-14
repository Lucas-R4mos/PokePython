class Pokemon:
    def __init__(self, id, species, forme, type1, type2, sex = None, level = None):
        self.id = id
        self.species = species
        self.forme = forme
        self.type1 = type1
        self.type2 = type2
        
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

# Cabeçalho da tabela pokemon.csv:
# id,ndex,species,forme,type1,type2,ability1,ability2,abilityH,hp,attack,defense,spattack,spdefense,speed,total,weight,height,dex1,dex2,class,percent-male,percent-female,pre-evolution,egg-group1,egg-group2
