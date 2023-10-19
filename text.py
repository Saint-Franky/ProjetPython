from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15
chaine = "azerty"
def generate_key_pair():
      key = RSA.generate(2048)
      private_key = key.export_key()
      public_key = key.publickey().export_key()
     #  file=open("Signature.txt","w")

      return private_key, public_key
private_key, public_key=generate_key_pair()
def creer_signature():
    rsa_key = RSA.import_key(private_key)
    hash_chaine = SHA256.new(chaine.encode())
    signature = pkcs1_15.new(rsa_key).sign(hash_chaine)
    return signature

def verif_signature( signature):
    rsa_key = RSA.import_key(public_key)
    hash_chaine = SHA256.new(chaine.encode())
    try:
        pkcs1_15.new(rsa_key).verify(hash_chaine, signature)
        return True
    except:
        return False

sig=creer_signature()

b=verif_signature(sig)
print(b)

