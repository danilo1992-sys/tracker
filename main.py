from InquirerPy import prompt
from components.celular import celular
from components.ip_track import ip_track
from components.ip import ip


def main():
    opciones = {
        "Numero de celular": celular,
        "Rastrear ip": ip_track,
        "Cual es mi ip": ip,
    }
    while True:
        menu = [
            {
                "type": "list",
                "message": "Selecione una opcion",
                "choices": [
                    "Numero de celular",
                    "Rastrear ip",
                    "Cual es mi ip",
                    "Salir",
                ],
                "name": "opcion",
            }
        ]
        result = prompt(menu)
        opcion = result["opcion"]

        if opcion == "Salir":
            break

        if opcion in opciones:
            opciones[opcion]()
        else:
            print(f"[!]Opcion '{opcion}' no valida")


if __name__ == "__main__":
    main()
