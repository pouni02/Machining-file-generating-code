# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 15:55:44 2021

@author: aline
"""

#! /usr/bin/python
import sys
from PySide6.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

pyqt4 = False
pyqt5 = False

# PyQt5 ?
try:
    from PyQt5.QtGui import *
    from PyQt5.QtWidgets import *
except ImportError as e:
    print("PyQt5 n'est pas installé.")
else:
    print("Utilisation de PyQt5")
    pyqt5 = True

# PyQt4 ?
# if not pyqt5:
#     try:
#         import PyQt4.QtGui
#     except ImportError as e:
#         print("PyQt4 n'est pas installé.")
#     else:
#         print("Utilisation de PyQt4")
#         pyqt4 = True


class WidgetSelectionFichiers(QWidget):

    def __init__(self):

        QWidget.__init__(self)


        # ATTRIBUTS
        # ---------
        self.liste_fichiers = QListWidget()

        # modes de selection : https://doc.qt.io/qt-5/qabstractitemview.html#SelectionMode-enum
        # on utilise le mode SingleSelection pour une question de simplicite
        self.liste_fichiers.setSelectionMode(QAbstractItemView.SingleSelection)

        self.creationWidget()



    # ------------------------------------------------------------------------
    # CREATION DU WIDGET
    # ------------------------------------------------------------------------

    def creationWidget(self):


        # ELEMENTS DU WIDGET
        # ------------------
        bouton_ajout = QPushButton('+')
        bouton_suppression = QPushButton('-')
        bouton_monter = QPushButton('↑')
        bouton_descendre = QPushButton('↓')


        # MISE EN FORME
        # -------------
        vbox = QVBoxLayout()
        vbox.addWidget(bouton_ajout)
        vbox.addWidget(bouton_suppression)
        vbox.addWidget(bouton_monter)
        vbox.addWidget(bouton_descendre)

        hbox = QHBoxLayout()
        hbox.addWidget(self.liste_fichiers)
        hbox.addLayout(vbox)

        groupbox = QGroupBox("Sélection des fichiers d'usinage")
        groupbox.setLayout(hbox)

        box = QVBoxLayout()
        box.addWidget(groupbox)

        self.setLayout(box)


        # COMPORTEMENT
        # ------------
        bouton_ajout.clicked.connect(self.ajoutFichiers)
        bouton_suppression.clicked.connect(self.suppressionFichier)
        bouton_monter.clicked.connect(self.monterFichier)
        bouton_descendre.clicked.connect(self.descendreFichier)



    # ------------------------------------------------------------------------
    # METHODES LOCALES AU WIDGET
    # ------------------------------------------------------------------------

    def ajoutFichiers(self):

        # si utilisation de PyQt4 :
        if pyqt4:
            fileDialog = QFileDialog(self)
            fileDialog.setFileMode(QFileDialog.ExistingFile)
            # Selection d'un ou plusieurs fichiers deja existants
            # https://doc.qt.io/qt-5/qfiledialog.html#FileMode-enum

            nom_fichier = fileDialog.getOpenFileName(self,"Sélection du fichier")
            self.liste_fichiers.addItem(nom_fichier)

        # si utilisation de PyQt5 :
        if pyqt5:
            fileDialog = QFileDialog(self)
            fileDialog.setFileMode(QFileDialog.ExistingFiles)
            # Selection d'un ou plusieurs fichiers deja existants
            # https://doc.qt.io/qt-5/qfiledialog.html#FileMode-enum

            liste_fichiers, _ = fileDialog.getOpenFileNames(self,"Sélection du(des) fichier(s)")

            for fichier in liste_fichiers:
                self.liste_fichiers.addItem(fichier)


    def suppressionFichier(self):

        # on recupere l'item selectionne ainsi que sa position dans la liste
        # selectedItems retourne une QListWidgetItem dont on prend le seul element, le premier
        # https://doc.qt.io/qt-5/qlistwidgetitem.html
        item = self.liste_fichiers.selectedItems()[0]
        index = self.liste_fichiers.row(item)

        # on supprime l'item en question
        self.liste_fichiers.takeItem(index)


    def monterFichier(self):

        # on recupere l'item selectionne ainsi que sa position dans la liste
        # selectedItems retourne une QListWidgetItem dont on prend le seul element, le premier
        # https://doc.qt.io/qt-5/qlistwidgetitem.html
        item = self.liste_fichiers.selectedItems()[0]
        index = self.liste_fichiers.row(item)

        # s'il n'est pas deja en haut de la liste, on le fait monter
        if index > 0:
            # on recupere l'item de la liste
            item = self.liste_fichiers.takeItem(index)
            # on l'insere dans la liste a la position du dessus
            self.liste_fichiers.insertItem(index-1, item.text())
            # on met a jour l'item selectionne
            item = self.liste_fichiers.item(index-1)
            self.liste_fichiers.setCurrentItem(item)


    def descendreFichier(self):

        # on recupere l'item selectionne ainsi que sa position dans la liste
        # selectedItems retourne une QListWidgetItem dont on prend le seul element, le premier
        # https://doc.qt.io/qt-5/qlistwidgetitem.html
        item = self.liste_fichiers.selectedItems()[0]
        index = self.liste_fichiers.row(item)

        # s'il n'est pas deja en bas de la liste, on le fait descendre
        if index < self.liste_fichiers.count()-1:
            # on recupere l'item de la liste
            item = self.liste_fichiers.takeItem(index)
            # on l'insere dans la liste a la position du dessous
            self.liste_fichiers.insertItem(index+1, item.text())
            # on met a jour l'item selectionne
            item = self.liste_fichiers.item(index+1)
            self.liste_fichiers.setCurrentItem(item)


    # ------------------------------------------------------------------------
    # ACCESSEURS
    # ------------------------------------------------------------------------


    # Retourner la liste des chemins des fichiers selectionnes
    # - liste de chaines de caracteres

    def listeFichiers(self):

        liste_fichiers = []

        for index in range(self.liste_fichiers.count()):
            fichier = self.liste_fichiers.item(index).text()
            liste_fichiers.append(fichier)

        return liste_fichiers




def main():
   app = QApplication(sys.argv)
   fen = WidgetSelectionFichiers()
   fen.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   main()
