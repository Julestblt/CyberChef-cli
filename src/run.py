import questionary
import pyfiglet
from constants import options_dict, command_arg_dict


def run(args):
    print(pyfiglet.figlet_format("CyberChef CLI", font="slant"))
    print("=====================================")

    command = hasattr(args, "command") and args.command or ""
    method = hasattr(args, "method") and args.method or ""

    if command:
        cmd = command_arg_dict[command]
        cmd(value=args.value or "", method=method)
    else:
        selected_option = questionary.select(
            "Choose an option:", list(options_dict.keys())).ask()
        options_dict[selected_option]()
