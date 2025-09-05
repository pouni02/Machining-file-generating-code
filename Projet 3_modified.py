# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 16:19:48 2023

@author: NADARADJANE Pounida - DUPRAT Robin GM4B
"""

# création d'une interface graphique par l'utilisation de l'utilitaire Transformation : Essai
import sys
#from PySide6.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
# import WidgetsGM
import re
import numpy as np

#QLabel sert à afficher du texte non éditable 
#QSpinBox : créer un champ nombre incrémentable
#QComboBox : menu déroulant
#QCheckBox : Case à cocher
#QSlider : Slider
#QListeWidget : Liste d'éléments


from WidgetsGM import WidgetSelectionFichiers


# class AnotherWindow(QWidget):
#     """
#     This "window" is a QWidget. If it has no parent, it
#     will appear as a free-floating window as we want.
#     """
#     def __init__(self):
#         super().__init__()
#         layout = QVBoxLayout()
#         self.label = QLabel("Another Window")
#         layout.addWidget(self.label)
#         self.setLayout(layout)

class  MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        
        #Définition du titre de la fenêtre
        self.setWindowTitle("Transformation")
        
        # on va commencer à créer des blocs, un widget : élément de texte, un bouton
        # self définit un element qui, def l'étendue de la variable, des objets que seule la fonction peut y accéder, restreindre l'utilisation de l'objet à la variable
        # on va créer un widget de formulaire, l'utilisateur pourra taper son nom, on a crée un formulaire, champ de texte
        
        self.selection_fichiers = WidgetSelectionFichiers()
        
        # Ajout des widgets
        # Dimension des X
        label_Xdim = QLabel("X Dimension (en mm)")
        self.Xdim = QDoubleSpinBox()
        self.Xdim.setMinimum(100)
        self.Xdim.setMaximum(float("inf")) # Intervalle pour la dimension selon X 
        # Dimension des Y
        label_Ydim = QLabel("Y Dimension (en mm)")
        self.Ydim = QDoubleSpinBox()
        self.Ydim.setMinimum(100)
        self.Ydim.setMaximum(float("inf")) # Intervalle pour la dimension selon Y 
        # Nombre de répétition selon X
        label_Xrepet = QLabel("Nombre de répétitions selon x")
        self.Xrepet = QDoubleSpinBox()
        self.Xrepet.setMaximum(float("inf"))
        # Nombre de répétition selon Y
        label_Yrepet = QLabel("Nombre de répétitions selon y")
        self.Yrepet = QDoubleSpinBox()
        self.Yrepet.setMaximum(float("inf"))
        # Ecart entre deux parties (en mm)
        label_offset = QLabel("Espacement entre 2 pièces (en mm)")
        self.offset = QDoubleSpinBox()
        self.offset.setMaximum(float("inf"))
        
        # Pièces à chosir
        
        label_choix = QLabel("Choix des pièces")
        self.choix = QLineEdit()
        
        # bouton select parts
        
        # self.select_button = QPushButton("Choix des pièces")
        # on crée un bouton
        self.button = QPushButton("Générer fichier(s)")
        
        # Création d'un groupe de widgets
        groupe1 = QGroupBox("Stock Surface")
        
        # Création d'une disposition en grille
        grille1 = QGridLayout()
        
        grille1.addWidget(label_Xdim, 1, 1)
        grille1.addWidget(self.Xdim, 1, 2)
        grille1.addWidget(label_Ydim, 2, 1)
        grille1.addWidget(self.Ydim, 2, 2)
        
        
        # On définit la grille1 comme disposition du groupe1
        groupe1.setLayout(grille1)

##############################################################################       
        # Création d'un deuxième groupe de widgets
        groupe2 = QGroupBox("Parameters")
        
        # Création d'une deuxième disposition en grille
        grille2 = QGridLayout()
        
        grille2.addWidget(label_Xrepet, 1, 1)
        grille2.addWidget(self.Xrepet, 1, 2)
        grille2.addWidget(label_Yrepet, 2, 1)
        grille2.addWidget(self.Yrepet, 2, 2)
        grille2.addWidget(label_offset, 3, 1)
        grille2.addWidget(self.offset, 3, 2)
        
        # On définit la grille2 comme disposition du groupe2
        groupe2.setLayout(grille2)

        groupe3 = QGroupBox("Choix des pièces : Préciser l'intervalle des pièces. Ex : S'il y a 6 pièces au total mais que vous ne voulez que les 3 premières pièces : 0;2. 0 étant la pièce de base. Veuillez donc saisir une valeur strictement positive pour la valeur mini. Si vous souhaitez garder toutes les pièces, mettez simplement l'intervalle avec toutes les pièces. Ex : 0;5")
        
        grille3 = QGridLayout()
        
        grille3.addWidget(label_choix, 1, 1)
        grille3.addWidget(self.choix, 1, 2)
        
        groupe3.setLayout(grille3)
        # self.count = int(self.Xrepet.value() + self.Yrepet.value())
        
        # # On définit la grille3 comme disposition du groupe3
        # for compte in range(self.count):
        #     checkbox = QCheckBox(f'Pièce {compte+1}')
        #     grille3.addWidget(checkbox)
            
        # groupe3.setLayout(grille3)
        
        # qvBox layout : les éléments vont se mettre les uns en dessous des autres : V pour vertical, QHbox : pour horizontalement : à côté des autres
        #layout : c'est pour dire comment on va les disposer
        
        # Création d'une disposition verticale QVBox
        
        layout = QVBoxLayout() #rester sur une disposition verticale
        layout.addWidget(self.selection_fichiers)# ici on ajoute le code WidgetGM dans notre code, dans notre layout vertical
        layout.addWidget(groupe1)
        layout.addWidget(groupe2)
        layout.addWidget(groupe3)
        # layout.addWidget(groupe3)
        # layout.addWidget(self.select_button)
        layout.addWidget(self.button)# ici on rajoute dans notre layout vertical le bouton définit précédemment
        
        #créer un widget central dans lequel on va tout mettre, et lui dire que je veux que la disposition soit égale à layout
        central_widget=QWidget()
        central_widget.setLayout(layout)
        
        self.setCentralWidget(central_widget)
        
        #maintenant lier le bouton à une fonction
        
        # self.select_button.connect(self.Choix_repet)
        
        self.button.clicked.connect(self.Transformation)
        
    
    
   
    # def Choix_repet(self):
        
        
        
        
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
        
        # On fait l'hypothèse que l'on ne pourra pas faire une translation supérieure aux 3 quarts de la dimension de la plaque
        self.norm_offset_x = self.Xdim.value()*0.25
        self.norm_offset_y = self.Ydim.value()*0.25
        # self.norm_offset_moy = int((self.norm_offset_x + self.norm_offset_y)/2)
        self.X_norm_repet = self.Xdim.value()*0.90 
        self.Y_norm_repet = self.Ydim.value()*0.90
        self.x_decal_max = int((self.max_x + self.offset.value()) * self.Xrepet.value()) # La coordonnée x de la dernière répétition
        self.y_decal_max = int((self.max_y + self.offset.value()) * self.Yrepet.value()) # La coordonnée y de la dernière répétition
        self.nb_repet_possible_x = int(self.X_norm_repet/(self.max_x + self.offset.value()) - 1) # On résoud l'équation (xmax + offset)*nb de repet x = x_norm (90%) avec nb de repet comme inconnu
        self.nb_repet_possible_y = int(self.Y_norm_repet/(self.max_y + self.offset.value()) - 1) # On résoud l'équation (ymax + offset)*nb de repet y = y_norm (90%) avec nb de repet comme inconnu
        self.offset_possible_x = (self.X_norm_repet / self.Xrepet.value()) - self.max_x # pareil avec offset comme inconnu
        self.offset_possible_y = (self.Y_norm_repet / self.Yrepet.value()) - self.max_y # pareil avec offset comme inconnu
        self.offset_possible_moy = int((self.offset_possible_x + self.offset_possible_y)/2) # la moyenne de ces offset normalisés
        
        self.total_repet = int(self.Xrepet.value() + self.Yrepet.value()) # nombre de répét 
        self.intervalle_str = self.choix.text() # on convertit l'intervalle de choix des pièces en texte
        self.liste_inter = self.intervalle_str.split(";") # on met ça dans une liste avec comme séparateur ;
        self.mini = int(self.liste_inter[0]) # La première valeur de la liste (en int) correspond à la valeur mini de l'intervalle
        self.maxi = int(self.liste_inter[1]) # La deuxième valeur de la liste (en int) correspond à la valeur maxi de l'intervalle
        
         
        # self.seuil_maxx = self.max_x + self.x_decal_max
        # self.seuil_maxy = self.max_y + self.y_decal_max
        
        
        # if(self.offset.value()==0): # Il ne peut pas y avoir un décalage nul 
        #     # Il y a un message d'erreur qui apparaît
        #     msg_box = QMessageBox() # Boîte de dialogue
        #     # Le type de cette boîte de dialogue est une erreur et non une information (cf plus bas lors de la transformation du fichier : "Fichiers transformés")
        #     # Le message d'erreur est explicite et va guider l'utilisateur sur les conditions à respecter
        #     # Pour cela, il lui donnera les intervalles à respecter pour être dans les normes
        #     msg_box.critical(self, "Erreur", "Veuillez choisir un décalage supérieur à 0 !")
        #     # Ajout du bouton "OK"
        #     ok_button = QPushButton("OK")
        #     msg_box.addButton(ok_button, QMessageBox.AcceptRole) # En cliquant sur le bouton OK, ça ferme la boite de dialogue
        # elif(self.offset.value()>=self.norm_offset_x or self.offset.value()>=self.norm_offset_y): # Si le décalage est supérieur aux 1/4 de la plaque
        #     # Il y a un message d'erreur qui apparaît
        #     msg_box = QMessageBox() # Boîte de dialogue
        #     # Le type de cette boîte de dialogue est une erreur et non une information (cf plus bas lors de la transformation du fichier : "Fichiers transformés")
        #     # Le message d'erreur est explicite et va guider l'utilisateur sur les conditions à respecter
        #     # Pour cela, il lui donnera les intervalles à respecter pour être dans les normes 
        #     msg_box.critical(self, "Erreur", "Pour éviter de dépasser les dimensions de la plaque, vous ne pouvez effectuer que des décalages d'une valeur inférieure au quart de la plaque.\n\nVeuillez rentrer une valeur valide comprise entre 0 et {} pour le décalage  ! ".format(self.offset_possible_moy/2))
        #     # Ajout du bouton "OK"
        #     ok_button = QPushButton("OK")
        #     msg_box.addButton(ok_button, QMessageBox.AcceptRole) # En cliquant sur le bouton OK, ça ferme la boite de dialogue
            
        # elif(self.x_decal_max >= self.X_norm_repet or self.y_decal_max >= self.Y_norm_repet): # si la coordonnée du max de la pièce selon x et/ou y dépasse les 90 % de la pièce
        # #     # Si on veut garder le même décalage : on doit trouver le nombre de répétition adéquat 
        # #     self.nb_repet_xnorm = (self.Xdim.value() - self.max_x)/(self.max_x + self.offset.value())
        # #     self.decalage = ((self.Xdim.value() - self.max_x)/self.Xrepet.value()) - self.max_x
            
        #     # Il y a un message d'erreur qui apparaît
        #     msg_box = QMessageBox() # Boîte de dialogue
        #     # Le type de cette boîte de dialogue est une erreur et non une information (cf plus bas lors de la transformation du fichier : "Fichiers transformés")
        #     # Le message d'erreur est explicite et va guider l'utilisateur sur les conditions à respecter
        #     # Pour cela, il lui donnera les intervalles à respecter pour être dans les normes 
        #     msg_box.critical(self, "Erreur", "Pour éviter de dépasser les dimensions de la plaque, vous ne pouvez effectuer que des répétitions ne dépassant pas les 9/10 (90%) de la plaque.\n\n Afin d'obtenir des répétitions conformes : 2 possiblilités s'offrent à vous : \n\n Si vous souhaitez garder le même décalage entre 2 pièces : Veuillez rentrer une valeur valide comprise entre 0 et {} pour les répétitions en X et entre 0 et {} pour les répétitions en Y !\n\n Si vous voulez garder le même nombre de répétitions selon x et y : Veuillez choisir un offset inférieur à {} ".format(self.nb_repet_possible_x,self.nb_repet_possible_y, self.offset_possible_moy/2))
        #     # Ajout du bouton "OK"
        #     ok_button = QPushButton("OK")
        #     msg_box.addButton(ok_button, QMessageBox.AcceptRole) # En cliquant sur le bouton OK, ça ferme la boite de dialogue
          
        # # elif(self.mini<0):
        # #     msg_box = QMessageBox() # Boîte de dialogue
        # #     # Le type de cette boîte de dialogue est une erreur et non une information (cf plus bas lors de la transformation du fichier : "Fichiers transformés")
        # #     # Le message d'erreur est explicite et va guider l'utilisateur sur les conditions à respecter
        # #     # Pour cela, il lui donnera les intervalles à respecter pour être dans les normes
        # #     msg_box.critical(self, "Erreur", " Veuillez choisir une valeur strictement positive !")
        # #     # Ajout du bouton "OK"
        # #     ok_button = QPushButton("OK")
        # #     msg_box.addButton(ok_button, QMessageBox.AcceptRole) # En cliquant sur le bouton OK, ça ferme la boite de dialogue  
        # elif(self.maxi>(self.total_repet -1)): # Si la valeur maxi de l'intervalle de choix est supérieur au nombre total de pièces répétées
        #     msg_box = QMessageBox() # Boîte de dialogue
        #     # Le type de cette boîte de dialogue est une erreur et non une information (cf plus bas lors de la transformation du fichier : "Fichiers transformés")
        #     # Le message d'erreur est explicite et va guider l'utilisateur sur les conditions à respecter
        #     # Pour cela, il lui donnera les intervalles à respecter pour être dans les normes
        #     msg_box.critical(self, "Erreur", "Attention, vous avez saisi un intervalle plus grand que le nombre de répétitions ! Veuillez choisir une valeur maximum inférieure ou égale à {}".format(self.total_repet-1))
        #     # Ajout du bouton "OK"
        #     ok_button = QPushButton("OK")
        #     msg_box.addButton(ok_button, QMessageBox.AcceptRole) # En cliquant sur le bouton OK, ça ferme la boite de dialogue
       
        # # # Si l'utilisateur ne s'est pas trompé : la condition est respectée
        
        # # # On passe à l'exécution du programme : calculs/ opérations de rotation et/ou translation...
        
        
    
        
        # select_part = QMessageBox() # Boîte de dialogue
        # Le type de cette boîte de dialogue est une erreur et non une information (cf plus bas lors de la transformation du fichier : "Fichiers transformés")
        # Le message d'erreur est explicite et va guider l'utilisateur sur les conditions à respecter
        # Pour cela, il lui donnera les intervalles à respecter pour être dans les normes 
        # select_part.question(self, "Choix des pièces", "Veuillez choisir les répétitions à effectuer parmi les {} répétitions".format(self.total_repet))
        # # Ajout du bouton "OK"
        # # for repet_total in range(self.total_repet):
            
        # ok_button = QPushButton("OK")
        # select_part.addButton(ok_button, QMessageBox.AcceptRole) # En cliquant sur le bouton OK, ça ferme la boite de dialogue
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
                        # self.a = int(self.liste[0]) # Elément zero de la liste en int
                        # self.b = int(self.liste[1]) # Elément 1 de la liste en int
                        # self.c = int(self.liste[2]) # Elément 2 de la liste en int

                        if((self.Xrepet.value()==self.Yrepet.value()) or (self.Xrepet.value()<self.Yrepet.value())): # Si x_repet = y_repet ou x_repet<y_repet : on va mettre y en 2e pour éviter que le programme s'arrête
                            for j in range((int(self.Yrepet.value())) + 1):
                                for i in range((int(self.Xrepet.value())) + 2):
                        # for i in range((int(self.Xrepet.value()))):
                                    self.x_decal = (self.max_x + self.offset.value()) * i
                                    # for j in range((int(self.Yrepet.value()))):
                                    self.y_decal = (self.max_y + self.offset.value()) * j
                                    self.x_nv = int(self.liste[0]) + self.x_decal
                                    self.y_nv = int(self.liste[1]) + self.y_decal
                                    self.z = int(self.liste[2])
                                    self.x_nv = int(self.x_nv)
                                    self.y_nv = int(self.y_nv)
                                    self.x_nv = str(self.x_nv)
                                    self.y_nv = str(self.y_nv)
                                    self.z = str(self.z)
                                    self.x_nv = 'Z' + self.x_nv # On rajoute le Z au premier élement de la liste
                                    self.z = self.z+ ';' # On rajoute le ; au dernier élément de la liste
                                    # On ajoute les nouvelles coordonnées après modification à la nouvelle liste qui s'appelle valeurs_modif
                                    self.valeurs_modif.append(self.x_nv) 
                                    self.valeurs_modif.append(self.y_nv)
                                    self.valeurs_modif.append(self.z)
                                    # On convertit les élements de la liste en chaine de caractères
                                    # Pour cela, on parcourt la nouvelle liste et on ajoute chaque élement à une nouvelle chaine de caractère
                                    # Et on sépare chaque élement par une virgule
                                    self.chaine = ','.join([d for d in self.valeurs_modif])
                                    # self.str2 = self.chaine[:-1] #car on a une virgule à la fin de la ligne (après le ;) --> on prend la ligne sans la virgule à la fin
                                    output_file.write(self.chaine)# Dans le nouveau fichier, on insert la ligne correspondant à la ligne de référence modifiée
                                    output_file.write('\n') # On va à la ligne pour copier la ligne suivante
                                    self.valeurs_modif = [] # On va réinitialiser la nouvelle liste pour qu'elle prenne les valeurs de la ligne suivante
                                    # pass
                        elif(self.Xrepet.value()>self.Yrepet.value()): # Si x_repet est plus grand que y_repet, on va mettre la boucle x en 2e pour éviter que le programme s'arrête
                            for i in range((int(self.Xrepet.value())) + 1): # On rajoute + 1 pour éviter que le programme s'arrête (ex : for j in range(0) --> aucune itération)
                                for j in range((int(self.Yrepet.value())) + 2):
                                    self.x_decal = (self.max_x + self.offset.value()) * i
                                    # for j in range((int(self.Yrepet.value()))):
                                    self.y_decal = (self.max_y + self.offset.value()) * j
                                    self.x_nv = int(self.liste[0]) + self.x_decal
                                    self.y_nv = int(self.liste[1]) + self.y_decal
                                    self.z = int(self.liste[2])
                                    self.x_nv = int(self.x_nv)
                                    self.y_nv = int(self.y_nv)
                                    self.x_nv = str(self.x_nv)
                                    self.y_nv = str(self.y_nv)
                                    self.z = str(self.z)
                                    self.x_nv = 'Z' + self.x_nv # On rajoute le Z au premier élement de la liste
                                    self.z = self.z+ ';' # On rajoute le ; au dernier élément de la liste
                                    # On ajoute les nouvelles coordonnées après modification à la nouvelle liste qui s'appelle valeurs_modif
                                    self.valeurs_modif.append(self.x_nv) 
                                    self.valeurs_modif.append(self.y_nv)
                                    self.valeurs_modif.append(self.z)
                                    # On convertit les élements de la liste en chaine de caractères
                                    # Pour cela, on parcourt la nouvelle liste et on ajoute chaque élement à une nouvelle chaine de caractère
                                    # Et on sépare chaque élement par une virgule
                                    self.chaine = ','.join([d for d in self.valeurs_modif])
                                    # self.str2 = self.chaine[:-1] #car on a une virgule à la fin de la ligne (après le ;) --> on prend la ligne sans la virgule à la fin
                                    output_file.write(self.chaine)# Dans le nouveau fichier, on insert la ligne correspondant à la ligne de référence modifiée
                                    output_file.write('\n') # On va à la ligne pour copier la ligne suivante
                                    self.valeurs_modif = [] # On va réinitialiser la nouvelle liste pour qu'elle prenne les valeurs de la ligne suivante
                                    
        
        
        
        
        
        
        
    
                
            
            #on ferme le fichier:
            fichier.close() # ici on parle de chaque fichier ouvert et que l'on parcourt
            output_file.write("\n")             # pour aller à la ligne
    
        output_file.close() # ici on parle de notre fichier de sortie, dans lequel on a tous les autres fichiers, et que l'on souhaite fermer à présent, après avoir terminé l'écriture
        # il a copié tous les fichiers dans le fichier transformation et il a fermé le fichier transformation
        #ouvrir une fenêtre avec un message
        QMessageBox.information(self, "Information", "Fichiers transformés ! ")
        
    
if __name__ == '__main__':
    #create the Qt Application
    app= QApplication(sys.argv)
    
    #create and show the form
    window=MainWindow()
    window.show()
    
    #Run the main Qt loop
    sys.exit(app.exec())