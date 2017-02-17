
class Bag():

    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(2)
        self.add(3)
    def data_in(self):
        print("the data is",self.data)

bag=Bag()
bag.add(10)
bag.addtwice(2)
bag.data_in()
#getattr(bag,[default])