"""Exercice 2 - Trouver un nombre tiré au hasard
Demandez au programme de choisir un nombre "a" au hasard entre 1 et 20.

Demandez à l'utilisateur de saisir un nombre. Comparez le nombre a avec le nombre saisi par l'utilisateur. Affichez s'il est plus grand, plus petit ou trouvé.

Vous pouvez complexifier l'exercice en comptabilisant et affichant le nombre de coups joués.
"""
from random import*
i= randint(1,20)
asked=int(input("donnez un nombre:"))
if asked<i:
  print("Plus petit!")
if asked>i:
  print("Plus grand!")