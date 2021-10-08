import math


class Shapes():
    """Initiates our Shapes class"""
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    @property
    def x(self) -> None:
        """Makes x a property"""
        return self._x

    @x.setter
    def x(self, x) -> float:
        """Creates a x setter with basic error-handling"""
        if not isinstance(x, (float, int)):
            raise TypeError(f"{x} must be float or int")
        self._x = x

    @property
    def y(self) -> None:
        """Makes y a property"""
        return self._y

    @y.setter
    def y(self, y) -> float:
        """Creates a y setter with basic error-handling"""
        if not isinstance(y, (float, int)):
            raise TypeError(f"{y} must be float or int")
        self._y = y

    def translate(self, value_x: float, value_y: float) -> None:
        """Translate the shapes x and y by the given x and y"""
        if not isinstance(value_x, (float, int)) or \
           not isinstance(value_y, (float, int)):
            raise ValueError(f"{value_x} and {value_y} must be float or int")
        self.x += value_x
        self.y += value_y

    def __repr__(self) -> str:
        return f"Shape(x:{self.x}, y:{self.y})"


class Circle(Shapes):
    def __init__(self, x: float, y: float, radius: float) -> None:
        """Initiates our circle class, inheriting from our Shapes class"""
        super().__init__(x, y)
        self.radius = radius
        self.area = self.set_area()
        self.circumf = self.set_circumf()

    @property
    def radius(self) -> None:
        """Makes radius a property"""
        return self._radius

    @radius.setter
    def radius(self, radius) -> float:
        """Create a radius setter with error-handling"""
        if not isinstance(radius, (float, int)):
            raise TypeError(f"{radius} must be float or int")
        if radius < 0:
            raise ValueError("radius must be larger than 0")
        self._radius = radius

    def set_area(self) -> float:
        """Returns the area of the circle"""
        return math.pi * self.radius**2

    def set_circumf(self) -> float:
        """Returns the circumferance of the circle"""
        return 2 * math.pi * self.radius

    def __repr__(self) -> str:
        return f"Circle(x={self.x}, y={self.y}, radius={self.radius})"

    def validate_circle(self, other: "Circle") -> bool:
        """Validates that the other object is of class 'Circle'"""
        if not isinstance(other, Circle):
            raise TypeError("Both must be of class Circle")
        return True

    def __eq__(self, other: "Circle") -> bool:
        """Check if the circle is equal to another circle"""
        if not self.validate_circle(other):
            return False
        if self.radius != other.radius:
            return False
        return True

    def is_inside(self, x: float, y: float) -> bool:
        """Calculate if a point is inside of our circle
            using the pythagoran theorem
            (on the circle counts as inside the circle)"""
        if not isinstance(x, (int, float)) or not isinstance(x, (float, int)):
            raise TypeError("x and y must be of type float or int")
        if (((x - self.x)**2 + (y - self.y) ** 2) <= self.radius**2):
            return True
        return False


class Rectangle(Shapes):
    def __init__(self, y, x, side1=1, side2=1) -> None:
        """Initiates our Rectangle class, inheriting from our Shapes class"""
        super().__init__(x, y)
        self.side1 = side1
        self.side2 = side2
        self.area = self.set_area()
        self.circumf = self.set_circumf()

    @property
    def side1(self) -> None:
        """Makes side1 a property"""
        return self._side1

    @side1.setter
    def side1(self, side1) -> float:
        """Creates a side1 setter with error-handling"""
        if not isinstance(side1, (float, int)):
            raise TypeError(f"{side1} must be float or int")
        if side1 <= 0:
            raise ValueError("Side 1 must be larger than 0")
        self._side1 = side1

    @property
    def side2(self) -> None:
        """Makes side2 a property"""
        return self._side2

    @side2.setter
    def side2(self, side2) -> float:
        """Creates a side2 setter with error-handling"""
        if not isinstance(side2, (float, int)):
            raise TypeError(f"{side2} must be float or int")
        if side2 <= 0:
            raise ValueError("Side 2 must be larger than 0")
        self._side2 = side2

    def set_area(self) -> float:
        """Returns the area of the rectangle"""
        return self.side1 * self.side2

    def set_circumf(self) -> float:
        """Returns the circumferance of the rectangle"""
        return (self.side1*2) + (self.side2*2)

    def validate_rect(self, other) -> bool:
        """Validates that both is of type 'Rectangle'"""
        if not isinstance(other, Rectangle):
            raise TypeError("Both must be of type Rectangle")
        return True

    def __eq__(self, other: "Circle") -> bool:
        """Checks if the rectangle has the same sides as another rectangle"""
        if not self.validate_rect(other):
            return False
        if self.side1 != other.side1 or self.side2 != other.side2:
            return False
        return True

    def is_inside(self, x: float, y: float) -> bool:
        """Calculate if a point is inside the rectangle
           inspiration:
           https://www.tutorialspoint.com/check-if-a-point-lies-on-or-inside-a-rectangle-in-python
           Checks if the given point is to the right of our rectangles x and y,
           and to the left of our side1 and side2.
           If so, returns True. Else, false
           """
        if not isinstance(x, (float, int)) or not isinstance(y, (float, int)):
            raise TypeError(f"x: {x} and y: {y} must be of type float or int")
        if (x > self.x and x < self.side1 and y > self.y and y < self.side2):
            return True
        return False

    def __repr__(self) -> str:
        return (f"Rectangle(x={self.x}, y={self.y}, " +
                f"side1={self.side1}, side2={self.side2})")
