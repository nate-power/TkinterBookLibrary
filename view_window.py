from tkinter import *
from tkinter import ttk
from database import *
import cart_window as cw


def view_window(cart):
    cart_man = cart
    root = Tk()
    root.title("Elite Library")
    root.geometry("800x550")

    view_lib_title = Label(root, text="Welcome to the Elite Library!", font="Courier")
    view_lib_title.grid(row=0, column=0, columnspan=8, pady=15)
    search_title_label = Label(root, text="Search by Title:")
    search_title_label.grid(row=1, column=0)
    search_title = Entry(root)
    search_title.grid(row=1, column=1)
    separator_1 = Label(root, text="or", font="Arial")
    separator_1.grid(row=1, column=2, padx=10)
    search_author_label = Label(root, text="Search by Author:")
    search_author_label.grid(row=1, column=3)
    search_author = Entry(root)
    search_author.grid(row=1, column=4)
    separator_2 = Label(root, text="or", font="Arial")
    separator_2.grid(row=1, column=5, padx=10)
    search_category_label = Label(root, text="Select a Category:")
    search_category_label.grid(row=1, column=6)
    search_category = ttk.Combobox(root, state="readonly")
    search_category['values'] = (
        '<None>',
        'Biography/Autobiography',
        'Crime',
        'Fantasy',
        'History',
        'Philosophy',
        'Romance',
        'Science Fiction',
        'Travel'
    )
    search_category.current(0)
    search_category.grid(row=1, column=7)
    search_message_label = Label(root, font="Bodoni")
    search_message_label.grid(row=3, column=0, columnspan=7)
    cart_message_label = Label(root, font=("Arial", 12))
    cart_message_label.grid(row=6, column=0, columnspan=9)

    def search():
        cart_message_label['text'] = ""
        search_message_label['text'] = ""
        for i in list_books.get_children():
            list_books.delete(i)

        count = 0
        query = "SELECT * FROM Book ORDER BY title"
        if search_title.get() != "" and search_author.get() == "" and search_category.get() == "<None>":
            for book in retrieve_data(query):
                if search_title.get().lower() in book[0].lower():
                    list_books.insert('', 'end', count, text="", values=(str(book[0]), str(book[1]), str(book[2])))
                    count += 1
            if count == 0:
                search_message_label['text'] = "No Matches Found"

        elif search_title.get() == "" and search_author.get() != "" and search_category.get() == "<None>":
            for book in retrieve_data(query):
                if search_author.get().lower() in book[1].lower():
                    list_books.insert('', 'end', count, text="", values=(str(book[0]), str(book[1]), str(book[2])))
                    count += 1
            if count == 0:
                search_message_label['text'] = "No Matches Found"

        elif search_title.get() == "" and search_author.get() == "" and search_category.get() != "<None>":
            for book in retrieve_data(query):
                if search_category.get() in book[2]:
                    list_books.insert('', 'end', count, text="", values=(str(book[0]), str(book[1]), str(book[2])))
                    count += 1
            if count == 0:
                search_message_label['text'] = "No Matches Found"
        elif search_title.get() == "" and search_author.get() == "" and search_category.get() == "<None>":
            search_message_label['text'] = "One search field must be filled"
        else:
            search_message_label['text'] = "Only one search field can be filled"

    def show_all():
        cart_message_label['text'] = ""
        search_title.delete(0, END)
        search_author.delete(0, END)
        search_category.current(0)
        for i in list_books.get_children():
            list_books.delete(i)
        search_message_label['text'] = ""
        count = 0
        for book in retrieve_data("SELECT * FROM Book ORDER BY title"):
            list_books.insert('', 'end', count, text="", values=(str(book[0]), str(book[1]), str(book[2])))
            count += 1

    search_btn = Button(root, text="Search", command=search)
    search_btn.grid(row=2, column=0, columnspan=9, ipadx=80, pady=10)
    show_all_btn = Button(root, text="Show All Books", command=show_all)
    show_all_btn.grid(row=5, column=0, columnspan=9, ipadx=70, pady=20)

    list_books = ttk.Treeview(root, columns=('Title', 'Author', 'Category'))
    list_books.grid(row=4, column=0, columnspan=7)
    y_scrollbar = Scrollbar(root, orient=VERTICAL)
    y_scrollbar.grid(row=4, column=6, sticky=N + S + E)
    list_books['yscrollcommand'] = y_scrollbar.set
    y_scrollbar.config(command=list_books.yview)

    list_books.heading('#0', text='')
    list_books.heading('Title', text='Title')
    list_books.heading('Author', text='Author')
    list_books.heading('Category', text='Category')

    list_books.column('#0', width=0, stretch=NO)
    list_books.column('Title', stretch=YES)
    list_books.column('Author', stretch=YES)
    list_books.column('Category', stretch=YES)

    # populate listbox with all books on start-up
    show_all()

    def cart_view():
        cart_message_label['text'] = ""
        cw.cart_window(cart_man)

    def get_book():
        row = list_books.focus()
        values = list_books.item(row).get('values')
        if len(values) > 0:
            was_added = False
            for books in cart_man.list_of_books:
                if books.title == values[0] and books.author == values[1]:
                    cart_message_label['text'] = '"' + str(values[0]) + '"' + " has already been added to your cart!"
                    was_added = True
                    break
            if not was_added:
                cart_man.add_book(values[0], values[1], values[2])
                cart_message_label['text'] = '"' + str(values[0]) + '"' + " added to cart!"

    add_to_cart = Button(root, text="Add to Cart", command=get_book)
    add_to_cart.grid(row=1, column=7, rowspan=4, ipady=20, ipadx=20)
    view_cart = Button(root, text="View Cart", command=cart_view)
    view_cart.grid(row=4, rowspan=5, column=7, ipadx=25, ipady=19)

    root.mainloop()