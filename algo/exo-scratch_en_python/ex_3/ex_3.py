"""
Exercice 3 - Afficher la puissance avec une boucle
Demandez un nombre  puis une puissance à l'utilisateur.

A l'aide d'une boucle, calculer le résultat du nombre élevé à la puissance.

Par exemple 6 puissance 4 donne 1296.
"""
number= int(input("donnez un nombre:"))
power=int(input("donnez une puissance:"))
for loop in range(power):
  number=number*power
print(number)