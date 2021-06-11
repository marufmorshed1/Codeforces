class Author:
    def __init__(self, *name):
        self.books = name[1::]
        if len(name) == 1:
            self.name = name[0]
            print("Author name: ", name[0])

        print("----")

    def addBooks(self):
        while (x < 0):


    def printDetails(self):
        for i in name:
            print(books[i+1])

    def changeName(self, name):
        name[0] = name


auth1 = Author('Humayun Ahmed')
auth1.addBooks('Deyal', 'Megher Opor Bari')
auth1.printDetails()
print("-----")
auth2 = Author()
print(auth2.name)
auth2.changeName('Mario Puzo')
auth2.addBooks('The Godfather', 'Omerta', 'The Sicilian')
auth2.printDetails()
print("-----")
auth3 = Author('Paolo Coelho', "The Alchemist", "The Fifth Mountain")
auth3.printDetails()
print("-----")
