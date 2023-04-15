import nmap

# tarama yapılacak IP adresi
ip = '192.168.1.1/24'

# nmap tarama objesi oluştur
nm = nmap.PortScanner()

# tarama işlemini başlat
nm.scan(ip, arguments='-p 1-1000')

# sonuçları yazdır
for host in nm.all_hosts():
    print('IP address:', host)
    for proto in nm[host].all_protocols():
        print('Protocol:', proto)
        lport = nm[host][proto].keys()
        sorted_ports = sorted(lport)
        for port in sorted_ports:
            print('Port:', port, 'Status:', nm[host][proto][port]['state'])
