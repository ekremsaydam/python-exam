import nmap

# subnet'in ilk üç octet'i
subnet = '192.168.1.'

# nmap tarama objesi oluştur
nm = nmap.PortScanner()

# tarama işlemini başlat
nm.scan(hosts=subnet+'0/24', arguments='-n -sP')

# sonuçları yazdır
for host in nm.all_hosts():
    if nm[host]['status']['state'] == 'up':
        print('IP address:', host)