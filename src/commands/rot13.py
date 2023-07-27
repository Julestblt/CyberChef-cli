import codecs
from utils.parse_args import parse_args


def rot13_encode(value: str) -> str:
    return codecs.encode(value, "rot_13")


def rot13_decode(data: str) -> str:
    return codecs.decode(data, "rot_13")


command_dict = {
    "Encode": rot13_encode,
    "Decode": rot13_decode,
}


def rot13_command(value: str = "", method: str = ""):
    print("Rot13 Command")
    print("=====================================")
    command_choice, value = parse_args(
        value=value, method=method, data_format="r13")
    print(command_dict[command_choice](value))
