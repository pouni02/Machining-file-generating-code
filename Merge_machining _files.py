# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 14:34:21 2023

"""


import sys 
#from PySide6.QtWidgets import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
from PySide6.QtWidgets import *

from WidgetsGM import WidgetSelectionFichiers # si on a la version 6 : on prend WidgetFileList



class MainWindow(QMainWindow):
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        
        # Définition du titre de la fenêtre:
            
        self.setWindowTitle("Fusion de fichiers !")
        
        #self.edit = QLineEdit("Quel est votre nom ? ")
        self.selection_fichiers = WidgetSelectionFichiers()
        self.button = QPushButton("Fusionner")
        
        layout = QVBoxLayout() # les éléments vont se placer les uns au-dessus des autres --> QHBox : horizontalement
        layout.addWidget(self.selection_fichiers)
        layout.addWidget(self.button)
        
        central_widget = QWidget()   # permet de féfinir un widget central dans lequel on peut mettre notre widget
        central_widget.setLayout(layout)
        
        self.setCentralWidget(central_widget)
        
        self.button.clicked.connect(self.fusion)
        
        
    #def bonjour(self):
      #  print(f"Bonjour {self.edit.text()}")
        
      #  QMessageBox.information(self, "Information", f"Bonjour {self.edit.text()} !" )
        
        
    def fusion(self):  # f pour formater : permet de faire ref à des variables dans les crochets
    # programme pour fusionner des fichiers
        file_dialog = QFileDialog(self)
        output_file_name = file_dialog.getSaveFileName()[0] # version 6 : file_dialog.getSaveFileName(self)[0] # un tableau peut avoir plusieurs éléments,mais ce qui nous intéresse, c'est l'élément 0
        
        output_file = open(output_file_name, "w")
        
        for chemin_fichier in self.selection_fichiers.listeFichiers():
            fichier = open(chemin_fichier, "r")
            
            for ligne in fichier:
                output_file.write(ligne)
                
            fichier.close()
            output_file.write("\n") 
        
        output_file.close()
        
        
        QMessageBox.information(self, "Information", "Fichiers fusionnés ! ")
            
        
if __name__ == '__main__':
    
    # Create the Qt Application
    
    app = QApplication(sys.argv)
    
    # Create and show the form
    
    window = MainWindow()
    window.show()
    
    # Run the main Qt loop
    
    sys.exit(app.exec())
    

