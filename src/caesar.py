#!/usr/local/bin/python3
"""
Demoprogramm fuer Caesaren-Verschluesselung.
HackerSchool 2020
"""

def caesar(klartext, schluessel):
    """
    Verschluesselt klartext durch Verschiebung der Buchstaben um
    schluessel gemaess Caesaren-Verschluesselung.
    """

    chiffre = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    alphabet += alphabet
    for i in range(len(klartext)):
        buchstabe = klartext[i]
        stelle = alphabet.index(buchstabe)
        chiffre += alphabet[stelle+schluessel]  
    return chiffre

demoklar = "HACKERSCHOOL"
s = 4
demochiffre = caesar(demoklar, s)
print("demochiffre = ", demochiffre)
entschluesselt = caesar(demochiffre, -s)
print("entschluesselt = ", entschluesselt)
