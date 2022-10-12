from string import ascii_uppercase

"""
Formule : 
    Pour un clef (a,b) et une lettre à encoder x on a :
    ax+b=resultat_encodage
"""

def encode_affine(texte:str,clef:tuple)->str:
    """Encode un texte donné avec le chiffrement affine grâce à une clef donnée.

    Args:
        texte (str): Un texte à encoder.
        clef (tuple): Un clef sous forme d'un tuble composé de deux entiers.

    Returns:
        str: Un texte encodé.
    """    

def convertir_en_nombres(texte:str)->list:
    """Convertie un texte donnné en une liste d'entiers suivant la position des lettres dans l'alphabet.

    Args:
        texte (str): Un texte à convertir.

    Returns:
        list: Une liste d'entiers.
    """   
    res = []
    texte_en_maj = texte_en_majuscules(texte)
    for lettre in texte_en_maj:
        for i in range(len(ascii_uppercase)):
            if lettre==ascii_uppercase[i]:
                res.append(i)

def texte_en_majuscules(texte:str)->str:
    """Retourne le texte donné en majuscules.

    Args:
        texte (str): Un texte à mettre en majuscules.

    Returns:
        str: Un texte en majuscules.
    """    
    res = ""
    for lettre in texte:
        res+=lettre.upper()
    return res