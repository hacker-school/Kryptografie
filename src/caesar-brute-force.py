#!/usr/local/bin/python3
"""
Demo für einen Brute-Force-Angriff auf eine Caesar-Verschlüsslung
HackerSchool 2020
"""

def caesar(text, schluessel):
    """
    Verschluesselt klartext durch Verschiebung der Buchstaben um
    schluessel gemaess Caesaren-Verschluesselung.
    """

    chiffre = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet += alphabet
    for i in range(len(text)):
        buchstabe = text[i]
        stelle = alphabet.index(buchstabe)
        chiffre += alphabet[stelle+schluessel]  
    return chiffre

demochiffre = "LEGOIVWGLSSP"
for i in range(27):
    print("i = ", i, " :", caesar(demochiffre, -i))
