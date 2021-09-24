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
  
