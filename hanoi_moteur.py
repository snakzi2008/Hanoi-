
#ce fichier n'est que le moteur et il ne permet pas d'avoir l'affichage graphique il faut lancer Hanoi.py 

########################################################################################## " moteur "
class Cellulas:
    def __init__(self, donnee: int) -> None:
        """
        la cellule de la pile 
        """
        self.donnee: int = donnee # donnee est un entier et possède la valeur donneé qui doit etre un entier 
        self.suivant: Cellulas | None = None # tout pareil pour self.donnee mais la c'est soit cellulas ou sinon c'est None # j'ai remarquer que si on a un verison ancienne de python le "|" ne marche pas il faut le remplacer par un "or" c'est la meme chose 

class Pilas:
    
    def __init__(self) -> None:
        """
        Initialise une liste chaînée vide.
        """
        self.tete: Cellulas | None = None # tete est soit cellulas ou None

    def empiler(self, nouvelle_donnee: int) -> None:
        """
        Ajoute un nouveau noeud avec la donnée spécifiee au début de la liste.

        donnee 
            nouvelle_donnee (int): La donnée à ajouter à la liste.
        """
        nouveau_noeud = Cellulas(nouvelle_donnee)
        nouveau_noeud.suivant = self.tete
        self.tete = nouveau_noeud

    def depiler(self) -> int | None:
        """
        Retire et retourne la donnée du noeud en tête de la liste.

        Returns:
            int | None: La donnée du noeud en tête de la liste, ou None si la liste est vide.
        """
        if self.tete is None:
            return None
        donnee = self.tete.donnee
        self.tete = self.tete.suivant
        return donnee

#fin du moteur 

# test du moteur 
def test_pile() -> None: 
    """
    Teste les fonctionnalités de la classe ListeChainee
    avec toute les assertions
    
    elle ne renvoie que des prints dans la console a part si ya des erreur du moteur ou elle stop la suite du programme et empeche le main de se lancer 

    """
    liste = Pilas()
    
    # Test de "l'empilasse "
    liste.empiler(10)
    assert liste.tete is not None and liste.tete.donnee == 10, "Erreur: La valeur en tête = 10"
    
    liste.empiler(20)
    assert liste.tete is not None and liste.tete.donnee == 20, "Erreur: La valeur en tête = 20"
    
    # Test" depilasse "
    valeur = liste.depiler()
    assert valeur == 20, "Erreur: La valeur dépilée == 20"
    
    valeur = liste.depiler()
    assert valeur == 10, "Erreur: La valeur dépilée == 10"
    
    valeur = liste.depiler()
    assert valeur is None, "Erreur: La liste devrait être vide après avoir dépilé tous les éléments"
    
    print("Tous les tests avec  succes. \nle moteur est fonctionelle ! ")

# fin du " moteur "
