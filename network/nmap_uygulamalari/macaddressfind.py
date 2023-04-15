import nmap

# subnet'in ilk üç octet'i
subnet = "192.168.1."

# nmap tarama objesi oluştur
nm = nmap.PortScanner()

# tarama işlemini başlat
# nm.scan(hosts=subnet + "0/24", arguments="-n -sP -sT")
nm.scan(hosts=subnet + "0/24", arguments="-sn")

# sonuçları yazdır
for host in nm.all_hosts():
    if nm[host]["status"]["state"] == "up":
        # Cihazın MAC adresini alın
        mac_addr = (nm[host]["addresses"]).get("mac", "Mac Not Found")
        # Cihazın IP adresini alın
        ip_addr = nm[host]["addresses"]["ipv4"]
        # Cihazın üreticisini alın
        listVendor = list(
            nm[host].get("vendor", {"NotFound": "Vendor Not Found"}).values()
        )
        vendor = "Not Found" if len(listVendor) == 0 else listVendor[0]
        # Sonuçları yazdırın
        print("IP : {}\tMAC : {}\tÜretici : {}".format(ip_addr, mac_addr, vendor))
