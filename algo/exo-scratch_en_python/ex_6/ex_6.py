"""
Exercice 6 - Trouver la plus grande valeur d'une liste
En partant sur la base de l'exercice précédent, vous trouverez la plus grande valeur de la liste
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
max= max(list)
print("la valeur maximale de la liste est: "+str(max)+".")