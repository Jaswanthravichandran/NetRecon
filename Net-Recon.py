from termcolor import colored
import time
from External_API import StartScan


banner = """"Banner Here"""""

menu = """
[1] Traceroute
[2] Ping Test
[3] DNS Lookup
[4] Reverse DNS
[5] Find DNS Host
[6] Find Shared DNS
[7] Zone Transfer
[8] Whois Lookup
[9] IP Location Lookup
[10] Reverse IP Lookup
[11] TCP Port Scan
[12] Subnet Lookup
[13] HTTP Header Check
[14] Extract Page Links
[15] Version
[16] Exit
"""


print(banner)
print(menu)


def main():

    try:
        choice = (input(colored('Enter option number : ', 'yellow')))

        if choice == '1':
            print("\n")
            print("[+] Traceroute script running..")
            target = (input(colored("[+] Target : ", 'blue')))
            print("\n")
            txt = StartScan(1, target)
            print(colored(txt, 'green'))

        elif choice == '2':
            print("\n")
            print("[+] Ping Test script running..")
            target = (input(colored("[+] Target : ", 'blue')))
            print("\n")
            txt = StartScan(2, target)
            print(colored(txt, 'green'))

        elif choice == '3':
            print("\n")
            print("[+] DNS Lookup script running..")
            target = (input(colored("[+] Target : ", 'blue')))
            print("\n")
            txt = StartScan(3, target)
            print(colored(txt, 'green'))

        elif choice == '4':
            print("\n")
            print("[+] Reverse DNS script running..")
            target = (input(colored("[+] Target : ", 'blue')))
            print("\n")
            txt = StartScan(4, target)
            print(colored(txt, 'green'))

        elif choice == '5':
            print("\n")
            print("[+] Find DNS Host script running..")
            target = (input(colored("[+] Target : ", 'blue')))
            print("\n")
            txt = StartScan(5, target)
            print(colored(txt, 'green'))

        elif choice == '6':
            print("\n")
            print("[+] Find Shared DNS script running..")
            target = (input(colored("[+] Target : ", 'blue')))
            print("\n")
            txt = StartScan(6, target)
            print(colored(txt, 'green'))

        elif choice == '7':
            print("\n")
            print("[+] Zone Transfer script running..")
            target = (input(colored("[+] Target : ", 'blue')))
            print("\n")
            txt = StartScan(7, target)
            print(colored(txt, 'green'))

        elif choice == '8':
            print("\n")
            print("[+] Whois Lookup script running..")
            target = (input(colored("[+] Target : ", 'blue')))
            print("\n")
            txt = StartScan(8, target)
            print(colored(txt, 'green'))

        elif choice == '9':
            print("\n")
            print("[+] IP Location Lookup script running..")
            target = (input(colored("[+] Target : ", 'blue')))
            print("\n")
            txt = StartScan(9, target)
            print(colored(txt, 'green'))

        elif choice == '10':
            print("\n")
            print("[+] Reverse IP Lookup script running..")
            target = (input(colored("[+] Target : ", 'blue')))
            print("\n")
            txt = StartScan(10, target)
            print(colored(txt, 'green'))

        elif choice == '11':
            print("\n")
            print("[+] TCP Port Scan script running..")
            target = (input(colored("[+] Target : ", 'blue')))
            print("\n")
            txt = StartScan(11, target)
            print(colored(txt, 'green'))

        elif choice == '12':
            print("\n")
            print("[+] Subnet Lookup script running..")
            target = (input(colored("[+] Target : ", 'blue')))
            print("\n")
            txt = StartScan(12, target)
            print(colored(txt, 'green'))

        elif choice == '13':
            print("\n")
            print("[+] HTTP Header Check script running..")
            target = (input(colored("[+] Target : ", 'blue')))
            print("\n")
            txt = StartScan(13, target)
            print(colored(txt, 'green'))

        elif choice == '14':
            print("\n")
            print("[+] Extract Page Links script running..")
            target = (input(colored("[+] Target : ", 'blue')))
            print("\n")
            txt = StartScan(14, target)
            print(colored(txt, 'green'))
            
        elif choice == '15':
            print("\n")
            print("[+] Version Checking..")
            time.sleep(2)
            version_number = "2.0"
            time.sleep(3)
            print("[+] Version : " + version_number)

        elif choice == '16':
            exit()

    except KeyboardInterrupt:
        print("\nAborted!")
        quit()
    except:
        print("Invalid Option !\n")
        return main()



if __name__ == '__main__':
    main()