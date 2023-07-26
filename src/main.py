import questionary


def ask_color():
    color = questionary.select(
        "What is your favorite color?",
        choices=[
            "Red", "Green", "Blue", "Yellow", "Other",
        ],
    ).ask()

    print("Your favorite color is:", color)


if __name__ == "__main__":
    ask_color()
