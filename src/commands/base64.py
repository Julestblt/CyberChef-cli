import base64
import binascii
import questionary


def base64_encode(value: str) -> str:
    return base64.b64encode(value.encode('utf-8')).decode('utf-8')


def base64_decode(data: str) -> str:
    try:
        return base64.b64decode(data.encode('utf-8')).decode('utf-8')
    except binascii.Error:
        return "Invalid Base64 string"


command_dict = {
    "Encode": base64_encode,
    "Decode": base64_decode
}


def base64_command():
    print("Base64 Command")
    command_choice = questionary.select(
        "Choose an option:", ["Encode", "Decode"]).ask()
    value = questionary.text("Enter the value:").ask()
    print(command_dict[command_choice](value))
