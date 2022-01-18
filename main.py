from urllib import request
import os
import json
import socket

banner = """Network Multi-tool by Lamp & ESCR development team
=========================================================
1. geoip [ip]                   | show ip information
2. sportscan [ip] [port]        | scan a single port
3. cportscan [ip] [start] [end] | custom port scanner
4. ping [ip] [timeout]          | ip pinger
=========================================================
"""

def geoip(addr):
    r = request.urlopen("https://api.ipfind.com/?ip=" + addr)
    p = json.loads(r.read())
    result = f"""
IP Address     : {p["ip_address"]}
Country        : {p["country"]}
Country Code   : {p["country_code"]}
Continent      : {p["continent"]}
City           : {p["city"]}
Region         : {p["region"]}
Region Code    : {p["region_code"]}
Postal Code    : {p["postal_code"]}
Timezone       : {p["timezone"]}
"""
    print(result)

def portscanner(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((str(ip), int(port)))
        return True
    except:
        return False

def main():
    os.system("cls" if os.name == "nt" else "clear")
    print(banner)
    while True:
        try:
            que = input(">> ")
            qw = que.split(" ")[0]
            if qw == "geoip" or qw == "GEOIP":
                qw, ip = que.split(" ")
                geoip(ip)
            elif qw == "cportscan" or qw == "CPORTSCAN":
                qw, ip, start, end = que.split(" ")
                print(f"[!] Start scanning port {start}-{end}")
                for port in range(int(start), int(end)):
                    if portscanner(ip, port):
                        print(f"[+] Port {port} is Open!")
                    else:
                        print(f"[-] Port {port} is Closed!")
            elif qw == "sportscan" or qw == "SPORTSCAN":
                qw, ip, port = que.split(" ")
                print(f"[!] Start scanning port {port}")
                if portscanner(ip, port):
                    print(f"[+] Port {port} is Open!")
                else:
                    print(f"[-] Port {port} is Closed!")
            elif qw == "ping" or qw == "PING":
                qw, ip, c = que.split(" ")
                os.system(f"ping {ip} -w {c}" if os.name == "nt" else f"ping -c {c} {ip}")
            elif qw == "cls" or qw == "CLS" or qw == "clear" or qw == "CLEAR":
                os.system("cls" if os.name == "nt" else "clear")
                print(banner)
        except:
            pass

if __name__ == '__main__':
    main()
