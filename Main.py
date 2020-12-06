import re, subprocess
from random import choice, randint

interface = input("Enter the interface  : ")

def main():
    inp = input("1. Manual change\t2. Random change\t3.Check old Mac\nEnter your choice : ")
    if inp == '1':
        new_mac = input("Enter the new mac you want to change : ")
        mac_changer(interface, new_mac)
        print("You successfully change your mac Address Manually.")
    elif inp == '2':
        new_mac = random_changer()
        mac_changer(interface, new_mac)
        print("You successfully changed your mac Address randomly.")
    elif inp == '3':
        current_mac()
    else:
        print("Invalid Option!")


def current_mac():
    output = subprocess.check_output(["ifconfig "+str(interface)], shell=True)
    currentmac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(output))
    print("your old mac address is : "+str(currentmac))

def mac_changer(interface, new_mac):
    subprocess.call(["ifconfig "+str(interface)+" down"], shell=True)
    subprocess.call(["ifconfig "+str(interface)+" hw ether "+str(new_mac)], shell=True)
    subprocess.call(["ifconfig "+str(interface)+" up"], shell=True)
    print("Your new mac address is : "+str(new_mac))

def random_changer():
    cisco = ['00', '40', '96']
    dell = ['00', '44', '4e']

    mac_address = choice([cisco, dell])

    for i in range(3):
        one = str(randint(0, 9))
        two = str(randint(0, 9))
        three = str(one+two)
        mac_address.append(three)
    return ":".join(mac_address)

if __name__ == '__main__':
    main()