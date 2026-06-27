import urllib.request
import urllib.error
import json
from tabulate import tabulate


def ip():
    url = "https://api.ipify.org?format=json"
    try:
        with urllib.request.urlopen(url) as resp:
            data = json.loads(resp.read())
            table = [["IP", data["ip"]]]
            print(tabulate(table, tablefmt="simple_grid"))
    except urllib.error.HTTPError as e:
        print(f"[!] Error al obtener la IP: {e.code}")
