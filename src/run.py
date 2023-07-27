import questionary
import pyfiglet
from constants import options_dict, command_config


def run(args):
    print(pyfiglet.figlet_format("CyberChef CLI", font="slant"))
    print("=====================================")

    command = hasattr(args, "command") and args.command or ""
    method = hasattr(args, "method") and args.method or ""
    print(command, method)
    print("=====================================")
    if command:
        cmd = command_config[command]['func']
        cmd(value=args.value or "", method=method)
    else:
        selected_option = questionary.select(
            "Choose an option:", list(options_dict.keys())).ask()
        options_dict[selected_option]()
