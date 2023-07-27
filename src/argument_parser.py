import argparse
from constants import command_config


def add_operation_subparser(subparsers, operation_name, operation_config):
    operation_parser = subparsers.add_parser(
        operation_name, help=operation_config['help'])

    for method in operation_config['methods']:
        if method == 'hash':
            method_shortcut = 'H'
        else:
            method_shortcut = method[0]
        operation_parser.add_argument(
            f'--{method}', f'-{method_shortcut}', action='store_true', help=f'{method} {operation_name}'
        )

    operation_parser.add_argument(
        'value', nargs='?', help=f'value for {operation_name} operation'
    )

    return operation_parser


def create_argument_parser():
    parser = argparse.ArgumentParser(description='CyberChef CLI')
    subparsers = parser.add_subparsers(dest='command')

    for operation, config in command_config.items():
        add_operation_subparser(subparsers, operation, config)

    return parser
