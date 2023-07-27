from commands.base64 import base64_command
from commands.url import url_command
from commands.hex import hex_command
from commands.binary import binary_command
from commands.rot13 import rot13_command
from commands.md5 import md5_command


command_config = {
    'b64': {
        'help': 'base64 operations',
        'methods': ['encode', 'decode'],
        'func': base64_command
    },
    'hex': {
        'help': 'hex operations',
        'methods': ['encode', 'decode'],
        'func': hex_command
    },
    'url': {
        'help': 'url operations',
        'methods': ['encode', 'decode'],
        'func': url_command
    },
    'bin': {
        'help': 'binary operations',
        'methods': ['encode', 'decode'],
        'func': binary_command
    },
    'r13': {
        'help': 'rot13 operations',
        'methods': ['encode', 'decode'],
        'func': rot13_command
    },
    'MD5': {
        'help': 'md5 operations',
        'methods': ['hash'],
        'func': md5_command
    },
}

options_dict = {
    'Base64': command_config['b64']['func'],
    'Url': command_config['url']['func'],
    'Hex': command_config['hex']['func'],
    'Binary':   command_config['bin']['func'],
    'Rot13': command_config['r13']['func'],
    'MD5': command_config['MD5']['func'],
    'Quit': exit
}
