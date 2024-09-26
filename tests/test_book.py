# tests/test_book.py

import unittest
from library.book import Book

class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book("1984", "George Orwell", "1234567890", 1949)

    def test_book_creation(self):
        self.assertEqual(self.book.title, "1984")
        self.assertEqual(self.book.author, "George Orwell")
        self.assertEqual(self.book.isbn, "1234567890")
        self.assertEqual(self.book.publication_year, 1949)
        self.assertFalse(self.book.is_borrowed)

    def test_borrow_book(self):
        self.book.borrow()
        self.assertTrue(self.book.is_borrowed)

    def test_return_book(self):
        self.book.borrow()
        self.book.return_book()
        self.assertFalse(self.book.is_borrowed)

    def test_borrow_book_already_borrowed(self):
        self.book.borrow()
        with self.assertRaises(Exception) as context:
            self.book.borrow()
        self.assertEqual(str(context.exception), "This book is already borrowed.")

    def test_return_book_not_borrowed(self):
        with self.assertRaises(Exception) as context:
            self.book.return_book()
        self.assertEqual(str(context.exception), "This book is not borrowed.")

if __name__ == "__main__":
    unittest.main()
