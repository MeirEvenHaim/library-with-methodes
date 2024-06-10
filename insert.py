# Import necessary libraries
from datetime import datetime, timedelta
from book_type import Book_type

# Functions to insert records
def insert_client(cur, conn):
    name = input("What is the client's name?\n")
    city = input("Where is your residence?\n")
    age = int(input("What is the client's age?\n"))
    cur.execute("INSERT INTO client (name, city, age) VALUES (?, ?, ?)", (name, city, age))
    conn.commit()

def insert_books(cur, conn):
    type = int(input("Pick a book loan type between 1-3:\n"))
    name = input("What is the book name?\n")
    author = input("Who is the author and what is their name?\n")
    year_of_publish = int(input("At which year was the book published?\n"))
    cur.execute("INSERT INTO books (name, author, year_of_publish, type) VALUES (?, ?, ?, ?)", (name, author, year_of_publish, type))
    conn.commit()

def find_book_by_name(cur):
    book_name = input("Hello, what is the book *name* you wish to find?\n")
    param = f"%{book_name}%"
    cur.execute("SELECT * FROM books WHERE name LIKE ?", (param,))
    return cur.fetchall()

def find_client_by_name(cur):
    client_name = input("Hello, what is the client's *name* you wish to find?\n")
    param = f"%{client_name}%"
    cur.execute("SELECT * FROM client WHERE name LIKE ?", (param,))
    return cur.fetchall()

def extract_bookId(b_id):
    for _, row in enumerate(b_id):
        print(row)
    user_choice = int(input("Which book ID do you need?\n"))
    return user_choice

def extract_clientId(c_id):
    for _, row in enumerate(c_id):
        print(row)
    user_choice = int(input("Which client ID do you need?\n"))
    return user_choice

from datetime import datetime, timedelta

from datetime import datetime, timedelta

def insert_borrow(cur, conn):
    BookID = find_book_by_name(cur)
    CustID = find_client_by_name(cur)
    B_id = extract_bookId(BookID)
    C_id = extract_clientId(CustID)
    
    cur.execute("SELECT type FROM books WHERE id = ?", (B_id,))
    type_row = cur.fetchone()
    if type_row:
        book_type = type_row[0]
        for t in Book_type:
            if book_type == t.name.strip("type"):
                interval = t.value
                break
    
    # Allow users to input date in any format
    LoanDate = input("Please insert the date the book has been borrowed (YYYY-MM-DD):\n")
    # Ensure the date is in the correct format for SQLite
    LoanDate = LoanDate.strip()  # Remove any leading/trailing spaces
    # Convert LoanDate to a valid format for SQLite
    LoanDate = datetime.strptime(LoanDate, "%Y-%m-%d").date()

    # Calculate ReturnDate based on the interval and LoanDate
    ReturnDate = LoanDate + timedelta(days=interval)
    
    cur.execute("INSERT INTO borrow (CustID, BookID, LoanDate, ReturnDate) VALUES (?, ?, ?, ?)",
                (C_id, B_id, LoanDate, ReturnDate))
    conn.commit()
