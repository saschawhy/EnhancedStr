from typing import TypeVar, Union, Literal, Optional
from time import sleep
import string


Number = Literal[0, 16777215]
PreferablyHex = TypeVar("PreferablyHex", Number, Literal[0x00, 0x00FFFFFF])
Finish = TypeVar("Finish", None, None)


class es(str):
    def out(self) -> Finish:
        """This is the final method to be called in a chain of methods.

        This will print out the final string.
        """
        print(self)

    def bold(self) -> "es":
        """This method will make the string bold.

        Returns
        -------
        :class:`pp`
            The string with the bold formatting.
        """
        return es(f"\x1b[1m{self}\x1b[22m")

    def dimmed(self) -> "es":
        """This method will make the string dimmed.

        Returns
        -------
        :class:`pp`
            The string with the dimmed formatting.
        """
        return es(f"\x1b[2m{self}\x1b[22m")

    def italic(self) -> "es":
        """This method will make the string italic.

        Returns
        -------
        :class:`pp`
            The string with the italic formatting.
        """
        return es(f"\x1b[3m{self}\x1b[23m")

    def underline(self) -> "es":
        """This method will make the string underlined.

        Returns
        -------
        :class:`pp`
            The string with the underlined formatting.
        """
        return es(f"\x1b[4m{self}\x1b[24m")

    def strikethrough(self) -> "es":
        """This method will make the string strikethrough.

        Returns
        -------
        :class:`pp`
            The string with the strikethrough formatting.
        """
        return es(f"\x1b[9m{self}\x1b[29m")

    def gradient(
        self, start: Union[PreferablyHex, Number], end: Union[PreferablyHex, Number], /
    ) -> "es":
        """This method will make the string a gradient.

        Parameters
        ----------
        :class:`PreferablyHex` or :class:`Number` start
            The start color of the gradient.
        :class:`PreferablyHex` or :class:`Number` end
            The end color of the gradient.

        Returns
        -------
        :class:`pp`
            The string with the gradient formatting.
        """
        reverse = False
        if start > end:
            start, end = end, start
            reverse = True
        # get the difference between the two colors
        r1, g1, b1 = (start >> 16) & 0xFF, (start >> 8) & 0xFF, start & 0xFF
        r2, g2, b2 = (end >> 16) & 0xFF, (end >> 8) & 0xFF, end & 0xFF
        r_partial, g_partial, b_partial = r2 - r1, g2 - g1, b2 - b1
        # get the length of the string
        length = len(self)
        # get the difference between each color
        r, g, b = r_partial / length, g_partial / length, b_partial / length
        # create the gradient
        gradient = ""
        for i in range(length):
            if not reverse:
                gradient += es(
                    f"\x1b[38;2;{int(r1 + r * i)};"
                    f"{int(g1 + g * i)};"
                    f"{int(b1 + b * i)}m{self[i]}\x1b[39m"
                )
            else:
                gradient += es(
                    f"\x1b[38;2;{int(r2 - r * i)};"
                    f"{int(g2 - g * i)};"
                    f"{int(b2 - b * i)}m{self[i]}\x1b[39m"
                )
        return es(gradient)

    def mixedGradient(
        self,
        start: Union[PreferablyHex, Number],
        end: Union[PreferablyHex, Number],
        stepSkipThreshold: int,
        /,
    ) -> "es":
        """This method will make the string a repeating gradient.

        Parameters
        ----------
        :class:`PreferablyHex` or :class:`Number` start
            The start color of the gradient.
        :class:`PreferablyHex` or :class:`Number` end
            The end color of the gradient.
        :class:`int` stepSkipThreshold
            The amount of steps to skip before the gradient repeats.

        Returns
        -------
        :class:`pp`
            The string with the repeating gradient formatting.
        """
        # same as gradient but with a step threshold, and then it reverses.
        # if the full string is not reached and max color is reached,
        # it will just repeat the gradient
        reverse = False
        if start > end:
            reverse = True
        # get the difference between the two colors
        r1, g1, b1 = (start >> 16) & 0xFF, (start >> 8) & 0xFF, start & 0xFF
        r2, g2, b2 = (end >> 16) & 0xFF, (end >> 8) & 0xFF, end & 0xFF
        r_partial, g_partial, b_partial = r2 - r1, g2 - g1, b2 - b1
        # get the length of the string
        length = len(self)
        # get the difference between each color
        r, g, b = r_partial / length, g_partial / length, b_partial / length
        # create the gradient
        gradient = ""
        for i in range(length):
            if not reverse:
                gradient += es(
                    f"\x1b[38;2;{int(r1 + r * i)};"
                    f"{int(g1 + g * i)};"
                    f"{int(b1 + b * i)}m{self[i]}\x1b[39m"
                )
            else:
                gradient += es(
                    f"\x1b[38;2;{int(r2 - r * i)};"
                    f"{int(g2 - g * i)};"
                    f"{int(b2 - b * i)}m{self[i]}\x1b[39m"
                )
            if i % stepSkipThreshold == 0:
                reverse = not reverse
        return es(gradient)

    def hexColor(self, dec: Union[PreferablyHex, Number], /) -> "es":
        """This method will make the string a specific color.

        Parameters
        ----------
        :class:`PreferablyHex` or :class:`Number` dec
            The color to make the string.

        Returns
        -------
        :class:`pp`
            The string with the color formatting.
        """
        r, g, b = (dec >> 16) & 0xFF, (dec >> 8) & 0xFF, dec & 0xFF
        return es(f"\x1b[38;2;{r};{g};{b}m{self}\x1b[39m")

    def outSBS(self, delay: float, abcOnly: Optional[bool] = True, /) -> Finish:
        """This method will print the string out step by step.

        Parameters
        ----------
        :class:`float` delay
            The delay between each character.
        :class:`bool` skipWhitespace
            Whether to skip whitespace or not.
        """
        for i in self:
            print(i, end="", flush=True)
            if abcOnly and i not in string.ascii_letters:
                continue
            sleep(delay)
        print()

    def outBlink(
        self, delay: float, amount: int, stopHidden: Optional[bool] = False, /
    ) -> Finish:
        """This method will print the string out with a blinking effect.

        Parameters
        ----------
        :class:`float` delay
            The delay between each character.
        :class:`int` amount
            The amount of times to blink.
        :class:`bool` stopHidden
            Whether to stop the string hidden or not.
        """
        for _ in range(amount):
            print(self, end="\r", flush=True)
            sleep(delay)
            print(" " * len(self), end="\r", flush=True)
            sleep(delay)
        if not stopHidden:
            print(self)
