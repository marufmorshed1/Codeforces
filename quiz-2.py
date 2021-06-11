class Author:
    def __init__(self, name=None, *books):
        self.name = name
        self.books = books
        self.book = self.books
        if name == None:
            self.name = "Default"

        else:
            print("Author Name: " + self.name)
            print("----")

    def addBooks(self, *book):
        self.book = book

    def printDetails(self):
        print("List of books")
        for i in self.book:
            print(i)

    def changeName(self, name):
        self.name = name
        print("Author Name:" + self.name)
        print("----")


auth1 = Author('Humayun Ahmed')
auth1.addBooks('Deyal', 'Megher Opor Bari')
auth1.printDetails()
print('-----')
auth2 = Author()
print(auth2.name)
auth2.changeName('Mario Puzo')
auth2.addBooks('The Godfather', 'Omerta', 'The Sicilian')
auth2.printDetails()
print('-----')
auth3 = Author('Paolo Coelho', 'The Alchemist', 'The Fifth Mountain')
auth3.printDetails()
print('-----')
