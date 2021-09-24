ch = 'Esope reste ici et se repose'

print (ch)
longueur = len(ch)
print(longueur)

print("")
print ( "1.1.2 afficher le deuxième mot de la chaine ch en utilisant les crochets et une plage [x :y]" )
print("")


print (ch[6:12])


print("")
print ( "1.1.3	afficher le dernier mot de la chaine ch en utilisant les crochets et une plage [x :y]" )
print("")


print (ch[21:28])

print("")
print ("1.1.4	afficher le dernier mot de la chaine ch en utilisant les crochets et une plage [x :]")
print("")

print (ch[22:])

print("")
print ("1.1.5 afficher le caractère ‘c’ de deux manières différentes")
print("")

print (ch[13:14])
print (ch[-15])

print("")
print("1.2.1 Initialiser les chaines suivantes")
print("")

meteo = 'aujourd’hui, il fait %s , la vitesse du vent est %s ,l’humidité est %s'

tempDeg = "24°"
vitesse = "12Km/h"
humide = "45%"

print ( meteo % (tempDeg,vitesse,humide))

print("")
print ("1.2.2 Variante")
print("")

temp = "beau"
vit = "faible"
humi = "correcte"

print ( meteo % (temp,vit,humi))

print("")
print ("1.2.3 Initialiser les chaines suivantes")
print("")

chaineA = "cette chaine "
chaineB = "contient %s caractères "
chaineC = "par contre "
chaineD = "celle-ci "

long = len(chaineA + chaineB)
print(long)

longe =len(chaineA+chaineB+chaineC)

print (chaineA + chaineB % (long))

chaineY = chaineD + chaineB + chaineC


print (chaineY % (len(chaineY)))

print("")
print ("1.2.4 Autre méthode de formatage de chaines")
print("")

chaineBnew = chaineB.replace("%s","{}") 
chaineE = chaineA + chaineBnew
chaineF = chaineB + chaineBnew + chaineC

print (chaineE.format (len(chaineE)))


