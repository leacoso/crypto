import fichier
import cipher 
import time
########################################################################################################
cle_de_cryptage="AZERQSDFWXCVTGBYHNUJPMILOK"
NBITERGLOB= 4000
NBITERSTATIC = 1300
path_stats = "./stats_EN/"
score = 0
################################################################################################
def cryptanalyse(text,n,cle_depart,fitness,compare):
    dictionnaire=cipher.ngram(n,path_stats)
    dic1=cipher.ngram(1,path_stats)
    key=cipher.hillClimbing(fitness,text,dictionnaire,NBITERGLOB,NBITERSTATIC,cle_depart,compare)
    print("  Clé  cryptage : "+cle_de_cryptage)
    print("\n  Lettres correctes : "+str(cipher.compare_cle(cle_de_cryptage,key))+"/26")
    print("SCORE OBTENU : " +str(fitness(cipher.decipher(text,key),dictionnaire)))
    print("\n  Score maximal : "+str(fitness(fichier.NETTOYER_lire_fichier("./text/textCLAIRE_EN.txt"),dictionnaire))+"\n")
    print("corélation : " +str(cipher.fitness2(cipher.decipher(text,key),dic1)))

    return key

################################################################################################
def comp1 (x,y):
    return x<y
def comp2 (x,y):
    return (abs(x) > abs(y))
alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ" 

dictionnaire=cipher.ngram(1,path_stats)
text=fichier.NETTOYER_lire_fichier("./text/textCLAIRE_EN.txt")
text=cipher.encipher(text,cle_de_cryptage)
#key = cryptanalyse(text,4,"",cipher.fitness1)
tps1 = time.time()
key=cryptanalyse(text,2,alphabet,cipher.fitness1,comp1)

#print("fit2: " +str(cipher.fitness2(cipher.decipher(text,key),dictionnaire)))
tps2 =  time.time()





    




