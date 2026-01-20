import os
import socket 
import ipaddress

local = host_name = socket.gethostname()
ip_adresa = socket.gethostbyname(host_name)
my_ip = ip_adresa
network = ipaddress.IPv4Network(f"{my_ip}/24", strict=False)


def logo():

    print("\033[31m██████████      ███████      █████████  █████   ████\033[0m")
    print("\033[31m░░███░░░░███   ███░░░░░███   ███░░░░░███░░███   ███░\033[0m")
    print("\033[31m ░███   ░░███ ███     ░░███ ███     ░░░  ░███  ███\033[0m")
    print("\033[31m ░███    ░███░███      ░███░███          ░███████\033[0m")
    print("\033[31m ░███    ░███░███      ░███░███          ░███░░███\033[0m")
    print("\033[31m ░███    ███ ░░███     ███ ░░███     ███ ░███ ░░███\033[0m")
    print("\033[31m ██████████   ░░░███████░   ░░█████████  █████ ░░████\033[0m")
    print("\033[31m░░░░░░░░░░      ░░░░░░░      ░░░░░░░░░  ░░░░░   ░░░░\033[0m")



logo()
print("------------------------------")
pomoc = print(f"\033[96mTvoje ip adresa: {my_ip},\033[0m")
pomoc2 = print(f"\033[96mPrvni ip (obvykle router): {list(network.hosts())[0]}\033[0m")
subnet = print(f"\033[96mSubnet maska: {network.broadcast_address}\033[0m")
cara = print("------------------------------")
zaklad_ip = input(f"\033[92mZadej svoji ip (format: 192.168.xxx.): \033[0m")
print("------------------------------")
od = int(input(f"\033[92mOd: \033[0m"))
print("------------------------------")
do = int(input(f"\033[92mDo: \033[0m"))

print("\033[92m\nVyber rezim:\033[0m")
print("\033[92m1 - vypis vsech IP\033[0m")
print("\033[92m2 - vypis jen ONLINE IP\033[0m")
volba = input("\033[92mTvoje volba (1/2): \033[0m")

print("\033[92m\n--- ONLINE IP ---\n\033[0m")


for i in range(od, do + 1):
    ip = f"{zaklad_ip}{i}"
    response = os.system(f"ping -n 1 -w 500 {ip} > nul")

    if response == 0:
        try:
            host_name = socket.gethostbyaddr(ip)[0]
        except:
            host_name = "NELZE ZJISTIT"

    if volba == "1":
        if response == 0:
            print(f"\033[32m{ip} je ONLINE | HOSTNAME: {host_name}\033[0m")

        else:
            print(f"\033[31m{ip} je offline\033[0m")


    elif volba == "2":
        if response == 0:
            print(f"\033[32m{ip} je ONLINE | HOSTNAME: {host_name}\033[0m")


    else:
        print("Neplatna volba")
        break
