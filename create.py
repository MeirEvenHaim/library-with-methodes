# Import necessary libraries
import sqlite3

# Function to create tables
def client(cur):
    cur.execute("""CREATE TABLE IF NOT EXISTS client(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                city TEXT,
                age INTEGER)""")

def books(cur):
    cur.execute("""CREATE TABLE IF NOT EXISTS books(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                author TEXT,
                year_of_publish INTEGER,
                type INTEGER CHECK(type <=3 AND type >= 1))""")

def borrow(cur):
    cur.execute("""CREATE TABLE IF NOT EXISTS borrow (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                CustID INTEGER,
                BookID INTEGER,
                LoanDate DATE,
                ReturnDate DATE,
                FOREIGN KEY (CustID) REFERENCES client(id),
                FOREIGN KEY (BookID) REFERENCES books(id))""")

def create_tables(cur):
    client(cur)
    books(cur)
    borrow(cur)
