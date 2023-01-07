import serial  # pip install pyserial
import time

com_port = "COM18"
connect_to_dongle = True

print("Dongle bağlanıyor...")

while connect_to_dongle:
    try:
        console = serial.Serial()
        console.port = com_port
        console.baudrate = 57600
        console.parity = serial.PARITY_NONE
        console.stopbits = serial.STOPBITS_ONE
        console.bytesize = serial.EIGHTBITS
        console.timeout = 0
        console.open()
        if console.is_open:
            connect_to_dongle = False
    except:
        print("Dongle takılı değil. Lütfen dongle yeniden bağlayın.")
        connect_to_dongle = False
    else:
        print("Dongle BAĞLANDI.")
    



