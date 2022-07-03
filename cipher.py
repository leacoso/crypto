import fichier 
import math 
import random 
import numpy as np #pip install numpy 
import matplotlib.pyplot as plt #python -m pip install -U matplotlib

########################################################################################################

def encipher(text ,cle):
    res=""
    c=''
    for c in text:
        res+=cle[ord(c)-65]
    return res 

########################################################################################################

def decipher(ctext ,cle):
    res=""
    c=''
    for c in ctext:
        res+=chr(cle.index(c)+65)
        
    return res  

########################################################################################################

def genKey(cle,c):
    if(cle==""):                                    # Cas de base: generation d'une cle
        res="".join(random.shuffle(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")))
        
    else:                                           # Modification de la cle existante
        l=list(cle)
        for i in range(0,c): 
            r1=1
            r2=1
            while(r1==r2):         
                r1=random.randint(0,25)
                r2=random.randint(0,25)
            
            tmp=l[r1]
            l[r1]=l[r2]
            l[r2]=tmp
        res = "".join(l)    
        
    return res

########################################################################################################

def fitness1(text,dictionaire): 
    n=dictionaire["-n"]
    res=0
    liste=list(text)
    for x in range(len(text)-n):
        res+=math.log2(dictionaire.get("".join(liste[x:x+n]),10))
    return res

########################################################################################################

def fitness2(text,dico_langue):  
    dico_text = dict_mono_grams_de_texte(text)
    x=[v for k, v in dico_text.items() if k!="-n"]
    y=[v for k, v in dico_langue.items() if k!="-n" ]
    r = np.corrcoef(x, y)
    return r[0][1]
    
########################################################################################################

def compare_cle(c1,c2):
    cmp=0
    cl1=list(c1)
    cl2=list(c2)
    for i in range(0,26):
        if(cl1[i]==cl2[i]):
            cmp+=1
    return cmp

########################################################################################################

def ngram(n,path):
    d = dict()
    d=fichier.lire_ngrame(path+str(n)+"grams.txt")
    return d

########################################################################################################

def dict_mono_grams_de_texte(text): # On construit un dictionnaire avec l'occurence de chaque lettre dans le texte 
    dico = dict()
    alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for s in alphabet:
        dico[s]=0
    for i in text : 
        dico[i]+=1
    dico["-n"]=1
    return dico

########################################################################################################  
  
def hillClimbing(fitness,text,dictionnaire,NBITERGLOB,NBITERSTATIC,cle):
    scorePar=0
    cmpS=0   
    if cle == "":                                        # Compteur stationaire                                           
        clePar=genKey(cle,1)
    else : 
        clePar = cle
    deciphered=decipher(text,clePar)
    score_init=fitness(text,dictionnaire)                # Score du texte chiffré initial
    scorePar=fitness(deciphered,dictionnaire)
    i=0
    while i<NBITERGLOB and cmpS<NBITERSTATIC:
        cleEnf=genKey(clePar,1)
        deciphered=decipher(text,cleEnf)
        scoreEnf=fitness(deciphered,dictionnaire)
        if((scorePar) < (scoreEnf)):
            scorePar=scoreEnf
            clePar=cleEnf
            cmpS=0
        else:                                       # Cas sans progression
            cmpS+=1
        i+=1
    #print("\nTEXTE CHIFFRE : \n"+text+"\n\n  Score initial : "+str(score_init)+"\n")
    #print("\nTEXTE DECHIFFRE : \n"+decipher(text,clePar)+"\n\n  Score final :  "+str(scorePar)+"\n  Cle appliquee : "+clePar)
    #fichier.ecriture_fichier("./text/textDECHIFRE.txt",decipher(text,clePar)+"\n Avec la cle :\n"+clePar)
    return clePar

########################################################################################################

def courbe(fitness,text,dictionnaire,NBITERGLOB,NBITERSTATIC,cle):
    n = dictionnaire["n"]
    plt.title("score en fonction des itérations des "+str(n)+"-gram")
    liste1 = []
    liste2 = []
    scorePar=0
    cmpS=0                                          # Compteur stationaire
    clePar=genKey(cle,1)
    deciphered=decipher(text,clePar)
    score_init=fitness(text,dictionnaire)                # Score du texte chiffré initial
    scorePar=fitness(deciphered,dictionnaire)
    i=0
    while i<NBITERGLOB and cmpS<NBITERSTATIC:
        cleEnf=genKey(clePar,1)
        deciphered=decipher(text,cleEnf)
        scoreEnf=fitness(deciphered,dictionnaire)
        liste1.append(i)
        liste2.append(scoreEnf)
        if(scorePar < scoreEnf):                    # La cle enfant a un meilleur score fitness que la cle parent
            scorePar=scoreEnf
            clePar=cleEnf
            cmpS=0
        else:                                       # Cas sans progression
            cmpS+=1
        i+=1
    plt.plot(liste1, liste2)
    plt.xlabel('temps')
    plt.ylabel('score')
    plt.show()
    return clePar

###################################################################################################

