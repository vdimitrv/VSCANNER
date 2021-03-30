#!/usr/bin/python3

import socket
from netaddr import IPNetwork

ip = input("Please enter IP range to scan: ex. 192.168.16.0/24 ",)
port = input("Please enter PORT range to scan: ex. 1-100 ")
port = port.replace('-', ' ').split(' ')

if len(port) > 1:
    port_low = int(port[0])
    port_high = int(port[1]) + 1
    port_range = range(port_low, port_high)

else:
    port_low = int(port[0])
    port_high = int(port[0]) + 1
    port_range = range(port_low, port_high)

for ip in IPNetwork(ip):
    for port in port_range:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        try:
            s.connect((str(ip), port))
            print("Port %d is open on %s" % (port, str(ip)))
            s.close()
        except:
            print("Port %d not open on %s" % (port, str(ip)))
            s.close()
print('Thank you for using VSCAN v2.0')
#!/usr/bin/python3

import socket
from netaddr import IPNetwork

ip = input("Please enter IP range to scan: ex. 192.168.16.0/24 ",)
port = input("Please enter PORT range to scan: ex. 1-100 ")
port = port.replace('-', ' ').split(' ')

if len(port) > 1:
    port_low = int(port[0])
    port_high = int(port[1]) + 1
    port_range = range(port_low, port_high)

else:
    port_low = int(port[0])
    port_high = int(port[0]) + 1
    port_range = range(port_low, port_high)

for ip in IPNetwork(ip):
    for port in port_range:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        try:
            s.connect((str(ip), port))
            print("Port %d is open on %s" % (port, str(ip)))
            s.close()
        except:
            print("Port %d not open on %s" % (port, str(ip)))
            s.close()
print('Thank you for using VSCAN v2.0')
