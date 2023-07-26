import questionary
import pyfiglet
from commands.base64 import base64_command

options_dict = {
    "Base64": base64_command,
    "Quit": exit
}


def main():
    print(pyfiglet.figlet_format("CyberChef CLI", font="slant"))
    print("=====================================")
    selected_option = questionary.select(
        "Choose an option:", options_dict.keys()).ask()
    options_dict[selected_option]()


if __name__ == "__main__":
    main()
