# EnhancedStr
A Python library for prettier, fully customizable console outputs.

</br>
</br>

## Code Example
```python
from enhanced_str import es, clearConsole


def main() -> None:
    clearConsole()

    es("You have a new message!").mixedGradient(0xFF00FF, 0xFFFFFF, 2).underline().out()

    print("\n")

    print(es("Cool forward color transition!").gradient(0x000000, 0xFFFFFF))
    print(es("Cool reverse color transition!").gradient(0xFFFFFF, 0x000000))

    print("\n")

    es("Error!").hexColor(0xFF0000).bold().out()
    es("Warning!").hexColor(0xFFFF00).bold().out()
    es("Success!").hexColor(0x00FF00).bold().out()

    print("\n")

    es("Alert: Something might be going wrong.").hexColor(0xFF7F7F).bold().outBlink(
        0.2, 5
    )

    print("\n")

    es("Hello World! This is a step by step character demonstration.").gradient(
        0x3D1E6D, 0xFFABFF
    ).bold().outSBS(0.02)

    while 1:
        ...


if __name__ == "__main__":
    main()
```
