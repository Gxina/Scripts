#!/usr/bin/python3
#-----------------------------------------
#	Auteur:Rose
#	Titre: API web « info césar » en Python à l’aide de la bibliothèque aiohttp.
#	Date:21/05/2021
#-----------------------------------------
"""On import des différentes librairies"""
import sys
import re
from aiohttp import web
from requests import get
from scapy.layers.inet import traceroute
"""On définie l'alphabet"""
alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
routes = web.RouteTableDef()
for i in range(len(alpha)):
	"""On dédouble la liste pour éviter les erreurs"""
	alpha.append(alpha[i])

def chiffrer(lettre,alpha,nombre:int()):
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


@routes.get(r'/chiffrer/{message}:{clef}')
async def chiffrer_handler(request):
	"""Fonction de chiffrement:
	http://localhost:8080/chiffrer/{message}:{clef}
	(exemple:http://localhost:8080/chiffrer/abc:2 ==> sorie : cde )

			Entrez le message en clair et le message s'affiche chiffré avec le
			décalage précédement définie dans URL.
	"""
	for i in range(len(alpha)):
		alpha.append(alpha[i])

	resultat = str()
	mess_clair = request.match_info['message']
	nombre = int(request.match_info['clef'])
	for lettre in mess_clair:
		resultat += chiffrer(lettre,alpha,nombre)

	data = {'Message clair:': mess_clair, 'Resultat': resultat}

	return web.json_response(data)

@routes.get(r'/dechiffrer/{message}')
async def dechiffrer_handler(request):
	"""Fonction de dechiffrer:
	http://localhost:8080/dechiffrer/{message}
	(exemple:http://localhost:8080/chiffrer/cde ==> sortie : abc )

			Entrez le message chiffré et le message s'affiche en chiffré avec les
			sortie déchiffréallant de 1 à 26.

	"""

	mess_chiffre= request.match_info['message']
	nombre = int()
	tota=str()
	mess_dede = list()

	for nombre in range(1,26):
		mess_dechiffre = str()

		for lettre in mess_chiffre:
			mess_dechiffre += chiffrer(lettre,alpha,nombre)
		mess_dede.append(mess_dechiffre)

	data = {'Message d entree:': mess_chiffre, 'Resultat': mess_dede}
	return web.json_response(data)

@routes.get(r'/decrypter/{message}')
async def decrypter_handler(request):
	"""Fonction de decrypter:
	http://localhost:8080/decrypter/{message}
	(exemple:http://localhost:8080/decrypter/cde
	==> la clef :24, Le mot du dico:abc,Votre mot déchiffré:abc )

			Entrez le message chiffré et le message s'affiche en déchiffré avec
			le nombre de clef avec le mot du dictionnaire.
			ATTENTION si le mot n'est pas dans le dictionnaire rien en s'affiche.
	"""

	mess_chiffre= request.match_info['message']
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
								data = {'La clef est de':nombre,'\nLe mot du dico:':mot,'\nVotre mot déchiffré:': tota}
								return web.json_response(data)
						dico.close()

def main():
	app = web.Application()
	app.add_routes(routes)
	web.run_app(app)


if __name__ == "__main__":
	main()
