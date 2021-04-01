import sqlite3



def create_db():
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS Book (
            title text,
            author text,
            category text,
            in_cart integer
        )""")
    conn.commit()
    conn.close()


def seed_data():
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("SELECT count(*) FROM Book")
    count = cur.fetchone()
    if count[0] == 0:
        cur.execute("INSERT INTO Book VALUES ('Survival In Auschwitz', 'Primo Levi', 'Biography/Autobiography', 0)")
        cur.execute("INSERT INTO Book VALUES ('Anthony Powell', 'Hilary Spurling', 'Biography/Autobiography', 0)")
        cur.execute("INSERT INTO Book VALUES ('Furiously Happy', 'Jenny Lawson', 'Biography/Autobiography', 0)")
        cur.execute("INSERT INTO Book VALUES ('Night', 'Elie Wiesel', 'Biography/Autobiography', 0)")
        cur.execute("INSERT INTO Book VALUES ('Furious Hours', 'Casey Cep', 'Crime', 0)")
        cur.execute("INSERT INTO Book VALUES ('Sometimes I Lie', 'Alice Feeney', 'Crime', 0)")
        cur.execute("INSERT INTO Book VALUES ('Never Let You Go', 'Chevy Stevens', 'Crime', 0)")
        cur.execute("INSERT INTO Book VALUES ('The Hunting Party', 'Lucy Foley', 'Crime', 0)")
        cur.execute("INSERT INTO Book VALUES ('The Night Watch', 'Sergei Lukyanenko', 'Fantasy', 0)")
        cur.execute("INSERT INTO Book VALUES ('What Is Not Yours Is Not Yours', 'Helen Oyeyemi', 'Fantasy', 0)")
        cur.execute("INSERT INTO Book VALUES ('The Bear and The Nightingale', 'Katherine Arden', 'Fantasy', 0)")
        cur.execute("INSERT INTO Book VALUES ('A Wild Sheep Chase', 'Haruki Murakami', 'Fantasy', 0)")
        cur.execute("INSERT INTO Book VALUES ('The Age of Light', 'Whitney Scharer', 'History', 0)")
        cur.execute("INSERT INTO Book VALUES ('The New York Trilogy', 'Paul Auster', 'History', 0)")
        cur.execute("INSERT INTO Book VALUES ('The Gene', 'Siddhartha Mukherjee', 'History', 0)")
        cur.execute("INSERT INTO Book VALUES ('Democracy in America', 'Alexis Tocqueville', 'History', 0)")
        cur.execute("INSERT INTO Book VALUES ('The Road to Character', 'David Brooks', 'Philosophy', 0)")
        cur.execute("INSERT INTO Book VALUES ('Social Contract', 'Jean Jacques Rousseau', 'Philosophy', 0)")
        cur.execute("INSERT INTO Book VALUES ('Leviathan, 1651', 'Thomas Hobbes', 'Philosophy', 0)")
        cur.execute("INSERT INTO Book VALUES ('The Book of Joy', 'Dalai Lama', 'Philosophy', 0)")
        cur.execute("INSERT INTO Book VALUES ('Without Merit', 'Colleen Hoover', 'Romance', 0)")
        cur.execute("INSERT INTO Book VALUES ('Shelter in Place', 'Nora Roberts', 'Romance', 0)")
        cur.execute("INSERT INTO Book VALUES ('The Glittering Court', 'Richelle Mead', 'Romance', 0)")
        cur.execute("INSERT INTO Book VALUES ('Uprooted', 'Naomi Novik', 'Romance', 0)")
        cur.execute("INSERT INTO Book VALUES ('Nemesis Games', 'James S. A. Corey', 'Science Fiction', 0)")
        cur.execute("INSERT INTO Book VALUES ('Dune', 'Frank Herbert', 'Science Fiction', 0)")
        cur.execute("INSERT INTO Book VALUES ('Fairest', 'Marissa Meyer', 'Science Fiction', 0)")
        cur.execute("INSERT INTO Book VALUES ('Recursion', 'Blake Crouch', 'Science Fiction', 0)")
        cur.execute("INSERT INTO Book VALUES ('Neither Here, Nor There', 'Bill Bryson', 'Travel', 0)")
        cur.execute("INSERT INTO Book VALUES ('The Summer Isles', 'Frans de Waal', 'Travel', 0)")
        cur.execute("INSERT INTO Book VALUES ('Notes From A Small Island', 'Bill Bryson', 'Travel', 0)")
        cur.execute("INSERT INTO Book VALUES ('The Little Book of Hygge', 'Meik Wiking', 'Travel', 0)")
    conn.commit()
    conn.close()


def retrieve_data(query):
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows


def update_cart(query):
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
    conn.close()

