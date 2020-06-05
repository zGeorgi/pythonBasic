class Kalkulat:
    num = 100

    def __init__(self, a, b):
        self.firstN = a
        self.secondN = b
        print("In parametrize constructor")

    def get_data(self):
        print("Minecraft")

    def summa(self):
        return self.secondN + self.firstN + Kalkulat.num


obj = Kalkulat(3, 5)
obj.get_data()
print(obj.summa())

obj1 = Kalkulat(5, 4)
obj1.get_data()
print(obj1.summa())
