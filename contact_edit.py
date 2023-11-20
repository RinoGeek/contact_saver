#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Spyder Editor
Author : ATOHOUN Marino as Rino_Geek
This is a temporary script file.
"""
import os
import csv

contacts = []

def ajout(nom_, prenom_, telephone_, email_, file_name="/home/rino/Documents/contact.csv"):
    file_exist = os.path.isfile(file_name)
    with open(file_name, 'a', newline='') as f:
        entete = ["nom", "prenom", "telephone", "email"]
        writer = csv.DictWriter(f, fieldnames=entete)
        if not file_exist:
            writer.writeheader()
        writer.writerow({"nom" : nom_,
                        "prenom" : prenom_,
                        "telephone" : telephone_,
                        "email" : email_})


def supp(element_supp, file_name="/home/rino/Documents/contact.csv"):
    with open(file_name, 'r', newline='') as f, open("/home/rino/Documents/file_temp.csv", 'w', newline='') as ft:
        reader = csv.DictReader(f)
        
        writer = csv.DictWriter(ft, fieldnames=reader.fieldnames)
        writer.writeheader()
        
        for line in reader:
            if line["nom"] != element_supp and line["prenom"] != element_supp and line["telephone"] != element_supp and line["email"] != element_supp:
                writer.writerow(line)
    os.rename('/home/rino/Documents/file_temp.csv', file_name)
    afficher()

def recherche(search, file_name="/home/rino/Documents/contact.csv"):
    with open(file_name, 'r', newline='') as f:
        reader = csv.DictReader(f)
        for line in reader:
            if line["nom"] == search or line["prenom"] == search or line["telephone"] == search or line["email"] == search:
                return ' '.join(list(line.values()))
            
    return "Contact non trouvé"
            
            
def afficher(file_name="/home/rino/Documents/contact.csv"):
    with open(file_name, 'r', newline='') as f:
        reader = csv.DictReader(f)
        for line in reader:
            print(' '.join(list(line.values())))

def modifier(modif):
    recherche(modif)
    if recherche(modif) != "Contact non trouvé":
        nom, prenom, telephone, email = input('nom : '), input('prenom : '), input('telephone : '), input('email : ')
        ajout(nom, prenom, telephone, email)
        print("contact modifié avec succès")
        
    else:
        print("Contact non trouvé")



#=======================================================================================================================================
    
def selection(choix):
    if choix == 1:
        return "voiçi la liste de vos contacts : \n", afficher()
    elif choix == 2:
        print('''\n
              ======================================================\n
                          \t         Ajout Contact \n
              ====================================================== \n
        ''')
        nom, prenom, telephone, email= input('nom : '), input('prenom : '), input('telephone : '), input('email : ')
        ajout(nom, prenom, telephone, email)
        print("Contact ajouté avec succès.")
    elif choix == 3:
        print('''\n
              ======================================================\n
                     \t             Recherche Contact \n
              ====================================================== \n
        ''')
        search = input("Entrez le nom, le prénom le Téléphone ou l'email que vous cherchez : ")
        print(recherche(search))
    elif choix == 4:
        print('''\n
              ======================================================\n
                      \t             Modification Contact \n
              ====================================================== \n
        ''')
        nom = input("Entrez le nom du Contact à modifier : ")
        modifier(nom)
    else :
        print('''\n
              ======================================================\n
                     \t              Supprimer Contact \n
              ====================================================== \n
        ''')
        nom = input("Entrez le nom du Contact à supprimer : ")
        supp(nom)
        
print('''\n
      ======================================================\n
             \t              ContactSaver \n
             \t              Options :  \n
             \t \t             1 : Liste de Contacts \n
             \t \t             2 : Ajout Contact \n
             \t \t             3 : Recherche Contact \n
             \t \t             4 : Modification Contact \n
             \t \t             5 : Suppression Contact \n
             \t \t             q : Quiter \n
      ====================================================== \n
''')

while selection(int(input("Entrez une option : "))) != 'q':
    selection(int(input("Entrez une option : ")))