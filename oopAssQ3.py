class Wadiya:
    def __init__(self):
        self.name = 'Aladeen'
        self.designation = 'President Prime Minister Admiral General'
        self.num_of_wife = 100
        self.dictator = True

    def view(self):
        print(" Name of president: ", self.name, "\n", "Designation: ", self.designation, "\n", "Number of wife: ",
              self.num_of_wife, "\n", "Is he/she a dictator: ", self.dictator)


wadiya = Wadiya()
print(" Part 1:")
wadiya.view()
print(" Part 2:")
wadiya.name = "Donald Trump"
wadiya.designation = "President"
wadiya.num_of_wife = 1
wadiya.dictator = False
wadiya.view()

print("previous information lost")
