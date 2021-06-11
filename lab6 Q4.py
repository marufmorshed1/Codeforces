class Cat:
    def __init__(self, *attr):
        if len(attr) == 2:
            self.color = attr[0]
            self.position = attr[1]
        elif len(attr) == 1:
            self.color = attr[0]
            self.position = "sitting"
        else:
            self.color = "White"
            self.position = "sitting"

    def printCat(self):
        print(self.color, "cat is", self.position)

    def changeColor(self, color):
        self.color = color


c1 = Cat()
c2 = Cat("Black")
c3 = Cat("Brown", "jumping")
c4 = Cat("Red", "purring")
c1.printCat()
c2.printCat()
c3.printCat()
c4.printCat()
c1.changeColor("Blue")
c3.changeColor("Purple")
c1.printCat()
c3.printCat()
