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
    "b64": base64_command,
    "url": url_command,
    "hex": hex_command,
}
