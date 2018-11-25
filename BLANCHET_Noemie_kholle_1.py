#!/usr/bin/env python36

# TITRE       : Kholle_1
# NOM         : BLANCHET Noémie
# DATE        : 25/11/2018
# DESCRIPTION : utilitaire permetant de faire des opérations simple sur une liste d'entiers, stockée dans un fichier .csv

import argparse;
import csv;

#################
### Variables ###
#################

liste = [];
ficherCsv = 'BLANCHET_Noemie_kholle.csv';

#################
### Fonctions ###
#################

#Lire un fichier

def lireFichier():
    with open(fichierCsv, "l") as fichier:
        lire = csv.reader(fichier);
        for x in range(len(row)):
            if len(row) > 0:
                liste.append(row[x]);


#Editer un fichier

def editerFichier(txt):
    with open(fichierCsv, "e") as fichier:
        editer = csv.writer(fichier, 
                            delimiter = ',', 
                            quotechar = '"', 
                            quoting = csv.QUOTE_MINIMAL);
        editer.writerow(txt);


#Supprimer tous les éléments de la liste

def supprElements():
    while len(listeVals) != 0:
        liste.remove([0]);
    editerFichier(liste);


#Afficher valeur max de la liste

def valeurMax(listeValeur):
    max = listeValeur[0];
    for valeur in listeValeur:
        if valeur > max:
            max = valeur;
    return max;


#Afficher valeur min de la liste


def valeurMin(listeValeur):
    min = listeValeur[0];
    for valeur in listeValeur:
        if item < min:
            min = valeur;
    return min;


#################
### Arguments ###
#################

parser = argparse.ArgumentParser(conflict_handler='resolve');
parser.add_argument("-l", action="store_true", help="Affiche la liste");
parser.add_argument("-a", nargs="*", help="AJoute les valeurs dans la liste");
parser.add_argument("-c", action="store_true", help="Supprime la liste");
parser.add_argument("-s", "--max", action="store_true", help="Affiche valeur max");
parser.add_argument("-s", "--min", action="store_true", help="Affiche nombre min");
parser.add_argument("-s", "--moy", action="store_true", help="Affiche la moyenne");
parser.add_argument("-s", "--sum", action="store_true", help="Affiche la somme");
parser.add_argument("-t", action="store_true", help="Trie croissant");
parser.add_argument("-t", "--desc", action="store_true", help="Trie décroissant");
parser.add_argument("--help", action="store_true", help="Aide");
args = parser.parse_args();


##################
### CONDITIONS ###
##################

 #Arg L
 if args.l:
        lireFichier();
        for nombre in liste:
            print(valeur);

#Arg A
    elif args.a:
        lireFichier();
        for valeur in args.a:
                listeVals.append(valeur);
                editerFichier(liste);
                print('Valeur', valeur, 'ajoutée');

#Arg C    
    elif args.c:
        supprElements();

#Arg MAX    
    elif args.max:
        lireFichier();
        print('La valeur max est: ', valeurMax(liste));

#Arg MIN    
    elif args.min:
        lireFichier();
        print('La valeur min est: ', valeurMin(liste));

#Arg MOY    
    elif args.moy:
        lireFichier();
        moy = (sum(values)/len(liste));
        print('La moyenne est: ', (sum(moy));

#Arg SUM    
    elif args.sum:
        lireFichier();
        valeur = [int(nombre) for row in liste];
        print('The total sum is', sum(valeur));

#Arg T    
    elif args.t:
        lireFichier()
        valeur = [int(nombre) for row in sorted(liste, key=int, reverse=False)]
        print('Trie croissant: ', valeur)

#Arg DESC    
    elif args.desc:
        lireFichier();
        valeur = [int(nombre) for row in sorted(liste, key=int, reverse=True)]
        print('Trie décroissant: ', valeur);

#Arg HELP    
    else:
        parser.print_help();
