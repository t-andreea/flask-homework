from classes.numbers import Numbers

class DecreaseOperate(Numbers):

    def __init__(self, a, b):
        super().__init__(a, b)

    def decrease(self):
        if self._a > self._b:
            return self._a - self._b
        else:
            return self._b - self._a