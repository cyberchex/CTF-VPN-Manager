#Python Script - CTF VPN Manager w a Killswitch
#Written By - CyberChex
#Date - 12/19/2023

#Import Linux OS Commands
import os
import subprocess

#Display Options
print('')
print('CyberChex CTF VPN Manager!')
print('')
print('************************* Before switching CTF sites, please execute Kill OpenVPN option *****************************')
print('************************* You might need to keep this terminal open after connecting     *****************************')
print('')
print('Select one of the following services:')
print('1 = Hackthebox Starting Point')
print('2 = Hackthebox Lab')
print('3 = Tryhackme')
print('4 = Tryhackme - West')
print('5 = PwnTillDawn')
print('6 = echoCTF')
print('')
print('')
print('Program Options')
#print('C = Check if VPN Tunnel is Activated') - IN DEV
#print('')
print('K = Kill OpenVPN')
print('')
print('Q = Quit')

print('Enter Option (1,2,3,4,5,6,C,K,Q)')

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
#elif option =='C' or option == 'c':
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


