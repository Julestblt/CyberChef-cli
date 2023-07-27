from utils.parse_args import parse_args
from hashlib import md5
from utils.print_result import print_result


def md5_hash(value: str) -> str:
    return md5(value.encode()).hexdigest()


command_dict = {
    "Hash": md5_hash,
}


def md5_command(value: str = "", method: str = ""):
    print("MD5 Command")
    command_choice, value = parse_args(
        value=value, method=method, data_format="MD5")
    print_result(command_dict[command_choice](value))
