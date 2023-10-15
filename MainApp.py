
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
                    # menuP() 
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
                else:
                    print("Il faut s'enregistrer avant de s'authentifier")

            else:
                print(f"Le fichier Authentification.txt n'existe pas.")
        
            choixB= input("Choisir(B1,B2,B3) : ")
            match choixB:
                case "B1":
                    menuB1()
                    choixB1= input("Choisir(B1-a,B1-b,B1-c,B1-d,B1-e) : ")
                    liste = ["Password", "azerty", "shadow", "hunter"]
                    match choixB1:
                        case "a":
                            listeMD5 = []
                            for element in liste:
                                hash_md5 = hashlib.md5(element.encode())
                                # Récupérer la représentation hexadécimale du hachage
                                hash_md5_hex = hash_md5.hexdigest()
                                listeMD5.append(hash_md5_hex)
                                print(listeMD5)
                        case "b":
                            listeSHA256 = []
                            for element in liste:
                                hash_sha256 = hashlib.sha256(element.encode())
                                hash_sha256_hex = hash_sha256.hexdigest()
                                listeSHA256.append(hash_sha256_hex)
                            print(listeSHA256)
                        case "c":
                            listeBlake2b = []
                            for element in liste:
                                hash_blake2b = hashlib.blake2b(element.encode())
                                hash_blake2b_hex = hash_blake2b.hexdigest()
                                listeBlake2b.append(hash_blake2b_hex)
                            print(listeBlake2b) 
                        # case "d":
                        #     def calculer_hachages(mot):
                        #     md5_hash = hashlib.md5(mot.encode()).hexdigest()
                        #     sha256_hash = hashlib.sha256(mot.encode()).hexdigest()
                        #     blake2b_hash = hashlib.blake2b(mot.encode()).hexdigest()
                        #     return md5_hash, sha256_hash, blake2b_hash

                        # def trouver_indice(listeMH, mot):
                        #     h_md5, h_sha256, h_blake2b = calculer_hachages(mot)
                        #     for i, (mh_md5, mh_sha256, mh_blake2b) in enumerate(listeMH):
                        #         if h_md5 == mh_md5 and h_sha256 == mh_sha256 and h_blake2b == mh_blake2b:
                        #             return i
                        #     return None

                        # # Exemple d'utilisation
                        # liste = ["password", "azerty", "shadow", "hunter"]
                        # listeMH = []

                        # for mot in liste:
                        #     h_md5, h_sha256, h_blake2b = calculer_hachages(mot)
                        #     listeMH.append((h_md5, h_sha256, h_blake2b))

                        # # Supposons que vous ayez une listeMH contenant des hachages
                        # # Voici comment trouver l'indice du mot "azerty" parmi les hachages
                        # indice = trouver_indice(listeMH, "azerty")

                        # if indice is not None:
                        #     print(f"Le mot se trouve à l'indice {indice}")
                        # else:
                        #     print("Mot non trouvé dans la listeMH")

                case "B2":
                    menuB2()
                case "B3":
                    # menuP()
                    exit
        case "C":
            break
            