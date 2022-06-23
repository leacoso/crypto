import fichier
import cipher 
########################################################################################################
cle_de_cryptage="AZERQSDFWXCVTGBYHNUJPMILOK"
NBITERGLOB= 3000
NBITERSTATIC = 1300
path_stats = "./stats_GERMINAL/"
################################################################################################
def cryptanalyse(text,n,cle_depart):
    dictionnaire=cipher.ngram(n,path_stats)
    key=cipher.hillClimbing(cipher.fitness1,text,dictionnaire,NBITERGLOB,NBITERSTATIC,cle_depart)
    print("  Clé  cryptage : "+cle_de_cryptage)
    print("\n  Lettres correctes : "+str(cipher.compare_cle(cle_de_cryptage,key))+"/26")#
    print("\n  Score maximal : "+str(cipher.fitness1(fichier.NETTOYER_lire_fichier("./text/textCLAIRE.txt"),dictionnaire))+"\n")
    return key

def cryptanalyse2(text,n,cle_depart):
    dictionnaire=cipher.ngram(n,path_stats)
    key=cipher.hillClimbing(cipher.fitness2,text,dictionnaire,NBITERGLOB,NBITERSTATIC,cle_depart)
    print("  Clé  cryptage : "+cle_de_cryptage)
    print("\n  Lettres correctes : "+str(cipher.compare_cle(cle_de_cryptage,key))+"/26")
    print("\n  Score maximal : "+str(cipher.fitness2(fichier.NETTOYER_lire_fichier("./text/textCLAIRE.txt"),dictionnaire))+"\n")
    return key

def dessin_cryptanalyse(text,n,cle_depart):
     dictionnaire=cipher.ngram(n,path_stats)
     key =  cipher.courbe(cipher.fitness1, text,dictionnaire,NBITERGLOB,NBITERSTATIC,cle_depart)
     return key

################################################################################################

def test1(text):
    #On commence par les monogram
    key = cryptanalyse(text,3,"")
    key = cryptanalyse2(text,1,key)

    #on continue par les trigram
     
def test2(text):
    dictionnaire1=cipher.ngram(2,path_stats)
    #bigram
    key = cryptanalyse(text,2,"")
    print("  Clé  cryptage : "+cle_de_cryptage)
    print("\n clé trouvée :  "+key)
    print("\n  Lettres correctes : "+str(cipher.compare_cle(cle_de_cryptage,key))+"/26")#
    print("\n  Score maximal : "+str(cipher.fitness2(fichier.NETTOYER_lire_fichier("./text/textCLAIRE.txt"),dictionnaire1))+"\n")
    

cle="ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
text=fichier.NETTOYER_lire_fichier("./text/textCLAIRE.txt")
text=cipher.encipher(text,cle_de_cryptage)
#cryptanalyse(text,1,cle)
test1(text)









    
    

   


