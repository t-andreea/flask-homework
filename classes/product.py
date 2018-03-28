from classes.numbers import Numbers

class ProductOperate(Numbers):

    def __init__(self,  a, b):
        super().__init__(a, b)

    def product(self):
        return self.a*self.b