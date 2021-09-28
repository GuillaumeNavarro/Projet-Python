for x in range(25):
  print("*",end="")
print("1.2 Afficher 25 étoiles « * » sur une ligne (avec une boucle )")

for x in range(21,145):
  print(x)
print ("---------------------")

a = 0
resultat = 0
phrase = "le carré de %s et %s"

for i in range(1,41):
 
  a=a+1
  resultat = a**2
  print ( phrase % (a,resultat))

print("")
print ("1.5 Calculer la somme de tous les entiers de 21 à 145 puis l’afficher")
print("")

y = 21
resultat = 0
somme = 0 

for x in range(21,145):
  
 somme = somme + x
 print (somme)
 
print ("Calculer 35! (factorielle).")  
print("")

 
n = 35
fact = 1
  
for i in range(1,n+1):
    fact = fact * i
      
print ("The factorial of n is : ",end="")
print (fact)

print ("1.7 Afficher un triangle rectangle composé d'étoiles « * » dont la largueur du côté est 15 * :")
print("")


for x in range(15):
  
  print("*")
  
  for x in range(x+1):
  
    print("*",end="")
      
print("")

print("")






dico ={
  "computer" : ("ordinateur"),
    
  "mouse" : ("souris"),

  "keyboard" : ("clavier"),

  "test" : ("Pierre louis"),

 }


reset = "o"

while (reset == "o"):
  
  mot = input('Entrez le mot : ')


  computer = dico[mot]
  mouse = dico[mot]
  keyboard = dico[mot]



  phrase = 'le mot traduit est %s'

  print ( phrase % (dico[mot]))
  reset = input('Voulez vous continuer ? o/n :')

fin = len(dico[mot])
print (fin)