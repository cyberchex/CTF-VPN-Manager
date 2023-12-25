# CTF-VPN-Manager
Python Project - This is a CTF (Capture The Flag) VPN Manager that allows you to save OpenVPN config files and easily start or kill them.  This project has saved me alot of time messing around with OpenVPN and Linux commands.

# About CTF-VPN-Manager

This is a home-grown Python project to manage OpenVPN config files needed for completing capture the flags.

# CTF-VPN-Manager Install/Config

Pre-req - You have installed OpenVPN already.

1) Clone the Repo - Open up terminal on main Desktop.  Enter this command to clone the repo: "git clone https://github.com/cyberchex/CTF-VPN-Manager.git"
2) Download your config files from each of the CTF sites.
3) Place each of the CTF config files in apporate sub-directories within Configs folder. (ie THM, THM-West, HTB-Starting-Point, HTB-Lab, PTD, etc)
4) Rename each of the OpenVPN files to exactly "ctf_config.ovpn" within each of the sub-directories.  DO NOT customize at this time.
5) Run "python3 start_vpn.py"
6) NOTE: You might need to keep Terminal Open, just minimize.  Run the script again and select "Kill OpenVPN" when done with the CTF VPN.

Link to YouTube Video the helps with the install.  Enjoy! 


2 min - https://youtu.be/ZEi74XySUj8
1 min - https://youtube.com/shorts/hXrh6znUS3Q?feature=share
