from pwn import *
import time
import itertools
import string

dictionnaire = './dictionnaire/francais.txt'

### permet de recuperer le mot suivant dans le dictionnaire
def motSuivant(f):
	return f.readline()

### permet d'essayer un mot de passe
def essaiMotDePasse(r, motDePasse):
	r.sendline(motDePasse)
	reponse = r.recvline()
	if('Rate' in reponse):
		return False
	else:
		print("Bravo, le mot de passe est bien " + motDePasse)
		return True

#le mot de passe contient des majuscules, des minuscules, et a une longueur de 4 caracteres
def AttackBruteForce(r):




	''' A COMPLETER '''	






	print("La fonction n'est pas encore implementee")

	###test d'un mot de passe
	motTest = "AAAA"	
	if(essaiMotDePasse(r, motTest)):
		return True
	return False

def AttackDictionnaire(r, d):




	''' A COMPLETER '''	





	print("La fonction n'est pas encore implementee")

	###test d'un mot de passe
	motTest = "AAAA"
	if(essaiMotDePasse(r, motTest)):
		return True
	return False

def Menu():
	print("Bienvenue\nCette application a pour but de programmer des fonctions pour trouver les mots de passes des programmes\navec les methodes de bruteforce et d'attaque par dictionnaire\nBonne chance\n")

	while(True):
		print("\n\nQue veux tu faire ?")
		print("1. Effectuer l'attaque de bruteforce")
		print("2. Effectuer l'attaque par dictionnaire")
		print("3. Quitter l'application")
		choix = input()
		choix = str(choix)[:1]
		if(choix == '1'):
			r = process('./executables/challenge1')
			start_time = time.time()
			if(AttackBruteForce(r)):
				print("Attaque reussie, bien joue !!")
				print("L'attaque a duree " + str(time.time() - start_time) + " secondes")
			else:
				print("Rate, il faut encore develloper ton programme")
			r.close()
		elif(choix == '2'):
			r = process('./executables/challenge2')
			f = open(dictionnaire, 'r')
			start_time = time.time()
			if(AttackDictionnaire(r, f)):
				print("Attaque reussie, bien joue !!")
				print("L'attaque a duree " + str(time.time() - start_time) + " secondes")
			else:
				print("Rate, il faut encore develloper ton programme")
			r.close()
			f.close()
		elif(choix == '3'):
			print("Merci d'avoir utilise cette application")
			break
		else:
			print("Choix incorrect")



Menu()
