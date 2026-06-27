import urllib.request
import urllib.error
import json
from InquirerPy import prompt
from tabulate import tabulate


def ip_track():
    ip = [{"type": "input", "message": "Ingrese la ip", "name": "ip"}]
    result = prompt(ip)
    raw = result["ip"]

    url = f"https://ipwho.is/{raw}"
    try:
        with urllib.request.urlopen(url) as resp:
            data = json.loads(resp.read())

            table = [
                ["IP", data["ip"]],
                ["Tipo", data["type"]],
                ["Pais", data["country"]],
                ["Region", data["region"]],
                ["Ciudad", data["city"]],
                ["Latitud", data["latitude"]],
                ["Longitud", data["longitude"]],
                ["Codigo Postal", data["postal"]],
            ]
            print(tabulate(table, tablefmt="simple_grid"))
    except urllib.error.HTTPError as e:
        print(f"Ip no encontrada : error {e.code}")
        return None
