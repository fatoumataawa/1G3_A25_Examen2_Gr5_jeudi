import pytest
from debogage_mot_long import mot_plus_long, pourcentage_mots_max  # Remplacer par le nom de ton fichier

#def mot_plus_long(liste_mots):
   # """
 #   Retourne le mot le plus long d'une liste.
  #  Ignore les éléments qui ne sont pas des chaînes de caractères.
#
 #   :param liste_mots: liste de mots
  #  :return: le mot le plus long ou None si la liste est invalide ou vide
 #   """

# ============================
# Tests pour mot_plus_long
# ============================
# TODO: Tests unitaires pour la fonction mot_plus_long (maximum 5 différents)
def mot_plus_long(mot1:str, mot2:str, )->str:
 @pytest.mark.parametrize("mot1, mot2, resultat_attendu", [
        ("poney", "girafe", "girafe"),
        ("hippopotame", "chien", "hippopotame"),
        ("chaton", "chat", "chaton"),
        ("ours", "crocrodile", "crocrodile"),
        ("éléphant", "tigre", "éléphant")
       ])

def test_mot_plus_long(mot1, mot2, resultat_attendu, fonction_a_tester=None):
    resultat = fonction_a_tester.mot_plus_long(mot1, mot2)

    assert isinstance(resultat, str)
    assert resultat == resultat_attendu

# ============================
# Tests pour pourcentage_mots_max
# ============================
def test_pourcentage_mots_max_normal():
    mots = ["poney", "girafe", "hippopotame", "chaton"]
    resultat = pourcentage_mots_max(mots, 5)

    assert resultat == 75.0

def test_pourcentage_mots_max_tous_superieur():
    """
    Lorsque tous les mots présents dépassent la taille,
    le pourcentage retourné est 100%.
    """
    # TODO: Complèter ce test unitaire.
    mots = ["pamplemousse", 42, "cacahuète", None]
    resultat = pourcentage_mots_max(mots, 8)

    assert resultat == 100

def test_pourcentage_mots_max_elements_invalides():
    mots = ["pamplemousse", 42, "cacahuète", None]
    resultat = pourcentage_mots_max(mots, 8)

    assert resultat == 100.0

def test_pourcentage_mots_max_liste_vide():
    mots = []
    resultat = pourcentage_mots_max(mots, 5)

    assert resultat is None

def test_pourcentage_mots_max_tous_inferieur():
    mots = ["chat", "chien", "rat"]
    resultat = pourcentage_mots_max(mots, 5)
    assert resultat == 0.0
    """
    Lorsque tous les mots présents sont
    plus petits que la taille, le pourcentage
    retourné est 0.0%.
    """
    # TODO: Ajouter le cas de test correspondant à la description
    #       au plan de tests et complèter ce test unitaire.


def test_pourcentage_mots_max_tous_inferieur():
    mots = 7
    resultat = pourcentage_mots_max(mots, 3)

    assert resultat == None