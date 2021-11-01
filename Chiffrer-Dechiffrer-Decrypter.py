#!usr/bin/python3
#-----------------------------------------
#	Auteur:Rose
#	Titre: Script Chiffrement de césar
#	Date:21/05/2021
#-----------------------------------------
"""On import des différentes librairies"""
import sys
import re
"""On définie l'alphabet"""
alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']



for i in range(len(alpha)):
	"""On dédouble la liste pour éviter les erreurs"""
	alpha.append(alpha[i])

def chiffrer(lettre,alpha,nombre):
	"""Fonction de chiffrement qui prend en entrer :
		- if lettre==' ' est définie pour ne pas prendre en compte les espaces.
		- elif alpha[i]==lettre:
		permet de décale la lettre par rapport au nombre choisis.
		- return '?' Met un ? s'il y a un caractère spécial dans le message clair.
	"""
	for i in range(len(alpha)):
		if lettre==' ':
			return ' '
		elif alpha[i]==lettre:
			return str(alpha[i+nombre])
	return '?'

while True :
	reponse = input('Chiffrer(C),Déchiffrer(D),DéCrypter(DC):')
	"""Fonction de chiffrement(C),Déchiffrerement(D),DéCrypter(DC) :
		- if chiffrement(C) est définie pour ne pas prendre en compte les
		espaces.
			Entrez le message en clair et le message s'affiche chiffré avec le
			décalage précédement définie.

		- elif Déchiffrerement(D)
			Entrez le message chiffré et cela teste toute les possibilités
			possible.

		- elif DéCrypter(DC)
			Affiche le mot déchiffré avec le nombre de décalage et le mot trouvé
			dans le dictionnaire.
	"""
	if reponse == "C":
		resultat = str()
		mess_clair = input('Entrez votre message:\n')
		nombre = int(input('Entrez votre nombre : '))
		for lettre in mess_clair:
			resultat += chiffrer(lettre,alpha,nombre)
		print('CLAIR :' ,mess_clair)
		print('CHIFFRER :',resultat)
		break

	elif reponse =="D":
		mess_clair = input('Entrez votre message:')
		nombre = int()
		for nombre in range(1,26):
			mess_dechiffre = str()
			for lettre in mess_clair:
				mess_dechiffre += chiffrer(lettre,alpha,nombre)
			print(mess_dechiffre)
		break

	elif reponse =="DC":
		mess_chiffre= input('Entrez votre message chiffré:')
		nombre = int()
		for nombre in range(1,26):
			mess_dechiffre = str()
			resultat = str()
			tota = list()
			mot = list()
			for lettre in mess_chiffre:
				resultat += chiffrer(lettre,alpha,nombre)
				if len(mess_chiffre) == len(resultat):
					tota = [resultat]
					dico = open("liste_francais.txt", "r")
					lignes = dico.readlines()
					for line in lignes :
						mot = [line.strip()]
						for i in range(len(mot)):
							for x in range(len(tota)):
								if mot[i] == tota[x]:
									print('La clef est de',nombre,'\nLe mot du dico:' ,mot[i],'\nVotre mot déchiffré:', tota[x])
							dico.close()
							break
