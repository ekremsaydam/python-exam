linux
ifconfig eth0 down
ifconfig eth0 hw ether 00:11:22:33:44:55
ifconfig eth0 up

windows
getmac.exe /v /fo list
net config workstation
Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Class\{4d36e972-e325-11ce-bfc1-08002be10318}\0002
New > String
NetworkAddress 001122334455

```
import subprocess

subprocess.call(["ifconfig", "eth0"," down"])
subprocess.call(["ifconfig", "eth0", "hw", "ether", "00:11:22:33:44:55"])
subprocess.call(["ifconfig", "eth0", "up"])
```

```
import subprocess
import optparse

parse_object = optparse.OptionParser()
parse_object.add_option("-i", "--interface", dest="interface", help="interface to change")
parse_object.add_option("-m", "--mac", dest="mac_address", help="new mac address")
(user_input,arguments) = parse_object.parse_args()

interface = user_input.interface
mac_address = user_input.mac_address

print("MyMacChanger started")
subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", mac_address])
subprocess.call(["ifconfig", interface, "up"])
```

```
import subprocess
import optparse
import re


def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--interface", dest="interface", help="interface to change")
    parse_object.add_option("-m", "--mac", dest="mac_address", help="new mac address")
    return parse_object.parse_args()


def change_mac_address(user_interface, user_mac_address):
    subprocess.call(["ifconfig", user_interface, "down"])
    subprocess.call(["ifconfig", user_interface, "hw", "ether", user_mac_address])
    subprocess.call(["ifconfig", user_interface, "up"])


def control_new_mac(user_interface):
    ifconfig = subprocess.check_output(["ifconfig", user_interface]).decode('utf8')

    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig)
    if new_mac:
        return new_mac.group(0)
    else:
        return None


print("MyMacChanger started")
(user_input, arguments) = get_user_input()
change_mac_address(user_input.interface, user_input.mac_address)

new_mac = control_new_mac(user_input.interface)
if user_input.mac_address == new_mac:
    print("Success!")
else:
    print("Error!")
```

Windows
netsh interface set interface name='Ethernet' admin=ENABLED
netsh interface set interface name='Ethernet' admin=DISABLED
runas /user:dev\devops "netsh interface set interface name='Ethernet' admin=DISABLED"
whoami

```
import scapy.all as scapy

# arp requiest
# broadcast
# response
arp_request_packet = scapy.ARP(pdst="192.168.200.1/24")
# scapy.ls(scapy.ARP())
broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
# scapy.ls(scapy.Ether())
combined_packet = broadcast_packet / arp_request_packet
(answered_list,unanswered_list) = scapy.srp(combined_packet, timeout=1)
# print(list(answered_list))
answered_list.summary()
```

https://scapy.readthedocs.io/en/latest/installation.html#latest-release
pip install --use-pep517 --pre scapy[complete]

```
"""Scapy denemeleri."""
# import scapy.all as scapy
# import optparse
# https://peps.python.org/pep-0389/
import argparse

from scapy.all import ARP, Ether, conf, srp


# arp_request = ARP(
#     psrc="192.168.100.5",
#     pdst="192.168.100.1/24",
# )
def user_input():
    # parse = optparse.OptionParser()
    # parse.add_option("-i", "--ipaddres", dest="ipaddress", help="ex: 192.168.1.1/24")
    parse = argparse.ArgumentParser()
    parse.add_argument("-i", "--ipaddress", dest="ipaddress", help="ex: 192.168.1.1/24")

    userinput = parse.parse_args()
    return userinput.ipaddress


def network_discovery(ip="192.168.100.1/24"):
    # type: ignore
    arp_request = ARP()
    arp_request.psrc = conf.route.route(ip.split("/")[0])[1]
    arp_request.pdst = ip
    # print(arp_request)
    # broadcast_package = Ether(dst="ff:ff:ff:ff:ff:ff")
    broadcast_package = Ether()
    broadcast_package.dst = "ff:ff:ff:ff:ff:ff"
    # print(broadcast_package)
    send_packet = broadcast_package / arp_request
    print(send_packet)

    ans, unans = srp(send_packet, timeout=10)
    for a in ans:
        print(a[1].psrc, a[1].src, sep="\t")
    # ans.summary()


ipaddress = user_input()
print(ipaddress)
if not ipaddress:
    print("use parameter. info --help")
else:
    network_discovery(ipaddress)
```

scapy
sniff(count=1000,prn=lambda x: x.summary())
