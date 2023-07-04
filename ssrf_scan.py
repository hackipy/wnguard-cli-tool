import requests, sys

try:
    def SCAN_SSRF():
        try:
            url = input("Enter target website url: ")
            if not url:
                print("\nYou didn't provide any input!")
                sys.exit(1)
            if url.startswith("http://") or url.startswith("https://"):
                headers = {"Host": "google.com"}
                response = requests.get(url, headers=headers)
                if response.status_code == 301 or response.status_code == 302 or response.status_code == 200 or response.status_code == 403:
                    output = [url," is vulnerable to Server Side Request Forgery!"]
                    print(output)
                    sys.exit(1)
                else:
                    output = [url," is not vulnerable to Server Side Request Forgery."]
                    print(output)
                    sys.exit(1)
            else:
                print("\nYou didn't provide url with valid http or https scheme.")
                sys.exit(1)
        except Exception as e:
            print("\nAn Error Occurred!")
            sys.exit(1)
except Exception as e:
    print("\nAn Error has occurred!")
    sys.exit(1)