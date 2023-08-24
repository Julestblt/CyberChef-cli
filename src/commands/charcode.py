from utils.parse_args import parse_args
from utils.print_result import print_result


def charcode_encode(value: str) -> str:
    return_value = ""
    for char in value:
        return_value += str(ord(char)) + " "
    return return_value


def charcode_decode(data: str) -> str:
    parsed_data = data.split(" ")
    try:
        return_value = ""
        for char in parsed_data:
            return_value += chr(int(char))
        return return_value
    except ValueError:
        return "Invalid Hex string"


command_dict = {
    "Encode": charcode_encode,
    "Decode": charcode_decode
}


def charcode_command(value: str = "", method: str = ""):
    print("Charcode Command")
    command_choice, value = parse_args(
        value=value, method=method, data_format="hex")
    print_result(command_dict[command_choice](value))
