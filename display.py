# Import necessary libraries
import sqlite3

# Functions to display records
def display_all_books(cur):
    cur.execute("SELECT * FROM books")
    return cur.fetchall()

def display_all_clients(cur):
    cur.execute("SELECT * FROM client")
    return cur.fetchall()

def display_all_borrow(cur):
    cur.execute("SELECT * FROM borrow")
    return cur.fetchall()
