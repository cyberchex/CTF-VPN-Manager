#Python Script - CTF VPN Manager w a Killswitch
#Written By - CyberChex
#Date - 12/30/2023

#Import Linux OS Commands
import os
import subprocess
import csv
import shutil

option = ""

#Function - Add CTF option
def add_ctf():


     #Get next ID in file
     with open('Configs/sites.txt') as csv_file:
         csv_reader = csv.reader(csv_file, delimiter=',')
         line_count = 0
         for row in csv_reader:
          line_count = line_count + 1
     #    print(f'Processed {line_count} lines.')

     #Get CTF site info from user
     print ('Enter CTF Site Name:')
     add_ctf_site_name = input ()
     add_ctf_site_config = '/' + add_ctf_site_name

     #Write CTF site info into sites file
     with open('Configs/sites.txt', 'a', newline='') as csvfile:
          fieldnames = ['id', 'site', 'location']
          writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
          writer.writerow({'id': line_count, 'site': add_ctf_site_name, 'location': add_ctf_site_config})
     
     #Create directory
     new_path = 'Configs/' + add_ctf_site_name
     os.mkdir(new_path)

     print ('CTF site Added into sites file!')

#Function - Remove CTF option
def remove_ctf():

     #Get ID from user
     print ('Enter ID to remove:')
     remove_ctf_site_id = input()

     #Read current sites records and remove matching id
     lines = list()
     with open('Configs/sites.txt', 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            lines.append(row)
            for field in row:
                if field == remove_ctf_site_id:
                    location = str(row[2])
                    lines.remove(row)
                    #remove sub-directory
                    remove_path = ('Configs' + location)
                    shutil.rmtree(remove_path)

     #Reload updated rows back to file
     with open('Configs/sites.txt', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)

     #Notify user of success
     print ('CTF site removed from sites file!')



#Function - Display New Menu Header Section
def menu_header():
     print('')
     print('CyberChex CTF VPN Manager!')
     print('')
     print('Before switching CTF sites, please execute Kill OpenVPN option.')
     print('You might need to keep this terminal open after connecting.')
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
     print('')
     print('A = Add VPN Site - IN DEV')
     print('C = Check if VPN Tunnel is Activated')
     print('R = Remove VPN Site -IN DEV')
     print('')
     print('K = Kill OpenVPN')
     print('')
     print('Q = Quit')

#Call display menu
display_menu()

#FUNCTION - Allow user to select option
def user_input_option():
     #Allow user to select option
     option = input('Enter Option (i.e 1-6, A, C, R, K, Q):')
     return option

#Call User Input Option
option = user_input_option()

def selection_actions(option):

     #Determine with VPN to Start, Quit CTF-VPN, or kill current VPN session
     #Make sure you have downloaded each of the CTF files from the sites and renamed them in right config folders.
     #THIS NEEDS TO BE UPDATED TO GRAB CURRENT LIST OF CTF SITES IF USER ADDS OR REMOVES, CANT BE STATIC ANYMORE!
     print(option)
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
          add_ctf()
     elif option == 'R' or option == 'r':
          remove_ctf()
     elif option =='C' or option == 'c':
          check_vpn()
     elif option =='Q' or option == 'q':
          quit()
          print('CTF-VPN-Manager Exited')
     else:
          print('Invalid Option! - Run the script again!')




print('')

#FUNCTION - Defining check if VPN Tunnel is activated
def check_vpn():
          #This code will check for active TUN session
          import psutil
          import logging, os, time
          import subprocess
          import sys

          procname = "openvpn"

          #while True:
          cmdout = subprocess.Popen(["ifconfig | grep tun"],stdout = subprocess.PIPE, shell=True).communicate()[0]
          var_cmdout = "cmdout: "+str(cmdout)
          #print (var_cmdout)
          #time.sleep(2)
          #-----
          if b'tun' in cmdout:
               os.system('clear')
               print ('VPN is currently ACTIVE!')
               #quit()

          if not b"tun" in cmdout: 
               # perform action for lost connection
               #var_killing = "killing "+str(procname)
               #print (var_killing)
               #for proc in psutil.process_iter():
                    # check whether the process name matches
                    #var_listing = "Listing procname: "+str(proc.name())
                    #print (var_listing)
                    #if proc.name() == procname:
                         #proc.kill()
                         #sys.exit()
                         #quit()
               #os.system('clear')
               print ('VPN is NOT active!')
               #quit()

#Call selection actions
selection_actions(option)