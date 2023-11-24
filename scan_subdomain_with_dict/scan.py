#! /usr/bin/python
#coding : utf-8

#imports
from threading import Thread, Lock
from queue import Queue
from colorama import init, Fore, Back, Style
import requests
import urllib3
import time
import os
import sys

init(autoreset=True)

__author__ = "Cyb3rPatriX-S3C"
__version__ = "1.0.0"

#--- banner ---#
def banner():
    global __version__, __author__

    b = Fore.GREEN+"""
    
    
                                                                                                        
                                                                                                    
                                                                                                    
                                                 ..                                                 
                                         :-=*##########*=-:                                         
                                   :*#%@@@@@@@@@@@@@@@@@@@@@@%#*:                                   
                               -%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%=                               
                           .+%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*.                           
                         =@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=                         
                       *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*                       
                    .%@@@@@@@@@@@@@@@@@#:                   +%@@@@@@@@@@@@@@@@%.                    
                  .*@@@@@@@@@@@@@@@*                             #@@@@@@@@@@@@@@*.                  
               . -@@@@@@@@@@@@@@+       .@@@#             @@        #@@@@@@@@@@@@@- .               
                *@@@@@@@@@@@@%      -@@@@@@     @.   %%    *@@@%      -@@@@@@@@@@@@*                
              .@@@@@@@@@@@@#      @@@@@@@#    @@@.   %@%    -@@@@@@      %@@@@@@@@@@@.              
             -@@@@@@@@@@@%     *@@@@@@@@*    #@@@.   %@@@    .@@@@@@@     :@@@@@@@@@@@-             
            -@@@@@@@@@@@*    *@@@@@@@@@#    %@@@@.   %@@@@     @@@@@@@@     %@@@@@@@@@@-            
           -%@@@@@@@@@@-                                                     *@@@@@@@@@%-           
          .#@@@@@@@@@@                                                        =@@@@@@@@@#:          
        . +@@@@@@@@@@    +@@@@@@@@@@@    @@@@@@@@.   %@@@@@@@.   #@@@@@@@@@    -@@@@@@@@@*..        
         :@@@@@@@@@@    +@@@@@@@@@@@*   +@@@@@@@@.   %@@@@@@@@    @@@@@@@@@@    +@@@@@@@@@-         
         #@@@@@@@@@+   =@@@@@@@@@@@@    @@@@@@@@@.   %@@@@@@@@*   :@@@@@@@@@@    #@@@@@@@@#.        
        :@@@@@@@@@%    @@@@@@@@@@@@-   @@@@@@@@@@.   @@%+-:::-+@#:+@@@@@@@@@@%    @@@@@@@@@:        
        +@@@@@@@@@:   *@@@@@@@@@@@@    @@@@@@@@@@@@=.             .+@@@@@@@@@@-   #@@@@@@@@*        
        @@@@@@@@@@    %@@@@@@@@@@@%   @@@@@@@@@@#                     %@@@@@@@+   .@@@@@@@@@        
       .@@@@@@@@@#   .@@@@@@@@@@@@#   @@@@@@@@@        -%%%%%%%-       .%@@@@@@    @@@@@@@@@.       
       .@@@@@@@@@#   :@@@@@@@@@@@@:   @@@@@@@:      #@@@@@@@@@@@@@=      =@@@@@    %@@@@@@@@.       
       :@@@@@@@@@*                         @.     +@@@@@@@@@@@@@@@@@.     =@       %@@@@@@@@:       
       .@@@@@@@@@#   :@@@@@@@@@@@@*   @@@@@-     #@@@@@@@@@@@@@@@@@@@@     #@@@    %@@@@@@@@.       
       .@@@@@@@@@#   .@@@@@@@@@@@@#   @@@@@:    +@@@@@@@@@@@@@@@@@@@@@%     @@@    @@@@@@@@@.       
        @@@@@@@@@@    %@@@@@@@@@@@@   #@@@=     @@%@#@%%@%@#@%%%%%%@%@@.    #@+   .@@@@@@@@@        
        +@@@@@@@@@:   *@@@@@@@@@@@@    @@@=    :@    .      . =      *@=    #@-   #@@@@@@@@*        
        :@@@@@@@@@%    @@@@@@@@@@@@%   *@@=     @@  :  @+     @-     @@-    #%    @@@@@@@@@:        
         #@@@@@@@@@+   +@@@@@@@@@@@@    @@+     @@%%@#%@@@%@%@@@%%@#@@%     %    #@@@@@@@@#.        
         :@@@@@@@@@@    *@@@@@@@@@@@@    @@:    :@@@@@@@@@@@@@@@@@@@@@-    -@   +@@@@@@@@@-         
        . +@@@@@@@@@@    +@@@@@@@@@@@#   :@#     :@@@@@@@@@@@@@@@@@@@-     %   :@@@@@@@@@*..        
          :#@@@@@@@@@@                      *     .*@@@@@@@@@@@@@@@*      #   -@@@@@@@@@#:          
           -%@@@@@@@@@@:                    +@.      =#@@@@@@@@@#-        *+ *@@@@@@@@@%-           
            =@@@@@@@@@@@*    *@@@@@@@@@@    =@@+         .:-..             .%@@@@@@@@@@=            
             -@@@@@@@@@@@%     #@@@@@@@@@    *@@@#.                 -.       :%@@@@@@@-             
              .@@@@@@@@@@@@#      @@@@@@@@.    @@= ##+:         :+#@ *#.      .@@@@@@:              
                *@@@@@@@@@@@@#      -@@@@@@+    @.   %  +@@@@@@%      #@*.    #@@@@*.               
               . -@@@@@@@@@@@@@@=       :@@@@            =@@        *@@@@@%#%@@@@@- .               
                  .*@@@@@@@@@@@@@@%=                             +@@@@@@@@@@@@@@*.                  
                    .%@@@@@@@@@@@@@@@@%*                    -#@@@@@@@@@@@@@@@@%.                    
                       *@@@@@@@@@@@@@@@@@@@@@@%%####%%%@@@@@@@@@@@@@@@@@@@@@#.                      
                         =@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=                         
                           .*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*.                           
                               =%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%=                               
                                   -*%@@@@@@@@@@@@@@@@@@@@@@@@%*-                                   
                                         :-+###%%%%%%###+=:                                         
                                                                                                    



            @@@@@@   @@@  @@@  @@@@@@@   @@@@@@@@  @@@  @@@  @@@  @@@@@@@   @@@@@@@@  @@@@@@@  
            @@@@@@@   @@@  @@@  @@@@@@@@  @@@@@@@@  @@@  @@@@ @@@  @@@@@@@@  @@@@@@@@  @@@@@@@@ 
            !@@       @@!  @@@  @@!  @@@  @@!       @@!  @@!@!@@@  @@!  @@@  @@!       @@!  @@@ 
            !@!       !@!  @!@  !@   @!@  !@!       !@!  !@!!@!@!  !@!  @!@  !@!       !@!  @!@ 
            !!@@!!    @!@  !@!  @!@!@!@   @!!!:!    !!@  @!@ !!@!  @!@  !@!  @!!!:!    @!@!!@!  
            !!@!!!   !@!  !!!  !!!@!!!!  !!!!!:    !!!  !@!  !!!  !@!  !!!  !!!!!:    !!@!@!   
                !:!  !!:  !!!  !!:  !!!  !!:       !!:  !!:  !!!  !!:  !!!  !!:       !!: :!!  
                !:!   :!:  !:!  :!:  !:!  :!:       :!:  :!:  !:!  :!:  !:!  :!:       :!:  !:! 
            :::: ::   ::::: ::   :: ::::   ::        ::   ::   ::   :::: ::   :: ::::  ::   ::: 
            :: : :     : :  :   :: : ::    :        :    ::    :   :: :  :   : :: ::    :   : :                                                                           
                                                                                                    
                                                                                                    
    

    version {v}
    Author  {a}
    """ .format(v=__version__, a=__author__)

    print (b)
    
    time.sleep(1)


#--- requirements_check ---#
def requirements_check():
        '''check requirements are met for software/program to run correctly'''
        check = True
        requirements = 'requirements.txt'
        with open(requirements, 'r') as rfp:
            for line in rfp.readlines():
                try:
                    line = line.strip()
                    exec("import " + line)
                except:
                    print("[ERROR] Missing module:", line)
                    check = False
        if check == False:
            sys.exit(1)

#--- clear function
def clear():
    if os.name == "nt":
    	os.system("cls")
    else:
    	os.system("clear")


#--- parse arguments ---#
def args_parser():
    #parse required argument/s needed for program
    import argparse
    parser = argparse.ArgumentParser(description="Faster Subdomain Scanner using Threads")
    parser.add_argument("domain", help="Domain to scan for subdomains without protocol (e.g without 'http://' or 'https://')")
    parser.add_argument("-l", "--wordlist", help="File that contains all subdomains to scan, line by line. Default is subdomains.txt", default="subdomains.txt")
    parser.add_argument("-t", "--num-threads", help="Number of threads to use to scan the domain. Default is 10", default=10, type=int)
    parser.add_argument("-o", "--output-file", help="Specify the output text file to write discovered subdomains", default="discovered-subdomains.txt")
    
    args = parser.parse_args()
    return args
	

#variables
q = Queue()
list_lock = Lock()
discovered_domains = []

class Subdomain_scanner:
    def __init__(self):
        self.domain = args_parser().domain
        self.output = args_parser().output_file
        self.wordlist = args_parser().wordlist
        self.num_threads = args_parser().num_threads
        self.output_file = args_parser().output_file


    def parse_url(self):
        #parse host from scheme, to use for certificate transparency abuse
        try:
            host = urllib3.util.url.parse_url(self.domain).host
        except urllib3.ConnectionError as e:
            print('[!] Invalid - Domain, try again...')
            sys.exit(1)
        except Exception as e:
            print("[!] Something went wrong! Check your Internet Connection!!!")
            sys.exit(1)
        return host
    

    def scan_subdomains(self, domain):
        global q
        while True:
            # get the subdomain from the queue
            subdomain = q.get()
            # construct & scan the subdomain
            url = f"http://{subdomain}.{self.domain}"
            try:
                requests.get(url)
            except requests.ConnectionError:
                pass
            else:
                print(Fore.WHITE+Back.BLACK+"["+Fore.GREEN+Back.BLACK+"+"+Fore.WHITE+Back.BLACK+"] Discovered subdomain:"+Fore.GREEN+Back.BLACK+"  "+url)
                # add the subdomain to the global list
                with list_lock:
                    discovered_domains.append(url)

            # we're done with scanning that subdomain
            q.task_done()

        
    def main(self, domain, n_threads, subdomains):
        global q

        # fill the queue with all the subdomains
        for subdomain in subdomains:
            q.put(subdomain)

        for t in range(n_threads):
            # start all threads
            worker = Thread(target=sub.scan_subdomains, args=(domain,))
            # daemon thread means a thread that will end when the main thread ends
            worker.daemon = True
            worker.start()



    
if __name__ == '__main__':
    clear()
    time.sleep(1)
    banner()
    # Check requirements are met, eg. modules are installed correctly etc.
    requirements_check()


    # subdomain scanner
    sub = Subdomain_scanner()
    sub.parse_url()

    sub.main(domain=sub.domain, n_threads=sub.num_threads, subdomains=open(sub.wordlist).read().splitlines())
    q.join()

    # save the file
    with open(sub.output_file, "w") as f:
        for url in discovered_domains:
            print(url, file=f)
