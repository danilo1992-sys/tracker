from phonenumbers import geocoder, carrier, timezone, number_type, PhoneNumberType
import phonenumbers
from InquirerPy import prompt
from tabulate import tabulate


def celular():
    cel = [
        {
            "type": "input",
            "message": "Ingrese el numero de celular (ej: +5491155551234)",
            "name": "celular",
        }
    ]
    result = prompt(cel)
    raw = result["celular"]

    try:
        number = phonenumbers.parse(raw)
    except phonenumbers.NumberParseException:
        print("[!] Numero no valido. Asegurese de incluir el codigo de pais (ej: +54).")
        return

    if not phonenumbers.is_valid_number(number):
        print("[!] El numero no es valido para el pais detectado.")
        return

    if not phonenumbers.is_possible_number(number):
        print("[!] El numero no es posible (longitud incorrecta).")
        return

    formatted = phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.E164)
    national = phonenumbers.format_number(
        number, phonenumbers.PhoneNumberFormat.NATIONAL
    )
    region = phonenumbers.region_code_for_number(number)
    operador = carrier.name_for_number(number, "es") or "Desconocido"
    ubicacion = geocoder.description_for_number(number, "es") or "Desconocida"
    zonas = timezone.time_zones_for_number(number)

    tipo_num = number_type(number)
    tipos = {
        PhoneNumberType.MOBILE: "Movil",
        PhoneNumberType.FIXED_LINE: "Linea fija",
        PhoneNumberType.FIXED_LINE_OR_MOBILE: "Movil o linea fija",
        PhoneNumberType.TOLL_FREE: "Linea gratuita (0800)",
        PhoneNumberType.PREMIUM_RATE: "Linea premium",
        PhoneNumberType.SHARED_COST: "Costo compartido",
        PhoneNumberType.VOIP: "VoIP",
        PhoneNumberType.PERSONAL_NUMBER: "Numero personal",
        PhoneNumberType.PAGER: "Pager",
        PhoneNumberType.UAN: "Numero de acceso universal",
        PhoneNumberType.VOICEMAIL: "Buzon de voz",
        PhoneNumberType.UNKNOWN: "Desconocido",
    }
    tipo_linea = tipos.get(tipo_num, "Desconocido")

    table = [
        ["Formato", formatted],
        ["Numero nacional", national],
        ["Pais", region],
        ["Tipo de linea", tipo_linea],
        ["Operador", operador],
        ["Ubicacion", ubicacion],
        ["Zona Horaria", ", ".join(zonas) if zonas else "Desconocida"],
    ]
    print(tabulate(table, tablefmt="simple_grid"))
