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
            que_args = que.split(" ")
            if que_args[0] == "geoip" or que_args[0] == "GEOIP":
                if len(que_args[1]) < 1:
                    print("Error, usage: geoip <ip>")
                else:
                    geoip(que_args[1])
            elif que_args[0] == "sportscan" or que_args[0] == "SPORTSCAN":
                if len(que_args[1]) < 1:
                    print("Error, usage: sportscan <url/ip> <port>")
                else:
                    if portscanner(que_args[1], que_args[2]):
                        print(f"[+] Port {que_args[2]} is Open!")
                    else:
                        print(f"[+] Port {que_args[2]} is Closed!")
            elif que_args[0] == "ping" or que_args[0] == "PING":
                if len(que_args[1]) < 1:
                    print("Error, usage: ping <ip> <timeout>")
                elif len(que_args[2]) < 1:
                    print("Error, usage: ping <ip> <timeout>")
                else:
                    os.system(f"ping {que_args[1]} -w {que_args[2]}" if os.name == "nt" else f"ping {que_args[1]} -c {que_args[2]}")
            elif que_args[0] == "cportscan" or que_args[0] == "CPORTSCAN":
                if len(que_args[1]) < 1:
                    print("Error, usage: cportscan <ip/url> <start port> <endport>")
                else:
                    start = que_args[2]
                    end = que_args[3]
                    for port in range(int(start), int(end)):
                        if portscanner(que_args[1], end):
                            print(f"Port {port} is Open!")
                        else:
                            print(f"Port {port} is Closed!")
            else:
                print("Invalid command.")
        except:
            pass

if __name__ == '__main__':
    main()
