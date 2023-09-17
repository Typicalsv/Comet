from colorama import Fore
from datetime import datetime
import speedtest as speed
import socket
import time
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

        if stop > 65535:
            print(Fore.RED + '[CRIT ERROR] - maximum port is 65535')
            sys.exit()

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
        print(Fore.GREEN+'-----Speed Test (20s)-----')
        print('')
        test = Ishowspeed()
        test.Speed()
elif select == '3':
    print('Work in progress!')
    #TODO
elif select == '4':
    print('Work in progress!')
    #TODO
elif select == '5':
    print('Work in progress!')
    #TODO
else: 
    print(Fore.RED+f'[CRIT ERROR] - There is no function such as: {select}')
    sys.exit()