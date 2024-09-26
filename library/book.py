# library/book.py

class Book:
    def __init__(self, title, author, isbn, publication_year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year
        self.is_borrowed = False

    def borrow(self):
        if self.is_borrowed:
            raise Exception("This book is already borrowed.")
        self.is_borrowed = True

    def return_book(self):
        if not self.is_borrowed:
            raise Exception("This book is not borrowed.")
        self.is_borrowed = False
