import requests, json, sys, socket


'''
        1. Empty Input Check
        2. If input starts with http or https
        3. Remove http or https
'''
try:
    def check_dns_resolution(target):
        try:
            ip = socket.gethostbyname(target)
            return True
        except socket.gaierror:
            return False

    def get_subdomains():
        domain = input("Enter target website url: ")

        if not domain:
            print("\n You didn't provide any input!")
            sys.exit(1)
        
        if domain.startswith("http://"):
            domain = domain.replace("http://", "", 1)
        elif domain.startswith("https://"):
            domain = domain.replace("https://", "", 1)

        if not check_dns_resolution(domain):
            print("\nTarget website doesn't resolve.")
            sys.exit(1)
        
        api_endpoint = 'https://otx.alienvault.com/api/v1/indicators/domain/'
        api_key = '<YOUR_API_KEY>'
        url = api_endpoint + domain + '/passive_dns'
        headers = {'X-OTX-API-KEY': api_key}

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            subdomains = {entry['hostname'] for entry in data['passive_dns']}
            for subdomain in subdomains:
                print(subdomain)
        else:
            output = "Not Found"
            print(output)
except Exception as e:
    print("\n An Error Occurred!")
    sys.exit(1)
