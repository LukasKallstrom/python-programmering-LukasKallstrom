import Shapes as s
import unittest
import math


class TestShapes(unittest.TestCase):
    def setUp(self) -> None:
        self.x, self.y, self.z = 1, 2, 3
        self.side1, self.side2 = 5, 10
        self.radius = 10

    def create_circle(self) -> "s.Circle":
        return s.Circle(self.x, self.y, self.z, self.radius)

    def create_rectangle(self) -> "s.Rectangle":
        return s.Rectangle(self.x, self.y, self.side1, self.side2)

    def create_cube(self) -> "s.Cube":
        return s.Cube(self.x, self.y, self.z, self.side1)

    def create_sphere(self) -> "s.Sphere":
        return s.Sphere(self.x, self.y, self.z, self.radius)

    # Test creating different shapes

    def test_create_circle(self) -> None:
        c = self.create_circle()
        self.assertEqual((c.x, c.y, c.radius), (self.x, self.y, self.radius))

    def test_create_rectangle(self) -> None:
        r = self.create_rectangle()
        self.assertEqual((r.x, r.y, r.side1, r.side2),
                         (self.x, self.y, self.side1, self.side2))

    def test_create_cube(self) -> None:
        cu = self.create_cube()
        self.assertEqual, ((cu.x, cu.y, cu.z, cu.side1),
                           (self.x, self.y, self.z, self.side1))

    def test_create_sphere(self) -> None:
        s = self.create_sphere()
        self.assertEqual((s.x, s.y, s.z, s.radius),
                         (self.x, self.y, self.z, self.radius))

    # Test __eq__

    def test_2_circles_eq(self) -> None:
        c1 = self.create_circle()
        c2 = s.Circle(1, 2, 3, 10)
        self.assertEqual(c1, c2)

    def test_2_rectangles_eq(self) -> None:
        r1 = self.create_rectangle()
        r2 = s.Rectangle(1, 2, 5, 10)
        self.assertEqual(r1, r2)

    def test_2_cubes_eq(self) -> None:
        c1 = self.create_cube()
        c2 = s.Cube(1, 2, 3, 5)
        self.assertEqual(c1, c2)

    def test_2_spheres_eq(self) -> None:
        c1 = self.create_sphere()
        c2 = s.Sphere(1, 2, 3, 5)
        self.assertEqual(c1, c2)

    # Test not __eq__

    def test_2_circles_not_eq(self) -> None:
        c1 = self.create_circle()
        c2 = s.Circle(1, 2, 3, 500)
        self.assertNotEqual(c1, c2)

    def test_2_rectangles_not_eq(self) -> None:
        r1 = self.create_rectangle()
        r2 = s.Rectangle(1, 2, 5, 500)
        self.assertNotEqual(r1, r2)

    def test_2_cubes_not_eq(self) -> None:
        c1 = self.create_cube()
        c2 = s.Cube(1, 2, 3, 500)
        self.assertNotEqual(c1, c2)

    def test_2_spheres_not_eq(self) -> None:
        c1 = self.create_sphere()
        c2 = s.Sphere(1, 2, 3, 500)
        self.assertNotEqual(c1, c2)

    # Test create negative Shapes

    def test_create_neg_circle(self) -> None:
        with self.assertRaises(ValueError):
            s.Circle(0, 0, 0, -10)

    def test_create_neg_rectangle(self) -> None:
        with self.assertRaises(ValueError):
            s.Rectangle(0, 0, -10, 10)

    def test_create_neg_cube(self) -> None:
        with self.assertRaises(ValueError):
            s.Cube(0, 0, 0, -10)

    def test_create_neg_sphere(self) -> None:
        with self.assertRaises(ValueError):
            s.Sphere(0, 0, 0, -10)

    # test area function

    def test_area_circle(self) -> None:
        c1 = self.create_circle()
        area = math.pi*10**2
        self.assertEqual(c1.face_area, area)

    def test_area_rectangle(self) -> None:
        r1 = self.create_rectangle()
        area = 5 * 10
        self.assertEqual(r1.face_area, area)

    def test_area_cube(self) -> None:
        c1 = self.create_cube()
        area = 6 * 5**2
        self.assertEqual(c1.surface_area, area)

    def test_area_sphere(self) -> None:
        s1 = self.create_sphere()
        area = 4 * math.pi * 5**2
        self.assertEqual(s1.face_area, area)

    # test circumferance function

    def test_circumferance_circle(self) -> None:
        c1 = self.create_circle()
        circ = 2 * math.pi * 10
        self.assertEqual(c1.circumf, circ)

    def test_circumferance_rect(self) -> None:
        r1 = self.create_rectangle()
        circ = 5 + 5 + 10 + 10
        self.assertEqual(r1.circumf, circ)

    def test_circumferance_sphere(self) -> None:
        s1 = self.create_sphere()
        circ = 2 * math.pi * 10
        self.assertEqual(s1.circumf, circ)


if __name__ == "__main__":
    unittest.main()
