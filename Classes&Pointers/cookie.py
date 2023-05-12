# Small revision
# This will be important , because we will create different classes for different data types.
# We will also need to create a data structure to hold the data.


class Cookie:
    """
    Represents a cookie with a color attribute.

    Attributes:
        color (str): The color of the cookie.
    """

    def __init__(self, color: str) -> None:
        """
        Initializes a new instance of the Cookie class with the specified color.

        Args:
            color (str): The color of the cookie to create.
        """
        self.color = color

    def get_color(self) -> str:
        """
        Gets the color of the cookie.

        Returns:
            str: The color of the cookie.
        """
        return self.color

    def set_color(self, color: str) -> None:
        """
        Sets the color of the cookie to the specified color.

        Args:
            color (str): The new color of the cookie.
        """
        self.color = color


if __name__ == "__main__":
    cookie_one = Cookie("green")
    cookie_two = Cookie("blue")

    print(f"Cookie one is {cookie_one.get_color()}")
    print(f"Cookie two is {cookie_two.get_color()}\n")

    cookie_one.set_color("yellow")

    if cookie_one.get_color() == "yellow":
        print("Cookie one is now yellow!")
        print("Cookie two is still blue!")
