from tkinter import *
from tkinter import ttk
from database import *
import checkout_window as chw


def cart_window(cart):
    cart_man = cart
    root = Tk()
    root.title("Nate's Library - Cart")
    root.geometry("850x400")

    your_cart_label = Label(root, text="Your Cart", font="Courier")
    your_cart_label.grid(row=0, column=0, columnspan=9, pady=10)
    btn_back = Button(root, text="Back to Library", command=root.destroy)
    btn_back.grid(row=3, column=0, ipadx=37, ipady=10, columnspan=6)
    list_cart = Listbox(root, bg="lightgrey", width=110, height=15, selectmode=SINGLE)
    list_cart.grid(row=1, column=2, columnspan=7, padx=10)
    y_scrollbar = Scrollbar(root, orient=VERTICAL)
    y_scrollbar.grid(row=1, column=8, sticky=N + S + E)
    list_cart['yscrollcommand'] = y_scrollbar.set
    y_scrollbar.config(command=list_cart.yview)

    def remove_item():
        if len(list_cart.curselection()) > 0:
            item = list_cart.get(list_cart.curselection())
            title = str(item).split(" by ")[0]
            update_cart(f"UPDATE Book SET in_cart = 0 WHERE title = '{title}'")
            count = 0
            for books in cart_man.list_of_books:
                if title == books.title:
                    del cart_man.list_of_books[count]
                count += 1
        populate_cart()
    remove_item_btn = Button(root, text="Remove Item", command=remove_item)
    remove_item_btn.grid(row=1, column=10, padx=15, ipadx=10, ipady=10)

    def checkout_view():
        root.destroy()
        chw.checkout_window(cart_man)

    checkout_btn = Button(root, text="Checkout", command=checkout_view)
    checkout_btn.grid(row=3, column=5, columnspan=4, ipadx=50, ipady=10, pady=5)
    removed_label = Label(root, font="Arial")
    removed_label.grid(row=2, column=0, columnspan=9)

    def populate_cart():
        checkout_btn['state'] = ACTIVE
        removed_label['text'] = ""
        list_cart.delete(0, END)
        count = 0
        for books in retrieve_data("SELECT title, author FROM Book WHERE in_cart = 1"):
            book_string = str(books[0]).title() + " by " + str(books[1]).title()
            list_cart.insert(count, book_string)
            count += 1
        if count == 0:
            removed_label['text'] = "Your cart is empty!"
            checkout_btn['state'] = DISABLED
    populate_cart()

    refresh_btn = Button(root, text="Refresh Cart", command=populate_cart)
    refresh_btn.grid(row=0, column=0, columnspan=3)
    root.mainloop()