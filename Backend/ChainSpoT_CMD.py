            ####################################################
            #      * File:   ChainSpoT.py                      #
            #      * Author: Ahmed Hesham Salah                #
            #      * Contact : ahmed.hesham_1999@yahoo.com     #
            #      * Created on Feb 3, 2019                    #
            #      * Copyright (C) 2019  Ahmed Hesham Salah    #
            ####################################################

##############################################################################
#    ChainSpoT is free software: you can redistribute it and/or modify       #
#    it under the terms of the GNU General Public License as published by    #
#    the Free Software Foundation, either version 3 of the License, or       #
#    (at your option) any later version.                                     #
#                                                                            #
#    ChainSpoT is distributed in the hope that it will be useful,            #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of          #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the           #
#    GNU General Public License for more details.                            #
#                                                                            #
#    You should have received a copy of the GNU General Public License       #
#    along with ChainSpoT.  If not, see <https://www.gnu.org/licenses/>.     #
##############################################################################

import pywifi
import time
import subprocess
import sys
import ctypes
import os
import platform
import re
import msvcrt


def main(password,room=0):
    # bug if one out and one come ... total subtract  equal 0
    devices = [0,0] #to expect the change in connecting devices in hotspot
    first_time = time.time() #keep the first time to print some messages after certian time
    if room == 0: #server
        check = False
        while True:
            while not check:
                power,id_list,room_list,comp_id =parse_wifi()
                if room_list:
                    check=start_hotspot(str(room_list[-1]+1)+".0.0",password)
                    print("[^_^] The hotspot network "+str(room_list[-1]+1)+".0.0"+" started")
                else:
                    check=start_hotspot("1.0.0",password)
                    print("[^_^] The hotspot network "+"1.0.0"+" started")

            time.sleep(2)
            supp = support_wifi()

            if supp ==2: #just check if the user turn off wifi while the script work
                print("\n[X] Sorry your WIFI is off , To use this script you must turn it on and try again")
                input("\n\t \t \t \t    PRESS ANY KEY TO EXIT...")
                sys.exit()

            devices[1]= connected_devices() #update
            if devices[1] != devices[0]: #check if there's the differance in the number of connecting devices in the right moment and the connecting devices from the last scanning
                differance=devices[1]-devices[0]
                if differance>0:
                    print("[!] Some new device connecting with you")
                    print("[!] now you have "+str(connected_devices())+" devices connecting with you \n")
                else:
                    print("[X] Some Device disconnecting with you")
                    print("[!] now you have "+str(connected_devices())+" devices connecting with you \n")

                devices[0]=connected_devices() #put the new status in the old one

            check=check_hotspot()
            if check == False:
                print("[X] The hotspot network stoped")
                print("[!] Trying to open it again")

            if check:
                if int(time.time()-first_time)%60==0:
                    print("\n[^_^] Every thing is fine \n[!] The hotspot still open")
                    print("\n[!] Remember: To EXIT the script press ESC key \n")

            if msvcrt.kbhit(): #a way to out from the script using ESC key
            	if ord(msvcrt.getch()) == 27:
            	    return 0

    else: #host     room != 0
        wifi_connect = False
        while True:
            while not wifi_connect:
                print("[!] Trying to connect to near spot...")
                timer=time.time() #pick a start time to use it to count how much time take to connect to the best wifi spot
                power,id_list,room_list,comp_id =parse_wifi()
               
                if id_list:
                    print("\n\t \t \t \t  ~ AVAILABLE CHAINSPOT MEMBERS ~\n")
                    print("\t \t SSID \t \t POWER \t \t COMPUTER ID \t \t HUB")
                    for i in id_list:
                        print("\t \t %s \t \t %s \t \t %s \t \t \t %s" %(i ,str(power[i]), i.split(".")[1] ,i.split(".")[2] ))
                    print("\n[!] Trying to connect to best available spot...\n")
                    wifi_connect = best_wifi(power,id_list,room,password)
                    if wifi_connect:
                        print("[^_^] You're successfully connecting to "+wifi_connect+" in "+str(time.time()-timer)+" second" )
                        i=1
                        while True:
                            if i in comp_id: #doing this to unique the computer id (avoid duplicates)
                                i+=1
                            else:
                                hotspot_name = wifi_connect.split(".")[0]+"."+str(i)+"."+str(int(wifi_connect.split(".")[2])+1)
                                break
                        start_hotspot(hotspot_name,password)
                        print("[^_^] The hotspot network "+hotspot_name+" started" +" in "+str(time.time()-timer)+" second \n")
                    else:
                        print("[X] Can't connecting to any near spots , I'll try again")

                else:
                    print("[X] There's no near spots , Please be near to any device in the network ")

                if int(time.time()-first_time)%60==0:
                    print("\n[!] Remember: To EXIT the script press ESC key\n")

                supp = support_wifi()
                if supp ==2: #just check if the user turn off wifi while the script work
                    print("\n[X] Sorry your WIFI is off , To use this script you must turn it on and try again")
                    input("\n\t \t \t \t    PRESS ANY KEY TO EXIT...")
                    sys.exit()

                if msvcrt.kbhit(): #a way to out from the script using ESC key
                	if ord(msvcrt.getch()) == 27:
                	    return 0


            time.sleep(2)
            supp = support_wifi() #just check if the user turn off wifi while the script work
            if supp ==2:
                print("\n[X] Sorry your WIFI is off , To use this script you must turn it on and try again")
                input("\n\t \t \t \t    PRESS ANY KEY TO EXIT...")
                sys.exit()

            if not check_connect(wifi_connect): #discover the dissconnecting maybe take awhile , until this moment i can't force windows to rescan wifi while i connecting to network , so i have to depend on the cash of the last scanning
                #windows rescaning maybe take 10 sec less or more , untill this rescaning i depend on the cash , so discover the dissconnecting take some time
                wifi_connect = False
                print("[X] You're dissconnecting")
                print("[!] Trying to reconnect")

            if not check_hotspot():
                print("[X] The hotspot network "+hotspot_name+" stoped")
                print("[!] Trying to open it again")
                start_hotspot(hotspot_name,password)
                print("[^_^] The hotspot network "+hotspot_name+" started")
            else:
                if wifi_connect:
                    if int(time.time()-first_time)%60==0:
                        print("\n[^_^] Every thing is fine \n[!] Your device still connecting to "+wifi_connect+" \n[!] The hotspot "+hotspot_name+ " still open")
                        print("\n[!] Remember: To EXIT the script press ESC key\n")

            devices[1]= connected_devices() #update
            if devices[1] != devices[0]: #check if there's the differance in the number of connecting devices in the right moment and the connecting devices from the last scanning
                differance=devices[1]-devices[0]
                if differance>0:
                    print("[!] Some new device connecting with you")
                    print("[!] now you have "+str(connected_devices())+" devices connecting with you \n")
                else:
                    print("[X] Some Device disconnecting with you")
                    print("[!] now you have "+str(connected_devices())+" devices connecting with you \n")

                devices[0]=connected_devices() #put the new status in the old one

            if msvcrt.kbhit(): #a way to out from the script using ESC key
            	if ord(msvcrt.getch()) == 27:
            	    return 0


##############################################################################################################
############################################ profile mangement ###############################################
##############################################################################################################

#to connect any wifi network you must save its profile
#this function creat xml file and save it to windows and delete the file after save it
#work for only WPA2PSK wifi
#input wifi SSID , wifi passwkord
def save_profile(wifi,password):
    xml_file = '''<?xml version="1.0"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
	<name>'''+wifi+'''</name>
	<SSIDConfig>
		<SSID>
			<hex>'''+str(wifi.encode().hex()).upper()+'''</hex>
			<name>'''+wifi+'''</name>
		</SSID>
	</SSIDConfig>
	<connectionType>ESS</connectionType>
	<connectionMode>auto</connectionMode>
	<MSM>
		<security>
			<authEncryption>
				<authentication>WPA2PSK</authentication>
				<encryption>AES</encryption>
				<useOneX>false</useOneX>
			</authEncryption>
			<sharedKey>
				<keyType>passPhrase</keyType>
				<protected>false</protected>
				<keyMaterial>'''+password+'''</keyMaterial>
			</sharedKey>
		</security>
	</MSM>
	<MacRandomization xmlns="http://www.microsoft.com/networking/WLAN/profile/v3">
		<enableRandomization>false</enableRandomization>
	</MacRandomization>
</WLANProfile>
'''
    with open("wifi.xml","w") as file:
        file.write(xml_file)
    cwd = os.getcwd()
    cmd_output = subprocess.check_output('netsh wlan add profile filename="'+cwd+"\wifi.xml" + '" user=all', shell=True).decode()
    try:
        os.remove(cwd+"\wifi.xml")
    except:
        pass
    if "is added" in cmd_output:
        out = subprocess.check_output('netsh wlan set profileparameter name='+wifi+' connectionmode=auto', shell=True).decode()
        if "updated successfully." in out:
            out=out.split(" ")
            interface=out[4]
            subprocess.check_output('netsh wlan set profileorder name='+wifi+' interface='+interface+' priority=1', shell=True)
        return True
    return False


#return list of saved profiles
#if there's not saved profiles , it'll return False
def show_profiles():
    cmd_output = subprocess.check_output("netsh wlan show profiles", shell=True).decode()
    cmd_output = cmd_output.replace("\r","")
    cmd_output = cmd_output.split("\n")
    list_output=[]
    for i in cmd_output:
        if ":" in i:
            list_output.append(i.split(":")[1][1:])
    if list_output:
        return list_output[1:]
    return False

#take list of profiles (which you want to delete) as parameter and delete them
def delete_profiles(profiles):
    for i in profiles:
        cmd_output = subprocess.check_output("netsh wlan delete profile name="+i, shell=True).decode()


##############################################################################################################
############################################## wifi mangement ################################################
##############################################################################################################
def support_wifi():
    try:
        cmd_output = subprocess.check_output("Netsh WLAN show interfaces", shell=True).decode()
        cmd_output = cmd_output.replace("\r","")
        cmd_output = cmd_output.split("\n")
        l=[]
        for i in cmd_output:
            if "Hardware" in i:
                l.append( i.split(":")[1][1:].split(" ")[1])
            if "Software" in i:
                l.append( i.split("Software")[1].strip())
        if l :
            if l[0] == "On" and l[1] == "On":
                return 1 #support wifi and it's turned on
            else:
                return 2 #support wifi but it's turned off
        else:
            return 1

    except:
        return False #not support wifi at all


#take wifi SSID as as parameter , check if it's connected or not and check it's signal power if it's more than 50% it'll return True , else return False
def check_connect(wifi_connect):
    cmd_output = subprocess.check_output("ipconfig", shell=True).decode()
    if "Default Gateway" in cmd_output:
        cmd_output = subprocess.check_output("Netsh WLAN show interfaces", shell=True).decode()
        if "SSID" in cmd_output:
            cmd_output = cmd_output.replace("\r","")
            list_output = cmd_output.split("\n")
            for i in list_output:
                if "SSID                   :" in i:
                    wifi_name =i.split(":")[1][1:]
                if "Signal                 :" in i:
                    wifi_power =int(i.split(":")[1][1:].replace("%",""))

            if wifi_name == wifi_connect and wifi_power >=50:
                return True
    return False


#first the function check if the profile wifi is save in this device or no , if no he will save it using save_profile()
#eventually connect to wifi if it work return True else return False
def connect_wifi(wifi,password):
    #other way
    #iface.connect(networks[wifi])
    if save_profile(wifi,password):
        try:
            cmd_output = subprocess.check_output('netsh wlan connect ssid="'+wifi+'" name="'+wifi+'"', shell=True).decode()
            if "completed successfully" in cmd_output:
                first_time=time.time()
                while time.time()-first_time <= 15:
                    time.sleep(1)
                    if check_connect(wifi):
                        return True
        except:
            pass

    return False


# "netsh wlan SHOW NETWORKS" command not actually re-scan the available wifi networks , it's just show the cash of the last scanning operation
#in this function we re-scan the wifi interface by pywifi library   Interface.scan()
def interface_scan():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    iface.scan()
    time.sleep(5)


#return dictionary {key:value} key is network SSID , value is percentage of SSID Power ex: 30,70,80,99
def power_wifi():
    interface_scan()
    cmd_output = subprocess.check_output("netsh wlan SHOW NETWORKS MODE=BSSID", shell=True)
    cmd_output = cmd_output.decode("ascii")
    cmd_output = cmd_output.replace("\r","")
    list_output = cmd_output.split("\n")
    list_output = list_output[4:]
    count = 0
    power = {}
    while count < len(list_output):
        if  "SSID" in list_output[count] and list_output[count][9:].strip() != "" :
            try:
                if "Signal" in list_output[count+5]:
            #Bug count + 5 list index out of range when connecting to wifi Signal element not exist
                    power[list_output[count][9:].strip()]=int(''.join(list(filter(str.isdigit, list_output[count+5]))))
            except:
                pass
        count += 1
    return power



##############################################################################################################
############################################ hotspot mangement ###############################################
##############################################################################################################

#check if user's device support hotspot or not
def support_hotspot():
    cmd_output = subprocess.check_output("netsh wlan show drivers", shell=True).decode()
    if "Hosted network supported  : Yes" in cmd_output:
        return True
    return False

#check if you open hotspot or not return True or False
def check_hotspot():
    cmd_output = subprocess.check_output("netsh wlan show hostednetwork", shell=True).decode()
    if "Started" in cmd_output:
        return True
    return False


#start hotspot networf if it works return True else return False
#input only hotspot name and password of hotspot
def start_hotspot(hotspot_name,password):
    cmd_output="" #because weird error " subprocess.CalledProcessError: Command 'netsh wlan set hostednetwork mode=allow ssid="D-Link" key="Ah123456"' returned non-zero exit status 1 "
    #despite the error the command work fine and it's open hotspot , i think it's just annoying error message , that's why i use try and except pass
    try:
        cmd_output = subprocess.check_output("netsh wlan set hostednetwork mode=allow ssid="+hotspot_name+" key="+password, shell=True).decode()
    except:
        pass

    if cmd_output=="":
        try:
            cmd_output = subprocess.check_output("netsh wlan start hostednetwork", shell=True).decode()
        except:
            pass
        if "started" in cmd_output or "" in cmd_output:
            return True
        else:
            return False

    elif "successfully changed" in cmd_output:
        cmd_output = subprocess.check_output("netsh wlan start hostednetwork", shell=True).decode()
        if "started" in cmd_output:
            return True
    else:
        return False

#return how many devices connected to your hotspot
def connected_devices():
    if check_hotspot():
        cmd_output = subprocess.check_output("netsh wlan show hostednetwork", shell=True).decode()
        cmd_output = cmd_output.replace("\r","")
        list_output = cmd_output.split("\n")
        for i in list_output:
            if "Number of clients      :" in i:
                clients =int(i.split(":")[1][1:])

        return clients

    return False



#check if you open hotspot or not then stop hotspot network if it done return True else return False
#input only hotspot name and password of hotspot
def stop_hotspot():
    cmd_output = subprocess.check_output("netsh wlan show hostednetwork", shell=True).decode()
    if check_hotspot():
        cmd_output = subprocess.check_output("netsh wlan stop hostednetwork", shell=True).decode()
        return True
    return False



###############################################################################################################
##########################################Server and host functions############################################
###############################################################################################################

#spot ID explain :
# room ID . computer ID . hub

#examples :
#1.0.0     It's server ID [sever ID must be number.0.0 ]
#1.1.1     It's host ID   [it's follow the room in the first number]

#Room ID :
#it's classification the network if we have muli chain spot networks in the same area

#Computer ID :
#it's classification the computer to handle them easily , it's unique for one room

#Hub :
#it's like a jump how host the communication pass from the server to the currently host


#it's return list of spot ID which contain rooms and computer ID return
def parse_wifi():
    power=power_wifi()
    networks= list(power.keys())
    r = re.compile("\d+\.\d+\.\d+")
    id_list = list(filter(r.match, networks))
    room_list = []
    comp_id=[]
    if id_list: #Bug we can remove "if id_list" for loop will do this check for us 
        for i in id_list:
            room_list.append(int(i.split(".")[0]))
            comp_id.append(int(i.split(".")[1]))
    return power , id_list, sorted(room_list) , sorted(comp_id)


#it's connect to the best chosse of spot ID list , it's need to id_list from parse_wifi() and take room ID and Password from the user
def best_wifi(power,id_list,room,password):
    sorted_ip=[]
    s = re.compile(str(room)+".\d+\.\d+")
    sorted_ip = list(filter(s.match, id_list))
    sorted_ip=sorted(sorted_ip,key=lambda t:(int(t.split('.')[2]),-power[t],int(t.split('.')[1]))) #Priority in sorting to hub to reduce hubs As much as possible
    #Second priority for the signal power To maintain network stability
    t = re.compile("\d+\.0.0") #filter spot ID to one room
    server_ip = list(filter(t.match, sorted_ip))
    if server_ip:
        wifi_connect =server_ip[0]
        if power[wifi_connect] >= 60:
            status = connect_wifi(wifi_connect,password)
            if status:
                return wifi_connect
    if sorted_ip:
        for wifi_connect in sorted_ip:
            if power[wifi_connect] >= 50:
                status = connect_wifi(wifi_connect,password)
                if status:
                    return wifi_connect
    return False




###############################################################################################################
################################################## Misc #######################################################
###############################################################################################################

#check if the script run as administrator or not if not  it'll restart the script with admin rights
def run_as_admin(argv=None, debug=False):
    shell32 = ctypes.windll.shell32
    if argv is None and shell32.IsUserAnAdmin():
        return True

    if argv is None:
        argv = sys.argv
    if hasattr(sys, '_MEIPASS'):
        # Support pyinstaller wrapped program.
        arguments = map(str, argv[1:])
    else:
        arguments = map(str, argv)
    argument_line = u' '.join(arguments)
    executable = str(sys.executable)
    if debug:
        print ('Command line: ', executable, argument_line)
    ret = shell32.ShellExecuteW(None, u"runas", executable, argument_line, None, 1)
    if int(ret) <= 32:
        return False
    return None


#################################################################################################################


if __name__ == '__main__':
    run_as_admin()
    if platform.release() != "10":
        print("\n[X] Sorry ChainSpoT support only windows 10 , We work on all operating system to support it soon , Be waiting")
        input("\n\t \t \t \t    PRESS ANY KEY TO EXIT...")
        sys.exit()

    supp = support_wifi()
    if supp ==1:

        ChainSpoT='''
                                                                                               ,----,
                                                                                             ,/   .`|
  ,----..    ,---,                                       .--.--.                           ,`   .'  :
 /   /   \ ,--.' |                  ,--,                /  /    '. ,-.----.              ;    ;     /
|   :     :|  |  :                ,--.'|         ,---, |  :  /`. / \    /  \    ,---.  .'___,/    ,'
.   |  ;. /:  :  :                |  |,      ,-+-. /  |;  |  |--`  |   :    |  '   ,'\ |    :     |
.   ; /--` :  |  |,--.  ,--.--.   `--'_     ,--.'|'   ||  :  ;_    |   | .\ : /   /   |;    |.';  ;
;   | ;    |  :  '   | /       \  ,' ,'|   |   |  ,"' | \  \    `. .   : |: |.   ; ,. :`----'  |  |
|   : |    |  |   /' :.--.  .-. | '  | |   |   | /  | |  `----.   \|   |  \ :'   | |: :    '   :  ;
.   | '___ '  :  | | | \__\/: . . |  | :   |   | |  | |  __ \  \  ||   : .  |'   | .; :    |   |  '
'   ; : .'||  |  ' | : ," .--.; | '  : |__ |   | |  |/  /  /`--'  /:     |`-'|   :    |    '   :  |
'   | '/  :|  :  :_:,'/  /  ,.  | |  | '.'||   | |--'  '--'.     / :   : :    \   \  /     ;   |.'
|   :    / |  | ,'   ;  :   .'   \;  :    ;|   |/        `--'---'  |   | :     `----'      '---'
 \   \ .'  `--''     |  ,     .-./|  ,   / '---'                   `---'.|
  `---`               `--`---'     ---`-'                            `---`


        '''
        print(ChainSpoT)
    elif supp ==2: #just check if the user turn off wifi
        print("\n[X] Sorry your WIFI is off , To use this script you must turn it on and try again")
        input("\n\t \t \t \t    PRESS ANY KEY TO EXIT...")
        sys.exit()
    else:
        print("\n[X] Sorry your device not support WIFI , you can't use this script")
        input("\n\t \t \t \t    PRESS ANY KEY TO EXIT...")
        sys.exit()

    print("[?] Are you... \n[1]  server  \n[2]  host ")
    chosse = input(">> ")
    chosse=chosse.strip()
    if chosse=="1":
        print("[?] Enter Server Password \n[!] Remember that the password has to be at least 8 characters in length ")
        password = input(">> ")
        if len(password)>=8:
            m = main(password)
        else:
            print("\n[X] Invalid input")
            input("\n\t \t \t \t    PRESS ANY KEY TO EXIT...")
            sys.exit()


    elif chosse=="2":
        print("[!] We'll show you some of available rooms")
        power,id_list,room_list,comp_id =parse_wifi()
        if room_list:
            room_list=sorted(list(set(room_list)))
            print("\n \t\t\t\t   ~ AVAILABLE ROOMS ~    \n")
            for i in room_list:
                print("\t\t\t\t\t    "+str(i))
            print("\n")
        else:
            print("[X] there's no available rooms")
        print("[!] This is an indicative list only , you can enter any room number you want even if not at the list\n[?] Enter room number ")
        room = input(">> ")
        try:
            room=room.strip()
            room = int(room)
        except:
            print("\n[X] Invalid input , It must be a number")
            input("\n\t \t \t \t    PRESS ANY KEY TO EXIT...")
            sys.exit()
        print("[?] Enter Server Password \n[!] Remember that the password has to be at least 8 characters in length ")
        password = input(">> ")
        if len(password)>=8:
            m = main(password,room)
        else:
            print("\n[X] Invalid input")
            input("\n\t \t \t \t    PRESS ANY KEY TO EXIT...")
            sys.exit()


    else:
        print("\n[X] Invalid input")
        input("\n\t \t \t \t    PRESS ANY KEY TO EXIT...")
        sys.exit()

    stop_hotspot()
    profiles=show_profiles()
    if profiles:
        r = re.compile("\d+\.\d+\.\d+")
        profiles = list(filter(r.match, profiles))
        if profiles:
            delete_profiles(profiles)
