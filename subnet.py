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

def subnetByNetworks(Octets, netMask):
    
    if netMask == 24:
        interestingOctet = 3
    elif netMask == 16:
        interestingOctet = 2
    elif netMask == 8:
        interestingOctet = 1
    else:
        print("error, correct octet not found")
    totalNetworks = inputInt("how many subnets would you like to create? ")
    addedBits = 0
    while ((2**addedBits) < totalNetworks):
        addedBits += 1
    print(addedBits)
    newNetMask = netMask + addedBits
    print("your new networks will be:")
    if interestingOctet == 3:
        octetValue = 0
        while (octetValue < 256):
            print(Octets[0], ".", Octets[1],".", Octets[2], ".", octetValue, "/", newNetMask)
            octetValue += 2 ** (8-addedBits)
        print("each network will contain", 2**(8-addedBits), "addresses", (2**(8-addedBits))-2, "of which are useable")
    elif interestingOctet == 2:
        octetValue = 0
        while (octetValue < 256):
            print(Octets[0], ".", Octets[1], ".", octetValue, ".", Octets[3], "/", newNetMask)
            octetValue += 2** (8-addedBits)
        print("each network will contain", (2**((8-addedBits)+8)), "addresses", (2**(((8-addedBits))+8))-2, "of which are useable")
    elif interestingOctet == 1:
        octetValue = 0
        while (octetValue < 256):
            print(Octets[0], ".", octetValue, ".", Octets[2], ".", Octets[3], "/", newNetMask)
            octetValue += 2**(8-addedBits)
        print("each network will contain", (2**((8-addedBits)+16)), "addresses", (2**((8-addedBits)+16))-2, "of which are useable")


def currentNetwork():
    IPAddress = getCurrentIPAddress()
    print(IPAddress)

def differentNetwork():
    IPAddress = input("Please enter your network ID and subnet mask in CIDR notation ")
    firstSplit = IPAddress.rsplit("/", 1)
    IPAddress = firstSplit[0]
    netMask = int(firstSplit[1])
    Octets = IPAddress.split(".")
    for i in range(len(Octets)-1):
        Octets[i] = int(Octets[i])
    print("select an option below")
    print("1) subnet based on desired number of networks")
    print("2) subnet based on desired number of addresses per network")
    choice = inputInt("option: ")
    if choice == 1:
        subnetByNetworks(Octets, netMask)
    elif choice == 2:
        subnetByAddresses(Octets, netMask)
    else:
        print("error in different network function")
        exit(0)


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
