"""
Exercice 1 - Permuter des variables
Vous allez créer 2 variables a et b et leur affecter respectivement 3 et 5.

Le but de l'exercice est de permuter les valeurs des variables.

a doit avoir 5 comme valeur et b doit avoir une valeur de 3.

Quelles sont vos remarques et constatations ?
"""
a=3
b=5
tmp=b+a
b=tmp-b
a=tmp-a
print("b="+str(b)+"et a="+str(a))
