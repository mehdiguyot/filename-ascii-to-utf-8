# Filename from ascii to utf-8
# This program convert filename in ascii to utf-8
# Code by Mehdi Guyot, for any request, contact mail@guyotmehdi.ch
# Website : guyotmehdi.ch

import os;
import sys;

for dossier, sous_dossiers, fichiers in os.walk(r'C:\Users\username\folder'):  #Set the folder you want
    for fichier in fichiers:
        print(os.path.join(dossier, fichier))
        pathFichier = (os.path.join(dossier, fichier))
        print(pathFichier.encode('latin1').decode())
        print("___________________________")
        os.rename(pathFichier, pathFichier.encode('latin1','ignore').decode('utf-8','ignore'))