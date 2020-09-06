#!/usr/local/bin/python3
"""
Demoprogramm: Statistik ueber Buchstaben
HackerSchool 2020
"""

from string import ascii_uppercase

class Counter(dict):
    def __missing__(self, key):
        return 0

stat = Counter()
cipher = "oXN 9kG XytGx6h4XGGXht sGt e4t"

for i in cipher:
    stat[i] += 1

sorted_stat = sorted(stat.items(), key=lambda x: x[1], reverse=True)

print(sorted_stat)

