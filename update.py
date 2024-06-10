# Import necessary libraries
from datetime import datetime

# Functions to update records
def update_client(cur, conn, client_id):
    name = input("Enter the new name:\n")
    city = input("Enter the new city:\n")
    age = int(input("Enter the new age:\n"))
    cur.execute("UPDATE client SET name = ?, city = ?, age = ? WHERE id = ?", (name, city, age, client_id))
    conn.commit()

def update_book(cur, conn, book_id):
    name = input("Enter the new book name:\n")
    author = input("Enter the new author name:\n")
    year_of_publish = int(input("Enter the new year of publish:\n"))
    type = int(input("Enter the new type (1-3):\n"))
    cur.execute("UPDATE books SET name = ?, author = ?, year_of_publish = ?, type = ? WHERE id = ?", 
                (name, author, year_of_publish, type, book_id))
    conn.commit()

def update_borrow(cur, conn, borrow_id):
    CustID = int(input("Enter the new customer ID:\n"))
    BookID = int(input("Enter the new book ID:\n"))
    LoanDate = input("Enter the new loan date (dd/mm/yy):\n")
    LoanDate = datetime.strptime(LoanDate, "%d/%m/%y")
    ReturnDate = input("Enter the new return date (dd/mm/yy):\n")
    ReturnDate = datetime.strptime(ReturnDate, "%d/%m/%y")
    cur.execute("UPDATE borrow SET CustID = ?, BookID = ?, LoanDate = ?, ReturnDate = ? WHERE id = ?", 
                (CustID, BookID, LoanDate.strftime("%Y-%m-%d"), ReturnDate.strftime("%Y-%m-%d"), borrow_id))
    conn.commit()
