if __name__ == '__main__':
    class Library():
        def __init__(self,books,library_name):
            self.books=books
            self.library_name=library_name
            self.number_of_books = len(self.books)
            self.dictionary={}
        def display_books(self):
            print(f"Welcome to {self.library_name} Library!")
            print(f"The books currently in the library are:")
            for i in range(1,self.number_of_books+1):
                print(f"{i}){self.books[i-1]}")
            while True:
                self.book_name = input("Please type the book name for proceeding further, type q for quitting:")
                self.book_name=self.book_name.title()
                if self.book_name in self.books:
                    print(f"You have selected : {self.book_name}")
                    saurav_library.display_features()
                    break
                elif self.book_name=="Q":
                    for k, v in self.dictionary.items():
                        print(f"{k}:{v}")
                    break
                else:
                    print("Sorry try again")
        def display_features(self):
            print("You have the following option you can do")
            print("1)Take a book by signing in\n2)Return a book\nPress b to go back:")
            while True:
                self.inp = input("Please Select the appropriate number or keyword : ")
                if (self.inp=="1") and self.book_name in self.dictionary.keys():
                    print("Sorry,The book is already taken, please return it!")
                    saurav_library.display_features()
                    break
                elif self.inp=="1":
                    saurav_library.lend_book(self.book_name)
                    break
                elif self.inp=="2" and self.book_name in self.dictionary.keys():
                    saurav_library.add_book(self.book_name)
                    break
                elif self.inp=="2":
                    print("The book has not been taken yet")
                    saurav_library.display_features()
                elif self.inp=="b":
                    saurav_library.display_books()
                    break
                else:
                    print("Please try again!")
        def lend_book(self,name_book):
            self.name_book=name_book
            self.userinfo=input("Please enter your name to take the book")
            print(f"Assigning {self.name_book} to {self.userinfo}.....")
            self.dictionary[self.name_book]=self.userinfo
            while True:
                self.goback=input("Type m to go back:")
                if self.goback=='m':
                    saurav_library.display_features()
                    break
                else:
                    print("Wrong input,try again")
        def add_book(self,return_book):
            self.return_book=return_book
            self.user_name=input("Please enter your username:")
            if self.user_name in self.dictionary.values():
                print("Thanks for returning!")
                del self.dictionary[self.book_name]
                saurav_library.display_features()
            else:
                print("Sorry wrong username")
                saurav_library.display_features()
    listofbooks=["Harry Porter","Python Crash Course","Css By Harry","Sherlock Holmes","Nightangle"]
    saurav_library=Library(listofbooks,"Saurav's")
    saurav_library.display_books()