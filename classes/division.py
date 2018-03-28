from classes.numbers import Numbers

class DivisionOperate(Numbers):

    def __init__(self, a, b):
        super().__init__(a, b)

    def division(self):
        if self.a == 0:
            return 0
        else:
            return self.a/self.b
