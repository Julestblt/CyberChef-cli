from utils.parse_args import parse_args
from utils.print_result import print_result


def hex_encode(value: str) -> str:
    return value.encode('utf-8').hex()


def hex_decode(data: str) -> str:
    try:
        return bytes.fromhex(data).decode('utf-8')
    except ValueError:
        return "Invalid Hex string"


command_dict = {
    "Encode": hex_encode,
    "Decode": hex_decode
}


def hex_command(value: str = "", method: str = ""):
    print("Hex Command")
    command_choice, value = parse_args(
        value=value, method=method, data_format="hex")
    print_result(command_dict[command_choice](value))
