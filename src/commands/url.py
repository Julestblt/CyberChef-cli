import urllib.parse
from utils.parse_args import parse_args


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
    print("=====================================")
    command_choice, value = parse_args(
        value=value, method=method, data_format="url")
    print(command_dict[command_choice](value))
