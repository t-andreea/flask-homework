from classes.numbers import Numbers

class AddOperate(Numbers):
    def __init__(self, a, b):
        super().__init__(a, b)

    def add(self):
        return self._a + self._b
