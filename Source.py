"""
 Create a class named as library
 Following functionalities should be performed:
 Display books
 Lend book - (show the person who has lended the book if not present.
 add book
 return book
 Manage a dictionary which contains the name of person and the name of book he lended

 Library(List of books, Library name)

 Program should run infinite times.
"""

class Library:

    ls = []
    libraryName = []

    def __init__(self, alist, alibraryname):

        self.ls = alist
        self.libraryName = alibraryname
        self.dict = {}

    def display_books(self):

        print("\nIt is display function.\n")
        print("Following are the books in your library : ")
        print(self.ls)
        print("\n")
        pass

    def dict_maintain(self, aname, abook):

        print("\nIt is dictionary maintain function.\n")
        self.dict[aname] = abook
        print("\n", self.dict, "\n")
        pass

    def lend_books(self):

        print("\nIt is lend books function.\n")
        index = 0
        found = 0
        boolean = 0
        name = input("Enter your full name : ")
        book_name = input("Enter book name : ")

        for item in self.ls:

            if book_name == self.ls[index]:

                self.ls.pop(index)
                found = 1
            index = index + 1

        if found == 0:

            for key, value in self.dict.items():

                if value == book_name:

                    print(f"The name of person who borrowed {value} book is {key}.")
                    print(f"Sorry for unconveneince....")
                    boolean = 1

        if boolean == 0:
            self.dict_maintain(name, book_name)

        print("\n", self.ls, "\n")
        pass

    def add_books(self):

        print("\nIt is add books function.\n")
        book_name = input("Enter book name : ")
        self.ls.append(book_name)
        print("\n", self.ls, "\n")

    def return_books(self):

        print("\nIt is return books function.\n")
        name = input("Enter your full name : ")
        book_name = input("Enter book name : ")
        poping_val = self.dict.pop(name, "This item does not exist.")

        if poping_val != "This item does not exist.":
            self.ls.append(book_name)

        print(poping_val)
        print("\n", self.dict, "\n")
        print("\n", self.ls, "\n")
        pass

    def __repr__(self):
        print(f"Name of Library is {self.libraryName} and books you entered in library are {self.ls}")


if __name__ == '__main__':

    lib_name = input("Now enter your library name : ")
    book_ls = []
    print("Enter a list of book you want to store in library.")

    while(True):
        entering_choice = int(input("If you dont want to enter books in list than press 0 else press 1."))

        if entering_choice != 0:
            book_name = input("Enter your book name here : ")
            book_ls.append(book_name)

        else: break

    lib1 = Library(book_ls, lib_name)
    print(lib1.__repr__())

    while(True):

        print("Enter 0 if you want to exit.")
        print("Enter 1 if you want to see all the books in library : ")
        print("Enter 2 if you want to lend book from library : ")
        print("Enter 3 if you want to add a new book")
        print("Enter 4 if you want to return a borrowed book to library : ")
        choice = int(input("Enter your choice here : "))

        if choice == 0:
            break

        elif choice == 1:
            lib1.display_books()
        elif choice == 2:
            lib1.lend_books()

        elif choice == 3:
            lib1.add_books()

        elif choice == 4:
            lib1.return_books()

        else: print("Enter correct option")

    print(lib1.__repr__())


