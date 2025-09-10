# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 16:19:48 2023

@author: pouni02
"""

# Création d'une interface graphique par l'utilisation de l'utilitaire Transformation
import sys
#from PySide6.QtWidgets import * # Problèmes avec la version 6 sur l'ordi perso
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
import re # Bibliothèque pour supprimer un caractère présent dans un élément d'une liste --> re.sub()
import numpy as np
import math 
import statistics

#QLabel sert à afficher du texte non éditable 
#QSpinBox : créer un champ nombre incrémentable
#QComboBox : menu déroulant
#QCheckBox : Case à cocher
#QSlider : Slider
#QListeWidget : Liste d'éléments


from WidgetsGM import WidgetSelectionFichiers # La bibliothèque que l'on avait utilisée en cours 

class  MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        
        # Définition du titre de la fenêtre
        self.setWindowTitle("Transformation")
        
        # On va créer un widget de formulaire, l'utilisateur pourra taper son nom, on a crée un formulaire, champ de texte
        
        self.selection_fichiers = WidgetSelectionFichiers()
        
        # Ajout des widgets
        
        # Dimensions de la plaque 
        
        # Dimension des X
        
        label_Xdim = QLabel("X Dimension (en mm)") # L'utilisateur renseigne la dimension de la plaque selon x em mm
        self.Xdim = QDoubleSpinBox() # QDoubleSpinBox au lieu de QSpinBox pour avoir des valeurs en float
        self.Xdim.setMinimum(float(500)) # On fixe la dimension minimum selon x de la plaque à 500mm car trop petite sinon (une plaque de côté 50 cm est réaliste)
        self.Xdim.setMaximum(float("inf")) # On fixe la valeur maximale selon x  à + l'infini pour permettre à l'utilisateur de rentrer les valeurs qu'il veut 
        
        # Dimension des Y
        
        label_Ydim = QLabel("Y Dimension (en mm)") # L'utilisateur renseigne la dimension de la plaque selon y em mm
        self.Ydim = QDoubleSpinBox() # QDoubleSpinBox au lieu de QSpinBox pour avoir des valeurs en float
        self.Ydim.setMinimum(float(500)) # On fixe la dimension minimum selon y de la plaque à 500mm car trop petite sinon (une plaque de côté 50 cm est réaliste)
        self.Ydim.setMaximum(float("inf")) # On fixe la valeur maximale selon y à + l'infini pour permettre à l'utilisateur de rentrer les valeurs qu'il veut 
        
        # Opérations
        
        # Rotation autour de Z
        
        label_Rotation = QLabel("Rotation angle (deg)") # Création d'un champ Rotation
        self.Rotation = QComboBox() # Liste déroulante
        self.Rotation.addItems([' ','90','-90','180']) # Les différents choix d'angle possibles : ' ' signifie pas de rotation souhaitée
        
        # Translation selon X
        
        label_Xtranslat = QLabel("X Translation (en mm)") # Création d'un champ Translation selon X
        self.Xtranslat = QDoubleSpinBox() # Champ pour rentrer la valeur (float)
        self.Xtranslat.setMaximum(float("inf")) # On fixe la valeur maximale selon x à + l'infini pour permettre à l'utilisateur de rentrer les valeurs qu'il veut (en cas d'erreur, il y aura un message d'erreur pour le guider)
        
        # Translation selon Y
        label_Ytranslat = QLabel("Y Translation (en mm)") # Création d'un champ Translation selon Y
        self.Ytranslat = QDoubleSpinBox() # Champ pour rentrer la valeur (float)
        self.Ytranslat.setMaximum(float("inf")) # On fixe la valeur maximale selon y à + l'infini pour permettre à l'utilisateur de rentrer les valeurs qu'il veut (en cas d'erreur, il y aura un message d'erreur pour le guider)
        
        # On crée un bouton pour générer le nouveau fichier
        self.button = QPushButton("Générer fichier(s)")
        
        # Création d'un groupe de widgets
        groupe1 = QGroupBox("Stock Surface") # Ce widget correspond aux données de la plaque
        
        # Création d'une disposition en grille
        grille1 = QGridLayout()
        
        grille1.addWidget(label_Xdim, 1, 1) # Affichage du champ "X dimension (em mm)"
        grille1.addWidget(self.Xdim, 1, 2) # Affichage du champ pour rentrer les valeurs
        grille1.addWidget(label_Ydim, 2, 1) # Affichage du champ "Y dimension (en mm)"
        grille1.addWidget(self.Ydim, 2, 2) # Affichage du champ pour rentrer les valeurs
        
        
        # On définit la grille 1 comme disposition du groupe1
        groupe1.setLayout(grille1)

##############################################################################       
        # Création d'un deuxième groupe de widgets
        groupe2 = QGroupBox("Rotation")
        
        # Création d'une deuxième disposition en grille
        grille2 = QGridLayout()
        
        grille2.addWidget(label_Rotation, 1, 1)
        grille2.addWidget(self.Rotation, 1, 2)
        
        
        # On définit la grille 2 comme disposition du groupe2
        groupe2.setLayout(grille2)
##############################################################################
        # Création d'un troisième groupe de widgets
        groupe3 = QGroupBox("Translation")
        
        # Création d'une troisième disposition en grille
        grille3 = QGridLayout()
        
        grille3.addWidget(label_Xtranslat, 1, 1)
        grille3.addWidget(self.Xtranslat, 1, 2)
        grille3.addWidget(label_Ytranslat, 2, 1)
        grille3.addWidget(self.Ytranslat, 2, 2)
        
        # On définit la grille 3 comme disposition du groupe2
        groupe3.setLayout(grille3) 

##############################################################################

        # qvBox layout : les éléments vont se mettre les uns en dessous des autres : V pour vertical, QHbox : pour horizontalement : à côté des autres
        #layout : c'est pour dire comment on va les disposer
        
        # Création d'une disposition verticale QVBox
        
        layout = QVBoxLayout() # Rester sur une disposition verticale
        layout.addWidget(self.selection_fichiers)# Ici on ajoute le code WidgetGM dans notre code, dans notre layout vertical
        # Le premier élément visible sur l'interface en partant du haut sera la sélection de fichiers
        layout.addWidget(groupe1) # En 2ème position : les données de la plaque
        layout.addWidget(groupe2) # En 3ème position : la rotation
        layout.addWidget(groupe3) # En 4ème position : les translations
        layout.addWidget(self.button)# ici on rajoute dans notre layout vertical le bouton définit précédemment : pour générer les fichiers
        
        # Créer un widget central dans lequel on va tout mettre, et lui dire que je veux que la disposition soit égale à layout
        central_widget=QWidget()
        central_widget.setLayout(layout)
        
        self.setCentralWidget(central_widget)
        
        # Maintenant on va lier le bouton à une fonction
        
        self.button.clicked.connect(self.Transformation) # En cliquant sur le bouton "Générer fichier(s)", ce dernier sera lié à la fonction Transformation et le programme effectura les calculs
        
    #   +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        
     # Voici le programme pour transformer des fichiers
         
    def Transformation(self):
        file_dialog=QFileDialog(self)# En cliquant sur le bouton transformer : une fenêtre enregistrer sous apparaît
        
        # Pour chaque fichier que l'on a choisit dans la base de données, on va les ouvrir en mode lecture
        
        for chemin_fichier in self.selection_fichiers.listeFichiers(): 
                fichier=open(chemin_fichier, "r") 
                
                # Dans un premier temps, on va trouver les max des coordonnées x et y
                
                # Une liste vide qui va contenir les coordonnées 
                self.coordonnees = [] 
                self.liste = [] # Liste qui va nous permettre de convertir les str en int
                # Pour un fichier donné, on parcourt chaque ligne 
                for  ligne in fichier : 
                    if ligne[0]=='Z':# Si la ligne commence par un Z 
                        # self.liste=ligne.split(",") # On va ajouter les coordonnées dans une liste : les coordonnées sont séparées par une virgule
                        # for self.num in self.liste: # On parcourt cette liste de coordonnées
                            # Cette méthode ne marche pas pour trouver les max
                            # dernier = self.liste[-1]       #le dernier element de la liste contient un espace (le point virgule ;)
                            # nouveau = re.sub(r';','',dernier) #cette chaine de caractere contient le dernier element de la liste valeurs mais sans le point virgule
                            # del(self.liste[-1])                  #on supprime le dernier element de la liste
                            # self.liste.append(nouveau)           #on le remplace par ce meme element sans le point virgule
                            # premier = self.liste[0]
                            # nouveau2 = re.sub(r'Z','',premier)
                            # del(self.liste[0])
                            # self.liste.insert(0,nouveau2)
                        self.sup_Zp = ligne.strip('Z;') # On supprime les caractères 'Z' et ';' présents dans les coordonnées
                        self.coordonnee = self.sup_Zp.split(',') # On va ajouter les coordonnées dans une liste, séparées par une virgule
                        # ça n'a pas supprimé le ; mais ça a ajouté un \n
                        dernier = self.coordonnee[2] # On prend la coordonnée selon z
                        dernier = dernier.strip(';\n') # On supprime le point virgule et le retour à la ligne
                        del(self.coordonnee[2]) # On supprime la coordonnée selon z de base de la liste contenant les coordonnées
                        self.coordonnee.append(dernier) # On ajoute la nouvelle coordonnée z sans le ; et le \n
                        self.liste = [int(coord) for coord in self.coordonnee] # Conversion des str en int
                        self.coordonnees.append(self.liste) # Liste de liste contenant les coordonnées de chaque ligne
        self.coord_x = [coord[0] for coord in self.coordonnees] # Liste des X
        self.coord_y = [coord[1] for coord in self.coordonnees] # Liste des Y
        self.coord_z = [coord[2] for coord in self.coordonnees] # Liste des Z
        self.max_x = max(self.coord_x) # Le plus grand x
        self.max_y = max(self.coord_y) # le plus grand y
        
        # On a trouvé xmax et ymax
        
        # On va maintenant passer au programme qui va effectuer les changements en fonction des choix de l'utilisateur
        
        # Seuil de la translation à respecter : 
        
        # On fait l'hypothèse que l'on ne pourra pas faire une translation supérieure aux 9/10 de la dimension de la plaque
        self.X_norm = self.Xdim.value()*0.9
        self.Y_norm = self.Ydim.value()*0.9
        self.translat_x_norm = self.max_x + self.Xtranslat.value() # La translation selon x + le max x pour voir si ça dépasse pas les 90% de la plaque
        self.translat_y_norm = self.max_y + self.Ytranslat.value() # La translation selon y + le max y pour voir si ça dépasse pas les 90% de la plaque
        
        if(self.translat_x_norm>=self.X_norm or self.translat_y_norm>=self.Y_norm): # Si la condition n'est pas respectée
            # Il y a un message d'erreur qui apparaît
            msg_box = QMessageBox() # Boîte de dialogue
            # Le type de cette boîte de dialogue est une erreur et non une information (cf plus bas lors de la transformation du fichier : "Fichiers transformés")
            # Le message d'erreur est explicite et va guider l'utilisateur sur les conditions à respecter
            # Pour cela, il lui donnera les intervalles à respecter pour être dans les normes 
            msg_box.critical(self, "Erreur", "Pour éviter de dépasser les dimensions de la plaque, vous ne pouvez effectuer que des translations ne dépassant pas les 9/10 (90 %) de la plaque.\n\nVeuillez rentrer une valeur valide comprise entre 0 et {} pour la translation en X et entre 0 et {} pour la translation en Y ! ".format(self.X_norm,self.Y_norm))
            # Ajout du bouton "OK"
            ok_button = QPushButton("OK")
            msg_box.addButton(ok_button, QMessageBox.AcceptRole) # En cliquant sur le bouton OK, ça ferme la boite de dialogue

        # Si l'utilisateur ne s'est pas trompé : la condition est respectée
        
        # On passe à l'exécution du programme : calculs/ opérations de rotation et/ou translation...
        
        else:
            output_file_name = file_dialog.getSaveFileName()[0] # Le nom que l'on va donner à ce nouveau fichier
            
            output_file = open(output_file_name, "w")# On va ouvrir ce nouveau fichier, pour le transformer
            # On veut récupérer le chemin du fichier
            for chemin_fichier in self.selection_fichiers.listeFichiers(): # pour chaque fichier que l'on a choisit dans la base de données, on va les ouvrir en mode lecture
                fichier=open(chemin_fichier, "r") # maintenant il faut lire ligne/ligne le fichier, donc créer une nouvelle boucle dans la boucle actuelle pour parcourir le fichier, pour chaque ligne dans le fichier:
                
                # self.liste = [] 
                # self.coordonnees = [] 
                self.valeurs_modif = [] # La liste qui va contenir les coordonnées modifiées après rotation et/ou translation 
                
                # On peut maintenant passer aux opérations de rotation et de translation : 
                
                # Pour un fichier donné, on parcourt chaque ligne 
                for  ligne in fichier : 
                    if ligne[0]=='Z':# Si la ligne commence par un Z on agit sur celle-ci 
                        self.liste=ligne.split(",") # On va mettre les coordonnées dans une liste : les coordonnées sont séparées par une virgule
                        for self.num in self.liste: # On parcourt cette liste
                            dernier = self.liste[-1]       # Le dernier element de la liste contient un point virgule ;
                            nouveau = re.sub(r';','',dernier) # Cette chaine de caractere contient le dernier element de la liste valeurs mais sans le point virgule
                            del(self.liste[-1])                  # On supprime le dernier element de la liste
                            self.liste.append(nouveau)           # On le remplace par ce meme element sans le point virgule
                            premier = self.liste[0] # Le premier élément de la liste contient un Z
                            nouveau2 = re.sub(r'Z','',premier) # Cette chaine de caractère contient le premier élement de la liste mais sans le Z
                            del(self.liste[0]) # On supprime le premier élément de la liste
                            self.liste.insert(0,nouveau2) # On le remplace par ce même élement mais sans le Z : on va préciser la position (ici 0) pour l'insérer en tête de liste
                            self.a = int(self.liste[0]) # Elément zero de la liste en int
                            self.b = int(self.liste[1]) # Elément 1 de la liste en int
                            self.c = int(self.liste[2]) # Elément 2 de la liste en int
                            if(self.Rotation.currentText() == ' '): # Si l'utilisateur ne souhaite pas effectuer de rotation 
                                self.a += self.Xtranslat.value() # On ajoute la translation selon x
                                self.b += self.Ytranslat.value() # On ajoute la translation selon y
                                # On va convertir les élement de la liste en str
                                self.a = str(self.a)
                                self.b = str(self.b)
                                self.c = str(self.c)
                                self.a = 'Z' + self.a # On rajoute le Z au premier élement de la liste
                                self.c = self.c + ';' # On rajoute le ; au dernier élément de la liste
                                # On ajoute les nouvelles coordonnées après modification à la nouvelle liste qui s'appelle valeurs_modif
                                self.valeurs_modif.append(self.a) 
                                self.valeurs_modif.append(self.b)
                                self.valeurs_modif.append(self.c)
                                # On convertit les élements de la liste en chaine de caractères
                                # Pour cela, on parcourt la nouvelle liste et on ajoute chaque élement à une nouvelle chaine de caractère
                                # Et on sépare chaque élement par une virgule
                                self.chaine = ','.join([d for d in self.valeurs_modif])
                                # self.str2 = self.chaine[:-1] #car on a une virgule à la fin de la ligne (après le ;) --> on prend la ligne sans la virgule à la fin
                                output_file.write(self.chaine)# Dans le nouveau fichier, on insert la ligne correspondant à la ligne de référence modifiée
                                output_file.write('\n') # On va à la ligne pour copier la ligne suivante
                                self.valeurs_modif = [] # On va réinitialiser la nouvelle liste pour qu'elle prenne les valeurs de la ligne suivante
                            
                            elif(self.Rotation.currentText() == '90'): # Si l'utilisateur choisit une rotation de 90°
                                self.r1 = self.b # La coordonnée x devient y
                                self.r2 = -self.a # La coordonnée y devient -x
                                self.r3 = self.c # z = z
                                self.r1 += self.Xtranslat.value() # On ajoute la translation selon x si l'utilsateur le veut
                                # On ajoute la translation selon y si l'utilisateur le veut
                                # On va en plus ajouter xmax afin d'avoir la pièce rotatée dans le cadre
                                # Sinon, la pièce rotatée sera dans les y négatifs
                                self.r2 += self.Ytranslat.value() + self.max_x 
                                # On va d'abord convetir les nouvelles coordonnées (qui sont en float) en int
                                self.r1 = int(self.r1)
                                self.r2 = int(self.r2)
                                self.r3 = int(self.r3)
                                # Puis on les convertit en str
                                self.r1 = str(self.r1)
                                self.r2 = str(self.r2)
                                self.r3 = str(self.r3)
                                self.r1 = 'Z' + self.r1 # On rajoute le Z à la première coordonnée
                                self.r3 = self.r3 + ';' # On rajoute le ; à la dernière coordonnée
                                # On ajoute les nouvelles coordonnées après modification à la nouvelle liste qui s'appelle valeurs_modif
                                self.valeurs_modif.append(self.r1)
                                self.valeurs_modif.append(self.r2)
                                self.valeurs_modif.append(self.r3)
                                # On convertit les élements de la liste en chaine de caractères
                                # Pour cela, on parcourt la nouvelle liste et on ajoute chaque élement à une nouvelle chaine de caractère
                                # Et on sépare chaque élement par une virgule
                                self.chaine = ','.join([d for d in self.valeurs_modif])
                                # self.str2 = self.chaine[:-1] #car on a une virgule à la fin de la ligne (après le ;) --> on prend la ligne sans la virgule à la fin
                                output_file.write(self.chaine) # Dans le nouveau fichier, on insert la ligne correspondant à la ligne de référence modifiée
                                output_file.write('\n') # On va à la ligne pour copier la ligne suivante
                                self.valeurs_modif = [] # On va réinitialiser la nouvelle liste pour qu'elle prenne les valeurs de la ligne suivante
                                
                            elif(self.Rotation.currentText() == '-90'): #Si l'utilisateur choisit une rotation de -90°
                                self.r1 = -self.b # La coordonnée x devient -y
                                self.r2 = self.a # La coordonnée y devient x
                                self.r3 = self.c # z = z
                                # On ajoute la translation selon x si l'utilisateur le veut
                                # On va en plus ajouter ymax afin d'avoir la pièce rotatée dans le cadre
                                # Sinon, la pièce rotatée sera dans les x négatifs
                                self.r1 += self.Xtranslat.value() + self.max_y
                                self.r2 += self.Ytranslat.value() # On ajoute la translation selon y si l'utilsateur le veut
                                # On va d'abord convetir les nouvelles coordonnées (qui sont en float) en int
                                self.r1 = int(self.r1)
                                self.r2 = int(self.r2)
                                self.r3 = int(self.r3)
                                # Puis on les convertit en str
                                self.r1 = str(self.r1)
                                self.r2 = str(self.r2)
                                self.r3 = str(self.r3)
                                self.r1 = 'Z' + self.r1 # On rajoute le Z à la première coordonnée
                                self.r3 = self.r3 + ';' # On rajoute le ; à la dernière coordonnée
                                # On ajoute les nouvelles coordonnées après modification à la nouvelle liste qui s'appelle valeurs_modif
                                self.valeurs_modif.append(self.r1)
                                self.valeurs_modif.append(self.r2)
                                self.valeurs_modif.append(self.r3)
                                # On convertit les élements de la liste en chaine de caractères
                                # Pour cela, on parcourt la nouvelle liste et on ajoute chaque élement à une nouvelle chaine de caractère
                                # Et on sépare chaque élement par une virgule
                                self.chaine = ','.join([d for d in self.valeurs_modif])
                                # self.str2 = self.chaine[:-1] #car on a une virgule à la fin de la ligne (après le ;) --> on prend la ligne sans la virgule à la fin
                                output_file.write(self.chaine) # Dans le nouveau fichier, on insert la ligne correspondant à la ligne de référence modifiée
                                output_file.write('\n') # On va à la ligne pour copier la ligne suivante
                                self.valeurs_modif = [] # On va réinitialiser la nouvelle liste pour qu'elle prenne les valeurs de la ligne suivante
                                
                            elif(self.Rotation.currentText() == '180'): # Si l'utilisateur choisit une rotation de 180°
                                self.r1 = -self.a # La coordonnée x devient -x
                                self.r2 = -self.b # La coordonnée y devient -y
                                self.r3 = self.c # z = z
                                # On ajoute la translation selon x et/ou y si l'utilisateur le veut
                                # On va en plus ajouter xmax et ymax afin d'avoir la pièce rotatée dans le cadre
                                # Sinon, la pièce rotatée sera dans les x et y négatifs
                                self.r1 += self.Xtranslat.value() + self.max_x
                                self.r2 += self.Ytranslat.value() + self.max_y
                                # On va d'abord convetir les nouvelles coordonnées (qui sont en float) en int
                                self.r1 = int(self.r1)
                                self.r2 = int(self.r2)
                                self.r3 = int(self.r3)
                                # Puis on les convertit en str
                                self.r1 = str(self.r1)
                                self.r2 = str(self.r2)
                                self.r3 = str(self.r3)
                                self.r1 = 'Z' + self.r1 # On rajoute le Z à la première coordonnée
                                self.r3 = self.r3 + ';' # On rajoute le ; à la dernière coordonnée
                                # On ajoute les nouvelles coordonnées après modification à la nouvelle liste qui s'appelle valeurs_modif
                                self.valeurs_modif.append(self.r1)
                                self.valeurs_modif.append(self.r2)
                                self.valeurs_modif.append(self.r3)
                                # On convertit les élements de la liste en chaine de caractères
                                # Pour cela, on parcourt la nouvelle liste et on ajoute chaque élement à une nouvelle chaine de caractère
                                # Et on sépare chaque élement par une virgule
                                self.chaine = ','.join([d for d in self.valeurs_modif])
                                # self.str2 = self.chaine[:-1] #car on a une virgule à la fin de la ligne (après le ;) --> on prend la ligne sans la virgule à la fin
                                output_file.write(self.chaine) # Dans le nouveau fichier, on insert la ligne correspondant à la ligne de référence modifiée
                                output_file.write('\n') # On va à la ligne pour copier la ligne suivante
                                self.valeurs_modif = [] # On va réinitialiser la nouvelle liste pour qu'elle prenne les valeurs de la ligne suivante

                
                # On ferme le fichier:
                fichier.close() # Ici on parle de chaque fichier ouvert et que l'on parcourt
                output_file.write("\n")             # Pour aller à la ligne
        
            output_file.close() # Ici on parle de notre fichier de sortie, dans lequel on a tous les autres fichiers, et que l'on souhaite fermer à présent, après avoir terminé l'écriture
            # Le programme a copié tous les fichiers dans le fichier transformation et il a fermé le fichier transformation
        
            
            
            
            # Ouvrir une fenêtre avec un message (de type information)
            QMessageBox.information(self, "Information", "Fichiers transformés ! ") # Cette fenêtre nous indique que les fichiers ont bien été transformés
        
    
if __name__ == '__main__':
    # Create the Qt Application
    app= QApplication(sys.argv)
    
    # Create and show the form
    window=MainWindow()
    window.show()
    
    # Run the main Qt loop
    sys.exit(app.exec())

    
