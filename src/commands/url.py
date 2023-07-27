import urllib.parse
from utils.parse_args import parse_args
from utils.print_result import print_result


def url_encode(value: str) -> str:
    return urllib.parse.quote(value)


def url_decode(value: str) -> str:
    return urllib.parse.unquote(value)


command_dict = {
    "Encode": url_encode,
    "Decode": url_decode
}


def url_command(value: str = "", method: str = ""):
    print("Url Command")
    command_choice, value = parse_args(
        value=value, method=method, data_format="url")
    print_result(command_dict[command_choice](value))
