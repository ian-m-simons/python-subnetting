import sys #may use commandline arguments later
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
    hostname = socket.gethostname()
    IPAddressList = socket.gethostbyname_ex(hostname)
    print(IPAddressList)


def subnetCurrentNetwork():
    IPAddress = getCurrentIPAddress()


def main():
    while (True):
        print("Welcome! Please select an option below")
        print("1) subnet current network")
        print("2) subnet a different network")
        print("3) exit")
        choice = inputInt("option: ")
        if choice == 1:
            subnetCurrentNetwork()
        elif choice == 3:
            break

if __name__ == "__main__":
    main()
