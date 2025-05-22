import json
import keyboard
from tabulate import tabulate  
#Extraire la liste des lecteurs 
def get_lecteurs():
    # Charger le fichier JSON
    with open("Data/lecteurs.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

#Enregistrer les lecteurs dans le fichier JSON 
def set_lecteurs(data):
    with open("Data/lecteurs.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("Fichier Lecteurs enregistré avec succès.")

def ajout_lecteur():
    data=get_lecteurs()
    lecteur={}
    id=len(data)+1
    while True:
        nom=input("Donner le nom du lecteur à ajouter: ")
        if nom!="":
            break
    lecteur["id"]=id
    lecteur["nom"]=nom
    data.append(lecteur)
    set_lecteurs(data)

def supprimer_lecteur():
    data=get_lecteurs()
    n=int(input("Donner l'identifiant du lecteur à supprimer: "))
    for d in data:
        if (d["id"]==n):
            data.remove(d)
            set_lecteurs(data)
            break
    else:
        print("cet identifiant n'existe pas")



#Mettre à jour les lecteurs
def update_lecteur():
    data=get_lecteurs()
    n=int(input("Donner l'identifiant du lecteur à mettre à jour: "))
    for d in data:
        if (d["id"]==n):
            r=input("Voulez vous changer le nom du lecteur y/n? ")
            if(r=="y"):
                nom=input("Donner le nouvel auteur: ")
                d["nom"]=nom
            break
    else:
        print("cet identifiant n'existe pas")
    set_lecteurs(data)

def afficher_lecteurs():
    data=get_lecteurs()
    lecteurs=[["ID","Nom"]]
    for d in data:
        lecteurs.append([d["id"],d["nom"]])
    print(tabulate(lecteurs, headers="firstrow", tablefmt="grid"))
    print("Appuyer sur C pour sortir")
    while True:
        if keyboard.read_key() == "c":
            break
        

 
            
            
    
    
