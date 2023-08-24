from base64 import b32encode, b32decode
import binascii
from utils.parse_args import parse_args
from utils.print_result import print_result


def base32_encode(value: str) -> str:
    return b32encode(value.encode('utf-8')).decode('utf-8')


def base32_decode(data: str) -> str:
    try:
        return b32decode(data.encode('utf-8')).decode('utf-8')
    except binascii.Error:
        return "Invalid Base32 string"
    except UnicodeDecodeError:
        return "Invalid Base32 string"


command_dict = {
    "Encode": base32_encode,
    "Decode": base32_decode
}


def base32_command(value: str = "", method: str = ""):
    print("Base32 Command")
    command_choice, value = parse_args(
        value=value, method=method, data_format="b32")
    print_result(command_dict[command_choice](value))
