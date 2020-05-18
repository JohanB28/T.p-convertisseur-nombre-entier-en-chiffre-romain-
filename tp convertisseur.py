#(nombrechoisi) permet de choisir un nombre
nombrechoisi = 20

# définition de la fontion
def nbrromain (nombrechoisi):

    nomnbr = ""

#While permet la répetition
#si nombre choisi est supérieur ou égal à 1000
#il faut ajouter au nombre la lettre M
#cette opération se répète jusqu'à l'obtention d'un nombre final
#####################################################################
    while nombrechoisi >= 1000 :                                  #
        nomnbr += "M"                                             #
        nombrechoisi -= 1000                                      #
#####################################################################
    if nombrechoisi >= 900 :                                      #
        nomnbr += "CM"                                            #
        nombrechoisi -= 900                                       #
#####################################################################
    if nombrechoisi >= 500 :                                      #
        nomnbr += "D"                                             #
        nombrechoisi -= 500                                       #
#####################################################################
    if nombrechoisi >= 400 :                                      #
        nomnbr += "CD"                                            #
        nombrechoisi -= 400                                       #
#####################################################################
    while nombrechoisi >= 100 :                                   #
        nomnbr += "C"                                             #
        nombrechoisi -= 100                                       #
#####################################################################
    if nombrechoisi >= 90 :                                       #
        nomnbr += "XC"                                            #
        nombrechoisi -= 90                                        #
#####################################################################
    if nombrechoisi >= 50:                                        #
        nomnbr += "L"                                             #
        nombrechoisi -= 50                                        #
#####################################################################
    if nombrechoisi >= 40:                                        #
        nomnbr += "XL"                                            #
        nombrechoisi -= 40                                        #
#####################################################################
    while nombrechoisi >= 10:                                     #
        nomnbr+= "X"                                              #
        nombrechoisi -= 10                                        #
#####################################################################
    if nombrechoisi == 9:                                         #
        nomnbr += "IX"                                            #
        nombrechoisi -= 9                                         #
#####################################################################
    if nombrechoisi >= 5:                                         #
        nomnbr += "V"                                             #
        nombrechoisi -= 5                                         #
#####################################################################
    if nombrechoisi == 4:                                         #
        nomnbr += "IV"                                            #
        nombrechoisi -= 4                                         #
#####################################################################
    while nombrechoisi > 0:                                       #
        nomnbr += "I"                                             #
        nombrechoisi -= 1                                         #
#####################################################################


#Print permet l'affichage du résultat sous forme de nombre romain
    print(nomnbr)

#rappel de la définition (chiffreromain)
nbrromain(nombrechoisi)
