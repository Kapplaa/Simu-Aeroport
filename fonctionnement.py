import core

def initialiser_motifs(nombre_motifs):
    largeur_motif = core.memory("tapis_largeur") // nombre_motifs
    motifs = [(core.memory("tapis_position")[0] + i * largeur_motif, core.memory("tapis_position")[1]) for i in range(nombre_motifs)]
    core.memory("motifs", motifs)

def dessiner_tapis_livraison():
    tapis_position = core.memory("tapis_position")
    tapis_largeur = core.memory("tapis_largeur")
    tapis_hauteur = core.memory("tapis_hauteur")
    core.Draw.rect((150, 150, 150), (tapis_position[0], tapis_position[1], tapis_largeur, tapis_hauteur))
    
    motifs = core.memory("motifs")
    for motif_position in motifs:
        core.Draw.rect((0, 0, 0), (motif_position[0], motif_position[1], 5, tapis_hauteur))

def dessiner_bouton_marche():
    couleur = (0, 255, 0) if core.memory("marche") == 1 else (255, 0, 0)
    position = core.memory("bouton_marche_position")
    largeur = core.memory("bouton_marche_largeur")
    hauteur = core.memory("bouton_marche_hauteur")
    core.Draw.rect(couleur, (position[0], position[1], largeur, hauteur))

def detecter_clic_bouton_marche():
    clic = core.getMouseLeftClick()
    if clic:
        x, y = clic
        position = core.memory("bouton_marche_position")
        largeur = core.memory("bouton_marche_largeur")
        hauteur = core.memory("bouton_marche_hauteur")
        
        if position[0] <= x <= position[0] + largeur and position[1] <= y <= position[1] + hauteur:
            core.memory("marche", 1 - core.memory("marche"))

def deplacer_motifs(distance):
    if core.memory("marche") == 1:
        motifs = core.memory("motifs")
        nouvelle_position = []
        for motif in motifs:
            nouvelle_position.append((motif[0] + distance, motif[1]))
            if nouvelle_position[-1][0] > core.memory("WINDOW_SIZE")[0]:
                nouvelle_position[-1] = (core.memory("tapis_position")[0], motif[1])
        core.memory("motifs", nouvelle_position)
