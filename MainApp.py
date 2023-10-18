
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
import hashlib

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
                    exit

        case "B":
            
                if os.path.exists("Authentification.txt"):
                    
                        login=input("Login: ")
                        mpd=getpass.getpass("PWD: ")
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
                            while True:
                                choixB= input("Choisir(B1,B2,B3) : ")
                                match choixB:
                                    case "B1":
                                        menuB1()
                                        choixB1= input("Choisir(B1-a,B1-b,B1-c,B1-d,B1-e) : ")
                                        liste = ["Password", "azerty", "shadow", "hunter"]
                                        match choixB1:
                                            case "a":
                                                listeMD5 = []
                                                hachage_MD5(liste,listeMD5)
                                            case "b":
                                                listeSHA256 = []
                                                hachage_SHA256(liste,listeSHA256)
                                            case "c":
                                                listeBlake2b = []
                                                hachage_Blake2b(liste,listeBlake2b)
                                            case "d":
                                                listeMH=[]
                                                mot=input("Entrer un mot de la liste [Password, azerty, shadow, hunter]: ")
                                                while(mot not in liste):
                                                    mot=input("Entrer un mot de la liste [Password, azerty, shadow, hunter]: ")
                                                calculer_hachages(mot,listeMH)
                                            case "e":
                                                    menuB()
                                                    False
                                    case "B2":
                                        menuB2()
                                        choixB2= input("Choisir(B2-a,B2-b,B2-c) : ")
                                        match choixB2:
                                                case "a":
                                                    menuB2A()
                                                    choixB2a= input("Choisir(a1,a2,a3) : ")
                                                    match choixB2a:
                                                         case "a1":
                                                              chaine=input("Veuillez entrer la chaine que vous voulez crypté en Cesar: ")
                                                              k=int(input("Veuillez entrer le decalage: "))
                                                              chiffrement_cesar(chaine,k)
                                                         case "a2":
                                                              chaine=input("Veuillez entrer la chaine que vous voulez crypté en Cesar: ")
                                                              k=int(input("Veuillez entrer le decalage: "))
                                                              chiffrement_cesar(chaine,-k)
                                                         case "a3":
                                                              exit
                                                case "b":
                                                    menuB2B()
                                                    choixB2b= input("Choisir(b1,b2,b3) : ")
                                                    match choixB2b:
                                                         case "b1":
                                                              chaine=input("Veuillez entrer la chaine que vous voulez crypté en Affine: ")
                                                              ka=int(input("Veuillez entrer le decalage Ka: "))
                                                              kb=int(input("Veuillez entrer le decalage Kb: "))
                                                              chiffrement_Affine(chaine,ka,kb)
                                                         case "b2":
                                                              chaine=input("Veuillez entrer la chaine que vous voulez crypté en Affine: ")
                                                              ka=int(input("Veuillez entrer le decalage Ka: "))
                                                              kb=int(input("Veuillez entrer le decalage Kb: "))
                                                              dechiffrement_Affine(chaine,ka,kb)
                                                         case "b3":
                                                              exit
                                                case "c":
                                                    menuB2C()
                                                    choixB2c= input("Choisir(c1,c2,c3,c4,c5) : ")
                                                    match choixB2c:
                                                         case "c1":
                                                              msg=input("Veuillez entrer le message a chiffrer: ")
                                                              generer_paireCle(8)
                                                              msgchiff=chiffrement_RSA(msg)
                                                              print("Le message chiffré en RSA est : "+str(msgchiff))
                                                         case "c2":
                                                                msg=input("Veuillez entrer le message a dechiffrer: ")
                                                                msgdechiff=dechiffrement_RSA(msg)
                                                                print("Le message dechiffré en RSA est : "+str(msgdechiff))
                                                         case "c3":
                                                            holy()
                                                         case "c4":
                                                              holy2()
                                                            
                                        
                        else:
                            print("Il faut s'enregistrer avant de s'authentifier")
                            
                         

                else:
                    print("Le fichier Authentification.txt n'existe pas.")
                     
               
        case "C":
            break
                