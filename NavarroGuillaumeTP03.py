print ("1.1 Modifier une liste")
print ("")

annee = ['Janvier','Février','Mars','Avril','Mai','Juin','Juillet','Août','Septembre',10,11,12]



x= 0

while x < 3:
  annee.remove(len(annee))
  x+=1
  print (annee)

print ("")
print ("1.1.2 Puis rajoutez les mois 'Octobre', 'Novembre', 'Décembre' à la fin")
print ("")



annee.append("octobre")
annee.append("novembre")
annee.append("decembre")
print (annee)

annee = ['Janvier','Février','Mars','Avril','Mai','Juin','Juillet','Août','Septembre',10,11,12]

x= 0

while x < 3:
  annee.remove(len(annee))
  x+=1
  print (annee)


a = "octobre"
b = "novembre"
c = "decembre"

annee.extend([a,b,c])
print (annee)

print ("")
print ("1.1.4 Pour aller plus loin : la liste ‘en compréhension’")
print ("")

x = [1, 2, 3, 4, 3, 5, 3, 1, 3, 2]
resultat = [y+1 for y in x]
print (resultat)

print ("2. Tuples")
print ("")

moisDeLannee = ('Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre')

quatre = moisDeLannee [4]
print (quatre)

trouver = "Mars" in moisDeLannee

print (trouver)

print ("")
print ("3. Dictionnaires")
print ("")

age = {"pierre" : 35 , "paul" : 32 , "Jacques" : 27 , "andre" : 23}
extra = { "david" : 22, "veronique" : 21 ,"sylvie" :  30 ,"damien" : 37}

age.update(extra)


print (age)

print ("")
print ("3.2 Accéder à une valeur à partir d’une clé")
print ("")


# prenom = input('Entrez le prénom : ')
print (age["sylvie"])

print ("")
print ("3.3 Accéder à une valeur à partir d’une clé")
print ("")


#prenom = input('Entrez le prénom : ')

if "jean" in age:
  print ("true")
else:
    print ("false")

print ("")
print ("3.4 Gérer des valeurs multiples")
print ("")

club ={
"pierre durand" : (1986,1.72,70),
  
"victor dupont" : (1987,1.89,57),

"paul dupuis" : (1989, 1.60, 92),

"jean rieux" : (1985, 1.88, 77),

 }


prenom = input('Entrez le prénom : ')

nomsportif = prenom
dateNaissSportif = club[prenom][0]
poidsSportif = club[prenom][2]
tailleSportif = club[prenom][1]

phrase = 'Le sportif nommé %s est né en %s, sa taille est de %s m et son poids est de %s Kg'

print ( phrase % (nomsportif,dateNaissSportif,tailleSportif,poidsSportif))

