class Book:
    def __init__(self,title,author,isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
    def display_details(self):
        print("book details")
        print(f"title:{self.title}")
        print(f"author:{self.author}")
        print(f"isbn:{self.isbn}")
book = Book("ramayana","valmiki","987-654-03-2")
book.display_details()
