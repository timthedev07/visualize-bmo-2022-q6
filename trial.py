import random
import 

random.seed(10)
CoordType = tuple[float, float]

class Circle:
    def __init__(self, rad, center: CoordType):
        self.center = center
        self.rad = rad
    def _equationHelper(self, val, axis):
        if val > 0:
            return f"({axis} - {val})^2"
        elif val < 0:
            return f"({axis} + {val})^2"
        else:
            return f"{axis}^2"
    def __str__(self):
        x, y = self.center
        radSquared = self.rad * self.rad
        return f"{self._equationHelper(x, 'y')} + {self._equationHelper(y, 'y')} = {radSquared}"
    def isOnCircle(self, point: CoordType):
      x, y = point
      return x**2 + y**2 == self.rad**2
    def randPointOnCircle(self, lineY):
      x = random.uniform(0, self.rad)
      while x == 0:



def main():
    C = Circle(1, (0, 0))
    lineY = random.uniform(0, 2)
    while lineY == 2 or lineY == 0:
      lineY = random.uniform(0, 2)

    initPoint = []


if __name__ == "__main__":
    main()
