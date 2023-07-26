import questionary


def parse_args(value: str, method: str) -> tuple[str, str]:
    command_choice = ""
    if (value == "" and method == ""):
        command_choice = questionary.select(
            "Choose an option:", ["Encode", "Decode"]).ask()
        value = questionary.text("Enter the value:").ask()
    elif (method is not None and value == ""):
        command_choice = method.capitalize()
        value = questionary.text("Enter the value:").ask()
    else:
        command_choice = method.capitalize()
    return (command_choice, value)
