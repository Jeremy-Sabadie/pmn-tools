"""
Exercice 4 - Faire la somme d'une liste
Demandez la longueur de la liste à l'utilisateur puis demandez autant de fois de saisir un nombre et alimentez une liste.

Une fois cette liste crée et alimentée, faites, à l'aide d'une boucle la somme de tous les nombres de la liste.

Voir le démo de l'exercice.
"""
list=[]
items=1
result=0
len=int(input("donnez la longueur de la liste:"))
for loop in range(len):
  ask=int(input("entrez un nombre:"))
  list.append(ask)
for loop in range(len):
  a=list.index(items)
  result= items+ a
  items=items+1
print(result)
sum=sum(list)
print("la somme des valeurs de la liste est de: "+str(sum)+".")