# Zone a completer avec vos reponses


def main() :
	###### exercice 00 (la fonction est definie puis appelee dans cette zone afin de confirmer son bon fonctionnement)
	print("exercice 00 #######################")
	def exempleHello (msg):
		return "bonjour {}, comment allez-vous ?".format(msg)
	salutations = exempleHello("Michel")
	print(salutations)
	print(salutations.split(sep=" "))
 
###### exercice 01
print("exercice 01 #######################")

   

nom = "vide"
stock = 0
phrase1 = "Vous avez saisie %s prénom"
  
while nom != "$":
  nom = input('Entrez un nom : ')
  stock = stock+1
  
  

print (phrase1 % (stock))
print ("")


###### exercice 02
print("exercice 02 #######################")
t =["Mary","Patricia","Linda","Barbara","Elizabeth","Jennifer","Maria","Susan","Margaret"]


for element in t:
	print (element)
print ("")

	
###### exercice 03
print("exercice 03 #######################")
import itertools

tabRepName = ['cdrom','lib64','root','srv','mnt','snap','lost+found','tmp','run','sbin','bin','home','boot','opt','etc','swapfile','lib','var','media','usr']	
tabRepSize = [4,4,4,4,8,8,16,76,2692,15416,15872,99992,108272,116300,191872,385840,616360,647768,1308416,3357908]

reps = {'cdrom': 4, 'lib64': 4, 'root': 4, 'srv': 4, 'mnt': 8, 'snap': 8, 'lost+found': 16, 'tmp': 76, 'run': 2692,
'sbin': 15416, 'bin': 15872, 'home': 99992, 'boot': 108272, 'opt': 116300, 'etc': 191872, 'swapfile': 385840,
'lib': 616360, 'var': 647768, 'media': 1308416, 'usr': 3357908}

print (reps)
print ("")

 	
###### exercice 04
  
print("exercice 04 #######################")
	

for cle, valeur in reps.items():
  print("repertoire", cle, "taille","=" ,valeur)
  print ("")


###### exercice 05
print("exercice 05 #######################")

for cle,valeur in reps.items():
  if valeur > 10000 and valeur < 100000:
   print("repertoir",cle," : taille = ",valeur)
   print("")

###### exercice 06
print("exercice 06 #######################")

tabSize = []


for cle,valeur in reps.items():
  tabSize = tabSize = [valeur]   
  print(tabSize)
print("")


###### exercice 07
print("exercice 07 #######################")

tableau = [5,5,7,8]

def totalSize(list):
  somme = 0
  longueur = len(tableau)
  for i in range(longueur):
    somme = somme + tableau[i]
  print (somme)
  
totalSize(tableau)

	
###### exercice 08
print("exercice 08 #######################")

























			
###### exercice 09
print("exercice 09 #######################")
	
	
	###### exercice 10
print("exercice 10 #######################")
	
###### exercice 11
print("exercice 11 #######################")
	
###### exercice 12
print("exercice 12 #######################")
		

if __name__=="__main__":
	print("main()")
	main()
