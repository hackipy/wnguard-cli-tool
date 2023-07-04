import requests

try:
    def scan_joomla(target):
        output = []
        sensitive_urls = [
        f'{target}/configuration.php',
        f'{target}/.htaccess',
        f'{target}/backup.sql',
        f'{target}/error.log',
        f'{target}/administrator/index.php',
        f'{target}/installation.php',
        f'{target}/temp/file.txt',
        f'{target}/user_uploads/image.jpg',
        ]

        for url in sensitive_urls:
            response = requests.get(url)
            if response.status_code == 200:
                output.append(url)
            else:
                pass
        return output
except Exception as e:
    pass

# print(scan_joomla("https://theswingband.com"))
