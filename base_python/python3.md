## Création de fonction 
Pour créer une fonction on utilisera le mot clé "def" qui est l'abréviation de « define »

    def nom_de_la_fonction(parametre1, parametre2, parametre3, parametreN):
    # Bloc d'instructions
Le code pour mettre la table de multiplication par 7 dans une fonction serait donc :
``` py
def table7()
    nb=7
    i=0
    while i < 10:
        print(i+1,'*',nb,'=',(i + 1)*nb)
        i += 1
```
### L'instruction return
L'instructionreturnsignifie qu'on va renvoyer la valeur, pour pouvoir la récupérer ensuite et la stocker dans une variable par exemple. Cette instruction arrête le déroulement de la fonction, le code situé après le return ne s'exécutera pas.
``` py
def carre(valeur):
    return valeur * valeur
variable=carre(5)
```
La variable variable contiendra, après exécution de cette instruction, 5 au carré, c'est-à-dire 25.

## Les modules 
Il existe un grand nombre de modules disponibles avec Python sans qu'il soit nécessaire d'installer des bibliothèques supplémentaires. Pour cette partie, nous prendrons l'exemple du module math qui contient, comme son nom l'indique, des fonctions mathématiques.
### La méthode import
Lorsque vous ouvrez l'interpréteur Python, les fonctionnalités du module math ne sont pas incluses. Il s'agit en effet d'un module, il vous appartient de l'importer si vous en avez besoin.
    
    >>> import math

Maintenant si vous utilisez la fonction sqrt du module math par expemple , cela vous renvoie la racine carrée du nombre passé en paramètre.
    >>> math.sqrt(16)
    >>> 4

Pour voir les differentes fonctions existantes utiliser 'help' avec comme argument le module 
    >>> help('math')
###  La méthode:from … import …
Elle sert à importer uniquement certaine fonction du module,au lieu d'importer tout le module.

Admettons que nous ayons uniquement besoin, dans notre programme, de la fonction renvoyant la valeur absolue d'une variable.
    >>> from math import fabs
    >>> fabs(-5)
    5
    >>> fabs(2)
    2
    >>>
Dans notre roulette nous allons nous interesser à la fonction "randrange" du module "random", une fois celle ci importer , il nous reste plus qu'a l'utiliser pour séléctioner le nombre gagnant:
``` py
from random import randrange

# On déclare les variables de départ
argent=500
continuer= True

print ("Bienvenu à la roulette becasino vous démarrez avec",argent,"€")

while continuer:
    ## On demande à l'utilisateur d'entrer le nombre sur lequel il veut parier
    nombre = -1
    while nombre < 0 or nombre > 36:
        nombre = input("Tapez le nombre sur lequel vous voulez miser (entre 0 et 36) : ")
        ## On convertit le nombre
        try:
            nombre=int(nombre)
        except:
            print("Vous n'avez pas entré de nombre")
            nombre = -1
    ## On demande à l'utilisateur d'entrer la somme qu'il veut parier      
    mise = 0
    while mise <= 0 or mise > argent:
        mise = input("Tapez le montant de votre mise : ")
        try:
            mise=int(mise)
        except:
            print("Vous n'avez pas entré de nombre")    
            mise = 0

    # on fait tourner la roulette
        gagnant = randrange(36)
        print("La roulette tourne... ... et s'arrête sur le numéro",gagnant)
```


 <a href="python4.md">NEXT >> </a>