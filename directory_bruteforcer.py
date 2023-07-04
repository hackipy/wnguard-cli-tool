from colorama import Fore
import concurrent.futures
import requests
import time
import validators
import socket
import sys

'''
1. Input of url and wordlist is empty
2. http or https is stripped
3. Ip is not entered
4. try except whole statement
5. Validate URL
'''
try:
    def all_func(user_input):
        # user_input = input(r"Enter Target Website URL: ")

        if user_input == "":
            print("No input provided!")
            sys.exit(1)
        else:
            pass

        if validators.url(user_input):
            pass
        else:
            print("Invalid URL provided! Kindly provide http or https schema.")
            sys.exit(1)


        def resolution_checker(hostname):
            try:
                socket.gethostbyname(hostname)
                return 1
            except socket.error:
                return 0

        url_check=user_input
        chk1="http://"
        chk2="https://"

        if chk1 in url_check:
            url_check = url_check.strip(chk1)
        elif chk2 in url_check:
            url_check = url_check.strip(chk2)

        if resolution_checker(url_check) == 0:
            print("[!] Unable to connect to the target!")
            sys.exit(1)

        url = user_input
        url.rstrip('/')
        url = url + "/"

        # Wordlist file
        wordlist = input("Enter path to Wordlist: ")
        if wordlist == "":
            print("No wordlist provided!")
            sys.exit(1)

        threads = 100
        concurrency = 100

        rps = 150


        sleep_time = 1 / rps

        print()
        def bruteforce(word):
            response = requests.get(url + word)
            # if response.status_code == 200:
            print(f'{url}{word} -> ({response.status_code})')
            # elif response.status_code == 403:
            #     print(f'[!] Forbidden Directory: {url}{word} -> ({response.status_code})')

        with open(wordlist, 'r') as f:
            words = f.read().splitlines()

        with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
            for word in words:
                while True:
                    if executor._work_queue.qsize() < concurrency:
                        executor.submit(bruteforce, word)
                        time.sleep(sleep_time)
                        break

except Exception as e:
    print("\n An Error Occured!")
    sys.exit(1)