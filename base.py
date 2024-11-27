import core
from fonctionnement import *
import valises

def setup():
    core.memory("WINDOW_SIZE", [800, 600])
    core.memory("fps", 60)
    core.WINDOW_SIZE = core.memory("WINDOW_SIZE")
    core.fps = core.memory("fps")

    core.memory("tapis_largeur", core.memory("WINDOW_SIZE")[0])
    core.memory("tapis_hauteur", 50)
    core.memory("tapis_position", [0, core.memory("WINDOW_SIZE")[1] // 2])
    core.memory("bouton_marche_position", [core.memory("WINDOW_SIZE")[0] - 100, 10])
    core.memory("bouton_marche_largeur", 80)
    core.memory("bouton_marche_hauteur", 40)
    core.memory("marche", 0)
    core.memory("compteur_creation", 0)

    initialiser_motifs(10)
    valises.initialiser_valises()

def run():
    detecter_clic_bouton_marche()
    dessiner_tapis_livraison()
    dessiner_bouton_marche()
    deplacer_motifs(5)

    valises.creer_nouvelles_valises(intervale=50)
    valises.dessiner_valises()
    valises.deplacer_valises(5)

core.main(setup, run)
