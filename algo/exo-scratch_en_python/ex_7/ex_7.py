"""
Exercice 7 - Liste des diviseurs d'un nombre
Vous demanderez la saisie d'un nombre puis vous ajouterez dans une liste tous les diviseurs de ce nombre.

Pour cet exercice vous utiliserez le modulo.
"""
list=[]
number=int(input("donnez un nombre:"))
for i in range(1,number+1):
  if number%i==0:
    list.append(i)
len= len(list)
print("lest diviseurs de:"+str(number)+"sont:"+ str(list)+".")
print("il y en a donc "+str(len)+" au total.")