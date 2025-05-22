from Fonctions.gestion_livres import *
from Fonctions.gestion_lecteurs import *
import keyboard

def get_emprunts():
    # Charger le fichier JSON
    with open("Data/Emprunts.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

#Enregistrer les emprunts dans le fichier JSON 
def set_emprunts(data):
    with open("Data/Emprunts.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("Fichier Emprunts enregistré avec succès.")

def ajout_emprunt():
    dliv=get_livres()
    lecteurs=get_lecteurs()
    emprunts=get_emprunts()
    titre=input("Donner le titre du livre recherché: ")
    #Vérifier si le livre est disponible
    for d in dliv:
        if (d["disponibles"]>0) and d["titre"]==titre:
            l=int(input("Saisissez l'identifiant du lecteur: "))
            #Vérifier si le lecteur existe
            for lec in lecteurs:
                if lec["id"]==l:
                    #Vérifier si lecteur a déjà emprunté des livres
                    for emp in emprunts:
                        #Ajouter le livre à la liste déjà empruntée
                        if emp["id"]==l:
                            emp["idL"].append(d["id"])
                            break
                    #Sinon ajouter le lecteur et le livre à liste des emprunts
                    else:
                        a={}
                        a["id"]=l
                        a["idL"]=[d["id"]]
                        emprunts.append(a)
                    
                    #Changer le nombre d'exemplaires disponibles
                    for dl in dliv:
                        if (dl["titre"]==titre):
                            dl["disponibles"]=dl["disponibles"]-1
                            set_livres(dliv)
                    break                        
            else:
                print("Ce lecteur n'existe pas")
            break
    else:
        print("Ce livre n'est pas disponible")
    set_emprunts(emprunts)
    

    
def supprimer_emprunt():  
    dliv=get_livres()
    emprunts=get_emprunts()
    n=int(input("Donner l'identifiant du livre à remettre: "))
    #Parcourir tous les imprunts pour trouver le livre
    for emp in emprunts:
        if n in emp["idL"]:
            #Une fois trouvé, le livre sera supprimé de la liste des emprunts
            emp["idL"].remove(n)
            # Si tous les livres sont rendu, le lecteur sera supprimé de la liste
            if emp["idL"]==[]:
                emprunts.remove(emp)
            
            #Le livre redevient disponible
            for dl in dliv:
                        if (dl["id"]==n):
                            dl["disponibles"]=dl["disponibles"]+1
                            set_livres(dliv)
            break
    else:
        print("Ce livre n'est pas dans la liste des emprunts")
    set_emprunts(emprunts)

def afficher_emprunts():
    emprunts=get_emprunts()
    dliv=get_livres()
    lecteurs=get_lecteurs()
    print("-------La liste des livres empruntés par lecteur------")
    listes=[["Lecteur","Livres"]]
    
    for emp in emprunts:
        ligne=[]
        livres=""
        for l in lecteurs:
            if emp["id"]==l["id"]:
                ligne.append(l["nom"])
        for d in dliv:
            if d["id"] in emp["idL"]:
                livres=livres+d["titre"]+"/"
        
        ligne.append(livres)
        listes.append(ligne)
    print(tabulate(listes, headers="firstrow", tablefmt="grid"))
    print("Appuyer sur C pour sortir")
    while True:
        if keyboard.read_key() == "c":
            break
        
    
    
    
    
    
    