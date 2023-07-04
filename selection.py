import sys, os, re
#WEB
from http_header_security import scan_headers
from web_port_scan import main_web_port_scan
from find_subdomains import get_subdomains
from xss_finder import XSS_SCAN
from sqli_scan import SQLi_SCAN
from password_bruteforcer import main_bruteforce
from ssrf_scan import SCAN_SSRF
from open_redirect_detector import SCAN_OPEN_REDIRECT
from scan_wp import scan_wordpress
from joomla_scan import scan_joomla
from drupal_scan import scan_drupal
from directory_bruteforcer import all_func
#Network

from net_port_scan import main_net_port_scan
from service_detector import main_net_port_serv_scan

# -----

try:
    def validate_ip_address(ip_address):
        pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
        if re.match(pattern, ip_address):
            return True
        else:
            return False
    def web_selection(mynumber):
        if mynumber == 1:
            try:
                scan_headers()
            except Exception as e:
                print("\n An Error Occured!")
                sys.exit(1)
        elif mynumber == 2:
            try:
                main_web_port_scan()
            except Exception as e:
                print("\n An Error Occured!")
                sys.exit(1)
        elif mynumber == 3:
            try:
                get_subdomains()
            except Exception as e:
                print("\n An Error Occured!")
                sys.exit(1)
        elif mynumber == 4:
            try:
                target= input('Enter your target website link: ')
                all_func(target)
            except Exception as e:
                print("\n An Error Occured!")
                sys.exit(1)
        elif mynumber == 5:
            try:
                XSS_SCAN()
            except Exception as e:
                print("\n An Error Occured!")
                sys.exit(1)
        elif mynumber == 6:
            try:
                SQLi_SCAN()
            except Exception as e:
                print("\n An Error Occured!")
                sys.exit(1)
        elif mynumber == 7:
            try:
                SCAN_SSRF()
            except Exception as e:
                print("\n An Error Occured!")
                sys.exit(1)
        elif mynumber == 8:
            try:
                SCAN_OPEN_REDIRECT()
            except Exception as e:
                print("\n An Error Occured!")
                sys.exit(1)
        elif mynumber == 9:
            try:
                main_bruteforce()
            except Exception as e:
                print("\n An Error Occured!")
                sys.exit(1)
        elif mynumber == 10:
            try:
                target = input("Enter target wordpress website url: ")
                if not target:
                    print("\nYou didn't enter target website.")
                    sys.exit(1)
                if target.startswith("http") or target.startswith("https"):
                    output = scan_wordpress(target)
                    for data in output:
                        print(data)
                else:
                    print("\nYou didn't enter valid url with http/https scheme.")
                    sys.exit(1)
            except Exception as e:
                print("\n An Error Occured!")
                sys.exit(1)
        elif mynumber == 11:
            try:
                target = input("Enter target joomla website url: ")
                if not target:
                    print("\nYou didn't enter target website.")
                    sys.exit(1)
                if target.startswith("http") or target.startswith("https"):
                    output = scan_joomla(target)
                    for data in output:
                        print(data)
                else:
                    print("\nYou didn't enter valid url with http/https scheme.")
                    sys.exit(1)
            except Exception as e:
                print("\n An Error Occured!")
                sys.exit(1)
        elif mynumber == 12:
            try:
                target = input("Enter target drupal website url: ")
                if not target:
                    print("\nYou didn't enter target website.")
                    sys.exit(1)
                if target.startswith("http") or target.startswith("https"):
                    output = scan_drupal(target)
                    for data in output:
                        print(data)
                else:
                    print("\n You didn't enter valid url with http/https scheme.")
                    sys.exit(1)
            except Exception as e:
                print("\n An Error Occured!")
                sys.exit(1)
        elif mynumber == 13:
            try:
                target=input("Enter the js endpoint: ")
                if not target:
                    print("\nYou didn't enter target js endpoint.")
                    sys.exit(1)
                if target.startswith("http") or target.startswith("https"):
                    os.system(f'python3 -W ignore js_analyzer.py -i {target} -o cli')
                else:
                    print("\nYou didn't enter target link with http/https scheme.")
                    sys.exit(1)
            except Exception as e:
                print("\n An Error Occured!")
                sys.exit(1)
        elif mynumber == 14:
            sys.exit(1)
        else:
            print("Invalid Choice... Exiting!")

    def net_selection(mynumber):
        if mynumber == 1:
            try:
                target_ip = input("Enter the target ip: ")
                starting_range = int(input("Enter the starting port range: "))
                ending_range = int(input("Enter the ending port range: "))
                if not target_ip or not starting_range or not ending_range:
                    print("\nYou didn't enter target ip and ranges!")
                    sys.exit(1)
                if starting_range <= 0 or ending_range > 65535:
                    print("\nYou didn't enter correct range!")
                    sys.exit(1)
                if validate_ip_address(target_ip):
                    main_net_port_scan(target_ip, starting_range, ending_range)
                else:
                    print("\nIP Address not valid!")
                    sys.exit(1)
            except Exception as e:
                    print("\nAn error occured!")
                    sys.exit(1)
        elif mynumber == 2:
            try:
                target_ip = input("Enter the target ip: ")
                starting_range = int(input("Enter the starting port range: "))
                ending_range = int(input("Enter the ending port range: "))
                if not target_ip or not starting_range or not ending_range:
                    print("\nYou didn't enter target ip and ranges!")
                    sys.exit(1)
                if starting_range <= 0 or ending_range > 65535:
                    print("\nYou didn't enter correct range!")
                    sys.exit(1)
                if validate_ip_address(target_ip):
                    main_net_port_serv_scan(target_ip, starting_range, ending_range)
                else:
                    print("\nIP Address not valid!")
                    sys.exit(1)
            except Exception as e:
                    print("\n An Error Occured!")
                    sys.exit(1)
        elif mynumber == 3:
            try:
                os.system("sudo python3 -W ignore sniffer.py")
            except Exception as e:
                    print("\n An Error Occured!")
                    sys.exit(1)
        elif mynumber == 4:
            sys.exit(1)
        else:
            print("Invalid Choice... Exiting!")

except Exception as e:
    print("\n An Error Occured!")
    sys.exit(1)