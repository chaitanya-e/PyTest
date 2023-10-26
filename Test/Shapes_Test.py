import math

import Source.Shapes as Shapes


class TestCircle:

    def test_one(self):
        assert True

    # this is like beforeTest in TestNG
    # runs before every test
    def setup_test(self, method):
        print(f"setting up {method}")
        print("setup")
        self.circle = Shapes.Circle()

    # this is like afterTest in TestNG
    # runs after every test
    def teardown_test(self, method):
        print(f"tearing down {method}")
        print("Teardown")
        del self.circle

    def test_two(self):
        assert True

    def test_circle_area(self):
        assert self.circle.area() == math.pi * self.circle.radius ** 2
