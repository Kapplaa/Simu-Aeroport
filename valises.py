import core
import random

def initialiser_valises():
    core.memory("valises", [])

def creer_valise():
    position_x = core.memory("tapis_position")[0]
    position_y = core.memory("tapis_position")[1]
    couleur = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
    taille = random.randint(30, 50)
    orientation = random.randint(0, 360)

    valise = {
        "couleur": couleur,
        "taille": taille,
        "orientation": orientation,
        "position": [position_x, position_y]
    }

    valises = core.memory("valises")
    valises.append(valise)
    core.memory("valises", valises)

def creer_nouvelles_valises(intervale=100):
    if len(core.memory("valises")) < 5 or core.memory("compteur_creation") % intervale == 0:
        creer_valise()
    core.memory("compteur_creation", core.memory("compteur_creation") + 1)

def dessiner_valises():
    valises = core.memory("valises")
    for valise in valises:
        couleur = valise["couleur"]
        taille = valise["taille"]
        position = valise["position"]
        core.Draw.rect(couleur, (position[0], position[1], taille, taille))

def deplacer_valises(vitesse):
    if core.memory("marche") == 1:
        valises = core.memory("valises")
        nouvelles_valises = []

        for valise in valises:
            valise["position"][0] += vitesse
            if valise["position"][0] <= core.memory("WINDOW_SIZE")[0]:
                nouvelles_valises.append(valise)

        core.memory("valises", nouvelles_valises)
