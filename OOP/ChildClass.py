from OOP.clas import Calculator


class ChildImpl(Calculator):
    num2 = 50

    def __init__(self):
        Calculator.__init__(self, 5, 4)

    def gatAll_data(self):
        return self.num2 + self.num + self.Summation()


obj = ChildImpl()
print(obj.gatAll_data())
