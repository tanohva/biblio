from Fonctions.gestion_livres import *
from Fonctions.gestion_lecteurs import *
from Fonctions.suivi_emprunt import *

import os
import time




while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n----------------------------------Menu Principal---------------------------------------------------- :")
    print("1. Gestion des livres   ||  2. Gestion des lecteurs   ||  3. Gestion des emprunts   ||  4. Quitter")
    choix = input("Entrez votre choix: ")

    match choix:
        case "1":
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("-----------------------------------------------------Menu du gestion des livres -----------------------------------------------------:")
                print("1. Ajout d'un livre  ||  2. Modification d'un livre  ||  3. Suppression d'un livre  ||  4. Listes de livres disponibles || 5. Quitter")
                livres_choix = input("Entrez votre choix: ")
                match livres_choix:
                    case "1":
                        ajout_livre()
                        time.sleep(2.5)
                    case "2":
                        update_livre()
                        time.sleep(2.5)
                    case "3":
                        supprimer_livre()
                        time.sleep(2.5)
                    case "4": 
                        livres_dispo()
                    case "5":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        break
                    case _:
                        print("Choix invalide, veuillez réessayer.")
                        time.sleep(2)
        case "2":
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("---------------------------------------------------Menu du gestion des lecteurs:--------------------------------------------------- :") 
                print("1. Ajouter un lecteur  ||  2. Modification d'un lecteur  ||  3. Suppression d'un lecteur  ||  4. Liste des lecteurs  || 5. Quitter")
                lecteurs_choix = input("Entrez votre choix: ")     
                match lecteurs_choix:
                    case "1":
                        ajout_lecteur()
                        time.sleep(2.5)
                    case "2":
                        update_lecteur()
                        time.sleep(2.5)
                    case "3":
                        supprimer_lecteur()
                        time.sleep(2.5)
                    case "4": 
                        afficher_lecteurs()
                    case "5":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        break
                    case _:
                        print("Choix invalide, veuillez réessayer.")
                        time.sleep(2)

        case "3":
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("---------------------------------Menu du gestion des emprunts ----------------------------------- :")
                print("1. Emprunt d'un livre  ||  2. Retour d'un livre  ||  3. Liste des emprunts en cours  ||  4. Quitter")
                emprunts_choix = input("Entrez votre choix: ")     
                match emprunts_choix:
                    case "1":
                        ajout_emprunt()
                        time.sleep(2.5)
                    case "2":
                        supprimer_emprunt()
                        time.sleep(2.5)
                    case "3":
                        afficher_emprunts()                
                    case "4": 
                        os.system('cls' if os.name == 'nt' else 'clear')
                        break
                    case _:
                        print("Choix invalide, veuillez réessayer.")
                        time.sleep(2)

        case "4":
            print("Au revoir")
            break
        case _:
            print("Choix invalide, veuillez réessayer.")
            time.sleep(2)