import argparse
from run import run
from sys import argv


def main():
    if len(argv) > 1:
        parser = argparse.ArgumentParser(description='CyberChef CLI')
        subparsers = parser.add_subparsers(dest='command')

        b64_parser = subparsers.add_parser('b64', help='base64 operations')
        b64_parser.add_argument(
            '-d', '--decode', action='store_true', help='decode base64')
        b64_parser.add_argument(
            '-e', '--encode', action='store_true', help='encode base64')
        b64_parser.add_argument('value', nargs='?', help='value for operation')

        hex_parser = subparsers.add_parser('hex', help='hex operations')
        hex_parser.add_argument(
            '-d', '--decode', action='store_true', help='decode hex')
        hex_parser.add_argument(
            '-e', '--encode', action='store_true', help='encode hex')
        hex_parser.add_argument('value', nargs='?', help='value for operation')

        url_parser = subparsers.add_parser('url', help='url operations')
        url_parser.add_argument(
            '-d', '--decode', action='store_true', help='decode url')
        url_parser.add_argument(
            '-e', '--encode', action='store_true', help='encode url')
        url_parser.add_argument('value', nargs='?', help='value for operation')

        args = parser.parse_args()

        args.method = ""

        if args.encode or args.decode:
            args.method = 'decode' if args.decode else 'encode'
        else:
            args.method = ""

        if args.command:
            run(args)
        else:
            parser.print_help()
    else:
        run(None)


if __name__ == "__main__":
    main()
