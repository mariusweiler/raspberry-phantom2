# -*- coding: utf-8 -*-

# import des fonctions pour la gestion des capteurs
from captormanagement import *
# import de la fonction pour faire gerer le buzzer
from buzzer import *
# import des fonctions de controle de vol pour le drone
from flightcommand import *
# import des fonctions de temps pour faire des pauses
import time
# import des fonctions d'open cv
import cv2

from communicationManagement import socketCommManagement

import Queue


from flightserver import *
# Declaration des variables du script
## Variable permettant de savoir si on a déjà tiré.
tireffectuer=False;
## variable permettant de connaitre la position du milieu de l'image pour aligner la cible
valeurmillieu=206;
## variable permettant de savoir si l'atterrissage a été effectué
atterrissageok=0;
## variable gardant le thread de commande de vol
fc = flightcommand();
# initialisations en début de script
## initialisation du buzzer
initialisebuzzer();

sfs=socketFlightServer();
laqueue=Queue();
scm=socketCommManagement();
scm.init(laqueue);
scm.start();

# initialisation de la camera
camera = PiCamera()
rawCapture = PiRGBArray(camera)

# PHASE -1 - PREPARATION DU VOL
## on écrit à l'écran
lcdWrite('Demarrage du drone d attaque.');
## on attend 4 secondes
time.sleep(4);
fc.stabiliser();
lcdWrite('Calibrez le GPS, puis appuyez sur le btn');
## on attend que l'utilisateur presse sur le bouton
waitButtonPress();
## on stabilise le drone, afin d'envoyer les commandes du mode "repos" avant de pouvoir l'allumer

lcdWrite('Appuyez sur le btn pour demarrer.');
waitButtonPress();
lcdWrite('Cest parti mon KIKI !');
time.sleep(1);
lcdWrite('Reculez - demar. dans 3');
time.sleep(1);
lcdWrite('Reculez - demar. dans 2');
time.sleep(1);
lcdWrite('Reculez - demar. dans 1');
time.sleep(1);
# PHASE 0 - ALLUMAGE DU DRONE
lcdWrite('Attaque en cours - Allumage');
fc.allumerEteindreDrone();
time.sleep(5);

# PHASE 1 - DECOLLAGE DE QUELQUE METRE
lcdWrite('Attaque en cours - Decollage');
fc.decollage(5);
time.sleep(1.5);
fc.stabiliser();


while not tireffectuer:
# PHASE 2 - STABILISATION ALTITUDE A 1M50 ET GYROSCOPE
    lcdWrite('Attaque en cours - Stabil.')
    fc.decollage(10);
    sfs.waitHeightOk();
    fc.stabiliser();

# PHASE 3 - RECHERCHE ET ALIGNEMENT DE CIBLE
    lcdWrite('Attaque en cours - Recherche.')
    # grab an image from the camera
    
    
    # Utilisation de la fonction pour détecter une personne
    # et stockage de son retour dans la variable rectangle
    laqueue.put('1');
    rect=sfs.getPersonPosition();
    ## Stockage des variables du premier rectangle (le seul pris en compte)
    ## dans des variables pour une meilleure lisibilité du code
    xA = rectangle[0];
    xB = rectangle[1];
    if xA and xB == 0:
        fc.rotationDrone(0,5)
        sleep(0.7)
        fc.stabiliser();
    else:
        if xA < valeurmillieu and xB <= valeurmillieu:
            fc.rotationDrone(0,5)
            sleep(0.7)
            fc.stabiliser();
        elif xA >= valeurmillieu and xB >= valeurmillieu:
            fc.rotationDrone(0,5)
            sleep(0.7)
            fc.stabiliser();
        else:
# PHASE 5 - TIR
            lcdWrite('Attaque en cours - FEUER FREI.')
            activatePistol()
    ## Le tir a ete fait, on change la variable tireffectuer    
            tireffectuer = True
    laqueue.put('0');

# PHASE 6 - ATTERRISSAGE
lcdWrite('Attaque en cours - Atterrissage.')
while not atterrissageok:
    if getAltitude() < 40:
        fc.atterrissage(3);
        time.sleep(0.3)
    else:
        fc.atterrissage(6);
        time.sleep(0.5)

# PHASE 7 - ARRET DU DRONE
lcdWrite('Attaque en cours - Arret.')
fc.allumerEteindreDrone();
laqueue.put('2');

lcdWrite('Attaque terminee...')



