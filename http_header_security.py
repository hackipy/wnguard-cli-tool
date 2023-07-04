import requests,sys,socket

try:
    def check_port(url):
        try:
            ip = socket.gethostbyname(url)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            result = sock.connect_ex((ip, 443))
            if result == 0:
                return "https://" + url
            else:
                result = sock.connect_ex((ip, 80))
                if result == 0:
                    return "http://" + url
        except socket.gaierror:
            print("\n Unable to connect to the target!")
            sys.exit(1)
        return None
    def scan_headers():
        '''
        1. Empty Input Check
        2. If input starts with http or https
        3. Remove http or https
        5. Port 80, 443 Check
        6. Processing input with http or https based on above 
        '''
        
        url = input("Enter target website url: ")

        if not url:
            print("\nYou didn't provide any input.")
            sys.exit(1)

        if url.startswith("http://"):
            url = url.replace("http://", "", 1)
        elif url.startswith("https://"):
            url = url.replace("https://", "", 1)

        url = check_port(url)
        response = requests.get(url)
        headers = response.headers

        def check_header(header_key, expected_value=None):
            header_value = headers.get(header_key, "").lower()
            if expected_value is None:
                return f"{header_key} : Fail" if not header_value else f"{header_key} : Pass"
            elif header_value == expected_value.lower():
                return f"{header_key} : Pass"
            else:
                return f"{header_key} : Fail"

        output = set()
        output.add(check_header("X-XSS-Protection"))
        output.add(check_header("X-Content-Type-Options", "nosniff"))
        output.add(check_header("X-Frame-Options", "deny") or check_header("X-Frame-Options", "Sameorigin"))
        output.add(check_header("Strict-Transport-Security"))
        output.add(check_header("Content-Security-Policy"))
        print()
        for data in output:
            print(data)
except Exception as e:
    print("\n An Error has occured!")
    sys.exit(1)