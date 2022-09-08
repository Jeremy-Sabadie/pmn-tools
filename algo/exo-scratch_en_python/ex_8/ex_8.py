"""
Vous écrirez un programme qui demande un nombre à l'utilisateur. Afficher si le nombre est pair ou impair. Vous ferez en sorte que si l'utilisateur saisi "q" le programme s'arrête.
"""
nb=int(input("entrez un nombre:"))
if nb%2==0:
  print("votre nombre est un nombre pair!")
else:
  print("votre nombre est un nombre impair!")