import requests
import os
import re

def get_ip (url, file = False, filename = None):
    url_ip = f"https://dns.adguard-dns.com/resolve?name={url}"
    header = {"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64; rv:141.0) Gecko/20100101 Firefox/141.0"}
    try:
        pattern = re.compile(r'\d+\.\d+\.\d+\.\d+')
        s = requests.Session()
        response = s.get(url_ip, headers=header)
        doc = pattern.findall(response.text)
        file_path = os.path.exists(str(filename))

        if file and file_path:
            with open(filename, 'a') as f:
                f.write(f'\n{doc}\n')
                f.close()

        elif file and file_path == False:
            with open('dns_response.txt', 'w') as f:
                f.write(f'\n{doc}\n')
                f.close()
        return doc

    except Exception as e:
        if e == IndexError: print("Usage: python3 main.py <link> <file=True or False> <filename>")

def get_directories(addrs):
    pass
