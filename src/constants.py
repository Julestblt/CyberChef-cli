from commands.base64 import base64_command
from commands.url import url_command
from commands.hex import hex_command
from commands.binary import binary_command
from commands.rot13 import rot13_command

options_dict = {
    'Base64': base64_command,
    'Url': url_command,
    'Hex': hex_command,
    'Binary': binary_command,
    'Rot13': rot13_command,
    'Quit': exit
}

command_arg_dict = {
    'b64': base64_command,
    'url': url_command,
    'hex': hex_command,
    'bin': binary_command,
    'r13': rot13_command,
}

command_config = {
    'b64': {
        'help': 'base64 operations',
        'methods': ['encode', 'decode']
    },
    'hex': {
        'help': 'hex operations',
        'methods': ['encode', 'decode']
    },
    'url': {
        'help': 'url operations',
        'methods': ['encode', 'decode']
    },
    'bin': {
        'help': 'binary operations',
        'methods': ['encode', 'decode']
    },
    'r13': {
        'help': 'rot13 operations',
        'methods': ['encode', 'decode']
    },
}
