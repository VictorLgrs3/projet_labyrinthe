

def voisins(lab, case):
    cases_voisins = []
    # La case à gauche de la case de départ
    try:
        if lab[case[0]][case[1] - 1] == 1:
            cases_voisins.append((case[0], case[1] - 1))
    except IndexError:
        pass
    # La case en bas de la case de départ
    try:
        if lab[case[0] + 1][case[1]] == 1:
            cases_voisins.append((case[0] + 1, case[1]))
    except IndexError:
        pass
    # La case à droite de la case de départ
    try:
        if lab[case[0]][case[1] + 1] == 1:
            cases_voisins.append((case[0], case[1] + 1))
    except IndexError:
        pass
    # La case en haut de la case de départ
    try:
        if lab[case[0] - 1][case[1]] == 1:
            cases_voisins.append((case[0] - 1, case[1]))
    except IndexError:
        pass
    return cases_voisins


if __name__ == '__main__':
    laby = [[0, 1, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 0],
            [0, 1, 0, 1, 0, 0],
            [0, 1, 0, 1, 1, 0],
            [0, 1, 1, 0, 1, 0],
            [0, 0, 0, 0, 1, 0]]



