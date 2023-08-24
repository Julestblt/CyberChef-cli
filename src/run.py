import questionary
import pyfiglet
from constants import command_config


def run(args):
    print(pyfiglet.figlet_format("CyberChef CLI", font="slant"))
    print("=====================================")

    command = hasattr(args, "command") and args.command or ""
    method = hasattr(args, "method") and args.method or ""
    if command:
        cmd = command_config[command]['func']
        cmd(value=args.value or "", method=method)
    else:
        selected_option = questionary.select(
            "Choose an option:", list(command_config.keys())).ask()
        command_config[selected_option]['func']()
