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

    # On établit le gain du joueur
    if gagnant == nombre:
        print('Bravo vous avez gagné',mise * 36,'€ !')
        argent += mise*36
    elif gagnant %2 == nombre %2:
        print('Vous avez misé sur la bonne couleur vous gagné',mise*2,'€ !')
        argent += mise*2
    else:
        print ('Désolé vous avez perdu')
        argent -= mise
    

    # On interrompt la partie si le joueur est ruiné
    if argent <= 0:
        print ('Vous êtes pauvre')
        continuer=False
    else: 
        print ('Vous avez maintenant',argent,'€')
        quitter = input("Voulez vous quitter la table (o/n) ?")
        if quitter == 'o' or quitter == 'O':
            print('Vous quittez le casino')
            continuer=False
