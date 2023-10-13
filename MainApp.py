
# Tapez le code principal
"""*********************************** 

Nom Programme : Exercice N 

Auteurs : 

      Nom Eya Ben Aouicha 

      Nom Wadhah Salhi 

Classe : CII-2-SIIR-D 

***********************************"""
from MaBiB import *
import re
import getpass
import os

Authdic={}
print("        |      Application Multi Taches   | ")
while True:
    menuP()
    choixP= input("Choisir(A,B,C) : ")
    match choixP:
        case "A":
            menuA()
            choixA= input("Choisir(A1,A2,A3) : ")
            match choixA:
                case "A1":
                    id=int(input("Veuillez entrer le N° d'inscription d'un etudiant: "))
                    email=input("Veuillez entrer le login: ")
                    password = getpass.getpass("Veuillez entrer votre mot de passe : ")
                    classe=input("Veuillez entrer votre classe CII-2-SSIR-A/B/C/D : ")
                    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
                    if re.fullmatch(email_pattern, email):
                        pwd=email.split("@")[0]+"&"+password
                        SauvegarderUtilisateur(id,email,pwd,classe)
                    else:
                        print(f"L'adresse email {email} n'est pas valide.")
                case "A2":
                    LireUtilisateur()   
                case "A3":
                    # menuP() 
                    exit

        case "B":
            
            if os.path.exists("Authentification.txt"):
            
                login=input("Login: ")
                mpd=input("PWD: ")
                pwd=login.split("@")[0]+"&"+str(mpd)
                file=open("Authentification.txt")
                user=file.read().split('\n') 
                element_recherche=f"Login&pwd: {pwd}"
                n=len(Authdic.keys())
                if element_recherche in user:
                    file.close()
                    n=n+1
                    login="Login"+str(n)
                    Authdic[login]=pwd
                    print(Authdic)
                    menuB()
                else:
                    print("Il faut s'enregistrer avant de s'authentifier")

            else:
                print(f"Le fichier Authentification.txt n'existe pas.")
        
            choixB= input("Choisir(B1,B2,B3) : ")
            match choixB:
                case "B1":
                    menuB1()
                case "B2":
                    menuB2()
                case "B3":
                    # menuP()
                    exit
        case "C":
            break
            