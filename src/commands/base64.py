import base64
import binascii
from utils.parse_args import parse_args


def base64_encode(value: str) -> str:
    return base64.b64encode(value.encode('utf-8')).decode('utf-8')


def base64_decode(data: str) -> str:
    try:
        return base64.b64decode(data.encode('utf-8')).decode('utf-8')
    except binascii.Error:
        return "Invalid Base64 string"


command_dict = {
    "Encode": base64_encode,
    "Decode": base64_decode
}


def base64_command(value: str = "", method: str = ""):
    print("Base64 Command")
    command_choice, value = parse_args(value=value, method=method)
    print(command_dict[command_choice](value))
