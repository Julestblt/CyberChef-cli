from run import run
from sys import argv
from argument_parser import create_argument_parser


def main():
    if len(argv) > 1:
        parser = create_argument_parser()
        args = parser.parse_args()

        args.method = ""

        if hasattr(args, "encode") or hasattr(args, "decode") or hasattr(args, "hash"):
            if hasattr(args, "encode") and args.encode:
                args.method = "encode"
            elif hasattr(args, "decode") and args.decode:
                args.method = "decode"
            elif hasattr(args, "hash") and args.hash:
                args.method = "hash"

        if args.command:
            run(args)
        else:
            parser.print_help()
    else:
        run(None)


if __name__ == "__main__":
    main()
