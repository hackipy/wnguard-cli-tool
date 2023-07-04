import requests

try:
    def scan_wordpress(target):
        output = []
        existence = True
        response = requests.get(target + "/robots.txt")
        if response.status_code == 200:
            if "Disallow: /wp-admin/" in response.text:
                output.append("Admin Panel leaked in robots.txt file: /wp-admin")
            else:
                output.append("Admin Panel not leaked.")
        else:
            output.append("robots.txt file not found.")
        response = requests.post(target + "/xmlrpc.php")
        if response.status_code == 406:
            output.append("xmlrpc.php is publicly accessible!.")
        else:
            output.append("xmlrpc.php file not found.")

        response = requests.get(target + "/wp-json/wp/v2/users")
        if response.status_code == 200:
            data = response.json()
            for user in data:
                name = user['name']
                output.append(f"Username of admin is {name}")
        else:
            output.append('No admin usernames found.')

        website_url = target

        url_list = [f"{website_url}/wp-config.php", 
                    f"{website_url}/.htaccess", 
                    f"{website_url}/wp-content/uploads/", 
                    f"{website_url}/wp-includes/"]
        
        for url in url_list:
            response = requests.get(url)
            if response.status_code == 200:
                output.append(f"Publicly Accessible: {url}")
            else:
                pass
        return output
except Exception as e:
    pass