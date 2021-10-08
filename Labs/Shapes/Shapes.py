import math


class Shapes():
    """Initiates our Shapes class"""
    def __init__(self, x: float, y: float, z=0) -> None:
        self.x = x
        self.y = y
        self.z = z

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

    @property
    def z(self) -> None:
        """Makes z a property"""
        return self._z

    @z.setter
    def z(self, z) -> float:
        """Creates a z setter with basic error-handling"""
        if not isinstance(z, (float, int)):
            raise TypeError(f"{z} must be float or int")
        self._z = z

    def translate(self, value_x: float, value_y: float, value_z=0) -> None:
        """Translate the shapes x and y by the given x and y"""
        if not isinstance(value_x, (float, int)) or \
           not isinstance(value_y, (float, int)):
            raise ValueError(f"{value_x} and {value_y} must be float or int")
        self.x += value_x
        self.y += value_y
        self.z += value_z

    def __repr__(self) -> str:
        return f"Shape(x:{self.x}, y:{self.y})"


class Circle(Shapes):
    def __init__(self, x: float, y: float, z: float, radius: float) -> None:
        """Initiates our circle class, inheriting from our Shapes class"""
        super().__init__(x, y, z)
        self.radius = radius
        self.face_area = self.set_face_area()
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

    def set_face_area(self) -> float:
        """Returns the face_area of the circle"""
        return math.pi * self.radius**2

    def set_circumf(self) -> float:
        """Returns the circumferance of the circle"""
        return 2 * math.pi * self.radius

    def __repr__(self) -> str:
        return f"Circle(x={self.x}, y={self.y}, radius={self.radius})"

    def validate_circle(self, other: "Circle") -> bool:
        """Validates that the other object is of class 'Circle'"""
        if not isinstance(other, Circle):
            return False
        return True

    def __eq__(self, other: "Circle" or "Sphere") -> bool:
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
    def __init__(self, x, y, side1, side2) -> None:
        """Initiates our Rectangle class, inheriting from our Shapes class"""
        super().__init__(x, y)
        self.side1 = side1
        self.side2 = side2
        self.face_area = self.set_face_area()
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

    def set_face_area(self) -> float:
        """Returns the face_area of the rectangle"""
        return self.side1 * self.side2

    def set_circumf(self) -> float:
        """Returns the circumferance of the rectangle"""
        return (self.side1*2) + (self.side2*2)

    def validate_rect(self, other) -> bool:
        """Validates that both is of type 'Rectangle'"""
        if not isinstance(other, Rectangle):
            raise TypeError("Both must be of type Rectangle")
        return True

    def __eq__(self, other: "Rectangle" or "Cube") -> bool:
        """Checks if the rectangle has the same sides as another rectangle
           (works for child class 'Cube' aswell)"""
        if not self.validate_rect(other):
            return False
        if self.side1 != other.side1 or self.side2 != other.side2:
            return False
        return True

    def is_inside(self, x: float, y: float) -> bool:
        """Calculate if a point is inside the rectangle
           code source (has been re-formated):
           https://www.tutorialspoint.com/check-if-a-point-lies-on-or-inside-a-rectangle-in-python
           Checks if the given point is to the right of our rectangles x and y,
           and to the left of our side1 and side2.
           If so, returns True. Else, false
           """
        if not isinstance(x, (float, int)) or not isinstance(y, (float, int)):
            raise TypeError(f"x: {x} and y: {y} must be of type float or int")
        if x > self.x and x < self.side1 and y > self.y and y < self.side2:
            return True
        return False

    def __repr__(self) -> str:
        return (f"Rectangle(x={self.x}, y={self.y}, " +
                f"side1={self.side1}, side2={self.side2})")


class Cube(Rectangle):
    def __init__(self, x, y, z, side1) -> None:
        """Cube initiation, inheriting from the Rectangle class"""
        super().__init__(x, y, side1, side2=side1)
        self.surface_area = self.set_surface_area()
        self.volume = self.set_volume()
        self.z = z

    @property
    def z(self) -> None:
        """Makes z a property"""
        return self._z

    @z.setter
    def z(self, z) -> float:
        """Creates a z setter with error-handling"""
        if not isinstance(z, (float, int)):
            raise TypeError(f"{z} must be float or int")
        self._z = z

    def set_surface_area(self) -> float:
        """Returns the surface area of the cube"""
        return 6 * (self.side1**2)

    def set_volume(self) -> float:
        """Returns the volume of the cube"""
        return self.side1 ** 3

    def __repr__(self) -> str:
        return (f"Cube(x={self.x}, y={self.y}, z={self.z} " +
                f"side={self.side1})")

    def is_inside_cube(self, x: float, y: float, z: float) -> bool:
        if self.is_inside(x, y):
            if isinstance(z, (float, int)):
                if z > self.z and z < self.side1:
                    return True
                return False
            raise TypeError(f"z: {z} must be of type int or float")
        return False

    def translate(self,
                  value_x: float,
                  value_y: float,
                  value_z: float) -> None:
        Shapes.translate(self, value_x, value_y)
        if not isinstance(value_z, (float, int)):
            raise TypeError(f"value_z {value_z} must be of type float or int")
        self.z += value_z


class Sphere(Circle):
    def __init__(self, x: float, y: float, z: float, radius: float) -> None:
        """Initiate Sphere class"""
        super().__init__(x, y, z, radius)
        self.volume = self.set_volume()
        self.surface_area = self.set_surface_area()

    def set_volume(self) -> float:
        """Returns the volume of our 3D sphere"""
        return (4/3) * math.pi * (self.radius ** 3)

    def set_surface_area(self) -> float:
        """returns the surface area of our 3D sphere"""
        return 4 * math.pi * self.radius**2

    def is_inside(self, x: float, y: float, z: float) -> bool:
        """Calculate if a point is inside of our Sphere
            using the pythagoran theorem
            (on the Sphere counts as inside the Sphere)"""
        if (not isinstance(x, (float, int)) or
           not isinstance(y, (float, int)) or
           not isinstance(z, (float, int))):
            raise TypeError("x and y must be of type float or int")
        if (((x - self.x)**2 + (y - self.y) ** 2 + (z - self.z)**2)
                <= self.radius**2):
            return True
        return False

    def __repr__(self) -> str:
        return (f"Sphere(x={self.x}, y={self.y}, " +
                f"z={self.z}, radius={self.radius})")
