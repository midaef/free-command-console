
from colorama import init, Fore, Back, Style
import time
import random
import sys
import os
import getpass
import sys
import platform
import requests


#-----------------------------------------------------
w = 50


def printkrasivo(s):
	s = printwithotstup(s)
	s = s + '\n'
	strtoprint = ''

	for i in s:
		strtoprint = strtoprint + str(i)
		sys.stdout.write('\r\r' + (strtoprint) + '')

		if i != ' ':
			time.sleep(0.01)
		else:
			pass


def printwithotstup(s):
	otstup = (w - len(s)) // 2
	return(otstup * ' ' + s)
#-----------------------------------------------------


init(autoreset=True)
printkrasivo('Free Сommand Сonsole[Version: 0.0.1]')
printkrasivo('(c)NameLess Corp (NameLess Corporation), 2018')
print('Your user: ' + Fore.RED + getpass.getuser())

while True:	
	vibor = str(input(str(os.getcwd())+' >>>'))
	vibor = vibor.rstrip()
	vibor = vibor.lstrip()

	if vibor == 'help':
		print(Fore.RED + 'Commands:')
		print('       1.system')
		print('       2.exit')
		print('       3.open')
		print('       4.write command')
		print('       5.info')
		print('       6.cls')
		print('       7.checknet')
		print('       8.wintools')
	if vibor == 'system':
		print('OS name: ' + Fore.RED + platform.system())
		print('Version: ' + Fore.RED + platform.version())
		print('Processor name: ' + Fore.RED + platform.processor())
		print('Machine type: ' + Fore.RED + platform.machine())
		print('System’s release: ' + Fore.RED + platform.release())
		print('Current directory: ' + Fore.RED + os.getcwd())
	if vibor == 'exit':
		exit()
	if vibor == 'write command':
		com = str(input('Input name of command:'))
		f = open(com + '.py', 'w')

		while True:
			f.write(input('Input code: ') + '\n')
			if input('next? ') != 'y':
				break

		f.close()
	if vibor == 'open':
		com	= str(input('Input command:'))
		os.system('python ' + com + '.py')
	if vibor == 'info':
		os.system('cls')
		printkrasivo('     _      _ _             ')
		printkrasivo(' ___| |_ __| (_) __ _ _ __  ')			
		printkrasivo('/ __| __/ _` | |/ _` | "_ \ ')
		printkrasivo('\__ \ || (_| | | (_| | | | |')
		printkrasivo('|___/\__\__,_|_|\__,_|_| |_|')
		printkrasivo('')
		printkrasivo('     _             _ _ ')
		printkrasivo('  __| | __ _ _ __ (_) |')
		printkrasivo(' / _` |/ _` | "_ \| | |')
		printkrasivo('| (_| | (_| | | | | | |')
		printkrasivo(' \__,_|\__,_|_| |_|_|_|')
		printkrasivo('                                _   ')
		printkrasivo(' _ __  _ __ ___  ___  ___ _ __ | |_ ')
		printkrasivo('| "_ \| "__/ _ \/ __|/ _ \ "_ \| __|')
		printkrasivo('| |_) | | |  __/\__ \  __/ | | | |_ ')
		printkrasivo('| .__/|_|  \___||___/\___|_| |_|\__|')
		printkrasivo('|_|                                 ')
		printkrasivo()
		printkrasivo('https://github.com/NameLessCorporation')
		printkrasivo('https://github.com/stdian')
		printkrasivo('https://github.com/DanilPresent')
		input()
		os.system('cls')
	if vibor == 'cls':
		os.system('cls')
	if vibor == 'checknet':
		ip = 'https://blockchain.info/ru/latestblock'

		for i in range(0, 4):
			req = requests.get(ip)
			print(req)

	if vibor == 'wintools':
		printkrasivo(Fore.RED + '  ███████  ' + Fore.GREEN + ' █         █')
		printkrasivo(Fore.RED + ' █████████ ' + Fore.GREEN + ' ██       ██')
		printkrasivo(Fore.RED + '███████████' + Fore.GREEN + ' ███████████')
		printkrasivo(Fore.RED + '███████████' + Fore.GREEN + ' ███████████')
		printkrasivo(Fore.RED + '███████████' + Fore.GREEN + ' ███████████')
		printkrasivo(Fore.RED + '██       ██' + Fore.GREEN + '  █████████ ')
		printkrasivo(Fore.RED + '█         █' + Fore.GREEN + '   ███████  ')
		printkrasivo(Fore.BLUE + '  ███████  ' + Fore.YELLOW + ' █         █')
		printkrasivo(Fore.BLUE + ' █████████ ' + Fore.YELLOW + ' ██       ██')
		printkrasivo(Fore.BLUE + '███████████' + Fore.YELLOW + ' ███████████')
		printkrasivo(Fore.BLUE + '███████████' + Fore.YELLOW + ' ███████████')
		printkrasivo(Fore.BLUE + '███████████' + Fore.YELLOW + ' ███████████')
		printkrasivo(Fore.BLUE + '██       ██' + Fore.YELLOW + '  █████████ ')
		printkrasivo(Fore.BLUE + '█         █' + Fore.YELLOW + '   ███████  ')
		print()
		printkrasivo('WinTools by NameLess')

		while True:
			com = input('wintools v1.0 > ')
			com = com.rstrip()
			com = com.lstrip()

			if com == 'help':
				print('1. ping')
				print('2. exit')
			if com == 'ping':
				ip = input('IP: ')
				os.system('ping ' + ip)
			if com == 'exit':
				break	
			if com == 'tree':
				d = input('Drive (ex C:) : ')
				os.system('tree ' + d + '/')
			if com == 'color':
				bg = input('color: ')
				os.system('color ' + bg)
