# Déclaration des fonctions dans cette bibliothèque
"""*********************************** 

Nom Programme : Exercice N 

Auteurs : 

      Nom Etudiant1 

      Nom Etudiant2 

Classe : CII-2-SIIR-D 

***********************************"""
def menuP():
     print("--------|      Menu Principal             |---------")
     print("                   A-Enregistrement")
     print("                   B-Authentification")
     print("                   C-Quitter")

def menuA():
     print("--------|    Menu A : Enregistrement     |---------")
     print("           A1-Sauvegarder Données utilisateur")
     print("           A2-Lire Données utilisateur")
     print("           A3-Revenir au menu principal")

def menuB():
     print("--------|    Menu B : Authentification     |---------")
     print("           B1-Hachage")
     print("           B2-Chiffrement")
     print("           B3-Revenir au menu principal")

def menuB1():
    print("--------|    Menu B1 : Hachage     |---------")
    print("           B1-a Hacher un message par MD5")
    print("           B1-b Hacher un message par SHA256")
    print("           B1-c Hacher un message par blake2b")
    print("           B1-d Cracker un message Haché")
    print("           B1-e Revenir au menu principal")

def menuB2():
     print("--------|    Menu B2 : Chiffrement     |---------")
     print("           B2-a Cesar")
     print("              B2-a1 Chiffrement message")
     print("              B2-a2 Déchiffrement message")
     print("              B2-a3 Revenir au MenuB2")
     print("           B2-b Affine")
     print("              B2-b1 Chiffrement message")
     print("              B2-b2 Déchiffrement message")
     print("              B2-b3 Revenir au MenuB2")
     print("           B2-c RSA")
     print("              B2-c1 Chiffrement message")
     print("              B2-c2 Déchiffrement message")
     print("              B2-c3 Signature")
     print("              B2-c4 Verification signature")
     print("              B2-c5 Revenir au MenuB2")
     print("           B2-d Revenir au menu principal")
    
def SauvegarderUtilisateur(id,login,pwd,classe):
     file=open("Authentification.txt","a")
     file.write(f"\nId_user: {id}\n")
     file.write(f"Login&pwd: {pwd}\n")
     file.write(f"Classe: CII-2-SIIR-{classe}\n")
     file.write(f"Email: {login}\n")
     file.close()

def LireUtilisateur():
     file=open("Authentification.txt")
     user=file.read().split('\n\n') 
     print(user[len(user)-1])
     file.close()
