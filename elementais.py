def multiplicador_elemento(elemento_def1, elemento_def2, elemento_atk):
    file = open('type-chart.csv')
    multiplicador_elemento = 1
    elemento_atk = elemento_atk.lower()
    for line in file:
        casa = line.split(',')
        if not casa[0] == elemento_def1.lower() and casa[1] == elemento_def2.lower():
            continue
        if elemento_atk == 'normal':
            multiplicador_elemento = casa[2]
        if elemento_atk == 'fire':
            multiplicador_elemento = casa[3]
        if elemento_atk == 'water':
            multiplicador_elemento = casa[4]
        if elemento_atk == 'electric':
            multiplicador_elemento = casa[5]
        if elemento_atk == 'grass':
            multiplicador_elemento = casa[6]
        if elemento_atk == 'ice':
            multiplicador_elemento = casa[7]
        if elemento_atk == 'fighting':
            multiplicador_elemento = casa[8]
        if elemento_atk == 'poison':
            multiplicador_elemento = casa[9]
        if elemento_atk == 'ground':
            multiplicador_elemento = casa[10]
        if elemento_atk == 'flying':
            multiplicador_elemento = casa[11]
        if elemento_atk == 'psychic':
            multiplicador_elemento = casa[12]
        if elemento_atk == 'bug':
            multiplicador_elemento = casa[13]
        if elemento_atk == 'rock':
            multiplicador_elemento = casa[14]
        if elemento_atk == 'ghost':
            multiplicador_elemento = casa[15]
        if elemento_atk == 'dragon':
            multiplicador_elemento = casa[16]
        if elemento_atk == 'dark':
            multiplicador_elemento = casa[17]
        if elemento_atk == 'steel':
            multiplicador_elemento = casa[18]
        if elemento_atk == 'fairy':
            multiplicador_elemento = casa[19]
    multiplicador_elemento = float(multiplicador_elemento)
    return multiplicador_elemento