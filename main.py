from copy import deepcopy
from pile import Pile
import matplotlib.pyplot as plt


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


def resolution(lab, entree, sortie):
    T = deepcopy(lab)
    case = entree
    T[case[0]][case[1]] = -1
    pile = Pile()
    vois = voisins(T, case)
    continuer = True

    while continuer:
        if len(vois) == 0:
            case = pile.depile()
            vois = voisins(T, case)
        else:
            pile.empile(case)
            case = vois[0]
            T[case[0]][case[1]] = -1
            vois = voisins(T, case)
        if pile.est_vide():
            continuer = False
        if case == sortie:
            pile.empile(case)
            continuer = False

    if pile.est_vide():
        return "Aucune solution"
    else:
        chemin = []
        while not pile.est_vide():
            chemin.append(pile.depile())
        return chemin


def affiche_solution(lab, entree, sortie):
    solution = resolution(lab, entree, sortie)
    T = deepcopy(lab)
    for i in solution:
        T[i[0]][i[1]] = 0.5
    plt.imshow(T, cmap="gray")
    plt.show()


if __name__ == '__main__':
    laby = [[0, 1, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 0],
            [0, 1, 0, 1, 0, 0],
            [0, 1, 0, 1, 1, 0],
            [0, 1, 1, 0, 1, 0],
            [0, 0, 0, 0, 1, 0]]

    affiche_solution(laby, (0, 1), (5, 4))



