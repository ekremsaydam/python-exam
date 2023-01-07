import sys
import serial

if sys.platform.startswith('win'):
    ports = ['COM'+str(i) for i in range(1, 257)]
print(ports)
active_port = []
for port in ports:
    try:
        s = serial.Serial(port)
        s.close()
        active_port.append(port)
    except:
        pass
print(active_port)
