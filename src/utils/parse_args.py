import questionary


def parse_args(value: str, method: str, data_format: str) -> tuple[str, str]:
    from constants import command_config

    command_choice = ""

    if (value == "" and method == ""):
        command_choice = questionary.select(
            "Choose an option:", command_config[data_format]["methods"]).ask()
        value = questionary.text("Enter the value:").ask()
    elif (method is not None and value == ""):
        command_choice = method.capitalize()
        value = questionary.text("Enter the value:").ask()
    else:
        command_choice = method.capitalize()
    return (command_choice.capitalize(), value)
