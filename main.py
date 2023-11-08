#! /usr/bin/python
#coding : utf-8

#imports
from colorama import init, Fore, Back, Style
import requests
import json
import argparse
import socket
import time
import urllib3
import os
import sys

init(autoreset=True)

__author__ = "CyberPatriX-S3C"
__version__ = "1.0.3"

#--- banner
def banner():
    global __version__, __author__

    b = Fore.GREEN +"""


                                      .-=+++*****+=.                                                    
                                :**-:::...:==.-**:                 .:-====-:..                      
                              .==.  :*#**+:... .:#+            .:**+:.....:-+##=.                   
                             .::               ..:###**+=-:..:=: ......    .:..=#-.                 
                             ...  .             --#%%%%%%%####+-=*-           :=*#-                 
                             ... .:           ..-##@@@@@@@@@@@@%*.             .=##.                
                            :+*+.:= ...-+++++..:=#@@@@@@@@@@@@@@*+:.           .-##=                
                         .=###%@#:#-:....   .  .+%@@@@@@@@@@@@@%*:.            .+*#*                
                       .+##%@@@@@%#+.  .=#%%%=  -#@@@@@@@@@@@@%*:        .-. ::***#=                
                    .:*##%@@@@@@@@#+. :@@@@@@%+.-#%%%%%@@@@@@@#-           :=-####-                 
                  .:+##%@@@@@@@@@@#*:.#@@@@@@%+:+#.       .-*#+            .+####+.                 
                 .-##%@@@@@@@@@@@@%#*--=++=--.=*#*:. .. .==:*+.  .=*#*-.  .=**#####-                
                .*#%@@@@@@@@@@@@@@=*#**+++++***###@. +#. .*%*. :*@@@@@@#:.-**##%@@##*.              
               :##%@@@@@@@@@@@@#:  :*##******###@@@. +@@+ .++  .:#@@@@@@#+*##%@@@@@%#*:             
             .-##@@@@@@@@@@@@#: .-@@@@@%%%#*-.=@@@@. +@@@#.-#:    =#@@%#**#%@@@@@@@@@##-.           
            .-##@@@@@@@@@@@%- .-@@@@@@@@@%- .#@@@@@. +@@@@#:=#:..:+**##*##*@@@@@@@@@@@##-.:..       
           .:##@@@@@@@@@@@*. .+%%%%%%%%%#- .*%%%%%#. =#%%%%*.-*##*****##*. -%@@@@@@@@@@##:.:==.     
           .##@@@@@@@@@@@+.                                   .:-=*#*+-.    :%@@@@@@@@@%##.  :#+.   
           *#%@@@@@@@@@@+. *@@@@@@@@@@@= .*@@@@@@@%. =%@@@@@@%. -%@@@@@@@@%- .%@@@@@@@@@%#*.  .=*:  
          =##@@@@@@@@@@+ .*@@@@@@@@@@@# .+@@@@@@@@@. +@@@@@@@@#. *@@@@@@@@@%:..%@@@@@@@@@##+.  .-#:.
         .##%@@@@@@@@@% .+@@@@@@@@@@@@:.:%@@@@@@@@@. +@@@@@@@@@=..@@@@@@@@@@%. :@@%##*****+:.   .=*.
         -##@@@@@@@@@@: -%@@@@@@@@@@@*..+@@@@@@@@@@:=#@@%%%%%%%%@@%@@@@@@@@@@*.=*+:              :*=
        .+#%@@@@@@@@@* .+@@@@@@@@@@@@=..%@@@@@@@@@@@##************#%@@@@@@@@@@#+..+*#*+:.     :..=##
        .*#@@@@@@@@@@- :%@@@@@@@@@@@%: :@@@@@@@@@%#******************#@@@@@@@%*.  -%@@@%:     .***##
        :*#@@@@@@@@@%: :@@@@@@@@@@@@#: +@@@@@@@%*******@@@@@@@@@%*******@@@@@%#.   #@@@%-    -*##*#=
        -*#@@@@@@@@@#: :============-. :====*@%*****%@@@@@@@@@@@@@@#*****%@+==##***#%###*******###=.
      ..:*#@@@@@@@@@#: ............... ....-@%****#@@@@@@@@@@@@@@@@@@#****%#:.-##****##########*=.  
  .:::.   ..-+%%@@@@%: -@@@@@@@@@@@@#: =@@@@%****#@@@@@@@@@@@@@@@@@@@@#***#@@@%.-*##%%@@@@%#*:.     
.-*-.  .:.   ..+#@@@@: :%@@@@@@@@@@@%- :@@@@#***#@@@@@@@@@@@@@%=%@@@@@%#***%@@* .*@@@@@@@@@#*.      
=*:.  .+@@#:   .-%@@@+ .*@@@@@@@@@@@@=..#@@@****%@@@*::+@=+#:%%...:@@@@#***#@@- :%@@@@@@@@%#=.      
#=    .*@@@%=.   +%@@@. -@@@@@@@@@@@@#..=@@@****%@@@@=.-@-+#.%%:#%.*@@@#***#@# .=@@@@@@@@@##-       
++.    :*@@@#=::=*%@@@* .*@@@@@@@@@@@@- :#@@****#@@@%+=@@%=*=@@++=%@@@@#***%@. :%@@@@@@@@@#*:       
:#-  .:=*##%%#***#%@@@@= .#@@@@@@@@@@@%..=@@%****%@@@@@@@@@@@@@@@@@@@@#***#@*..*@@@@@%*#%%#+..      
.-##************##%@@@@@- .%@@@@@@@@@@@# .+@@#****%@@@@@@@@@@@@@@@@@@#****%%:.+@@@@%*: :+=.-*=      
 .:*#*********##%@@@@@@@%- .............. ..+@#****#@@@@@@@@@@@@@@@%#****#%-.*@@@@%#***#@*. :#:     
    .*###**###%@@@@@@@@@@@-. :***********-  +%@%******%@@@@@@@@@@#*******#@%%@@@@@%#**###****#=     
      ..:+*-.=#%@@@@@@@@@@@*. .*@@@@@@@@@@=. *@@@#*************************#@@@@@@@##*******##:     
             .=##@@@@@@@@@@@@=. :#@@@@@@@@@= .=@@@@%#**************#%%*******%@@@@@@%###**##*-      
              .=##@@@@@@@@@@@@%=. .+%@@@@@@@*..-%@@=*%@%%%####%%%@%+=*@%******@@@@@@##+++==:.       
                :##%@@@@@@@@@@@@@*. .:=%@@@@@%: .#@. +#:-=%@@@@*-...-%@@@#**#@@@@@%##:.             
                 .+##@@@@@@@@@@@@@@@+. ...-+@@@=..:. ...:@#=:..  -%@@@@@@@@@@@@@@##*.               
                  .-##%@@@@@@@@@@@@@@@@%=...              ...:*@@@@@@@@@@@@@@@@%##:                 
                    .=##%@@@@@@@@@@@@@@@@@@@@#*=------=+#%@@@@@@@@@@@@@@@@@@@%##=.                  
                      .=##%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%##=.                    
                        .-*##%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%##*-.                      
                          ..=###%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%###-..                        
                              .-#####%@@@@@@@@@@@@@@@@@@@@@@@@@@%####*:.                            
                                  .-**####%%%@@@@@@@@@@@@%%%#####+-.      {v}                          
                                       .:=++***########***++-:.                                



                 8""""8              8""""8                                       
                 8      e   e eeeee  8    " eeeee  eeeee eeeee  eeeee  eeee eeeee 
                 8eeeee 8   8 8   8  8e     8   8  8   8 8   8  8   8  8    8   8 
                     88 8e  8 8eee8e 88  ee 8eee8e 8eee8 8eee8e 8eee8e 8eee 8eee8e
                 e   88 88  8 88   8 88   8 88   8 88  8 88   8 88   8 88   88   8
                 8eee88 88ee8 88eee8 88eee8 88   8 88  8 88eee8 88eee8 88ee 88   8
                                                            {a}

                                       
    """ .format(v=__version__, a=__author__)

    print (b)
    
    time.sleep(1)


#--- requirements_check
def requirements_check():
        '''check requirements are met for software/program to run correctly'''
        checks = True
        requirements = 'requirements.txt'
        with open(requirements, 'r') as rfp:
            for line in rfp.readlines():
                try:
                    line = line.strip()
                    exec("import " + line)
                except:
                    print("[ERROR] Missing module:", line)
                    checks = False
        if checks == False:
            sys.exit(1)

#--- clear function
def clear():
    if os.name == "nt":
    	os.system("cls")
    else:
    	os.system("clear")


#--- parse arguments
def args_parser():
	#parse required argument/s needed for program
	parser = argparse.ArgumentParser()
	parser.add_argument('-d', '--domain', type=str, required=True, help='domain - ssubdomains(ex use. http(s)://facebook.com)')
	parser.add_argument('-o', '--output', type=str, required=False, help='filename - filename for output data(ex use. facebook.txt)')
	args = parser.parse_args()
	return args


active_subdomains = []

class Abuse_certificate_transparency:
	def __init__(self):
		self.domain = args_parser().domain
		self.output = args_parser().output


	def parse_url(self):
		#parse host from scheme, to use for certificate transparency abuse
		try:
			host = urllib3.util.url.parse_url(self.domain).host
		except Exception as e:
			print(f'Invalid - Domain, try again...')
			sys.exit(1)
		return host


	def request_json(self):
		#request json data to get list of registered subdomains with cert trans records
		subdomains = []
		try:
			r = requests.get(f'https://crt.sh/?q=%.{abuse.parse_url()}&output=json')
			#r = requests.get('https://crt.sh/?q=%.facebook.com&output=json')
			if r.status_code != 200:
				print('{!} host status-code: %s\n ~ unable to access records using this abuse certificate transparency method' % (r.status_code))
			else:
				try:
					json_data = json.loads(r.text)
					for sub in (json_data):
						subdomains.append(sub['name_value'])
				except Exception as e:
					print(f'json_data:Error {e}')
					pass
		except Exception as e:
			print(f'request_json//Error: {e}')
			pass
		return subdomains


	def active_subs(self):
		#check registered subdomains to see if active or not
		global active_subdomains

		for sub in abuse.request_json():
			try:
				sub = socket.gethostbyname_ex(sub)
				if sub in active_subdomains:
					pass
				else:
					active_subdomains.append(sub)
			except:
				continue
		number_all = len(abuse.request_json())
		number_active = len(active_subdomains)

		Style.RESET_ALL

		try:
			print('\n',Fore.GREEN+'''\n\n{!} There are %s %s %s''' %
				(Fore.RED+Back.BLACK+str(number_all), Fore.RED+Back.BLACK+'REGISTERED', Fore.GREEN+'subdomains for this domain.'))
			time.sleep(2)

			index = Fore.GREEN+Back.BLACK+str('INDEX:green')
			sub_red = Fore.RED+Back.BLACK+str('SUBDOMAIN:red')
			line = Fore.CYAN+Back.BLACK+str('*****************************')
			print('\n%s\n%s %s\n%s\n' % (line, index, sub_red, line))
			time.sleep(1.3)

			for index, sub in enumerate(abuse.request_json()):
				print(Fore.GREEN+str(index+1),Fore.RED+str(sub))

			print('\n',Fore.GREEN+'''\n\n{!} There are %s %s %s''' %
				(Fore.RED+Back.BLACK+str(number_active), Fore.RED+Back.BLACK+'ACTIVE', Fore.GREEN+'subdomains for this domain.'))
			time.sleep(2)

			index = Fore.GREEN+Back.BLACK+str('INDEX:green')
			dns_white = Fore.WHITE+Back.BLACK+str('DNS SERVER:white')
			sub_red = Fore.RED+Back.BLACK+str('SUBDOMAIN:red')
			ip_yell = Fore.BLUE+Back.BLACK+str('IP_ADDR:blue')
			line = Fore.CYAN+Back.BLACK+str('************************************************************')
			print('\n%s\n%s %s %s %s\n%s\n' % (line, index, dns_white, sub_red, ip_yell, line))
			time.sleep(1.3)

			for index, sub in enumerate(active_subdomains):
				print(Fore.GREEN+str(index+1), Fore.WHITE+Back.BLACK+str(sub[0]), Fore.RED+Back.BLACK+str(sub[1]), Fore.BLUE+Back.BLACK+str(sub[2]))

		except Exception as e:
			print(f'active_subdomains//Error: {e}')
			pass

		return active_subdomains


	def write_file(self,):
		#write registerd subdomains and active subdomains to file
		global active_subdomains
		try:
			if self.output is not None:
				reg = 'REGISTERED_'+self.output
				active = 'ACTIVE_'+self.output
				with open(reg,'w') as r:
					for index, sub in enumerate(abuse.request_json()):
						text = f'{index} {sub}\n'
						r.write(text)
				with open(active,'w') as a:
					for index, sub in enumerate(active_subdomains):
						text = f'{index} {sub}\n'
						a.write(text)
		except Exception as e:
			print(f'write_file//Error: {e}')
			pass

#--- main ---#
if __name__ == '__main__':
    clear()
    time.sleep(1)
    banner()
    requirements_check()

    # Abuse certificate authority to get all and active subdomains of a domain
    abuse = Abuse_certificate_transparency()
    abuse.parse_url()
    abuse.request_json()
    abuse.active_subs()
    abuse.write_file()

    sys.exit(0)
