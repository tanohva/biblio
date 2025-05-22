import json
import keyboard
from tabulate import tabulate  
#Extraire la liste des livres 
def get_livres():
    # Charger le fichier JSON
    with open("Data/livres.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

#Enregistrer les livres dans le fichier JSON 
def set_livres(data):
    with open("Data/livres.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("Fichier Livres enregistré avec succès.")

#Ajouter un livre
def ajout_livre():
    data=get_livres()
    livre={}
    id=len(data)+1
    while True:
        titre=input("Donner le titre du livre à ajouter: ")
        if (titre!=""):
            break
    while True:
        auteur=input("Donner l'auteur du livre à ajouter: ")
        if (auteur!=""):
            break
    while True:
        exemplaires=int(input("Donner le nombre d'exemplaires du livre à ajouter: "))
        if (exemplaires>0):
            break
        
    livre["id"]=id
    livre["titre"]=titre
    livre["auteur"]=auteur
    livre["exemplaires"]=exemplaires
    livre["disponibles"]=exemplaires
    data.append(livre)
    set_livres(data)

#Suppression d'un livre
def supprimer_livre():
    data=get_livres()
    n=int(input("Donner l'identifiant du livre à supprimer: "))
    for d in data:
        if (d["id"]==n):
            data.remove(d)
            set_livres(data)
            break
    else:
        print("cet identifiant n'existe pas")

#Mettre à jour un livre
def update_livre():
    data=get_livres()
    n=int(input("Donner l'identifiant du livre à mettre à jour: "))
    for d in data:
        if (d["id"]==n):
            r=input("Voulez vous changer le titre du livre y/n? ")
            if(r=="y"):
                titre=input("Donner le nouveau titre: ")
                d["titre"]=titre
            r=input("Voulez vous changer l'auteur du livre y/n? ")
            if(r=="y"):
                auteur=input("Donner le nouvel auteur: ")
                d["auteur"]=auteur
            set_livres(data)
            break
    else:
        print("cet identifiant n'existe pas")
    
        
def livres_dispo():
    # Charger le fichier JSON
    data=get_livres()
    dispo=[["ID","Titre","Auteur", "disponible"]]
    for d in data:
        if d["disponibles"]>0:
            livre_dispo=[d['id'],d['titre'],d['auteur'],d['disponibles']]
            dispo.append(livre_dispo)
    
    print(tabulate(dispo, headers="firstrow", tablefmt="grid"))
    print("Appuyer sur C pour sortir")
    while True:
        if keyboard.read_key() == "c":
            break
    
            
    
    