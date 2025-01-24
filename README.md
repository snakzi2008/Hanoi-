Ce fichier README a été crée le [24/01/2025] par [GOUNANE;Idir]
Description générale : 
Ce projet est décomposé en 4 Parties dans 2 fichiers : le moteur et les tests qui sont dans le fichier hanoi_moteur.py et la partie graphique et le lanceur qui se trouvent dans le fichier Hanoi.py 
Pour lancer le Jeu il faut lancer Hanoi.py 

Hanoi.py : fichier principale du programe il possède :

- la classe TourDeHanoi qui initialise la majorité des données pour réaliser le Jeu
- le main() qui crée la fenetre nommée fen et aussi demande le nombre de disque demander pour la résolution ( avec le calcul du nombre d'étape )
- puis les lignes test_pile() lance les assertion et test et main() le jeu

hanoi_moteur.py : fichier secondaire ( mais essentielle ) au jeu il possède : 
- une classe Cellulas pour crée les cellules
- une classe Pilas qui possède toute les methodes pour manipuler la pile
- test_pile() qui test le moteur se sont les assertions pour verifier si le moteur est fonctionelle. 

le fichier .gitignore est inutile, on peut l'enlever ( il est la car j'ai voulu utiliser github pour essayer avec un projet )
 [text](https://github.com/snakzi2008/Hanoi-NSI.git) 
 
