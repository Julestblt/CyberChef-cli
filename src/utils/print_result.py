from colorama import Fore, Style


def print_result(value: str) -> None:
    print("=====================================\n")
    print(f"{Style.BRIGHT}{Fore.BLUE}Result: {Style.RESET_ALL}{Fore.GREEN}{value}")
    print(Style.RESET_ALL)
