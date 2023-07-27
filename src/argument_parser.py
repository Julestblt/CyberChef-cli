import argparse


def add_operation_subparser(subparsers, operation_name, help_text):
    operation_parser = subparsers.add_parser(operation_name, help=help_text)
    operation_parser.add_argument(
        '-d', '--decode', action='store_true', help=f'decode {operation_name}')
    operation_parser.add_argument(
        '-e', '--encode', action='store_true', help=f'encode {operation_name}')
    operation_parser.add_argument(
        'value', nargs='?', help=f'value for {operation_name} operation')
    return operation_parser


def create_argument_parser():
    parser = argparse.ArgumentParser(description='CyberChef CLI')
    subparsers = parser.add_subparsers(dest='command')

    add_operation_subparser(subparsers, 'b64', 'base64 operations')
    add_operation_subparser(subparsers, 'hex', 'hex operations')
    add_operation_subparser(subparsers, 'url', 'url operations')
    add_operation_subparser(subparsers, 'bin', 'binary operations')

    return parser
