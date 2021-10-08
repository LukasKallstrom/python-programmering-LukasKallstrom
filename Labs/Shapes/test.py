import math

class Shapes():
    def __init__(self, x:float, y:float) -> None:
        self.x = x
        self.y = y

    @property
    def x(self) -> None:
        return self._x

    @x.setter
    def x(self, x) -> float:
        if not isinstance(x, (float,int)):
            raise TypeError(f"{x} must be float or int")
        if x < 0:
            raise ValueError("x must be larger than 0")
        self._x = x
    
    @property
    def y(self) -> None:
        return self._y

    @y.setter
    def y(self, y) -> float:
        if not isinstance(y, (float,int)):
            raise TypeError(f"{y} must be float or int")
        if y < 0:
            raise ValueError("y must be larger than 0")
        self._y = y
    
    def __repr__(self) -> str:
        return f"Shape(x:{self.x}, y:{self.y})"
    

class Circle(Shapes):
    def __init__(self, x:float, y:float, radius:float) -> None:
        super().__init__(x, y)
        self.radius = radius
        self.area = self.set_area()
        self.circumf = self.set_circumf()
    
    @property
    def radius(self) -> None:
        print("Radius getter running")
        return self._radius

    @radius.setter
    def radius(self, radius) -> float:
        if not isinstance(radius, (float,int)):
            raise TypeError(f"{radius} must be float or int")
        if radius < 0:
            raise ValueError("radius must be larger than 0")
        self._radius = radius

    def set_area(self) -> float:
        return math.pi * self.radius**2

    def set_circumf(self) -> float:
        return 2 * math.pi * self.radius


class Rectangle(Shapes):
    def __init__(self, y, x, side1=1, side2=1) -> None:
        super().__init__(x, y)
        self.side1 = side1
        self.side2 = side2
        self.area = self.set_area()
        self.circumf = self.set_circumf()

    @property
    def side1(self) -> None:
        return self._side1

    @side1.setter
    def side1(self, side1) -> float:
        if not isinstance(side1, (float,int)):
            raise TypeError(f"{side1} must be float or int")
        if side1 <= 0:
            raise ValueError("Side 1 must be larger than 0")
        self._side1 = side1
    
    @property
    def side2(self) -> None:
        return self._side2

    @side2.setter
    def side2(self, side2) -> float:
        if not isinstance(side2, (float,int)):
            raise TypeError(f"{side2} must be float or int")
        if side2 <= 0:
            raise ValueError("Side 2 must be larger than 0")
        self._side2 = side2

    def set_area(self) -> float:
        return self.side1 * self.side2

    def set_circumf(self) -> float:
        return (self.side1*2) + (self.side2*2)

    

