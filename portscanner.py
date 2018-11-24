import socket
import sys
from datetime import datetime

target = "" #choose your target
targetIP = socket.gethostbyname(target) # get ip of target

tstart = datetime.now()

try:
    for p in range(0, 65535):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((targetIP, p))
        if result == 0:
            print("Port: " + str(p))
        sock.close()
except Exception:
    print("fail")
    sys.exit()

tend = datetime.now()
diff = tend - tstart

print("Scan completed in " + str(diff))
