import requests, sys

try:
    def SCAN_OPEN_REDIRECT():
        try:
            url = input("Enter your target website endpoint: ")
            if not url:
                print("You didn't provide any input!")
                sys.exit(1)
            if url.startswith("http://") or url.startswith("https://"):
                response = requests.head(url)
                if response.status_code in (301, 302):
                    output = [url," is vulnerable to Open Redirect Vulnerability."]
                    print(output)
                    sys.exit(1)
                else:
                    output = [url," is not vulnerable to Open Redirect Vulnerability."]
                    print(output)
                    sys.exit(1)
            else:
                print("You didn't provide valid URL with http or https scheme.")
                sys.exit(1)
        except Exception as e:
            pass
except Exception as e:
    print("\nAn Error Occured!")
    sys.exit(1)