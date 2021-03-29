import sys
import socket

# GET IP IN RANGE:
ip = input("Please enter IP: ")
parts = ip.split(".")
a = '.'

# GET RANGE HOST NUMBER VALUES:
start = int(input("Please enter start host number: "))
end = int(input("Please enter end host number: "))
iplist = []
# CREATE ALL IPs IN THE RANGE AND RUN PORT SCAN:
for x in range(start, end + 1):
    print(parts[0] + a + parts[1] + a + parts[2] + a + str(x))
    iptest = (parts[0] + a + parts[1] + a + parts[2] + a + str(x))
    iplist.append(iptest)
    print('IP to be scanned: ' + str(iptest))
#   print(iplist)
    try:
        for port in range(1, 100):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((iptest, port))
            if result == 0:
                print("Port {} is open".format(port))
            s.close()

        # RETURNS ERROR INDICATOR
    except socket.error:
        print("Server not responding !!!!")
        print("Thank you for using my script")
        sys.exit()

# END OF SCRIPT
print("Thank you for using VALE script")
