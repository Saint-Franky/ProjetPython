# Déclaration des fonctions dans cette bibliothèque
"""*********************************** 

Nom Programme : Exercice N 

Auteurs : 

      Nom Wadhah Salhi 

      Nom Eya Ben Aouicha 

Classe : CII-2-SIIR-D 

***********************************"""
import hashlib
# import Crypto
import random
import math
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256

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
     print("           B2-b Affine")
     print("           B2-c RSA")
     print("           B2-d Revenir au menu principal")

def menuB2A():
      print("              B2-a1 Chiffrement message")
      print("              B2-a2 Déchiffrement message")
      print("              B2-a3 Revenir au MenuB2")

def menuB2B():
     print("              B2-b1 Chiffrement message")
     print("              B2-b2 Déchiffrement message")
     print("              B2-b3 Revenir au MenuB2")

def menuB2C():
     print("              B2-c1 Chiffrement message")
     print("              B2-c2 Déchiffrement message")
     print("              B2-c3 Signature")
     print("              B2-c4 Verification signature")
     print("              B2-c5 Revenir au MenuB2")    

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

def hachage_MD5(liste,listeMD5):
     for element in liste:
       hash_md5 = hashlib.md5(element.encode())
       hash_md5_hex = hash_md5.hexdigest()
       listeMD5.append(hash_md5_hex)
       print(listeMD5)

def hachage_SHA256(liste,listeSHA256):
     for element in liste:
       hash_SHA256 = hashlib.sha256(element.encode())
       hash_SHA256_hex = hash_SHA256.hexdigest()
       listeSHA256.append(hash_SHA256_hex)
       print(listeSHA256)

def hachage_Blake2b(liste,listeBlake2b):
     for element in liste:
       hash_blake2b = hashlib.blake2b(element.encode())
       hash_blake2b_hex = hash_blake2b.hexdigest()
       listeBlake2b.append(hash_blake2b_hex)
       print(listeBlake2b) 

def calculer_hachages(mot,listeMH):
       md5_hash = hashlib.md5(mot.encode()).hexdigest()
       sha256_hash = hashlib.sha256(mot.encode()).hexdigest()
       blake2b_hash = hashlib.blake2b(mot.encode()).hexdigest()
       listeMH.append(md5_hash)
       listeMH.append(sha256_hash)
       listeMH.append(blake2b_hash)
       print(listeMH)

def chiffrement_cesar(chaine,k):
     chaine_chiff=""
     for i in chaine:
          if i.isalpha() :
               i_chiff = (ord(i) - ord("A") + k) % 26
               i_chiff = i_chiff + ord("A")
               chaine_chiff += chr(i_chiff)
          else:
               chaine_chiff += i
     print(chaine_chiff)


def chiffrement_Affine(chaine,ka,kb):
     chaine_chiff=""
     for i in chaine:
          if i.isalpha() :
               j = ord("A")
               x=ord(i) - j
               i_chiff = (ka*x + kb) % 26 + j
               chaine_chiff += chr(i_chiff)
          else:
               chaine_chiff += i
     print(chaine_chiff)

def dechiffrement_Affine(chaine,ka,kb):
     chaine_chiff=""
     for i in chaine:
          if i.isalpha() :
               j = ord("A")
               x=ord(i) - j
               i_chiff =int( (pow(ka,-1)*(x- kb)) % 26) +j
               chaine_chiff += chr(i_chiff)
          else:
               chaine_chiff += i
     print(chaine_chiff)

def generer_nbPremier(bits):
    while True:
        num = random.getrandbits(bits)
        if num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            return num

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return (x1 + m0) if x1 < 0 else x1

def generer_paireCle(bits):
    p = generer_nbPremier(bits)
    q = generer_nbPremier(bits)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randint(2, phi - 1)
    while math.gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)
    d = mod_inverse(e, phi)
    file=open("key.txt","w")
    file.write( str(e) + "," +str(n) +"\n" +str(d) +","+ str(n))
#     e: publique, d: privé

def chiffrement_RSA(msg):
     file=open("key.txt","r")
     keys=file.read().split('\n')
     e=keys[0].split(',')[0]
     n=keys[0].split(',')[1]
     print(f"e: {e}, n: {n}")
     return [pow(ord(char), int(e), int(n)) for char in msg]  

def dechiffrement_RSA(msg):
    file=open("key.txt","r")
    keys=file.read().split('\n')
    d=keys[1].split(',')[0]
    n=keys[1].split(',')[1]
    return ''.join([chr(pow(int(char), int(d), int(n))) for char in str(msg).split(",")])

def extract_public_key(private_key):
    key = RSA.import_key(private_key)
    public_key = key.publickey().export_key()
    return public_key
def generate_key_pair():
      key = RSA.generate(2048)
      private_key = key.export_key()
      public_key = key.publickey().export_key()
      return private_key, public_key
private_key, public_key=generate_key_pair()

def holy():
  def sign_string(data, private_key):
      key = RSA.import_key(private_key)
      h = SHA256.new(data.encode('utf-8'))
      signer = PKCS1_v1_5.new(key)
      signature = signer.sign(h)
      return signature
  private_key, _ = generate_key_pair()
  data_to_sign = input("Enter the string to sign: ")

  signature = sign_string(data_to_sign, private_key)
  signature_hex = signature.hex()
  print("Signature (Hexadecimal):", signature_hex)

public_key = extract_public_key(private_key)

def holy2():
     def verify_signature(data, signature, public_key):
          key = RSA.import_key(public_key)
          h = SHA256.new(data.encode('utf-8'))
          verifier = PKCS1_v1_5.new(key)
          return verifier.verify(h, signature)
     data_to_verify = input("Enter the string to verify: ")
     signature_hex = input("Enter the hexadecimal signature: ")
     signature = bytes.fromhex(signature_hex)
     if verify_signature(data_to_verify, signature, public_key):
          print("Signature est valide.")
     else:
          print("Signature est invalide.")

