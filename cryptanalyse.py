import fichier
import cipher 
import time
import sys
import os
def clear():
     os.system('cls' if os.name == 'nt' else 'clear')

########################################################################################################

clear()
n=len(sys.argv)
if((n<=2) or (n>=4)):
    #print("run by using command :\npython CSV2LATEX.py  <./path/file1.csv> <./path/file2.csv> <..> ...\n")
      sys.exit("run by using command :\npython cryptanalyse.py  <n:NGRAMME> <./path/texte.txt> \n")

########################################################################################################

cle_de_cryptage="WQAZSXCDERFVTYGHBNUJIKPLOM"
NBITERGLOB= 3000
NBITERSTATIC = 1500
path_stats = "./stats_EN/"
score = 0

################################################################################################

def cryptanalyse(text,n,cle_depart,fitness,compare):
    dictionnaire=cipher.ngram(n,path_stats)
    dic1=cipher.ngram(1,path_stats)
    key=cipher.hillClimbing(fitness,text,dictionnaire,NBITERGLOB,NBITERSTATIC,cle_depart,compare)
    print("cle obtenu : "+key)
    print("\nSCORE OBTENU : " +str(fitness(cipher.decipher(text,key),dictionnaire)))
    print("corélation : " +str(cipher.fitness2(cipher.decipher(text,key),dic1)))

    return key

################################################################################################

def comp1 (x,y):
    return x<y

################################################################################################

alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
text=fichier.NETTOYER_lire_fichier(sys.argv[2])
tps1 = time.time()
key=cryptanalyse(text,int(sys.argv[1]),alphabet,cipher.fitness1,comp1)
tps2 =  time.time()
print("time : "+str(tps2-tps1))
print(fichier.lire_fichier("./text/textDECHIFRE.txt"))

########################################################################################################




    




