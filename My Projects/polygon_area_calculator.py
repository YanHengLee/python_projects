class Rectangle:
    """
    Represents a rectangle defined by its width and height.
    Provides methods to calculate geometric properties and
    display the shape using text.
    """

    def __init__(self, width, height):
        # Initialize rectangle dimensions
        self.width = width
        self.height = height

    def set_width(self, new_width):
        """Set a new width for the rectangle."""
        self.width = new_width

    def set_height(self, new_height):
        """Set a new height for the rectangle."""
        self.height = new_height

    def get_area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def get_perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        """Return the length of the rectangle's diagonal."""
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        """
        Return a string representation of the rectangle
        using '*' characters.

        If the width or height is greater than 50, a message
        is returned instead to prevent excessive output.
        """
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        pic = ""
        stars = "*" * self.width
        for _ in range(self.height):
            pic = stars + "\n" + pic
        return pic

    def get_amount_inside(self, shape):
        """
        Return the number of times another shape can fit
        inside this rectangle based on area comparison.

        If the other shape is larger, return 0.
        """
        if self.get_area() > shape.get_area():
            return int(self.get_area() / shape.get_area())
        return 0

    def __str__(self):
        """Return a string representation of the rectangle."""
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    """
    Represents a square, which is a special type of rectangle
    where all sides are equal.
    """

    def __init__(self, side):
        # Initialize square with equal width and height
        self.width = side
        self.height = side

    def set_side(self, new_side):
        """Set a new side length for the square."""
        self.width = new_side
        self.height = new_side

    def set_width(self, new_side):
        """
        Set a new width for the square.
        Height is updated as well to maintain square properties.
        """
        self.width = new_side
        self.height = new_side

    def set_height(self, new_side):
        """
        Set a new height for the square.
        Width is updated as well to maintain square properties.
        """
        self.width = new_side
        self.height = new_side

    def __str__(self):
        """Return a string representation of the square."""
        return f"Square(side={self.width})"
