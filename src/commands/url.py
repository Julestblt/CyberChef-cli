import questionary
import urllib.parse


def url_encode(value: str) -> str:
    return urllib.parse.quote(value)


def url_decode(value: str) -> str:
    return urllib.parse.unquote(value)


command_dict = {
    "Encode": url_encode,
    "Decode": url_decode
}


def url_command():
    print("Url Command")
    command_choice = questionary.select(
        "Choose an option:", ["Encode", "Decode"]).ask()
    value = questionary.text("Enter the value:").ask()
    print(command_dict[command_choice](value))
