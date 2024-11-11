import sys #may use commandline arguments later
import netifaces #going to switch to this later
import socket

def inputInt(prompt):
    success = False
    while (not success):
        response = input(prompt)
        try:
            response = int(response)
            success = True
        except:
            print("[Error] Input must be integer")
    return response

def getCurrentIPAddress():
    #currently only grabbing loopback address need to get IP Address associated with default route
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        s.connect(('192.168.0.1', 53))
        IPAddress = s.getsockname()[0]
    except:
        IPAddress = '127.0.0.1'
    finally:
        s.close()
    return IPAddress


def currentNetwork():
    IPAddress = getCurrentIPAddress()
    print(IPAddress)

def differentNetwork():
    IPAddress = input("Please enter your network ID and subnet mask in CIDR notation ")
    firstSplit = IPAddress.rsplit("/", 1)
    IPAddress = firstSplit[0]
    netMask = firstSplit[1]
    Octets = IPAddress.split(".")
    print("select an option below")
    print("1) subnet based on desired number of networks")
    print("2) subnet based on desired number of addresses per network")
    choice = inputInt("option: ")
    if choice == 1:
        subnetByNetworks(Octets, netMask)
    if choice == 2:
        subnetByAddresses(Octets, netMask)




def main():
    while (True):
        print("Welcome! Please select an option below")
        print("1) subnet current network")
        print("2) subnet a different network")
        print("3) exit")
        choice = inputInt("option: ")
        if choice == 1:
            currentNetwork()
        elif choice == 2:
            differentNetwork()
        elif choice == 3:
            break

if __name__ == "__main__":
    main()
