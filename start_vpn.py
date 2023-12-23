#Python Script - CTF VPN Manager w a Killswitch
#Written By - CyberChex
#Date - 12/23/2023

#Import Linux OS Commands
import os
import subprocess
import csv

#Define Function - Current list of CTF Sites Managed
#def ctf_sites():
#     with open('Configs/sites.txt') as csv_file:
#         csv_reader = csv.reader(csv_file, delimiter=',')
#         line_count = 0
#         for row in csv_reader:
#             if line_count == 0:
#                 print(f'Column names are {", ".join(row)}')
#                 line_count += 1
#             else:
#                 print(f'\t{row[0]} equals {row[1]} CTF Site, and is located in {row[2]}.')
#                 line_count += 1
#         print(f'Processed {line_count} lines.')



#Debug View
#Call Function - List of CTF Sites Managed
#ctf_sites()

#Function - Display New Menu Header Section
def menu_header():
     print('')
     print('CyberChex CTF VPN Manager!')
     print('')
     print('************************* Before switching CTF sites, please execute Kill OpenVPN option *****************************')
     print('************************* You might need to keep this terminal open after connecting     *****************************')
     print('')
     print('Select one of the following options:')

#Call Function - Menu Header
menu_header()

#Function - Display Menu Selections from CTF File
def menu_selections():
     with open('Configs/sites.txt') as csv_file:
         csv_reader = csv.reader(csv_file, delimiter=',')
         line_count = 0
         for row in csv_reader:
             if line_count == 0:
                 #print(f'Column names are {", ".join(row)}')
                 line_count += 1
             else:
                 print(f'\t{row[0]} = {row[1]} CTF Site')
                 line_count += 1
         #print(f'Processed {line_count} lines.')

menu_selections()

#Function - Diplay Current Menu Selections
def display_menu():

     print('')
     print('')
     print('Program Options')
     #print('T = Check if VPN Tunnel is Activated') - IN DEV
     #print('')
     #print('A = Add VPN Site') - IN DEV
     #print('')
     #print('R = Remove VPN Site) - IN DEV
     #print('')
     #print('C = Config Setup') - IN DEV
     print('K = Kill OpenVPN')
     print('')
     print('Q = Quit')

     print('Enter Option (1,2,3,4,5,6,K,Q)')

display_menu()

#def menu(user_selection):
#     return option



option = input()

print('')

#Determine with VPN to Start, Quit CTF-VPN, or kill current VPN session
#Make sure you have downloaded each of the CTF files from the sites and renamed them in right config folders.
if option =='K' or option == 'k':
     os.system('sudo killall openvpn')
     print('Openvpn Killed! by CTF-VPN-Manager')
elif option =='1':
     os.system('sudo -b openvpn Configs/HTB-Starting-Point/ctf_config.ovpn')
     print('Hack The Box Starting Point VPN Activated!')
elif option =='2':
     os.system('sudo openvpn Configs/HTB-Lab/ctf_config.ovpn')
     print('Hack The Box Lab VPN Activated!')
elif option =='3':
     os.system('sudo openvpn Configs/THM/ctf_config.ovpn')
     print('Try Hack Me VPN Activated!')
elif option =='4':
     os.system('sudo openvpn Configs/THM-West/ctf_config.ovpn')
     print('Try Hack Me West VPN Activated!')
elif option =='5':
     os.system('sudo openvpn Configs/PTD/ctf_config.ovpn')
     print('PwnTillDawn VPN Activated!')
elif option =='6':
     os.system('sudo openvpn Configs/echoCTF/ctf_config.ovpn')
     print('echoCTF VPN Activated!')
elif option == 'A' or option == 'a':
     #Allow user to add a new CTF site
     print('In Dev')
elif option == 'C' or option == 'c':
     #Allow user to pick which config file to manage
     print('In Dev')


#elif option =='T' or option == 't':
     #This code will check for active TUN session - IN DEV
#     import psutil
#     import logging, os, time
#     import subprocess
#     import sys
#
#     procname = "openvpn"

#     while True:
#         cmdout = subprocess.Popen(["ifconfig | grep tun"],stdout = subprocess.PIPE, shell=True).communicate()[0]
#         var_cmdout = "cmdout: "+str(cmdout)
#         print (var_cmdout)
#         time.sleep(2)
#         #-----
#         if b'tun' in cmdout:
#             print ('seems to be ok')
#         if not b"tun" in cmdout: 
#             # perform action for lost connection
#             var_killing = "killing "+str(procname)
#             print (var_killing)
#             for proc in psutil.process_iter():
#                 # check whether the process name matches
#                 var_listing = "Listing procname: "+str(proc.name())
#                 print (var_listing)
#                 if proc.name() == procname:
#                     proc.kill()
#                     sys.exit()
#                     quit()
elif option =='Q' or option == 'q':
     quit()
     print('CTF-VPN-Manager Exited')
else:
     print('Invalid Option! - Run the script again!')


