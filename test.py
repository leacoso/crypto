import fichier
import cipher 
import time
########################################################################################################
cle_de_cryptage="AZERQSDFWXCVTGBYHNUJPMILOK"
NBITERGLOB= 4000
NBITERSTATIC = 1300
path_stats = "./stats_GERMINAL/"
score = 0
################################################################################################
def cryptanalyse(text,n,cle_depart,fitness):
    dictionnaire=cipher.ngram(n,path_stats)
    key=cipher.hillClimbing(fitness,text,dictionnaire,NBITERGLOB,NBITERSTATIC,cle_depart)
    print("  Clé  cryptage : "+cle_de_cryptage)
    print("\n  Lettres correctes : "+str(cipher.compare_cle(cle_de_cryptage,key))+"/26")
    print("SCORE OBTENU : " +str(fitness(cipher.decipher(text,key),dictionnaire)))
    print("\n  Score maximal : "+str(fitness(fichier.NETTOYER_lire_fichier("./text/textCLAIRE.txt"),dictionnaire))+"\n")
    return key

################################################################################################

cle="ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
dico = cipher.ngram(4,path_stats)
text=fichier.NETTOYER_lire_fichier("./text/textCLAIRE.txt")
text=cipher.encipher(text,cle_de_cryptage)
#key = cryptanalyse(text,4,"",cipher.fitness1)
tps1 = time.time()
key3 = cryptanalyse(text,2,"",cipher.fitness1)
key4 = cryptanalyse(text,1,key3,cipher.fitness1)
tps2 =  time.time()

def test1(text):
    cle="ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
    dico = cipher.ngram(4,path_stats)
    text=fichier.NETTOYER_lire_fichier("./text/textCLAIRE.txt")
    text=cipher.encipher(text,cle_de_cryptage)
    #key = cryptanalyse(text,4,"",cipher.fitness1)
    tps1 = time.time()
    key3 = cryptanalyse(text,1,"",cipher.fitness2)
    tps2 =  time.time()

    




