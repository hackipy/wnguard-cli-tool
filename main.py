from banner import banner
from selection import web_selection, net_selection
import sys, os

try:
    banner()
    print("\nWelcome to WNGUARD CLI Tool!")
    print("1. Website Scanning Mode")
    print("2. Network Scanning Mode")
    print("3. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except Exception as ValueError:
        print("\n Invalid Input!")
        sys.exit(1)

    if choice == 1:
        os.system('clear')
        banner()
        print("\n1. HTTP Headers Scan -- Scans for missing security HTTP Headers")
        print("2. Port Scan -- Scans for open ports on a web server")
        print("3. Subdomain Enumeration -- Scans for subdomains of a website")
        print("4. Content Discovery -- Discover contents on a web server by directory bruteforcing")
        print("5. XSS Scan -- Scans for xss vulnerabilities on a website")
        print("6. SQLi Scan -- Scans for sql injection vulnerabilities on a website")
        print("7. SSRF Scan -- Scans for server side request forgery on a website")
        print("8. Open Redirect Scan -- Scans for open redirect on a website")
        print("9. BruteForce Authentication -- Bruteforces authentication for weak credentials")
        print("10. Scan Wordpress -- Scans wordpress for information leakage")
        print("11. Scan Joomla -- Scans joomla for information leakage")
        print("12. Scan Drupal -- Scans drupal for information leakage")
        print("13. Javascript File Analyzer -- Scans information leakage in js files.")
        print("14. Exit")
        try:
            web_choice = int(input("\nEnter your choice: "))
        except Exception as ValueError:
            print("\n Invalid Input!")
            sys.exit(1)
        web_selection(web_choice)
    elif choice == 2:
        os.system('clear')
        banner()
        print("\n1. Port Scan -- Scans for open ports on a web server")
        print("2. Service Enumeration -- Enumerates services on a network")
        print("3. Traffic Snifer -- Sniff Traffic on the network")
        print("4. Exit")
        try:
            net_choice = int(input("\nEnter your choice: "))
        except Exception as ValueError:
            print("\n Invalid Input!")
            sys.exit(1)
        net_selection(net_choice)
    elif choice == 3:
        print("\n You Exited!")
        sys.exit(1)
    else:
        print("\nInvalid choice!")

except Exception as e:
    print("\nError Occured!")
    sys.exit(1)