choix = 0

class Joueur:

    def __init__(self, nom, vie, vitesse, inventaire):
        self.nom = nom
        self.vie = vie
        self.vitesse = vitesse
        self.inventaire = inventaire
        print("bienvenue au joueur : ", nom, "/ vie : ", vie, "/ vitesse : ", vitesse, "/ objet dans l'inventaire : ",
              inventaire)

    def get_nom(self):
        return self.nom

    def get_vie(self):
        return self.vie

joueur1 = Joueur("Jackson", 20, 5, ["sword"])
print("Joueur : ", joueur1.get_nom(), "/ vie : ", joueur1.get_vie())
class Monstre:

    def __init__(self, colere, type, force, vitesse):
        self.colere = colere
        self.type = type
        self.force = force
        self.vitesse = vitesse

    def get_colere(self):
        return self.colere

    def get_type(self):
        return self.type

    def get_force(self):
        return self.force

    def get_vitesse(self):
        return self.vitesse

    def combat(self, combat):
        self.colere -= combat
        print("oh, le monstre 1 a perdu ", combat, " de vie")


monstre1 = Monstre(10, "fire", 5, 4)
print("Monstre 1", "| vie : ", monstre1.colere, "/ type : ", monstre1.type, "/ force : ", monstre1.force, "/ vitesse : ", monstre1.vitesse)

monstre2 = Monstre(12, "ice", 10, 6)
print("Monstre 2", "| vie : ", monstre2.colere, "/ type : ", monstre2.type, "/ force : ", monstre2.force, "/ vitesse : ",monstre2.vitesse)

choix = int(input("Entrée (1) pour commencer le combat, (2) pour afficher l'inventaire, (3) pour se soigner, (4) pour quitter :"))
while choix != 4 :

    if choix == 1 :
        if monstre1.vitesse > monstre2.vitesse:
            monstre2.combat(1)
        else :
            monstre1.combat(1)
    print("vie monstre 1 :", monstre1.colere)
    print("vie monstre 2 :", monstre2.colere)
    choix = int(input("Entrée (1) pour commencer le combat, (2) pour afficher l'inventaire, (3) pour se soigner, (4) pour quitter :"))

    if choix == 2 :
        print("inventaire : ", joueur1.inventaire)
        choix = int(input("Entrée (1) pour commencer le combat, (2) pour afficher l'inventaire, (3) pour se soigner, (4) pour quitter :"))

    if choix == 3 :
        joueur1.vie = 20
        print("vie du joueur  à été soigner donc la vie du joueur est de : ", joueur1.vie)
        choix = int(input("Entrée (1) pour commencer le combat, (2) pour afficher l'inventaire, (3) pour se soigner, (4) pour quitter :"))




