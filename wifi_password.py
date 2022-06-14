"""(15.04.2022)WIFI agina katilirken kullanilan sifrelerin gösterilmesi."""
import subprocess

data = subprocess.check_output("netsh wlan show profiles").\
    decode(encoding="cp1252").split('\n')

wlanNameList = [v.split(':')[1].strip()
                for v in data if "All User Profile" in v]
wlanNameAndPasswordList = []
for SID in wlanNameList:
    data = subprocess\
        .check_output("netsh wlan show profiles " + SID + " key=clear")\
        .decode("cp1252").split('\n')
    wlanNameAndPasswordList += [(SID, WIFIpass.split(':')[1].strip())
                                for WIFIpass in data
                                if "Key Content" in WIFIpass]

for SID, password in wlanNameAndPasswordList:
    print(f"{SID:<20} : {password}")
