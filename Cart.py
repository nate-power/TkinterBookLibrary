from Book import *
from database import *

class Cart:
    def __init__(self):
        self.list_of_books = []
        self.num_of_books = 0

    def add_book(self, title, author, category):
        temp = Book(title, author, category)
        self.list_of_books.insert(self.num_of_books, temp)
        self.num_of_books += 1
        update_cart(f"UPDATE Book SET in_cart = 1 WHERE title = '{title}'")
