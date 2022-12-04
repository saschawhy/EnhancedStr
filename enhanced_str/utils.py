import os


def clearConsole() -> None:
    os.system("cls" if os.name == "nt" else "clear")
