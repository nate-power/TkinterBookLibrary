from tkinter import *
from database import *
import datetime
from Cart import *
from tkinter import filedialog
import os


def checkout_window(cart):
    cart_man = cart
    root = Tk()
    root.title("Checkout Receipt")
    root.geometry("500x400")

    receipt_label = Label(root, text="Receipt", font="Courier")
    receipt_label.grid(row=0, column=0, columnspan=7)
    date_label = Label(root, font=("Courier", 10))
    date_label.grid(row=1, column=0, columnspan=7)

    now = datetime.datetime.now()
    checkout_date_time = str(now.strftime("%Y-%m-%d %I:%M:%S %p"))
    date_label['text'] = "Item(s) checked out at: " + checkout_date_time

    list_cart = Listbox(root, bg="lightgrey", width=75, height=15, selectmode=SINGLE)
    list_cart.grid(row=2, column=0, columnspan=7, padx=10)
    y_scrollbar = Scrollbar(root, orient=VERTICAL)
    y_scrollbar.grid(row=2, column=6, sticky=N + S + E)
    list_cart['yscrollcommand'] = y_scrollbar.set
    y_scrollbar.config(command=list_cart.yview)

    count = 0
    for books in retrieve_data("SELECT title, author FROM Book WHERE in_cart = 1"):
        book_string = str(books[0]).title() + " by " + str(books[1]).title()
        list_cart.insert(count, book_string)
        count += 1

    for books in retrieve_data("SELECT title FROM Book WHERE in_cart = 1"):
        update_cart(f"UPDATE Book SET in_cart = 0 WHERE title = '{books[0]}'")
        count = 0
        for books_in_list in cart_man.list_of_books:
            if books_in_list.title == books[0]:
                del cart_man.list_of_books[count]
            count += 1

    due_date_label = Label(root, text="Item(s) must be returned by: ", font=("Courier", 10))
    due_date_label.grid(row=3, column=0, columnspan=7)

    # add three weeks to the checkout date
    checkout_date = str(now.strftime("%d-%m-%Y"))
    checkout_date_obj = datetime.datetime.strptime(checkout_date, "%d-%m-%Y")
    return_interval = datetime.timedelta(days=21)
    due_date = str(checkout_date_obj + return_interval)
    due_date = due_date.split(" ")[0]
    due_date_label['text'] += due_date

    def save_to_file():
        content = "<Elite Library - Library Receipt>\n" + date_label['text'] + "\n\n" + "Item(s):\n"
        for item in list_cart.get(0, END):
            content += item + '\n'
        content += "\n" + due_date_label['text']
        file_name = "Library Receipt - " + checkout_date
        home_dir = os.path.expanduser("~")
        directory = "Documents"
        path = os.path.join(home_dir, directory)
        if not os.path.isdir(path):
            path = home_dir
        text_file = filedialog.asksaveasfilename(
            initialdir=path,
            defaultextension=".txt",
            title="Save Receipt",
            initialfile=file_name,
            filetypes=(("Text Files", "*.txt"), ("All Files", "*.*"))
        )
        if text_file:
            text_file = open(text_file, 'w')
            text_file.write(content)
            text_file.close()

    save_btn = Button(root, text="Save Receipt to Text File", command=save_to_file)
    save_btn.grid(row=4, column=0, columnspan=7, pady=10)

    root.mainloop()
