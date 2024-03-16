import re
import uuid

from pixqrcode.utils.format_values import FormatValues


def return_key_map(status: bool, value: str, method: str) -> dict:
    return {
        "status": status,
        "value": value,
        "method": method
    }


def key_mobile(key: str) -> dict:
    mobile = FormatValues.mobile(key)

    if not re.match(r'^.55\d{3}', mobile) and re.match(r"^\d{11}$", mobile):
        if not re.match(r'^55\d{3}', mobile):
            mobile = f"+55{mobile}"
        else:
            mobile = f"+{mobile}"

    if not re.match(r'^.+55\d{3}', mobile):
        return return_key_map(False, mobile, "mobile")
    return return_key_map(True, mobile, "mobile")


def key_cpf(key: str) -> dict:
    if re.match(r"^(\d{3}\.\d{3}\.\d{3}-\d{2})$", key):
        return return_key_map(True, FormatValues.mobile(key), "cpf")
    elif re.match(r"^\d{10}$", key):
        return return_key_map(True, key, "cpf")
    else:
        return return_key_map(False, key, "cpf")


def key_cnpj(key: str) -> dict:
    if re.match(r"^[0-9]{2}\.?[0-9]{3}\.?[0-9]{3}/?[0-9]{4}-?-?[0-9]{2}$", key):
        return return_key_map(True, FormatValues.mobile(key), "cnpj")
    elif re.match(r"^\d{14}$", key):
        return return_key_map(True, key, "cnpj")
    else:
        return return_key_map(False, key, "cnpj")


def key_email(key: str) -> dict:
    if re.match(r"^((?!\.)[\w\-_.]*[^.])(@\w+)(\.\w+(\.\w+)?[^.\W])$", key):
        return return_key_map(True, key, "email")
    else:
        return return_key_map(False, key, "email")


def key_random(key: str) -> dict:
    try:
        return return_key_map(bool(uuid.UUID(key)), key, "uuid")
    except ValueError:
        return return_key_map(False, key, "uuid")
