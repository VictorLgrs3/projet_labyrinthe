class Pile:

    def __init__(self):
        self.donnees = []

    def est_vide(self):
        return self.donnees == []

    def empile(self, x):
        self.donnees.append(x)

    def depile(self):
        assert(not(self.est_vide())), "pile vide"
        element_depile = self.donnees.pop()
        return element_depile

    def consulter_sommet(self):
        return self.donnees[-1]

    def __str__(self):
        res = ""
        for i in range(len(self.donnees)-1,0,-1):
            res = res + str(self.donnees[i]) + "\n"
        res = res + str(self.donnees[0])
        return res
