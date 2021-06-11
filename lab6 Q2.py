class Customer:
    def __init__(self, name):
        self.name = name

    def greet(self, name=None):
        print('Hello')

    def purchase(self, *food):
        x = 0
        for i in food:
            x += 1
        print(self.name, ", you purchased", x, "item(s)")
        for i in food:
            print(i)


customer_1 = Customer("Sam")
customer_1.greet()
customer_1.purchase("chips", "chocolate", "orange juice")
print("-----------------------------")
customer_2 = Customer("David")
customer_2.greet("David")
customer_2.purchase("orange juice")