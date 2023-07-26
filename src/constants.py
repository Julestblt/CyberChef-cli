from commands.base64 import base64_command
from commands.url import url_command
from commands.hex import hex_command

options_dict = {
    "Base64": base64_command,
    "Url": url_command,
    "Hex": hex_command,
    "Quit": exit
}

command_arg_dict = {
    "b64:e": (base64_command, "encode"),
    "b64:d": (base64_command, "decode"),
    "url:e": (url_command, "encode"),
    "url:d": (url_command, "decode"),
    "hex:e": (hex_command, "encode"),
    "hex:d": (hex_command, "decode"),
    "b64": (base64_command, None),
    "url": (url_command, None),
    "hex": (hex_command, None)
}
