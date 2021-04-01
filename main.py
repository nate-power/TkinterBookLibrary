from database import *
from Cart import *
import view_window as vw


def main():
    # create a manager to hold all books in cart
    cart_man = Cart()

    # create or connect to database
    create_db()

    # seed initial data into database
    seed_data()

    # populate list of books in cart array
    for books in retrieve_data("SELECT title, author, category FROM Book WHERE in_cart = 1"):
        cart_man.add_book(str(books[0]), str(books[1]), str(books[2]))

    # view for displaying library is the landing page of application
    vw.view_window(cart_man)


if __name__ == '__main__':
    main()
