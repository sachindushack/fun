import random
from os import system
import time

red='\033[1;91m'
green='\033[1;92m'
yellow='\033[1;93m'
purple='\033[1;95m'
cyan='\033[1;96m'
blue='\033[1;94m'
white='\033[1;97m'

name = input ('Enter Your name : ')
title = name.title()
time.sleep(5)
system('clear')
print (green,'Hello ' + name + '!\n',white)
print ('')
print ('simple login ')
print ('')

log_ask = input("are you want to run this script 'y'/'n' <: ")
time.sleep(0.3)
if log_ask == 'y':

	first_name = input(green + 'First Name <: ' + white) 
	last_name = input(green + 'Last Name <: ' + white)
	print ('')
	birth_year = input(green + 'Birth Year <: ' + white)
	birth_month = input(green + 'Birth Month <: ' + white)
	birth_day = input(green + 'Birth Day <: ' + white)
	rand = random.randint(1,999)
	email_address = (f'{first_name}{last_name}{rand}@gmail.com')
	password = input(green + 'Enter your password <: ' + white)
	print ('')
	print (f'Hello {name} Your email adress \n>> {green}{email_address}{white} <<\n Password >>{green} {password} {white}<<')
	remember = input ("Are you remembar Email and Password 'y'/'n: ")
	time.sleep(0.3)
	if remember == 'y':
		time.sleep(10)
		system('clear')
		login_acc = input(green + "Are sure want to log in fb account 'y'/'n' : " + white)
		if login_acc == 'y':
			print ('Log in ...')
			fb_email = input(green + 'Enter Your Email <: ' + white)
			if fb_email == email_address:
				fb_pass = input(green + 'Enter your password <: ' +white)
				if fb_pass == password:
					print (cyan + 'Login succec' + white)
					print ('')
					print (f'{green}Name : {cyan}{first_name} {last_name}{white}')
					print (f'{green}Birthdate : {cyan}{birth_year}/{birth_month}/{birth_day}{white}')
					print ('')
					time.sleep(5)

					system('pkg install cmatrix')
					system('clear')
					time.sleep(0.9)
					system('cmatrix')
					time.sleep(0.3)
					system('exit()')



				else:
					print (red + 'password incorrect' + white)
					time.sleep(0.3)
					system('exit()')
			else:
				print (red + 'invalid email' + white)
				time.sleep(0.4)
				system('exit()')

		elif login_acc == 'n':
			print (green + 'Bye see you next time '+ white)
			time.sleep(0.5)
			system('exit()')
		else:
			print (red + 'invalid option ' + white)
			time.sleep(0.5)
			system('exit()')

	else:
		print ('should remambar it')


elif log_ask == 'n':
	print (f'{green}  Bye ! {name} { white}')
