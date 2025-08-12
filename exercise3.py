class Book:
    def __init__(self, title, author, year):
        self.author = author
        self.title = title
        self.year = year
        self.is_checked_out = False

    def checkout(self):
        self.is_checked_out = True

    def return_book(self):
        self.is_checked_out = False

    def __str__(self):  # note: double underscores
        return f"{self.title} by {self.author} ({self.year}) - Checked out: {self.is_checked_out}"


class Library:
    def __init__(self):
        self.collection = []

    def add_book(self, book):
        self.collection.append(book)

    def list_books(self):
        for book in self.collection:
            print(book)

    def find_book(self, title):
        for book in self.collection:
            if book.title.lower() == title.lower():
                return book
        return None
    
    def available_books(self):
        for book in self.collection:
          if not book.is_checked_out:
             print(book)










     



