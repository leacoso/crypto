import fichier 
import math 
import random 
import numpy as np
import matplotlib.pyplot as plt


coef = 0


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
        liste=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        random.shuffle(liste)
        res="".join(liste)
        
    
    else:                                           # Modification de la cle existante
        res=cle
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
    n=dictionaire["n"]
    res=0
    liste=list(text)
    for x in range(len(text)-n):
        res+=math.log2(dictionaire.get("".join(liste[x:x+n]),10))
    return res

########################################################################################################

def dict_mono_grams_texte(text): # On construit un dictionnaire avec l'occurence de chaque lettre dans le texte 
    text2 = fichier.nettoyer_texte(text)
    dico = dict()
    res = text2
    for i in res : 
        if i not in dico : 
            dico[i]=1
        else :
            dico[i]= dico[i]+1
    return dico

def dict_mono_grams_fichier(nomfichier): 
    text = fichier.NETTOYER_lire_fichier(nomfichier)
    return dict_mono_grams_texte(text)
########################################################################################################

def fitness2(text,dico_langue):  
    calcul_coef(dico_langue) 
    dico_text = dict_mono_grams_texte(text)
    s1 = 0
    s2 =0
    moyenne1= 0
    moyenne2= 0
    nb1=0
    nb2=0
    finale = 0

    for lettre in dico_text: 
        
        moyenne1 = moyenne1 + dico_text[lettre]
        nb1=nb1+1
    
    for lettre in dico_langue: 
        if lettre != "crypto" and lettre != "n":
            moyenne2 = moyenne2 + dico_langue[lettre]
            nb2=nb2+1

    
    moyenne1=moyenne1/nb1
    moyenne2=moyenne2/nb2
    
    for i in dico_langue: 
        if i not in dico_text: 
            if i!='n' and i!='crypto':
                s1 = s1 - moyenne1*(dico_langue[i]-moyenne2)
                s2 = s2+ (moyenne1)**2
        else:
            s1 = s1 + (dico_text[i]-moyenne1)*(dico_langue[i]-moyenne2)
            s2 = s2+ (dico_text[i]-moyenne1)**2
    
    finale = s1/(math.sqrt(s2)*coef)
    return finale

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
    d=fichier.lire_ngrame(path+str(n )+"grams.txt")
    return d

########################################################################################################  
  
def hillClimbing(fitness,text,dictionnaire,NBITERGLOB,NBITERSTATIC,cle):
    
    scorePar=0
    cmpS=0   
    if cle == "":                                        # Compteur stationaire                                           
        clePar=genKey(cle,1)
    else : 
        clePar = cle
    print("CLE DEBUT = "+cle)
    deciphered=decipher(text,clePar)
    score_init=fitness(text,dictionnaire)                # Score du texte chiffré initial
    scorePar=fitness(deciphered,dictionnaire)
    i=0
    while i<NBITERGLOB and cmpS<NBITERSTATIC:
        cleEnf=genKey(clePar,1)
        deciphered=decipher(text,cleEnf)
        scoreEnf=fitness(deciphered,dictionnaire)
        if(scorePar < (scoreEnf)):
            #print("on change de score,SCORE = "+str(scoreEnf)+" la nouvelle clé est "+cleEnf )# La cle enfant a un meilleur score fitness que la cle parent
            scorePar=scoreEnf
            clePar=cleEnf
            cmpS=0
        else:                                       # Cas sans progression
            cmpS+=1
        i+=1
        

    #print("\nTEXTE CHIFFRE : \n"+text+"\n\n  Score initial : "+str(score_init)+"\n")
    print("\nTEXTE DECHIFFRE : \n"+decipher(text,clePar)+"\n\n  Score final :  "+str(scorePar)+"\n  Cle appliquee : "+clePar)
    fichier.ecriture_fichier("./text/textDECHIFRE.txt",decipher(text,clePar)+"\n Avec la cle :\n"+clePar)
   
    return clePar

########################################################################################################

def calcul_coef(dico_langue): 
    global coef
    moyenne = 0
    s = 0
    n=0
    #calcul de la moyenne
    for lettre in dico_langue: 
        moyenne = moyenne + dico_langue[lettre]
        n= n+1
    moyenne = moyenne/n
    
    for i in dico_langue : 
        if i!="n" and i!="crypto":
            s = s+ (dico_langue[i]-moyenne)**2
        
    s = math.sqrt(s)
    coef = s
    
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
    #print("\nTEXTE CHIFFRE : \n"+text+"\n\n  Score initial : "+str(score_init)+"\n")
    #print("\nTEXTE DECHIFFRE : \n"+decipher(text,clePar)+"\n\n  Score final :  "+str(scorePar)+"\n  Cle appliquee : "+clePar)
    fichier.ecriture_fichier("./text/textDECHIFRE.txt",decipher(text,clePar)+"\n Avec la cle :\n"+clePar)
    
    return clePar


###################################################################################################

