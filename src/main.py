from run import run
from sys import argv
from argument_parser import create_argument_parser


def main():
    if len(argv) > 1:
        parser = create_argument_parser()
        args = parser.parse_args()

        args.method = ""
        if args.encode or args.decode:
            args.method = 'decode' if args.decode else 'encode'

        if args.command:
            run(args)
        else:
            parser.print_help()
    else:
        run(None)


if __name__ == "__main__":
    main()
