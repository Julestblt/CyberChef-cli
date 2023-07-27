from utils.parse_args import parse_args
from utils.print_result import print_result


def binary_encode(value: str) -> str:
    return " ".join(format(ord(x), 'b') for x in value)


def binary_decode(data: str) -> str:
    return "".join(chr(int(x, 2)) for x in data.split())


command_dict = {
    "Encode": binary_encode,
    "Decode": binary_decode
}


def binary_command(value: str = "", method: str = ""):
    print("Binary Command")
    command_choice, value = parse_args(
        value=value, method=method, data_format="bin")
    print_result(command_dict[command_choice](value))
