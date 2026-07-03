# Library Management

class Book:
    def __init__(self, title, author):
        self.author = author
        self.title = title
        self.available = True

    def borrowed_book(self):
        if self.available == False:
            print(f"the title of book {self.title} is already borrowed")

        else:
            print(f"successfully borrow {self.title} from the library")
            self.available = False

    def return_book(self):
        if self.available == True:
            print(f"the book {self.title} is already available")

        else:
            print(f"book return succesful name {self.title}")
            self.available = True

    def show_status(self):
        print( f"title: {self.title}\n "
              f"author: {self.author}\n "
              f"available: {self.available}")
        

book1 = Book("Wings of Fire", "A.P.J. Abdul Kalam")

book1.show_status()

book1.borrowed_book()
book1.show_status()

book1.borrowed_book()

book1.return_book()
book1.show_status()

book1.return_book()