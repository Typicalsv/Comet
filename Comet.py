from ipregistry import IpregistryClient
from colorama import Fore
from datetime import datetime
import speedtest as speed
import socket
import sys
import os

#Clear console function

def Clean():
     os.system('cls' if os.name == 'nt' else 'clear')

# Search for open ports

class Ports:

    def __init__(self, lhost, start, stop, timeout):

        self.lhost = lhost
        self.start = start
        self.stop = stop
        self.timeout = timeout


    def scan_ports(self):

        for port in range(self.start, self.stop+1):
            sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sckt.settimeout(self.timeout)
            answ = sckt.connect_ex((self.lhost, port))

            if answ == 0:
                print(Fore.GREEN + f'Open port ~{port}')
            else:
                print(Fore.RED + f'Closed port ~{port}')

            sckt.settimeout(None)
            sckt.close()


def get_port_range():

        start = int(input(Fore.BLUE + 'Specify start port... '))
        stop = int(input('Specify end port... '))
        print('')
        if start < 1:
            print(Fore.RED + '[CRIT ERROR] - port number have to be at least 1')
            sys.exit()

        elif stop > 65535:
            print(Fore.RED + '[CRIT ERROR] - maximum port is 65535')
            sys.exit()

        elif start > stop:
             print(Fore.RED + '[CRIT ERROR] - end port should be bigger value than start port')

        return start, stop



lhost = '127.0.0.1'
timeout = 0.00001

#test speed of the internet

class Ishowspeed:

    def Speed(self):

        st = speed.Speedtest()
        st.get_best_server()

        download_speed = st.download() / 10**6
        upload_speed = st.upload() / 10**6

        print(Fore.BLUE+f"Download speed: {download_speed:.2f} Mbps")
        print(Fore.BLUE+f"Upload speed: {upload_speed:.2f} Mbps")
        print('')
        return download_speed, upload_speed
    
class Scanner:

    def __init__(self, ip_base, port):

        self.ip_base = ip_base
        self.port = port
        self.active_hosts = []

    def scan(self):
        
        for i in range(1, 255):
            target_ip = f"{self.ip_base}.{i}"
            target = (target_ip, self.port)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.00000001)
            result = sock.connect_ex(target)
            if result == 0:
                self.active_hosts.append(target_ip)
            sock.close()

class Cip:

    def checkIp():

        cos = input(Fore.BLUE+'Do you have client API key? (y/n)')
        if(cos == 'n'): 
            Clean()
            print(Fore.GREEN+'Head to ipregistry.com -> register -> run this app again.')
            sys.exit()

        elif(cos == 'y'): 
            Clean()
            choice = input(Fore.BLUE+'Enter your API key:')

            if(choice == ''):  

                print(Fore.RED + '[CRIT ERROR] - Enter correct value')
                sys.exit()

        else: 
            print(Fore.RED + '[CRIT ERROR] - Enter correct value')
            sys.exit()

        cli = IpregistryClient(choice)
        choi  = input(Fore.BLUE+'Look up address of this machine or other? (m/o)')

        if(choi == 'm'):

            info = cli.lookup()
            print(info)

        elif(cos == 'o'): 
           
           addr = input(Fore.BLUE+'Enter address:')
           infoo = cli.lookup(addr)
           print(infoo)

        else: 
            print(Fore.RED + '[CRIT ERROR] - Enter correct value')
            sys.exit()
     
Clean()
print(Fore.GREEN+'Welcome to Comet! ')
print(Fore.GREEN+'What would you like to do?')
print('')
print(Fore.RED+'1. Look for open ports')
print(Fore.RED+'2. Identify active hosts')
print(Fore.RED+'3. Listen for TCP/IP/HTTP movement')
print(Fore.RED+'4. Speed test')
print(Fore.RED+'5. Capture packets')
select = input(Fore.BLUE+'Select function (1-5)... ')
Clean()



if select == '1':

    print(Fore.GREEN+('-----Port Scanner-----'))
    print('')
    start, stop = get_port_range()
    port_scanner = Ports(lhost, start, stop, timeout)
    port_scanner.scan_ports()

elif select == '2':
        print(Fore.GREEN+'-----Active Hosts-----')
        print(Fore.RED+'   (May take long)')
        print('')
        x = int(input(Fore.BLUE+'Enter port you want to search on for active hosts... '))
        Clean()
        print(Fore.GREEN+'-----Active Hosts-----')
        print('')

        if x < 1:
            print(Fore.RED + '[CRIT ERROR] - port number have to be at least 1')
            sys.exit()

        elif x > 65535:
            print(Fore.RED + '[CRIT ERROR] - maximum port is 65535')
            sys.exit()

             
        scan = Scanner('10.0.0', x)
        scan.scan()

        if scan.active_hosts:
            for host in scan.active_hosts:   
             print(Fore.BLUE+'Active host: '+host)

elif select == '3':

    Cip.checkIp()

elif select == '4':
        
        print(Fore.GREEN+'-----Speed Test (20s)-----')
        print('')
        test = Ishowspeed()
        test.Speed()

elif select == '5':
    print('Work in progress!')
    #TODO
else: 
    print(Fore.RED+f'[CRIT ERROR] - There is no function such as: {select}')
    sys.exit()
