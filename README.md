Projet RPG Arena
Bienvenue dans le projet RPG Arena, un jeu de combat au tour par tour mettant en scène des personnages héroïques dans une arène. Ce projet est écrit en Python et utilise plusieurs fichiers pour organiser le code de manière modulaire.

Fichiers du projet

character.py : Définition de la classe de base Character et des classes dérivées Warrior, Mage, et Thief.

dice.py : Définition de la classe Dice pour simuler le lancer de dés.

engine.py : Moteur principal du jeu, initialise les personnages, les fait s'affronter et affiche les statistiques.

game.py : Interface utilisateur du jeu, gère l'interaction avec les joueurs, la sélection des personnages et l'affichage de l'état du jeu.

mage.py : Définition de la classe Mage héritant de Character, avec des méthodes spécifiques pour les attaques et les compétences.

thief.py : Définition de la classe Thief héritant de Character, avec des méthodes spécifiques pour les attaques et les compétences.

warrior.py : Définition de la classe Warrior héritant de Character, avec des méthodes spécifiques pour les attaques et les compétences.

Comment jouer


Exécutez le fichier game.py pour lancer le jeu.

Chaque joueur doit choisir un personnage parmi le guerrier, le mage et le voleur.

Les joueurs s'affrontent tour à tour, choisissant entre une attaque de base, une attaque critique (avec un risque) ou l'utilisation d'une potion.

Le jeu continue jusqu'à ce qu'un joueur soit vaincu.