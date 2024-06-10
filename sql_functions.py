# # Import the necessary libraries
# from book_type import Book_type
# import sqlite3
# from datetime import datetime, timedelta

# # Connect to the database
# def connect():
#     """
#     Connect to the SQLite database and return the connection and cursor objects.
#     """
#     conn = sqlite3.connect("library.db")
#     cur = conn.cursor()
#     return conn, cur

# # Create tables
# def client(cur):
#     """
#     Create the client table if it doesn't already exist.
#     """
#     cur.execute("""CREATE TABLE IF NOT EXISTS client(
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 name TEXT,
#                 city TEXT,
#                 age INTEGER)""")

# def books(cur):
#     """
#     Create the books table if it doesn't already exist.
#     """
#     cur.execute("""CREATE TABLE IF NOT EXISTS books(
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 name TEXT,
#                 author TEXT,
#                 year_of_publish INTEGER,
#                 type INTEGER CHECK(type <=3 AND type >= 1))""")

# def borrow(cur):
#     """
#     Create the borrow table if it doesn't already exist.
#     """
#     cur.execute("""CREATE TABLE IF NOT EXISTS borrow (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 CustID INTEGER,
#                 BookID INTEGER,
#                 LoanDate DATE,
#                 ReturnDate DATE,
#                 FOREIGN KEY (CustID) REFERENCES client(id),
#                 FOREIGN KEY (BookID) REFERENCES books(id))""")

# def Create_table(cur):
#     """
#     Create all necessary tables by calling the respective table creation functions.
#     """
#     client(cur)
#     books(cur)
#     borrow(cur)

# # Insert data into tables
# def insert_client(cur, conn):
#     """
#     Insert a new client into the client table.
#     """
#     name = input("What is the client's name?\n")
#     city = input("Where is your residence?\n")
#     age = int(input("What is the client's age?\n"))
#     cur.execute("INSERT INTO client (name, city, age) VALUES (?, ?, ?)", (name, city, age))
#     conn.commit()

# def insert_books(cur, conn):
#     """
#     Insert a new book into the books table.
#     """
#     type = int(input("Pick a book loan type between 1-3:\n"))
#     name = input("What is the book name?\n")
#     author = input("Who is the author and what is their name?\n")
#     year_of_publish = int(input("At which year was the book published?\n"))
#     cur.execute("INSERT INTO books (name, author, year_of_publish, type) VALUES (?, ?, ?, ?)", (name, author, year_of_publish, type))
#     conn.commit()

# # Find data in tables
# def find_book_by_name(cur):
#     """
#     Find books by their name in the books table.
#     """
#     book_name = input("Hello, what is the book *name* you wish to find?\n")
#     param = f"%{book_name}%"
#     cur.execute("SELECT * FROM books WHERE name LIKE ?", (param,))
#     return cur.fetchall()

# def find_client_by_name(cur):
#     """
#     Find clients by their name in the client table.
#     """
#     client_name = input("Hello, what is the client's *name* you wish to find?\n")
#     param = f"%{client_name}%"
#     cur.execute("SELECT * FROM client WHERE name LIKE ?", (param,))
#     return cur.fetchall()

# # Extract IDs from query results
# def extract_bookId(b_id):
#     """
#     Extract the book ID from the list of book records.
#     """
#     for _, row in enumerate(b_id):
#         print(row)
#     user_choice = int(input("Which book ID do you need?\n"))
#     return user_choice

# def extract_clientId(c_id):
#     """
#     Extract the client ID from the list of client records.
#     """
#     for _, row in enumerate(c_id):
#         print(row)
#     user_choice = int(input("Which client ID do you need?\n"))
#     return user_choice

# # Insert a borrow record
# def insert_borrow(cur, conn):
#     """
#     Insert a new borrow record into the borrow table.
#     """
#     BookID = find_book_by_name(cur)
#     CustID = find_client_by_name(cur)
#     B_id = extract_bookId(BookID)
#     C_id = extract_clientId(CustID)
    
#     # Get the interval according to book type
#     cur.execute("SELECT type FROM books WHERE id = ?", (B_id,))
#     type_row = cur.fetchone()
#     if type_row:
#         book_type = type_row[0]
#         for t in Book_type:
#             if book_type == t.name.strip("type"):
#                 interval = t.value
#                 break
    
#     LoanDate = input("Please insert the date the book has been borrowed (dd/mm/yy):\n")
#     LoanDate = datetime.strptime(LoanDate, "%d/%m/%y")
#     ReturnDate = LoanDate + timedelta(days=interval)
    
#     cur.execute("INSERT INTO borrow (CustID, BookID, LoanDate, ReturnDate) VALUES (?, ?, ?, ?)",
#                 (C_id, B_id, LoanDate.strftime("%Y-%m-%d"), ReturnDate.strftime("%Y-%m-%d")))
#     conn.commit()

# # Update records
# def update_client(cur, conn, client_id):
#     """
#     Update an existing client record in the client table.
#     """
#     name = input("Enter the new name:\n")
#     city = input("Enter the new city:\n")
#     age = int(input("Enter the new age:\n"))
#     cur.execute("UPDATE client SET name = ?, city = ?, age = ? WHERE id = ?", (name, city, age, client_id))
#     conn.commit()

# def update_book(cur, conn, book_id):
#     """
#     Update an existing book record in the books table.
#     """
#     name = input("Enter the new book name:\n")
#     author = input("Enter the new author name:\n")
#     year_of_publish = int(input("Enter the new year of publish:\n"))
#     type = int(input("Enter the new type (1-3):\n"))
#     cur.execute("UPDATE books SET name = ?, author = ?, year_of_publish = ?, type = ? WHERE id = ?", 
#                 (name, author, year_of_publish, type, book_id))
#     conn.commit()

# def update_borrow(cur, conn, borrow_id):
#     """
#     Update an existing borrow record in the borrow table.
#     """
#     CustID = int(input("Enter the new customer ID:\n"))
#     BookID = int(input("Enter the new book ID:\n"))
#     LoanDate = input("Enter the new loan date (dd/mm/yy):\n")
#     LoanDate = datetime.strptime(LoanDate, "%d/%m/%y")
#     ReturnDate = input("Enter the new return date (dd/mm/yy):\n")
#     ReturnDate = datetime.strptime(ReturnDate, "%d/%m/%y")
#     cur.execute("UPDATE borrow SET CustID = ?, BookID = ?, LoanDate = ?, ReturnDate = ? WHERE id = ?", 
#                 (CustID, BookID, LoanDate.strftime("%Y-%m-%d"), ReturnDate.strftime("%Y-%m-%d"), borrow_id))
#     conn.commit()

# # Display data
# def display_all_books(cur):
#     """
#     Display all records from the books table.
#     """
#     cur.execute("SELECT * FROM books")
#     return cur.fetchall()

# def display_all_clients(cur):
#     """
#     Display all records from the client table.
#     """
#     cur.execute("SELECT * FROM client")
#     return cur.fetchall()

# def display_all_borrow(cur):
#     """
#     Display all records from the borrow table.
#     """
#     cur.execute("SELECT * FROM borrow")
#     return cur.fetchall()

# # Remove data
# def remove_book(cur, conn, book_id):
#     """
#     Remove a book record from the books table.
#     """
#     cur.execute("DELETE FROM books WHERE id = ?", (book_id,))
#     conn.commit()

# def remove_client(cur, conn, client_id):
#     """
#     Remove a client record from the client table.
#     """
#     cur.execute("DELETE FROM client WHERE id = ?", (client_id,))
#     conn.commit()
