import questionary
import pyfiglet
from sys import argv
from constants import options_dict, command_arg_dict


def main():
    print(pyfiglet.figlet_format("CyberChef CLI", font="slant"))
    print("=====================================")
    if len(argv) > 1 and argv[1] in command_arg_dict:
        command, method = command_arg_dict[argv[1]]
        if method and len(argv) == 2:
            command(method=method)
        elif method and len(argv) > 2:
            command(value=argv[2], method=method)
        else:
            command()
    elif len(argv) == 1:
        selected_option = questionary.select(
            "Choose an option:", list(options_dict.keys())).ask()
        options_dict[selected_option]()


if __name__ == "__main__":
    main()
