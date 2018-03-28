from classes.numbers import Numbers

class DecreaseOperate(Numbers):

    def __init__(self, a, b):
        super().__init__(a, b)

    def decrease(self):
        if self.a > self.b:
            return self.a - self.b
        else:
            return self.b - self.a