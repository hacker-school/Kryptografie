#!/usr/local/bin/python3
"""
Demoprogramm: Base64 Ver- und Entschluesselung
HackerSchool 2020
"""

from base64 import standard_b64encode, standard_b64decode

enc = standard_b64encode("Dies ist eine Base64 Demo.")
dec = standard_b64decode(enc)

print(enc)
print(dec)

