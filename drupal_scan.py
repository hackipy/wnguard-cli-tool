import requests
try:
    def scan_drupal(target):
        output = []
        sensitive_urls = [
        f'{target}/sites/default/settings.php',
        f'{target}/sites/default/services.yml',
        f'{target}/install.php',
        f'{target}/install.php.txt',
        f'{target}/tmp',
        f'{target}/private',
        f'{target}/admin-specific-file.php',
        f'{target}/README.txt',
        f'{target}/sites',
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

# print(scan_drupal("https://scilms.com"))
